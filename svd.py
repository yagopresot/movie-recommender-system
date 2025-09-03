import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import NearestNeighbors

# Caminhos dos arquivos
genome_scores_file = r'Dataset/genome_scores.csv'
genome_tags_file = r'Dataset/genome_tags.csv'
ratings_file = r'Dataset/rating.csv'
movies_file = r'Dataset/movie.csv'  # Novo arquivo adicionado

# Carregar os dados
genome_scores_df = pd.read_csv(genome_scores_file)
genome_tags_df = pd.read_csv(genome_tags_file)
ratings_df = pd.read_csv(ratings_file)
movies_df = pd.read_csv(movies_file)  # Carregar dados dos filmes

# Mapeamento de IDs para títulos
movie_id_to_title = movies_df.set_index('movieId')['title'].to_dict()

# Mesclar genome_scores e genome_tags
merged_tags_df = pd.merge(genome_scores_df, genome_tags_df, on='tagId', how='left')


# Criar matriz esparsa de características
def create_feature_matrix(ratings_df, merged_tags_df):
    # Matriz de tags dos filmes
    movie_tag_matrix = merged_tags_df.pivot_table(
        index='movieId', columns='tag', values='relevance', aggfunc='mean'
    ).fillna(0)

    # Mapear usuários e filmes para índices
    users = ratings_df['userId'].unique()
    movies = ratings_df['movieId'].unique()
    user_index = {u: i for i, u in enumerate(users)}
    movie_index = {m: i for i, m in enumerate(movies)}

    # Criar matriz esparsa de avaliações
    row = ratings_df['userId'].map(user_index)
    col = ratings_df['movieId'].map(movie_index)
    data = ratings_df['rating']

    rating_matrix = csr_matrix((data, (row, col)),
        shape=(len(users), len(movies)))

    return rating_matrix, movie_tag_matrix, user_index, movie_index


# Aplicar SVD
def apply_svd(matrix, n_components=20):
    svd = TruncatedSVD(n_components=n_components, random_state=42)
    matrix_reduced = svd.fit_transform(matrix)
    return matrix_reduced, svd


# Obter recomendações otimizado
def get_recommendations(user_id, rating_matrix, matrix_reduced, user_index, movie_index, n_recommendations=5):
    if user_id not in user_index:
        return []

    # Configurar modelo de vizinhos
    model = NearestNeighbors(n_neighbors=20, metric='cosine', algorithm='brute')
    model.fit(matrix_reduced)

    # Encontrar vizinhos mais próximos
    user_row = user_index[user_id]
    _, indices = model.kneighbors([matrix_reduced[user_row]])

    # Filmes não avaliados
    user_ratings = rating_matrix[user_row].toarray().flatten()
    unrated = [m_id for m_id, col in movie_index.items() if user_ratings[col] == 0]

    # Calcular scores
    recommendations = {}
    for movie_id in unrated:
        col = movie_index[movie_id]
        ratings = rating_matrix[indices[0], col].toarray().flatten()
        valid_ratings = ratings[ratings > 0]

        if len(valid_ratings) > 0:
            recommendations[movie_id] = valid_ratings.mean()

    return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]


# Execução principal
if __name__ == "__main__":
    # Criar matrizes
    rating_matrix, movie_tags, user_index, movie_index = create_feature_matrix(ratings_df, merged_tags_df)

    # Redução de dimensionalidade
    matrix_reduced, _ = apply_svd(rating_matrix, n_components=20)

    # Mostrar IDs válidos
    print("Exemplos de IDs de usuários válidos:")
    print(list(user_index.keys())[:10])

    try:
        user_id = int(input("\nDigite o ID do usuário para recomendações: "))
    except ValueError:
        print("ID inválido!")
        exit()

    # Gerar recomendações
    recs = get_recommendations(user_id, rating_matrix, matrix_reduced, user_index, movie_index)

    if recs:
        print(f"\nTop recomendações para o usuário {user_id}:")
        for movie_id, score in recs:
            title = movie_id_to_title.get(movie_id, "Título não encontrado")
            print(f"• {title} (ID: {movie_id}): Score {score:.2f}")
    else:
        print("Nenhuma recomendação encontrada.")