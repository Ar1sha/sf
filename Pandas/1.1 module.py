import pandas as pd
# contries = pd.Series({
#     'UK':'England',
#     'CA':'Canada',
#     'RU': 'Russia'
# },
# name = 'contries')
# print(contries.loc[['UK','RU']])
contries_df = pd.DataFrame({
    'country':['England', 'Canada', 'USA'],
    'population':['52.29', '38.05', '322.28'],
    'area': [133396, 9984679, 9392919]
})
contries_df.index = ['UK', 'CA', 'US']
x = contries_df.mean(axis = 0, numeric_only = True)
# print(contries_df)
contries_df.to_csv('D:\sf\Pandas\data\contries.csv', index=False, sep=';')