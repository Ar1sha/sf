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
print(melb_df.info())
melb_df = melb_df.drop('Address', axis=1)
reports = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')
reports['Time']= pd.to_datetime(reports['Time'], dayfirst=False)
reports_year = reports['Time'].dt.year
reports_NV = reports[reports['State']== 'NV']
