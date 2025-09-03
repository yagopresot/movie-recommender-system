# genre_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os  # Adicionado para manipulação de diretórios


def main():
    # Criar pasta para imagens
    os.makedirs('images', exist_ok=True)

    movies = pd.read_csv('Dataset/movie.csv')

    # Separando os gêneros e contando
    movies['genres_list'] = movies['genres'].str.split('|')
    movies_exploded = movies.explode('genres_list')
    genre_counts = movies_exploded['genres_list'].value_counts().reset_index()
    genre_counts.columns = ['genres_list', 'count']  # Renomeando colunas

    plt.figure(figsize=(12, 6))
    colors_genre = sns.color_palette("coolwarm", len(genre_counts))

    # Gráfico corrigido
    sns.barplot(
        x='genres_list',
        y='count',
        data=genre_counts,
        hue='genres_list',  # Adicionado para corrigir o warning
        palette=colors_genre,
        legend=False  # Remove legenda redundante
    )

    plt.xlabel("Gênero", fontsize=12)
    plt.ylabel("Número de filmes", fontsize=12)
    plt.title("Distribuição de filmes por gênero", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salvando na pasta images
    plt.savefig(os.path.join('images', 'movies_by_genre.png'), dpi=300)
    plt.show()


if __name__ == '__main__':
    main()