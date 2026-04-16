import pandas as pd


df1 = pd.read_csv('./data/daily_sales_data_0.csv')
df2 = pd.read_csv('./data/daily_sales_data_1.csv')
df3 = pd.read_csv('./data/daily_sales_data_2.csv')


df = pd.concat([df1, df2, df3], ignore_index=True)


df = df[df['product'] == 'pink morsel']


df['price'] = df['price'].astype(str).str.replace('$', '').astype(float)
df['sales'] = df['quantity'] * df['price']


final_df = df[['sales', 'date', 'region']]


final_df.to_csv('formatted_data.csv', index=False)
print("Data successfully cleaned and saved to formatted_data.csv!")