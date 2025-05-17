import pandas as pd

# set options
pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)

# load dataframe from csv
df = pd.read_csv("../data/enterprise_saas_segment_data.csv")

# remove CostToServe from AvgRevenue
df["NetAvgRevenue"] = df["AvgRevenue"] - df["CostToServe"]

# define scoring weights (totals to 1)
score_weights = {
    "NetAvgRevenue": 1,
    "RetentionRate": 0,
    "ExpansionPotential": 0,
    "StrategicFit": 0
}

# normalize each column (min-max scale)
for column in score_weights:
    if score_weights[column] >= 0:
        df[f"{column}_normal"] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    else:
        df[f"{column}_normal"] = (df[column].max() - df[column]) / (df[column].max() - df[column].min())

# compute weighted scores
df["WeightedScore"] = sum(df[f"{column}_normal"] * abs(score_weights[column]) for column in score_weights)

# group by segment and calculate avg of all numeric columns
segment_summary = df.groupby("Segment").agg({
    "WeightedScore": "mean",
    "NetAvgRevenue": "mean",
    "RetentionRate": "mean",
    "ExpansionPotential": "mean",
    "StrategicFit": "mean"
}).reset_index()

# sort by highest WeightedScore
segment_summary = segment_summary.sort_values(by="WeightedScore", ascending=False)

# export to csv
segment_summary.to_csv("../data/summary_revenue_weighted.csv", index=False)

# round for readability and print
segment_summary = segment_summary.round(2)
print(segment_summary)