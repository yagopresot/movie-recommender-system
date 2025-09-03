# ratings_movies_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os  # Adicionado para manipulação de caminhos


def main():
    # Cria a pasta de imagens se não existir
    os.makedirs('images', exist_ok=True)

    ratings = pd.read_csv('Dataset/rating.csv')
    movies = pd.read_csv('Dataset/movie.csv')

    # Mesclando ratings com filmes
    ratings_movies = pd.merge(ratings, movies, on='movieId')
    ratings_movies['genres_list'] = ratings_movies['genres'].str.split('|')
    ratings_exploded = ratings_movies.explode('genres_list')

    avg_ratings_by_genre = ratings_exploded.groupby('genres_list')['rating'].mean().reset_index()

    plt.figure(figsize=(12, 6))
    colors_avg = sns.color_palette("viridis", len(avg_ratings_by_genre))
    sns.barplot(
        x='genres_list',
        y='rating',
        data=avg_ratings_by_genre,
        hue='genres_list',
        palette=colors_avg,
        legend=False
    )
    plt.xlabel("Gênero", fontsize=12)
    plt.ylabel("Rating médio", fontsize=12)
    plt.title("Média de Ratings por Gênero", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salva na pasta images
    plt.savefig(os.path.join('images', 'avg_ratings_by_genre.png'), dpi=300)
    plt.show()

    print(avg_ratings_by_genre.head())


if __name__ == '__main__':
    main()