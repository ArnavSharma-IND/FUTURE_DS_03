import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./bank/bank-full.csv", sep=";")

df["Conversion"] = df["y"].map({
    "yes": 1,
    "no": 0
})

total = len(df)
converted = df["Conversion"].sum()
not_converted = total - converted
conversion_rate = converted / total * 100

print("="*50)
print(f"Total Customers Contacted: {total}")
print(f"Converted Customers: {converted}")
print(f"Not Converted: {not_converted}")
print(f"Conversion Rate: {conversion_rate:.2f}%")
print("="*50)

contact = df.groupby("contact")["Conversion"].mean()*100

plt.figure(figsize=(8,5))
contact.plot(kind="bar")
plt.title("Conversion Rate by Contact Type")
plt.ylabel("Conversion Rate (%)")
plt.show()

job = df.groupby("job")["Conversion"].mean()*100

plt.figure(figsize=(10,5))
job.sort_values().plot(kind="barh")
plt.title("Conversion Rate by Job")
plt.xlabel("Conversion Rate (%)")
plt.show()

month = df.groupby("month")["Conversion"].mean()*100

plt.figure(figsize=(8,5))
month.plot(marker='o')
plt.title("Conversion Rate by Month")
plt.ylabel("Conversion Rate (%)")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["age"], bins=20)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()