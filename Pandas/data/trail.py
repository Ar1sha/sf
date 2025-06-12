import pandas as pd
data = pd.read_csv('D:\sf\Pandas\data\melb_data.csv',encoding='utf-8', sep=',')
data['Car'] = data['Car'].astype('int64')
data['Bedroom'] = data['Bedroom'].astype('int64')
data['Bathroom'] = data['Bathroom'].astype('int64')
data['Propertycount'] = data['Propertycount'].astype('int64')
data['YearBuilt'] = data['YearBuilt'].astype('int64')
# print(data.loc[3521, 'Landsize'] / data.loc[1690, 'Landsize'])
# print(data['Coordinates'].dtype)
# print(data['CouncilArea'].isna().sum())
# print(data.describe().loc[:,['Price']])
# print(data['Distance'].value_counts())
# print(data.describe().loc[:,['BuildingArea']])
# print(data['Propertycount'].value_counts(normalize=True))
# print(data['Distance'].std())
BA_mean = data['BuildingArea'].mean()
BA_median = data['BuildingArea'].median()
# print(abs(BA_mean - BA_median)/BA_mean)
x = [1, 2, 4, 2, 3, 2, 1, 5, 6]
x_moda = pd.Series(x).mode()
# print(data['Bedroom'].mode())
# mask1 = data['Bathroom'] == 0
# print(data[mask].shape[0])
# mask2 = data[(data['SellerG']== 'Nelson') & (data['Price']>3000000)].shape[0]
# mask3 = data[data['BuildingArea']==0]['Price'].min()
# mask4 = data[(data['Price']>1000000) & ((data['Rooms']>5) | (data['YearBuilt']<2015))].shape[0]
# mask5 = data[(data['Price']<3000000) &(data['Type']=='h')].mode()



