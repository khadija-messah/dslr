import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os 
import Describe
def visualisation_histogramme(df, matiere):
    os.makedirs("histograms", exist_ok=True)
    maisons = df["Hogwarts House"].dropna().unique()
    fig, ax = plt.subplots(2, 2, figsize=(10, 8))
    for i, maison in enumerate(maisons):
        data = df[df["Hogwarts House"] == maison][matiere].dropna()
        ax[i // 2, i % 2].hist(data, bins=20, alpha=0.7)
        ax[i // 2, i % 2].set_title(f"Histogram of {matiere} in {maison}")
        ax[i // 2, i % 2].set_xlabel(matiere)
        ax[i // 2, i % 2].set_ylabel("Frequency")
    plt.tight_layout()
    fig.savefig(f"histograms/histogram_{matiere}.png")
    plt.close(fig)

def calcule_stats(df, matiere):
    maisons = df["Hogwarts House"].dropna().unique()
    stats = {}
    for maison in maisons:
        data = df[df["Hogwarts House"] == maison][matiere].dropna()
        stats[maison] = {
            "mean": Describe.Mymean(data, len(data)),
            "median": Describe.MyMedian(data),
            "std_dev": Describe.StandardDeviation(data, Describe.Mymean(data, len(data)), len(data)),
        }
    return stats
def main():
    df = pd.read_csv("datasets/dataset_train.csv")
    matieres = [
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination",
        "Muggle Studies",
        "Ancient Runes",
        "History of Magic",
        "Transfiguration",
        "Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying"
    ]

    for matiere in matieres:
        visualisation_histogramme(df, matiere)
        stats = calcule_stats(df, matiere)
        for maison, stat in stats.items():
            print(f"Stats for {matiere} in {maison}:")
            for key, value in stat.items():
                print(f"  {key}: {value}")
        print("--------------------------------------------------------")
if __name__ == "__main__":
    main()