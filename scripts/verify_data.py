import pandas as pd

# set options
pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)

# load dataframe from csv
df = pd.read_csv("../data/enterprise_saas_segment_data.csv")
print(df.head())

# check for nulls
print(df.isnull().sum())

# check types
print(df.dtypes)

# check ranges
print(df.describe())

# check row / column count
print(f"\nDataFrame Contains {df.shape[0]} rows and {df.shape[1]} columns")

# check for distribution bias
print(df["Segment"].value_counts())