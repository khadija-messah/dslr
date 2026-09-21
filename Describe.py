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

    df = df.select_dtypes(include="number")
    countdf = len(df)
    data = {
        "count":[],
        "mean":[],
        "std":[],
        "min":[],
        "25%":[],
        "50%":[],
        "75%":[],
        "max":[]
    }
    for i in df:
        data["count"].append(countdf)
        data["mean"].append(Mymean(df[i],countdf))
        data["std"].append(StandardDeviation(df[i],Mymean(df[i],countdf),countdf))
        data["min"].append(Mymin(df[i]))
        data["25%"].append(Myquartile25(df[i]))
        data["50%"].append(MyMedian(df[i]))
        data["75%"].append(Myquartile75(df[i]))
        data["max"].append(Mymax(df[i]))

    print("      ", end="")
    columns = df.columns
    for column in columns:
        print(column, "|",end="")
    print()
    for i in data:
        print(i,"  ",end="")
        for a in data[i]:
            print(f"{a:.6f}"," ",end="")
        print()

def main():
    if not ParcingFile():
        return
    DataCleaning()
if __name__ == "__main__":
    main()