# skimpy

Piccola libreria Python per caricamento, ispezione, pulizia e visualizzazione rapida di dataset tabulari (CSV/JSON).

## Caratteristiche

- Caricamento di file CSV e JSON
- Anteprima rapida dei dati con `head()`
- Sommario statistico con `summary()`
- Pulizia base: rimozione NaN, rinomina colonne
- Esportazione dati puliti in CSV
- Grafici base con matplotlib e seaborn
- CLI minima per uso rapido da terminale

## Struttura del progetto

```text
skimpy/
├── README.md
├── pyproject.toml
├── .gitignore
├── LICENSE
├── skimpy/
│   ├── __init__.py
│   ├── io.py
│   ├── inspect.py
│   ├── viz.py
│   ├── clean.py
│   └── cli.py
├── tests/
├── examples/
```

## Installazione


git clone <URL_DEL_TUO_REPO>
cd skimpy
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install pandas matplotlib seaborn


## Uso come libreria


from skimpy.io import load_csv, save_csv
from skimpy.inspect import head, summary
from skimpy.clean import drop_na, rename_cols
from skimpy.viz import plot_hist

df = load_csv("data/sample.csv")

print(head(df, 5))
print(summary(df))

cleaned = drop_na(df)
cleaned = rename_cols(cleaned, {"old_name": "new_name"})

save_csv(cleaned, "output/cleaned.csv")
plot_hist(cleaned, "value", save_path="output/value_hist.png", show=False)


## Uso da terminale

python -m skimpy.cli data/sample.csv


## Note privacy

- Non caricare dati sensibili nel repository.
- Aggiungi a `.gitignore` cartelle come `data/`, `output/`, `.venv/` e file temporanei.

## Roadmap MVP

- Supporto CSV/JSON
- Head, summary, info
- Drop NaN e rinomina colonne
- Istogramma, scatter, boxplot
- Export CSV
- CLI minima

