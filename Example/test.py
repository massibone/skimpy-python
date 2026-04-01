import pandas as pd
import os

# Percorso temporaneo per il test
test_csv = "test_data.csv"

# 1. Preparazione dati fittizi
data = {'col1': [1, 2, None, 4],
        'col2': ['a', 'b', 'c', None],
        'value': [10, 20, 30, 40]}
pd.DataFrame(data).to_csv(test_csv, index=False)

# 2. Caricamento
df = pd.read_csv(test_csv)  # o qua la nostra load_csv

# 3. Pulizia selettiva rimuovendo righe con NA in 'col2'
cleaned = df.dropna(subset=['col2'])

# 4. Riassunto e piccola verifica
print(cleaned.describe())
print(cleaned.head())

# 5. Salvataggio e istogramma
cleaned.head(2).to_csv("subset.csv", index=False)
from skimpy import plot_hist
plot_hist(df, 'value', save_path="hist.png", show=False)

# 6. Pulizia test
os.remove(test_csv)
os.remove("subset.csv")
os.remove("hist.png")
