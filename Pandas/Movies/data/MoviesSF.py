import pandas as pd
dates  = pd.read_csv('D:\sf\Pandas\Movies\data\dates.csv', sep=',')
ratings1 = pd.read_csv( 'D:/sf/Pandas/Movies/data/ratings1.csv', sep=',')
ratings2 = pd.read_csv( 'D:/sf/Pandas/Movies/data/ratings2.csv', sep=',')
movies = pd.read_csv( 'D:/sf/Pandas/Movies/data/movies.csv', sep=',')
# -------------INFO-----------------
# userId — уникальный идентификатор пользователя, который выставил оценку;
# movieId — уникальный идентификатор фильма;
# rating — рейтинг фильма.
# dates — таблица с датами выставления всех оценок.
# date — дата и время выставления оценки фильму.
# movies — таблица с информацией о фильмах.
# movieId — уникальный идентификатор фильма;
# title — название фильма и год его выхода;
# genres — жанры фильма.

ratings = pd.concat([ratings1, ratings2], ignore_index=True)
ratings = ratings.drop_duplicates(ignore_index=True)
ratings = pd.concat([ratings, dates], axis=1)
joined_false = ratings.join(
    movies,
    rsuffix='_right',
    how='left'
)
joined = ratings.join(
    movies.set_index('movieId'),
    on='movieId',
    how='left'
)
# print(joined_false[['movieId','movieId_right']])
merged = ratings.merge(
    movies,
    on='movieId',
    how='left'
)
import re 
def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None

###RESOULT
merged['year_release'] = merged['title'].apply(get_year_release)
year_1999 = merged[merged['year_release'] == 1999]
# print(year_1999.groupby("title")['rating'].mean().sort_values(ascending=True))
year_2010 = merged[merged['year_release']==2010]
# print(year_2010.groupby(by='genres')['rating'].mean().sort_values(ascending=True))
# print(merged.groupby(by='userId')['rating'].agg(['nunique','mean']).sort_values(by='mean', ascending=False))
year_2018 = merged[merged['year_release'] == 2018]
year_2018_ratings = year_2018.groupby('genres')['rating'].agg(['mean','count'])
# print(year_2018_ratings[year_2018_ratings['count']>10].sort_values(by='mean', ascending=False))
# trail1 = merged[merged['genres']=='Action|Adventure']
# trail2 = merged[merged['genres']=='Action|Adventure|Animation|Children|Comedy|IMAX']
print(year_2018_ratings[year_2018_ratings=='Animation|Children|Mystery'])
