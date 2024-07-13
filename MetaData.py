
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# defining file path we are in the same folder
file_path = "Life Expectancy Data.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame to verify it was imported correctly
print(df.head())



# Plot histograms for all numerical columns
plt.figure(figsize=(15, 10))
df.hist(bins=20, edgecolor='black', linewidth=1.2, grid=False)
plt.tight_layout()
plt.show()

# Box plots for selected numerical columns
plt.figure(figsize=(15, 10))
sns.boxplot(data=df[['Life expectancy ', 'Adult Mortality', 'Alcohol', 'BMI ', 'GDP']])
plt.title('Box Plots of Selected Columns')
plt.xticks(rotation=45)
plt.show()

data.drop_duplicates(implace=True)

