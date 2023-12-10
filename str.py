# -*- coding: utf-8 -*-
"""Steam Store Games

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Iv88HrrltQ4Gxd8vdnIozVL3jR0uV6W1

# **1.**   **Intoduction**

Hello, the aim of my project is analise and check dataset of steam games since the begging of Steam and till the middle of 2019, we have huge amount of information, so let's get started

### Import libraries
"""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

"""### Reading the dataset"""

df = pd.read_csv('steam.csv')
df

"""# **2.**   **Data cleanup**

Let's clean dataset from dublicates and Nans and delete appid and steamspy_tags, because they are useless and we don't need them
"""

df = df.drop_duplicates()
df.dropna(inplace=True)
df = df.drop(["appid", "steamspy_tags"], axis=1)

df.info()

df

"""So, we can see, that now we have clean dataset

# **3. Overview**

So, in this dataset we have huge amount of data, where we have a lot of information about each game, for example release date, publisher, amount of achivements, rating, quantity of owners and prices. So we can check mean and median price.

### Mean, median and standard deviation for different columns

Mean, median and standard deviation for price for every game
"""

mean_price = df['price'].mean()
median_price = df['price'].median()
standard_deviation_price = df['price'].std()
print(f'Mean price: {round(mean_price, 3)}')
print(f'Median price: {median_price}')
print(f'Standard deviation of price: {round(standard_deviation_price, 3)}')

"""Mean, median and standard deviation for amoun of achivements"""

mean_achievements = df['achievements'].mean()
median_achievements = df['achievements'].median()
standard_deviation_achievements = df['achievements'].std()
print(f'Mean amount of achievements: {round(mean_achievements, 3)}')
print(f'Median amount of achievements: {median_achievements}')
print(f'Standard deviation of amount of achievements: {round(standard_deviation_achievements, 3)}')

"""Mean, median and standard deviation for possitive raings"""

mean_positive_rating = df['positive_ratings'].mean()
median_positive_rating = df['positive_ratings'].median()
standard_deviation_positive_rating = df['positive_ratings'].std()
print(f'Mean amount positive rating: {round(mean_positive_rating, 3)}')
print(f'Median amount positive rating: {median_positive_rating}')
print(f'Standard deviation of amount of positive rating: {round(standard_deviation_positive_rating, 3)}')

"""Mean, median and standard deviation for negative raings"""

mean_negative_rating = df['negative_ratings'].mean()
median_negative_rating = df['negative_ratings'].median()
standard_deviation_negative_rating = df['negative_ratings'].std()
print(f'Mean amount negative rating: {round(mean_negative_rating, 3)}')
print(f'Median amount negative rating: {median_negative_rating}')
print(f'Standard deviation of amount of negative rating: {round(standard_deviation_negative_rating, 3)}')

"""The percentage of positive and negative reviews for each game"""

amount_of_reviews = df.positive_ratings.values + df.negative_ratings.values
df.positive_ratings
ar_percentage_of_pos_reviews = df.positive_ratings.values / amount_of_reviews * 100
ar_percentage_of_neg_reviews = df.negative_ratings.values / amount_of_reviews * 100
reviews = pd.DataFrame({'name' : list(df.name),'pos' : list(ar_percentage_of_pos_reviews),'neg' : list(ar_percentage_of_neg_reviews)})
reviews

"""Made new column for prices in rubles"""

df['converted price'] = df['price'] * 92

"""### Proportion of gamers on each platform"""

size = df.platforms.value_counts().to_list()
size2 = size[:3]
size2.append(sum(size[3:]))
platforms = 'windows;mac;linux', 'windows;mac', 'windows', 'rest'
df_platforms = pd.DataFrame({'platforms': platforms, 'proportion': size2,})
fig = px.pie(df_platforms, values='proportion', names='platforms',
             title='Platform Ratio')
st.plotly_chart(fig)

"""It was obvious, that the most popular platfrom is windows, but there are interseting fact, that around 2 percent of games are exclusive for macos or linux

### Average price per year for all games
"""

df['release_year'] = df['release_date'].str.split('-').str[0]
df['release_month'] = df['release_date'].str.split('-').str[1]
sorted_years = sorted(df['release_year'].unique())
average_price_per_year = df.groupby('release_year')['price'].mean()
df_average_price_per_year = pd.DataFrame({'release_year': sorted(df.release_year.unique()), 'price($)': average_price_per_year,})
df_average_price_per_year
fig = px.line(df_average_price_per_year, x ='release_year', y='price($)', title='Average price per year')
st.plotly_chart(fig)

