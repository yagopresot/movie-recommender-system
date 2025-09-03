# ratings_distribution.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def main():
    # Criar pasta para imagens
    os.makedirs('images', exist_ok=True)

    # Leitura dos dados
    ratings = pd.read_csv('Dataset/rating.csv')

    # Distribuição de ratings por filme
    ratings_per_movie = ratings.groupby('movieId').size().sort_values()
    plt.figure(figsize=(10, 7))
    plt.hist(ratings_per_movie, bins=100, range=(0, 2000), color='skyblue', edgecolor='black')
    plt.xlabel("Número de ratings por filme", fontsize=12)
    plt.ylabel("Contagem de filmes", fontsize=12)
    plt.title("Distribuição de ratings por filme", fontsize=14)
    plt.savefig(os.path.join('images', 'ratings_per_movie.png'), dpi=300)
    plt.show()

    # Distribuição de ratings por usuário
    ratings_per_user = ratings.groupby('userId').size().sort_values()
    plt.figure(figsize=(10, 7))
    plt.hist(ratings_per_user, bins=100, range=(0, 1000), color='lightgreen', edgecolor='black')
    plt.xlabel("Número de ratings por usuário", fontsize=12)
    plt.ylabel("Contagem de usuários", fontsize=12)
    plt.title("Distribuição de ratings por usuário", fontsize=14)
    plt.savefig(os.path.join('images', 'ratings_per_user.png'), dpi=300)
    plt.show()

    # Distribuição dos valores de rating (corrigido)
    plt.figure(figsize=(10, 5))
    order_ratings = sorted(ratings['rating'].unique())
    palette_colors = sns.color_palette("viridis", len(order_ratings))

    ax = sns.countplot(
        x='rating',
        data=ratings,
        order=order_ratings,
        hue='rating',  # Adicionado para corrigir o warning
        palette=palette_colors,
        legend=False  # Remove legenda redundante
    )

    plt.xlabel("Valor do rating", fontsize=12)
    plt.ylabel("Contagem", fontsize=12)
    plt.title("Distribuição dos valores de rating", fontsize=14)

    # Adicionando porcentagens
    total_ratings = ratings.shape[0]
    for patch in ax.patches:
        count = patch.get_height()
        percentage = int(count / total_ratings * 100)
        x = patch.get_x() + patch.get_width() / 2
        y = patch.get_height()
        ax.annotate(f'{percentage}%', (x, y), ha='center', va='bottom', fontsize=10)

    plt.savefig(os.path.join('images', 'rating_value_distribution.png'), dpi=300)
    plt.show()


if __name__ == '__main__':
    main()