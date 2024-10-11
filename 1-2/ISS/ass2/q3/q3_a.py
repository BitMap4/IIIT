import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
from bs4 import BeautifulSoup

import pymysql
url = "https://www.imdb.com/chart/toptv/"
response = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
soup = BeautifulSoup(response.text, 'html.parser')

script=soup.find('script',id='_NEXT_DATA_').text.strip()
data=json.loads(script)
dicti = data['props']['pageProps']['pageData']['chartTitles']['edges']
for i in range(0,250):
    genres=dicti[i]['node']['titleGenres']['genres']
    tv_show_list[i].append(" ".join([i['genre']['text'] for i in genres]))

conn = pymysql.connect(host="localhost", user="bitmap4", password="", database="top_250_shows")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shows (
        title VARCHAR(200), 
        year INT,
        rating FLOAT,
        genres VARCHAR(300),
        episodes INT
    )
''')
for movie in soup.select('.ipc-metadata-list-summary-item')[:250]:
    try:        
        from bs4 import BeautifulSoup
        title = movie.find('h3', class_='ipc-title__text').text
        year = movie.find('span', class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item').text
        episodes = movie.find_all('span', class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item')[1].text
        rating = movie.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.split()[0]

        cursor.execute('''
            INSERT INTO shows (title, year, rating, episodes) 
            VALUES (%s, %s, %s, %s)
        ''', (title, year, rating, episodes))

    except:
        continue


df = pd.read_sql_query("SELECT episodes FROM shows", conn)
frequency_count = df['episodes'].value_counts().sort_index()
frequency_count.plot(kind='line')
plt.title('Frequency count of TV-shows having n episodes')
plt.xlabel('No. of episodes')
plt.ylabel('Frequency count')
plt.show()

conn.commit()
conn.close()