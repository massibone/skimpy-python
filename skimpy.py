# skimpy.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from pathlib import Path

def load_csv(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"{path} non trovato")
    return pd.read_csv(path)

def head(df, n=5):
    return df.head(n)

def summary(df):
    return df.describe(include='all').transpose()

def drop_na(df, subset=None):
    return df.dropna(subset=subset)

def rename_cols(df, mapping):
    return df.rename(columns=mapping)

def save_csv(df, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

def plot_hist(df, column, bins=30, show=True, save_path=None):
    plt.figure(figsize=(7,4))
    sns.histplot(df[column].dropna(), bins=bins, kde=False)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: python skimpy.py <csv_path>")
        sys.exit(1)
    csv_path = sys.argv[1]
    df = load_csv(csv_path)
    print("Prime righe:")
    print(head(df, 5))
    print("\nSommario:")
    print(summary(df))
    # esempio: salva le prime 100 righe pulite
    cleaned = drop_na(df)
    save_csv(cleaned.head(100), "output/clean_head_100.csv")
    # se esiste una colonna numerica chiamata 'value', creiamo istogramma
    if 'value' in df.columns:
        plot_hist(df, 'value', save_path="output/value_hist.png", show=False)
        print("Istogramma salvato in output/value_hist.png")

if __name__ == "__main__":
    main()
