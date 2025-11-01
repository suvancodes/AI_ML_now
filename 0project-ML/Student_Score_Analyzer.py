import pandas as pd
import numpy as np

data = {
    'Name': ['Ram', 'Sita', 'Laxman', 'Hanuman'],
    'Maths': [80, 95, 70, 88],
    'Physics': [75, 85, 80, 90],
    'Chemistry': [82, 78, 85, 88]
}

df = pd.DataFrame(data)


df['total'] = df[['Maths','Physics','Chemistry']].sum(axis=1)
df['Average'] = np.round(df['total']/3,2)
df['Grade'] = df['Average'].apply(lambda x: 'A' if x >= 85 else 'B' if x >= 70 else 'C')

topper = df.loc[df['total'].idxmax()]
print('topper is: ',topper['Name'])

print(df)

df.to_csv('result.csv',index=False)


# pd.DataFrame()	Converts dictionary to DataFrame (table format)
# .sum(axis=1)	Sums values across columns for each row
# np.round(value, 2)	Rounds numerical values to 2 decimal places
# .apply(lambda x: ...)	Applies a custom function to each element
# .idxmax()	Returns index of the max value in a column
# .loc[]	Accesses specific row(s) by index
# .to_csv()	Exports DataFrame to a CSV file

