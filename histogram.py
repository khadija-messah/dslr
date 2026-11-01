import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os 
import Describe


def visualisation_histogramme(df, matiere):
    os.makedirs("histograms", exist_ok=True)
    maisons = df["Hogwarts House"].dropna().unique()
    all_data = df[matiere].dropna()
    bins = np.histogram_bin_edges(all_data, bins=15)
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))
    for i, maison in enumerate(maisons):
        data = df[df["Hogwarts House"] == maison][matiere].dropna()
        ax[i // 2, i % 2].hist(data, bins=bins)
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

def compare_stats(stats, maisons, matiere):
    for maison in maisons:
        print(f"Statistics for {matiere} in {maison}:")
        print(f"Mean: {stats[maison]['mean']:.6f}")
        print(f"Median: {stats[maison]['median']:.6f}")
        print(f"Standard Deviation: {stats[maison]['std_dev']:.6f}")

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
        compare_stats(stats, df["Hogwarts House"].dropna().unique(),matiere)
        print("===============================================")
    print("The four houses have similar score distributions in Care of Magical Creatures. Their means, medians and standard deviations are close, and the histograms show similar shapes")
if __name__ == "__main__":
    main()