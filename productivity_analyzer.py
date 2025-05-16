import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from collections import defaultdict

# Load habit data
habits_df = pd.read_csv("habits.csv", parse_dates=["date"])

# Convert Yes/No to binary
habits_df["exercise"] = habits_df["exercise"].map({"Yes": 1, "No": 0})
habits_df["daily_review"] = habits_df["daily_review"].map({"Yes": 1, "No": 0})

# Load calendar data
with open("calendar_data.json", "r") as f:
    calendar_events = json.load(f)

# Process calendar durations per day
calendar_summary = defaultdict(float)
for event in calendar_events:
    start = datetime.fromisoformat(event["start"])
    end = datetime.fromisoformat(event["end"])
    duration = (end - start).seconds / 3600  # in hours
    calendar_summary[start.date()] += duration

# Merge calendar and habits
# Merge calendar and habits
calendar_df = pd.DataFrame(list(calendar_summary.items()), columns=["date", "calendar_hours"])

# 🔧 Ensure both columns are in datetime format
habits_df["date"] = pd.to_datetime(habits_df["date"])
calendar_df["date"] = pd.to_datetime(calendar_df["date"])

full_df = pd.merge(habits_df, calendar_df, how="left", on="date").fillna(0)


# ---- Analysis Section ---- #

# Correlation matrix
corr = full_df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Between Habits and Productivity")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Scatter plot: Sleep vs Productivity
plt.figure(figsize=(6, 4))
sns.scatterplot(data=full_df, x="sleep_hours", y="productivity_score")
plt.title("Sleep Hours vs Productivity")
plt.tight_layout()
plt.savefig("sleep_vs_productivity.png")
plt.close()

# Insights
print("\n=== Productivity Insights ===")
if full_df["exercise"].corr(full_df["productivity_score"]) > 0.5:
    print("💡 Regular exercise strongly correlates with higher productivity.")
if full_df["sleep_hours"].corr(full_df["productivity_score"]) > 0.5:
    print("💡 More sleep generally means better productivity.")
if full_df["calendar_hours"].corr(full_df["mood"]) < -0.3:
    print("⚠️ More scheduled time correlates with lower mood. Consider more breaks.")
print("✅ Full analysis saved in CSV and PNG visualizations.")

