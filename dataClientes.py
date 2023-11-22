import pandas as pd
import numpy as np

np.random.seed(42)

n_samples = 1000
categorias = ['Electrónicos', 'Ropa', 'Hogar', 'Deportes']
generos = ['Mujer', 'Hombre']

data = {
    'Categoria': np.random.choice(categorias, n_samples),
    'Genero': np.random.choice(generos, n_samples)
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo de Excel
df.to_excel('dataClientes.xlsx', index=False)
