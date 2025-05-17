import pandas as pd
import glob
import os

# define folder
outputs = "../output/"

# gather all relevant CSVs in folder (excluding the final if it already exists)
csv_files = [f for f in glob.glob(os.path.join(outputs, "*.csv")) if "score_summary" not in f]

# load all files into a list of DataFrames
dfs = [pd.read_csv(f) for f in csv_files]

# merge on 'Segment' starting with the first DataFrame
combined_df = dfs[0].copy()
combined_df = combined_df.rename(columns=lambda c: c if c == "Segment" else f"{c}_1")

for i, df in enumerate(dfs[1:], start=2):
    df = df.rename(columns=lambda c: c if c == "Segment" else f"{c}_{i}")
    combined_df = pd.merge(combined_df, df, on="Segment", how="inner")

# average all numeric columns (excluding 'Segment')
metrics = [col for col in combined_df.columns if col != "Segment"]
combined_df["WeightedScore_Avg"] = combined_df[[c for c in metrics if "WeightedScore" in c]].mean(axis=1)

# average other columns too
if any("NetAvgRevenue" in c for c in metrics):
    combined_df["NetAvgRevenue_Avg"] = combined_df[[c for c in metrics if "NetAvgRevenue" in c]].mean(axis=1)

# keep only segment and final scores
final_summary = combined_df[["Segment", "WeightedScore_Avg"]]
final_summary = final_summary.sort_values(by="WeightedScore_Avg", ascending=False).round(3)

# export to CSV
final_summary.to_csv("../output/score_summary.csv", index=False)