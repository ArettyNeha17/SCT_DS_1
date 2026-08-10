import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# SkillCraft Technology - Data Science
# Task 01: Population Age Distribution
# ==========================================

# Load the dataset
df = pd.read_csv("population_age.csv")

# Display the first few rows
print("First 10 records:")
print(df.head(10))

# Display information about the dataset
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df["Age"].describe())

# ==========================================
# Create Histogram
# ==========================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["Age"],
    bins=10,
    edgecolor="black"
)

# Add title and axis labels
plt.title("Population Age Distribution", fontsize=16)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Number of People", fontsize=12)

# Add grid
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Adjust layout
plt.tight_layout()

# Save the chart
plt.savefig("age_distribution.png", dpi=300, bbox_inches="tight")

# Display the chart
plt.show()

print("\nTask 01 completed successfully!")
print("Chart saved as: age_distribution.png")