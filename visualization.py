import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("smart_grid_data.csv")

df["Time"] = pd.to_datetime(df["Time"])

plt.figure(figsize=(12,5))
plt.plot(df["Time"], df["Power"])
plt.xlabel("Time")
plt.ylabel("Power (W)")
plt.title("Power Consumption Pattern")
plt.xticks(rotation=45)
plt.grid()
plt.show()


plt.figure(figsize=(12,5))
plt.plot(df["Time"], df["Current"])
plt.xlabel("Time")
plt.ylabel("Current (A)")
plt.title("Current Variation")
plt.xticks(rotation=45)
plt.grid()
plt.show()