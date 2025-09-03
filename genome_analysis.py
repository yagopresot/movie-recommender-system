# genome_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os  # Adicionado para manipulação de diretórios


def main():
    # Criar pasta para imagens
    os.makedirs('images', exist_ok=True)

    genome_tags = pd.read_csv('Dataset/genome_tags.csv')
    genome_scores = pd.read_csv('Dataset/genome_scores.csv')

    # Mesclando os dados genômicos
    genome = pd.merge(genome_scores, genome_tags, on='tagId')
    top_genome_tags = genome.groupby('tag')['relevance'].mean().sort_values(ascending=False).head(10).reset_index()

    plt.figure(figsize=(10, 5))
    colors_genome = sns.color_palette("magma", len(top_genome_tags))

    # Gráfico corrigido
    sns.barplot(
        x='tag',
        y='relevance',
        data=top_genome_tags,
        hue='tag',  # Adicionado para corrigir o warning
        palette=colors_genome,
        legend=False  # Remove legenda redundante
    )

    plt.xlabel("Genome Tag", fontsize=12)
    plt.ylabel("Relevância média", fontsize=12)
    plt.title("Top 10 Genome Tags por Relevância Média", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salvando na pasta images
    plt.savefig(os.path.join('images', 'top_genome_tags.png'), dpi=300)
    plt.show()


if __name__ == '__main__':
    main()