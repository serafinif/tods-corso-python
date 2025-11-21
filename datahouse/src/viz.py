from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_hist_price(df: pd.DataFrame):
    Path("output/grafici").mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8, 5))
    sns.histplot(df["price"], bins=50, color="skyblue", kde=True)
    plt.title("Distribuzione Prezzi Case")
    plt.xlabel("Prezzo ($)")
    plt.tight_layout()
    plt.savefig("output/grafici/hist_price.png", dpi=150)
    plt.close()


def plot_price_by_bedrooms(df: pd.DataFrame):
    plt.figure(figsize=(8, 5))
    sns.barplot(x="bedrooms", y="price", data=df, estimator="mean", ci=None)
    plt.title("Prezzo medio per numero camere")
    plt.savefig("output/grafici/price_by_bedrooms.png", dpi=150)
    plt.close()


def plot_price_by_waterfront(df: pd.DataFrame):
    plt.figure(figsize=(6, 5))
    sns.boxplot(x="waterfront", y="price", data=df)
    plt.title("Prezzo per vista mare (0=no, 1=sì)")
    plt.savefig("output/grafici/price_by_waterfront.png", dpi=150)
    plt.close()


def plot_corr_heatmap(df: pd.DataFrame):
    corr = df[["price", "sqft_living", "bedrooms", "bathrooms", "grade", "condition"]].corr()
    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlazione tra variabili numeriche")
    plt.tight_layout()
    plt.savefig("output/grafici/correlation_heatmap.png", dpi=150)
    plt.close()
