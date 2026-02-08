import pandas as pd

df = pd.read_excel('data/lab_data.xlsx')
print('✅ ALL DATA LOADED SUCCESSFULLY!\n')
print(f'📊 Total Records: {len(df)}')
print(f'🔬 Unique Labs: {df["Lab Name"].nunique()}')
print(f'👥 Unique Riders: {df["Rider Name"].nunique()}')
print('\nData by Lab:')
print(df.groupby('Lab Name').size())
print('\n✅ Your data is ready to use!')
