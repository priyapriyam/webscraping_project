import requests
from bs4 import BeautifulSoup 
from pprint import pprint

url_2='https://www.imdb.com/title/tt0100095/'

def scrape_movie_details(movie_url):
    response=requests.get(movie_url)
    # print (response.text)
    soup_2=BeautifulSoup(response.text,'html5lib')
    # pprint (soup_2)
    movie_name_2=soup_2.find("div",class_="title_wrapper").h1.get_text()
    # print (movie_name_2)
    name=movie_name_2[0:5]
    # print (name)

    name = soup_2.find("div",class_="title_wrapper").h1.get_text()
    # print (name)
    splitList= name.split()
    # print (splitList)
    splitList.remove(splitList[-1])
    # print (splitList)
    movieName = " ".join(splitList)
    # print (movieName)

    country1=soup_2.find("div",attrs={"class":"article","id":"titleDetails"})
    country_name=country1.findAll("div",class_="txt-block")
    # print country_name
    
    country=""
    language_list=[]
    try:
        for i in country_name[0:5]:
            # print(i)
            head=i.h4.get_text()

        # except AttributeError:
        #     print "something went wrong"

            if (head=="Country:"):
                country=i.find("a").get_text()
                # print (country)
            elif(head=="Language:"):
                launguages= i.findAll("a")
                # print launguages
                for i in launguages:
                    text=i.get_text() 
                    language_list.append(text)
                    # print language_list
    except AttributeError:
        print "something went wrong"        
    summary=soup_2.find("div",class_="plot_summary")
    movie_bio=summary.find("div",class_="summary_text").get_text().strip()
    # print (movie_bio)
    
    director=summary.find("div",class_="credit_summary_item")
    director_list=director.findAll("a")
    
    director_name=[]
    for i in director_list:
        movie_director=i.get_text()
        director_name.append(movie_director)
       # print (director_name)
        
    movie_genre=soup_2.find("div",class_="subtext")
    # print movie_genre
    genre_name=movie_genre.findAll("a")
    # print (genre_name)
    genre_name.pop()

    genre_list=[]
    for i in genre_name:
        # print i
        main=i.get_text()
        genre_list.append(main)
    # print (genre_list)

    movie_poster=soup_2.find("div",class_="poster").a["href"]
    # print movie_poster
    movie_poster_url="https://www.imdb.com"+movie_poster
    # print movie_poster_url

    sub_runtime=soup_2.find("div",class_="subtext").time["datetime"]
    runtime=sub_runtime
    # print runtime
    movie_run_time=""
    for i in runtime:
        if i.isdigit():
            movie_run_time=movie_run_time+i
    # print movie_run_time
    # print runtime
    details_dict={}
    details_dict["name"]=movieName
    details_dict["director"]= director_name
    details_dict["country"]=country
    details_dict["language"]=language_list
    details_dict["poster_image_url"]=movie_poster_url
    details_dict["bio"]=movie_bio
    details_dict["runtime"]= movie_run_time
    details_dict["genre"]= genre_list
    return details_dict
movie_details_data=scrape_movie_details(url_2)
# pprint (movie_details_data)

# fourth task completed############################