"""So, we can see that in 2002 was quiet strange peak and average price was 8$, but the highest average price was in 2013

### Left only main genre, because others aren't such important
"""

split_genres = df['genres'].str.split(';').str[0]
df['genres'] = split_genres
df

"""### Number of releases per year"""

number_of_releases = df['release_year'].value_counts().sort_index()
df_number_of_releases_per_year = pd.DataFrame({'Year': sorted_years, 'Number of Releases': number_of_releases})
fig = px.line(df_number_of_releases_per_year, x ='Year', y='Number of Releases', title='Games Released on Steam by Year')
st.plotly_chart(fig)

"""So, 2018 was the richest in releases, but in fact, there are linear dependence and in 2019 releases were more than in 2018, but we don't have information about it

### Made exactly numbers of owners
"""

split_owners = df['owners'].str.split('-').str[1]
df['owners'] = split_owners.astype(np.int64)
df

"""### The next interesting thing is that there are 6 times more owners of action games than other genres"""

owners_per_genre = pd.DataFrame.from_dict(dict(df.groupby('genres')['owners'].sum()), orient='index', columns = ['Owners'])
unique_genres = df['genres'].unique()
owners_per_genre

fig = px.bar(owners_per_genre, x='Owners', labels={'index': 'Genres'}, title= 'Popularity of each genre')
fig.update_traces(marker_color='red')
st.plotly_chart(fig)

"""### Here we can see average playtime in all games per year"""

average_price_per_year = df.groupby('release_year')['average_playtime'].mean()
average_price_per_year

"""### Earnings of each company over all years since the beginning of Steam"""

df['earnings'] = df['price'] * df['owners']
df_publishers = pd.DataFrame.from_dict(dict(df.groupby('publisher')['earnings'].sum()), orient='index', columns = ['Earnings'])
df_publishers = df_publishers.sort_values('Earnings', ascending = False)
df_publishers_top = df_publishers[:10]
fig = px.bar(df_publishers_top, y='Earnings', labels={'index': 'Companies'}, title= 'Earnings of the most big and popular companies')
fig.update_traces(marker_color='pink')
st.plotly_chart(fig)

"""I only showed top 10 companies, but they are the most popular, so the most interesing to know how much have they earned

# Hypothesis
## Let's prove that action games have been the most popular and the most profitable since the start of the Steam platform

Here we can see that earnings of action games over all years are the highest among all genres.
"""

most_popular_genres = ['Action', 'Adventure', 'Casual', 'Indie', 'RPG', 'Strategy']
df_genres = pd.DataFrame.from_dict(dict(df.groupby('genres')['earnings'].sum()), orient='index', columns = ['Earnings'])
df_genres

"""### Let's also check that action games were actually the most popular and the most profitable through the years

Earnings for each year of action games
"""

df_actions = df.loc[df['genres'] == 'Action']
actions_earnings = df_actions.groupby('release_year')['earnings'].sum()
actions_earnings

"""Earnings for each year of adventure games"""

df_adventures = df.loc[df['genres'] == 'Adventure']
adventures_earnings = df_adventures.groupby('release_year')['earnings'].sum()
adventures_earnings

"""Earnings for each year of indie games"""

df_indie = df.loc[df['genres'] == 'Indie']
indie_earnings = df_indie.groupby('release_year')['earnings'].sum()
indie_earnings

"""Earnings for each year of RPG games"""

df_rpg = df.loc[df['genres'] == 'RPG']
rpg_earnings = df_rpg.groupby('release_year')['earnings'].sum()
rpg_earnings

"""Earnings for each year of strategies"""

df_strategy = df.loc[df['genres'] == 'Strategy']
strategy_earnings = df_strategy.groupby('release_year')['earnings'].sum()
strategy_earnings

fig_action = px.line(actions_earnings, y="earnings", title='Earnings from Actions')
st.plotly_chart(fig)

fig_adventures = px.line(adventures_earnings, y="earnings", title='Earnings from Adventures')
st.plotly_chart(fig)

fig_indie = px.line(indie_earnings, y="earnings", title='Earnings from Indies')
st.plotly_chart(fig)

fig_rpg = px.line(rpg_earnings, y="earnings", title='Earnings from RPGs')
st.plotly_chart(fig)

fig_strategy = px.line(strategy_earnings, y="earnings", title='Earnings from Strategies')
st.plotly_chart(fig)

"""So, we can see, that action games were definitely the most profitavle over all years exceppt 2005, but I gess it is the mistake of data, because there are 0 earnings, but it can't be true, for example in 2005 call of duty 2 was released."""