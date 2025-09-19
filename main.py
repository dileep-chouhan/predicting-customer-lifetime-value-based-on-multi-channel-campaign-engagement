import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# --- 1. Synthetic Data Generation ---
np.random.seed(42)  # for reproducibility
num_customers = 500
data = {
    'CustomerID': range(1, num_customers + 1),
    'Channel': np.random.choice(['Email', 'Social Media', 'Search', 'Display'], size=num_customers),
    'CampaignSpend': np.random.uniform(10, 100, size=num_customers),
    'EngagementScore': np.random.randint(1, 11, size=num_customers), # 1-10 scale
    'CLV': np.random.exponential(scale=500, size=num_customers) #Exponential distribution for CLV
}
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Feature Engineering ---
#No significant cleaning needed for synthetic data, but real-world data would require handling missing values etc.
# --- 3. Analysis ---
# Analyze CLV by channel
clv_by_channel = df.groupby('Channel')['CLV'].agg(['mean', 'median', 'count'])
print("\nCLV by Channel:\n", clv_by_channel)
#Correlation analysis between CampaignSpend and CLV
correlation, p_value = stats.pearsonr(df['CampaignSpend'], df['CLV'])
print(f"\nCorrelation between Campaign Spend and CLV: {correlation:.2f} (p-value: {p_value:.3f})")
# --- 4. Visualization ---
# Bar plot of average CLV by channel
plt.figure(figsize=(10, 6))
sns.barplot(x='Channel', y='CLV', data=df, estimator=np.mean)
plt.title('Average Customer Lifetime Value by Channel')
plt.xlabel('Marketing Channel')
plt.ylabel('Average CLV')
plt.tight_layout()
plt.savefig('clv_by_channel.png')
print("Plot saved to clv_by_channel.png")
#Scatter plot of CampaignSpend vs CLV
plt.figure(figsize=(10,6))
sns.scatterplot(x='CampaignSpend', y='CLV', data=df)
plt.title('Campaign Spend vs. Customer Lifetime Value')
plt.xlabel('Campaign Spend')
plt.ylabel('CLV')
plt.savefig('campaign_spend_vs_clv.png')
print("Plot saved to campaign_spend_vs_clv.png")
#Further analysis could involve regression modeling to predict CLV based on channel and spend.  This example focuses on basic descriptive statistics and visualization.