import pandas as pd  

df = pd.read_csv('input.csv')

column_names = df.columns

print(df)
print(column_names)


keywords = column_names[1::]

print(keywords)

urls = df["url"].to_list()
print(urls)