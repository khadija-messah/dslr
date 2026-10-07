import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("datasets/dataset_train.csv")
    print(df)

if __name__ == "__main__":
    main()