import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# define folder
input_folder = "../output/"

# grab all CSVs (skip visuals or final summary if needed)
csv_files = [f for f in glob.glob(os.path.join(input_folder, "*.csv")) if "final" not in f]

# for each file: load, create chart, save
for filepath in csv_files:
    df = pd.read_csv(filepath)

    # skip files without a weighted score
    score_column = "WeightedScore"
    if "WeightedScore_Avg" in df.columns:
        score_column = "WeightedScore_Avg"
    elif score_column not in df.columns:
        print(f"Skipping {filepath} — no score column found.")
        continue

    # create chart
    plt.figure(figsize=(8, 4))
    df_sorted = df.sort_values(by=score_column, ascending=True)
    plt.barh(df_sorted["Segment"], df_sorted[score_column], color="skyblue")
    plt.xlabel("Score")
    plt.title(f"Segment Scores — {os.path.basename(filepath).replace('.csv', '')}")
    plt.tight_layout()

    # save chart
    filename = os.path.basename(filepath).replace(".csv", ".png")
    chart_path = os.path.join("../output/charts/", filename)
    plt.savefig(chart_path)
    plt.close()