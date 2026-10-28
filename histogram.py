import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("datasets/dataset_train.csv")
    maisons = df["Hogwarts House"].dropna().unique()
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
        print("matiere: ", matiere,"\n")
        print("--------------------------------\n")
        data = []
        for maison in maisons:
            data = df[df["Hogwarts House"] == maison][matiere].dropna()
            print("maison: ", maison,"\n")
        fig,ax = plt.subplots(2,2)
        ax[0,0].hist(df[df["Hogwarts House"] == maisons[0]][matiere].dropna())
        ax[0,0].set_title(f"Histogram of {matiere} ----  in {maisons[0]}")
        ax[0,1].hist(df[df["Hogwarts House"] == maisons[1]][matiere].dropna())
        ax[0,1].set_title(f"Histogram of {matiere} ----  in {maisons[1]}")
        ax[1,0].hist(df[df["Hogwarts House"] == maisons[2]][matiere].dropna())
        ax[1,0].set_title(f"Histogram of {matiere} ----  in {maisons[2]}")
        ax[1,1].hist(df[df["Hogwarts House"] == maisons[3]][matiere].dropna())
        ax[1,1].set_title(f"Histogram of {matiere} ----  in {maisons[3]}")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()