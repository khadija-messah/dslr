import sys
from pathlib import Path
import pandas as pd

def ParcingFile():
    if len(sys.argv) != 2:
        print("Incorrect number of arguments. Please provide exactly one argument.")
        return False
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"The provided path '{path}' is not a valid file.")
        return False
    return True

def DataCleaning():
    df = pd.read_csv(sys.argv[1])
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.drop(columns = "First Name")
    df = df.drop(columns = "Last Name")
    df = df.drop(columns = "Birthday")
    df = df.drop(columns = "Best Hand")
    df = df.drop(columns = "Index")
    MyDescribe(df)

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


def MyMedian(column):
    sorted_column = sorted(column)
    n = len(sorted_column)
    if n % 2 == 1:
        median = sorted_column[n // 2]
    else:
        median = (sorted_column[n // 2 - 1] + sorted_column[n // 2]) / 2
    return median
def Myquartile25(column):
    sorted_column = sorted(column)
    n = len(sorted_column)
    quartile_index = n // 4
    if quartile_index > 0:
        return sorted_column[quartile_index - 1]
    else:
        return sorted_column[0]

def Myquartile75(column):
    sorted_column = sorted(column)
    n = len(sorted_column)
    quartile_index = 3 * n // 4
    if quartile_index < n:
        return sorted_column[quartile_index]
    else:
        return sorted_column[n - 1]

def MyDescribe(df):

    countdf = len(df)
    print("arithmancy     astronomy     herbology")
    data = [{
        "count": countdf,
        "countArithmancy": countdf,
        "countAstronomy": countdf,
        "countHerbology": countdf
    }]

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

    medianArithmancy = MyMedian(df["Arithmancy"])
    medianAstronomy = MyMedian(df["Astronomy"])
    medianHerbology = MyMedian(df["Herbology"])
    
    quartile25Arithmancy = Myquartile25(df["Arithmancy"])
    quartile25Astronomy = Myquartile25(df["Astronomy"])
    quartile25Herbology = Myquartile25(df["Herbology"])

    quartile75Arithmancy = Myquartile75(df["Arithmancy"])
    quartile75Astronomy = Myquartile75(df["Astronomy"])
    quartile75Herbology = Myquartile75(df["Herbology"])


def main():
    if not ParcingFile():
        return
    DataCleaning()
if __name__ == "__main__":
    main()