from bs4 import BeautifulSoup
import requests
import json
# import pprint
def movie_scrap():
    url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    
    find_movie=soup.find("div",class_="lister")
    find_movie1=find_movie.find("tbody",class_="lister-list")
    find_movie2=find_movie1.find_all("tr")
    list=[]
    serial=0
    for i in find_movie2:
        serial+=1
        movie_name=i.find("td",class_="titleColumn").a.get_text()  
        movie=movie_name
        movie_year=i.find("td",class_="titleColumn").span.get_text()[1:5] 
        year=int(movie_year)
        movie_rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        rating=float(movie_rating)
        movie_link=i.find("td",class_="titleColumn").a["href"]
        link="https://www.imdb.com/"+movie_year

        dict={"serial":serial,"movie name":movie,"movie_year":year,"movie_rating":rating,"movie link":link}
        list.append(dict)
        with open("movie_task1.json","w")as file:
            json.dump(list,file,indent=6)
    return list
movie_scrap()