import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"

data = pd.read_csv("rfm_data.csv")
print(data.head())

from datetime import datetime
import pandas as pd

# Load data (assuming it's already loaded)
# data = pd.read_csv("your_file.csv")

# Ensure 'PurchaseDate' is in datetime format
data['PurchaseDate'] = pd.to_datetime(data['PurchaseDate'], errors='coerce')

# Drop rows with invalid dates if necessary
data.dropna(subset=['PurchaseDate'], inplace=True)

# Calculate Recency
data['Recency'] = (datetime.now() - data['PurchaseDate']).dt.days

# Calculate Frequency
frequency_data = data.groupby('CustomerID')['OrderID'].count().reset_index()
frequency_data.rename(columns={'OrderID': 'Frequency'}, inplace=True)
data = data.merge(frequency_data, on='CustomerID', how='left')

# Calculate Monetary Value
monetary_data = data.groupby('CustomerID')['TransactionAmount'].sum().reset_index()
monetary_data.rename(columns={'TransactionAmount': 'MonetaryValue'}, inplace=True)
data = data.merge(monetary_data, on='CustomerID', how='left')

# Print result
print(data.head())

