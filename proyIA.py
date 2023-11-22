import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Se carga los datos desde un archivo Excel
df = pd.read_excel('dataClientes.xlsx')

# Se codifica las variables categóricas a numéricas
label_encoder = LabelEncoder()
df['Categoria_Encoded'] = label_encoder.fit_transform(df['Categoria'])
df['Genero_Encoded'] = label_encoder.fit_transform(df['Genero'])

print("\nDataFrame después de la codificación:")
print(df.head())

# Se selecciona las características relevantes
features = df[['Categoria_Encoded', 'Genero_Encoded']]

# Se prueba diferentes números de clusters
for num_clusters in range(2, 6):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(features)
    silhouette_avg = silhouette_score(features, kmeans.labels_)
    print(f'Número de Clusters: {num_clusters}, Índice de Silueta: {silhouette_avg}')

    # Visualiza los resultados para num_clusters = 5
    if num_clusters == 5:
        plt.scatter(features['Categoria_Encoded'], features['Genero_Encoded'], c=kmeans.labels_, cmap='viridis')
        plt.xlabel('Categoria')
        plt.ylabel('Genero')
        plt.title(f'Segmentación de Clientes con K-Means (Clusters = {num_clusters})')
        plt.show()

# Se imprime el DataFrame con las etiquetas de cluster
df['Cluster'] = kmeans.labels_
print(df.head())
