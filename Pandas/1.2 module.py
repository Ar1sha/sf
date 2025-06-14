import pandas as pd
melb = pd.read_csv('D:\sf\Pandas\data\melb_data.csv', sep=',')
melb_df = melb.copy()
melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
total_rooms = melb_df['Bathroom']+melb_df['Rooms']+melb_df['Bedroom']
melb_df['MeanRoomsArea'] = melb_df['BuildingArea'] / total_rooms
diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
melb_df['WeekSale'] = (melb_df['Date'].dt.dayofweek)
weekend_count = ((melb_df['WeekSale'])>=5).sum()
# print(melb_df['Address'].nunique())
def get_street_type(address):
    exclude_list = ['N', 'S', 'W', 'E']
    address_list = address.split(' ')
    street_type = address_list[-1]
    if street_type in exclude_list:
        street_type = address_list[-2]
    return street_type
street_types = melb_df['Address'].apply(get_street_type)
popular_stypes = street_types.value_counts().nlargest(10).index
melb_df['Street_type']= street_types.apply(lambda x: x if x in popular_stypes else 'other')
def get_weekend(weekday):
    return 1 if weekday in [5,6] else 0
melb_df['Weekend'] = melb_df['WeekSale'].apply(get_weekend)
mean_price_weekend = melb_df[melb_df['Weekend']==1]['Price'].mean()
popular_sellorG = melb_df['SellerG'].value_counts().nlargest(49).index
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_sellorG else 'other')
Nelson_price = melb_df[melb_df['SellerG']=='Nelson']['Price'].min()
other_price = melb_df[melb_df['SellerG']=='other']['Price'].min()
Suburb_main = melb_df['Suburb'].value_counts().nlargest(119).index
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x:x if x  in Suburb_main else 'other' )

melb_df = melb_df.drop('Address', axis=1)
melb_df2 = pd.read_csv('D:\sf\Pandas\data\melb_df.csv', sep=',')
# reports = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')
# reports['Time']= pd.to_datetime(reports['Time'], dayfirst=False)
# reports_year = reports['Time'].dt.year
# reports_NV = reports[reports['State']== 'NV']
melb_df2['Date']= pd.to_datetime(melb_df2['Date'])
date_quater = melb_df2['Date'].dt.quarter

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
max_uniqe = 150  
for col in melb_df2.columns:
    if melb_df2[col].nunique()<max_uniqe and col not in cols_to_exclude:
        melb_df2[col] = melb_df2[col].astype('category')

# print(melb_df2.sort_values(by='AreaRatio', ascending=False, ignore_index=True).loc[1558, 'BuildingArea'])
maskType = melb_df2['Type']=='townhouse'
maskRooms = melb_df2['Rooms']>2
# print(melb_df2[maskType & maskRooms].sort_values(by=['Rooms', 'MeanRoomsSquare'], ascending=[True, False], ignore_index=True).iloc[18]['Price"])
# print(melb_df2.groupby('Regionname')['Distance'].min().sort_values(ascending=False))
# print(melb_df2.groupby(['MonthSale'])['Price'].agg(['count','mean', 'max']).sort_values(by='count', ascending=False))
# print(melb_df2.groupby('Type')['Price'].agg('describe'))
# print(melb_df2.groupby(by='Rooms')['Price'].agg('describe'))
# print(melb_df2.groupby(by='Regionname')['Lattitude'].agg('describe'))
spt = pd.to_datetime('01.09.2017', dayfirst=True)
may = pd.to_datetime('01.05.2017')
maskDate=  (spt>melb_df2['Date'])& (melb_df2['Date']>may)
# print(melb_df2.groupby('SellerG')['Date'])
filter_spt_may = melb_df2[maskDate]
# print(filter_spt_may.groupby('SellerG')['Price'].agg(['count']).sort_values(by='count', ascending=True))
pivot = melb_df2.pivot_table(
    values='BuildingArea',
    index='Type',
    columns='Rooms',
    aggfunc=['median'],
    fill_value=0
)
pivot2=melb_df2.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc=['median'],
    fill_value=0
)
print(pivot2['median']['unit'].sort_values())