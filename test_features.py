import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv('初中物理data_difficulty.csv')

train, test = train_test_split(data, test_size=0.2, random_state=42)

train.to_csv('Train-d.csv', index=False)
test.to_csv('Test-d.csv', index=False)
