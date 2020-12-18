#utils.py

import requests
import json
import datetime
import calendar
import matplotlib.pyplot as plt

#https://docs.python.org/3/library/datetime.html
def getDay(date): 
    day = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M').weekday() 
    return (calendar.day_name[day]) 
    
token = "BQAk1-6tEhdU_qMUU4oylI82FAAHOShwHmz__zN68NRqQPoUnKb7Ihs6yl0ZyJgzrUOH-QmTK8mzBeTO0sxRP45pakv_AAwJmb2qsMjTABh2j4lZfzKDMTwT5-1naIzHEaFfdwfuK3ktPsCU4q5s3LkV "
API_endpoint = "https://api.spotify.com/v1/search"

def make_request(fullURL):
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + token}

    response = requests.get(url=fullURL, headers=headers)
    json_object = json.loads(response.text)

    return json_object

def search_request(search_term, search_type):
    search_term = requests.utils.quote(search_term)
    search_type = requests.utils.quote(search_type)
    url = API_endpoint + "?q=" + search_term
    url += "&type=" + search_type
    print(url)
    json_obj = make_request(url)
    return json_obj

def get_genres(json_obj):
    artists = json_obj["artists"]
    items = artists["items"]
    first_artist_item = items[0] # TODO: are they sorted by match confidence/popularity?
    genres = first_artist_item["genres"]
    return genres

def main(ser, x):
    for i in range(0, len(ser), 1):
        json_obj = search_request(ser[i], "artist")
        genres = get_genres(json_obj)
        x.append(genres)
    
def histogram(x, y):
    plt.figure()
    plt.hist(x)
    plt.title(y)
    plt.xlabel("Genres")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    plt.show()