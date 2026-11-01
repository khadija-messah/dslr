import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def visualisation_scatter_plot(df, matieres):
    os.makedirs("scatter_plots", exist_ok=True)
    for i, matier1 in enumerate(matieres):
        print(f"Creating scatter plot for {matier1} et index {i}")
        j = i + 1
        while j < len(matieres):
            matier2 = matieres[j]
            plt.figure(figsize=(8, 6))
            plt.scatter(df[matier1], df[matier2], c=df["Hogwarts House"].astype('category').cat.codes, cmap='viridis', alpha=0.5)
            plt.title(f"Scatter Plot: {matier1} vs {matier2}")
            plt.xlabel(matier1)
            plt.ylabel(matier2)
            plt.colorbar(label='Hogwarts House')
            plt.savefig(f"scatter_plots/scatter_plot_{matier1}_vs_{matier2}.png")
            plt.close()
            j += 1

def correlation_matrix(df, matieres):
    for i , matier1 in enumerate(matieres):
        j = i + 1
        while j < len(matieres):
            matier2 = matieres[j]
            correlation = df[matier1].corr(df[matier2])
            print(f"Correlation between {matier1} and {matier2}: {correlation}")
            j += 1
        print("\n")
    print("the two features that are similar are:  astronomy and defense against the dark arts with a correlation of -1.0")


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
    visualisation_scatter_plot(df, matieres)
    correlation_matrix(df, matieres)
if __name__ == "__main__":
    main()