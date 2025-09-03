# data_overview.py
import pandas as pd
import os


def df_mem_usage(df, df_name="DataFrame"):
    BYTES_TO_MB_DIV = 0.000001
    mem = round(df.memory_usage().sum() * BYTES_TO_MB_DIV, 3)
    print(f"Memória usada por {df_name}: {mem} MB")


def main():
    print("Diretório de trabalho atual:", os.getcwd())

    # Leitura dos arquivos
    ratings = pd.read_csv('Dataset/rating.csv')  # userId, movieId, rating, timestamp
    movies = pd.read_csv('Dataset/movie.csv')  # movieId, title, genres
    tags = pd.read_csv('Dataset/tag.csv')  # userId, movieId, tag, timestamp
    links = pd.read_csv('Dataset/link.csv')  # movieId, imdbId, tmdbId
    genome_tags = pd.read_csv('Dataset/genome_tags.csv')  # tagId, tag
    genome_scores = pd.read_csv('Dataset/genome_scores.csv')  # movieId, tagId, relevance

    # Exibindo as primeiras linhas
    print("Ratings:")
    print(ratings.head(), "\n")
    print("Movies:")
    print(movies.head(), "\n")
    print("Tags:")
    print(tags.head(), "\n")
    print("Links:")
    print(links.head(), "\n")
    print("Genome Tags:")
    print(genome_tags.head(), "\n")
    print("Genome Scores:")
    print(genome_scores.head(), "\n")

    # Informações gerais e uso de memória
    df_mem_usage(ratings, "ratings")
    print("Formato do DataFrame ratings:", ratings.shape)
    print(ratings.describe())
    print("Ratings ausentes:", ratings['rating'].isnull().sum())


if __name__ == '__main__':
    main()
