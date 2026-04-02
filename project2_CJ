
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BC Census 2016 data.csv")

df.head()
df.info()
df.describe()

high_stress = df[df["shelt_rent_30plus_rate"] > 50]

task1 = high_stress[[
    "chsa",
    "pha",
    "shelt_rent_30plus_rate",
    "shelt_rent_subsidized_rate",
    "shelt_rent_mo_cost_mean",
    "income_after_tax_mean"
]].sort_values("shelt_rent_30plus_rate", ascending=False)

task1
task1["rent_to_income_ratio"] = (
    task1["shelt_rent_mo_cost_mean"] * 12
) / task1["income_after_tax_mean"]

task1


task2 = df.groupby("pha").agg({
    "shelt_rent_subsidized_rate": ["mean", "median"],
    "shelt_rent_30plus_rate": "mean",
    "shelt_rent_mo_cost_mean": "mean",
    "income_after_tax_mean": "mean"
}).round(2)

# Clean column names
task2.columns = ["_".join(col) for col in task2.columns]

task2
task2["shelt_rent_subsidized_rate_mean"].plot(
    kind="bar",
    title="Average Rental Subsidization Rate by PHA",
    ylabel="Subsidization Rate (%)",
    xlabel="Provincial Health Authority"
)

plt.show()

summary = df.groupby("pha")[[
    "shelt_rent_subsidized_rate",
    "shelt_rent_30plus_rate"
]].mean().round(2)

summary
