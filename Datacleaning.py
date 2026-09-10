import sys
from pathlib import Path
import pandas as pd

def ParcingFile():
    print("Parsing file...")
    if len(sys.argv) != 2:
        print("Incorrect number of arguments. Please provide exactly one argument.")
        return False
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"The provided path '{path}' is not a valid file.")
        return False
    print("parsing file completed successfully.")
    return True

def DataCleaning():
    print("Cleaning data...")
    df = pd.read_csv(sys.argv[1])
    print(len(df))
    df = df.dropna()
    print(len(df))
    df = df.drop_duplicates()
    print(len(df))
    df = df.drop(columns = "First Name")
    df = df.drop(columns = "Last Name")
    df = df.drop(columns = "Birthday")
    df = df.drop(columns = "Best Hand")
    df = df.drop(columns = "Index")
    MyDescribe(df)
    print("Data cleaning completed successfully.")

def Mymean(column, count):
    sum = 0
    for value in column:
        sum += value
    mean = sum / count if count > 0 else 0
    return mean

def MyDescribe(df):
    print("Describing data...")
    countdf = len(df)
    meanArithmancy = Mymean(df["Arithmancy"],countdf)
    meanAstronomy = Mymean(df["Astronomy"],countdf)
    meanHerbology = Mymean(df["Herbology"],countdf)
    print(f"DataFrame length: {countdf}")
    print(f"Mean of Arithmancy column: {meanArithmancy}, mean described by pandas: {df['Arithmancy'].mean()}")
    print(f"Mean of Astronomy column: {meanAstronomy}, mean described by pandas: {df['Astronomy'].mean()}")
    print(f"Mean of Herbology column: {meanHerbology}, mean described by pandas: {df['Herbology'].mean()}")
    print("Data description completed successfully.")


def main():
    if not ParcingFile():
        return
    DataCleaning()
if __name__ == "__main__":
    main()