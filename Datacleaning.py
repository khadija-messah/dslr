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
def Mymin(column):
    min_value = float('inf')
    for value in column:
        if value < min_value:
            min_value = value
    return min_value
def Mymax(column):
    max_value = float('-inf')
    for value in column:
        if value > max_value:
            max_value = value
    return max_value
def StandardDeviation(column, mean, count):
    sum = 0
    for value in column:
        sum += (value - mean) ** 2
    variance = sum / count if count > 0 else 0
    std_dev = variance ** 0.5
    return std_dev

def MyDescribe(df):

    print("Describing data...")
    countdf = len(df)
    meanArithmancy = Mymean(df["Arithmancy"],countdf)
    meanAstronomy = Mymean(df["Astronomy"],countdf)
    meanHerbology = Mymean(df["Herbology"],countdf)

    std_devArithmancy = StandardDeviation(df["Arithmancy"], meanArithmancy, countdf)
    std_devAstronomy = StandardDeviation(df["Astronomy"], meanAstronomy, countdf)
    std_devHerbology = StandardDeviation(df["Herbology"], meanHerbology, countdf)

    minArithmancy = Mymin(df["Arithmancy"])
    minAstronomy = Mymin(df["Astronomy"])
    minHerbology = Mymin(df["Herbology"])

    maxArithmancy = Mymax(df["Arithmancy"])
    maxAstronomy = Mymax(df["Astronomy"])
    maxHerbology = Mymax(df["Herbology"])

def main():
    if not ParcingFile():
        return
    DataCleaning()
if __name__ == "__main__":
    main()