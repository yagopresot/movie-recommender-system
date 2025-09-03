# Sistema de Recomendação de Filmes usando SVD

## 📂 Estrutura do Projeto
├── Dataset/ # Arquivos de dados originais (não incluído no repositório)
├── images/ # Gráficos gerados pelas análises
├── data_overview.py # Análise exploratória inicial
├── genome_analysis.py # Análise de tags genômicas
├── genre_analysis.py # Análise de distribuição por gêneros
├── ratings_distribution.py # Análise de distribuição de ratings
├── ratings_movies_analysis.py # Relação entre ratings e gêneros
└── svd.py # Sistema principal de recomendação

## 🛠️ Requisitos
- Python 3.8+
- Bibliotecas:
  ```bash
  pip install pandas matplotlib seaborn scikit-learn scipy

🎬 Dataset
Base de dados do MovieLens 25M contendo: # https://www.kaggle.com/datasets/veeralakrishna/movielens-25m-dataset #
25 milhões de ratings
62 mil filmes
32 gêneros diferentes
Tags genômicas de relevância

🔍 Análises Realizadas
1. Pré-processamento e Visualização
Distribuição de ratings (usuários e filmes)
Análise de gêneros mais populares
Relação entre ratings e gêneros
Tags genômicas mais relevantes

Exemplos de gráficos gerados na pasta images:
avg_ratings_by_genre.png
top_genome_tags.png
rating_value_distribution.png

2. Sistema de Recomendação (SVD)
Implementação de algoritmo híbrido usando:
Truncated SVD para redução dimensional (20 componentes)
k-NN com similaridade por cosseno
Combinação de ratings e tags genômicas

Funcionamento:
Cria matriz esparsa de features (create_feature_matrix())
Redução dimensional com SVD (apply_svd())
Busca por filmes não avaliados usando vizinhos mais próximos

🚀 Como Executar
Baixe o dataset do Kaggle e coloque na pasta Dataset

Execute as análises:
python data_overview.py
python genre_analysis.py
python ratings_distribution.py
python ratings_movies_analysis.py
python genome_analysis.py

Execute o sistema de recomendação:
python svd.py

Entrada/Saída esperada:
Exemplos de IDs de usuários válidos: [1, 2, 3, ..., 162541]
Digite o ID do usuário para recomendações: 123
Top recomendações para o usuário 123:
• Filme ID 550: Score 4.80
• Filme ID 122: Score 4.75
• Filme ID 318: Score 4.70

⚠️ Considerações
Requer mínimo 8GB de RAM
Processamento inicial demora ~15 minutos
IDs de usuário devem estar entre 1 e 162541
Gráficos são salvos automaticamente na pasta images

📌 Conclusão
Sistema completo para análise de dados cinematográficos e recomendações personalizadas usando decomposição matricial (SVD) e filtragem colaborativa.
