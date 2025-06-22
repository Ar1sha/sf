import pandas as pd
df = pd.read_csv('D:\sf\Pandas\citibike-tripdata.csv', sep=',')

#starttime — время начала поездки (дата, время);
#stoptime — время окончания поездки (дата, время);
#start station id — идентификатор стартовой стоянки;
#start station name — название стартовой стоянки;
#start station latitude, start station longitude — географическая широта и долгота стартовой стоянки;
#end station id — идентификатор конечной стоянки;
#end station name — название конечной стоянки;
#end station latitude, end station longitude — географическая широта и долгота конечной стоянки;
#bikeid — идентификатор велосипеда;
#usertype — тип пользователя (Customer — клиент с подпиской на 24 часа или на три дня, Subscriber — подписчик с годовой арендой велосипеда);
#birth year — год рождения клиента;
#gender — пол клиента (0 — неизвестный, 1 — мужчина, 2 — женщина).
df = df.drop(['start station id', 'end station id'], axis=1)
df = df.rename(columns={'birth year':'age'})
age_col = 2018 - df['age']
age_over_60 = (age_col>60).sum()
df['starttime'] = pd.to_datetime(df['starttime'])
df['stoptime'] = pd.to_datetime(df['stoptime'])
df['trip duration']=df['stoptime']-df['starttime']
df['weekend'] = df['starttime'].dt.dayofweek >= 5
def get_time_of_day(time_hours):
    time_hours = time_hours.hour
    if 0<=time_hours <=6:
        return 'night'
    if 7<=time_hours<=12:
        return 'morning'
    if 12<time_hours<=18:
        return 'day'
    else:
        return 'evening'
df['timeOfDay']= df['starttime'].apply(get_time_of_day)
print((df['timeOfDay']=='day').sum()/(df['timeOfDay']=='night').sum())
