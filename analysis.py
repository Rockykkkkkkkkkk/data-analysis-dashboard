import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/sample_data.csv")

print(data.head())

data.describe()

plt.figure()
data["value"].hist()
plt.title("Data Distribution")
plt.show()
