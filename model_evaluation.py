import pandas as pd

# =========================================
# LOAD FINAL THEFT DETECTION RESULTS
# =========================================

df = pd.read_csv("final_theft_detection_result.csv")

df.columns = df.columns.str.strip()

# Standardize Status
df["Status"] = (
    df["Status"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# Convert Power Difference
df["Power_Difference"] = pd.to_numeric(
    df["Power_Difference"],
    errors="coerce"
)

# Remove invalid values
df = df.dropna(
    subset=["Power_Difference"]
).reset_index(drop=True)


# =========================================
# BASIC COUNTS
# =========================================

total = len(df)

normal_count = (
    df["Status"] == "NORMAL"
).sum()

theft_count = (
    df["Status"] == "THEFT SUSPECTED"
).sum()

theft_percentage = (
    theft_count / total * 100
) if total > 0 else 0


# =========================================
# POWER DIFFERENCE STATISTICS
# =========================================

overall_mean = df["Power_Difference"].mean()

normal_mean = df.loc[
    df["Status"] == "NORMAL",
    "Power_Difference"
].mean()

theft_mean = df.loc[
    df["Status"] == "THEFT SUSPECTED",
    "Power_Difference"
].mean()

min_difference = df["Power_Difference"].min()

max_difference = df["Power_Difference"].max()


# =========================================
# FINAL OUTPUT
# =========================================

print("\n======================================")
print("       SMART GRID MODEL EVALUATION")
print("======================================")

print(f"\nTotal Readings        : {total}")
print(f"Normal Readings      : {normal_count}")
print(f"Theft Suspected      : {theft_count}")
print(f"Anomaly Percentage   : {theft_percentage:.2f}%")

print("\n------ POWER DIFFERENCE ------")

print(f"Overall Mean         : {overall_mean:.2f} W")
print(f"Normal Mean          : {normal_mean:.2f} W")
print(f"Theft Mean           : {theft_mean:.2f} W")
print(f"Minimum Difference   : {min_difference:.2f} W")
print(f"Maximum Difference   : {max_difference:.2f} W")


# =========================================
# SAVE SUMMARY
# =========================================

summary = pd.DataFrame({
    "Metric": [
        "Total Readings",
        "Normal Readings",
        "Theft Suspected",
        "Anomaly Percentage",
        "Overall Mean Difference",
        "Normal Mean Difference",
        "Theft Mean Difference",
        "Minimum Difference",
        "Maximum Difference"
    ],

    "Value": [
        total,
        normal_count,
        theft_count,
        round(theft_percentage, 2),
        round(overall_mean, 2),
        round(normal_mean, 2),
        round(theft_mean, 2),
        round(min_difference, 2),
        round(max_difference, 2)
    ]
})

summary.to_csv(
    "model_evaluation_summary.csv",
    index=False
)

print("\nEvaluation completed.")
print("File saved as model_evaluation_summary.csv")