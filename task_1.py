import requests
from bs4 import BeautifulSoup 
from pprint import pprint
import unicodedata
movie_url="https://www.imdb.com/india/top-rated-indian-movies/"
# print(movie_url)
#whole data of IMDB website
 
def scrape_top_list(movies_list):
    request = requests.get(movies_list)
    soup = BeautifulSoup(request.text, "html5lib")
    data=soup.find("div",class_="article")
    # print data
    position=1
    title=data.find("h1",class_="header")  
    # print (title.get_text())

    movie=soup.find("tbody",class_="lister-list")
    movie_data=movie.find("tr")    
    # print (movie_data)
    tags=movie.findAll("tr")
    # print tags
    movies=[]
    for t in tags:
        year=t.find("span",class_="secondaryInfo").get_text()
        s=str(year[1:5])
        years=int(s)
        #  print int(s)

        rating=t.find("td",class_="ratingColumn").get_text().strip()
        # print (rating)

        film_name=t.find("td",class_="titleColumn")
        movie_name=film_name.a.get_text()
        # print (movie_name)
    
        div = soup.find("div", class_="article")
        t_body = div.find("tbody",class_="lister-list")
        url= t.a["href"]
        url2="https://www.imdb.com"+url
        # print (url2)
    
        new_dic={}
        new_dic["position"]=position
        new_dic["movie_name"] = str(movie_name)
        new_dic["movie_year"] = years
        new_dic["movie_url"] = url2
        new_dic["movie_rating"]= float(rating)
        # pprint (new_dic)
        position=position+1
        movies.append(new_dic)
    return movies
total_data=scrape_top_list(movie_url)
# pprint (total_data)

# #first task completed######################

# years_list=[]
# def movie_years(years):
#     for i in range(len(years)):
#         years_list.append (years[i]["movie_year"]) 
#     return years_list 
# year_data=movie_years(total_data)
# # print year_data

# dublicates=[]
# def dublicate_years(movie_year):
#     for index in range(len(movie_year)):
#         if movie_year[index] not in dublicates:
#             dublicates.append(years_list[index])
#     dublicates.sort()
#     # print dublicates
#     return dublicates
# diffrent_years=dublicate_years(year_data)
# # print b 
# year_dic={}
# def group_by_year(movies,movie_data):
#     for i in range(len(movies)):
#         year_data= movies[i]
#         year_dic[year_data]=[]
#     # print year_dic 
#     for i in year_dic:
#         # print i
#         for j in total_data:
#             # print j
#             if i == j["movie_year"]:
#                 (year_dic[i]).append (j)
#     return (year_dic)                                                                                                                                                                                                                                                                                                                                              
# data=group_by_year(diffrent_years,year_data)
    
# # #second task completed######################
# new_list=[]
# new=[]
# new1=[]
# new2=[]
# new_dict={}
# def group_by_decade(years,movies):
#     for index in years:
#         modules=index%10
#         year=index-modules
#         range=year+10
#         if range not in new1:
#             decade=range-10
#             new.append(decade)
#             new1.append(range)
#     # print (new1)
#     # print new
#     for i in new:
#         key=i
#         new_dict[key]=[]
#     for i in new_dict:
#         for j in total_data:
#             if i < j["movie_year"] and (i+10)>j["movie_year"]:
#                 (new_dict[i]).append (j)
#     # pprint (new_dict)
# group_by_decade(diffrent_years,total_data) 

# #third task completed########################

# url_2='https://www.imdb.com/title/tt0100095/'


# def scrape_movie_details(movie_url):
#     response=requests.get(movie_url)
#     # print (response.text)
#     soup_2=BeautifulSoup(response.text,'html5lib')
#     # pprint (soup_2)
#     movie_name_2=soup_2.find("div",class_="title_wrapper").h1.get_text()
#     # print (movie_name_2)
#     name=movie_name_2[0:5]
#     # print (name)

#     name = soup_2.find("div",class_="title_wrapper").h1.get_text()
#     # print (name)
#     splitList= name.split()
#     # print (splitList)
#     splitList.remove(splitList[-1])
#     # print (splitList)
#     movieName = " ".join(splitList)
#     # print (movieName)

#     country1=soup_2.find("div",attrs={"class":"article","id":"titleDetails"})
#     country_name=country1.findAll("div",class_="txt-block")
#     # print country_name
    
#     country=""
#     language_list=[]
#     # try:
#     for i in country_name[0:5]:
#         # print(i)
#         head=i.h4.get_text()

#     # except AttributeError:
#         # print "something went wrong"

#         if (head=="Country:"):
#             country=i.find("a").get_text()
#             # print (country)
#         elif(head=="Language:"):
#             launguages= i.findAll("a")
#             # print launguages
#             for i in launguages:
#                 text=i.get_text() 
#                 language_list.append(text)
#                 # print language_list
            
#     summary=soup_2.find("div",class_="plot_summary")
#     movie_bio=summary.find("div",class_="summary_text").get_text().strip()
#     # print (movie_bio)
    
#     director=summary.find("div",class_="credit_summary_item")
#     director_list=director.findAll("a")
    
#     director_name=[]
#     for i in director_list:
#         movie_director=i.get_text()
#         director_name.append(movie_director)
#        # print (director_name)
        
#     movie_genre=soup_2.find("div",class_="subtext")
#     # print movie_genre
#     genre_name=movie_genre.findAll("a")
#     # print (genre_name)
#     genre_name.pop()

#     genre_list=[]
#     for i in genre_name:
#         # print i
#         main=i.get_text()
#         genre_list.append(main)
#     # print (genre_list)

#     movie_poster=soup_2.find("div",class_="poster").a["href"]
#     # print movie_poster
#     movie_poster_url="https://www.imdb.com"+movie_poster
#     # print movie_poster_url

#     sub_runtime=soup_2.find("div",class_="subtext").time["datetime"]
#     runtime=sub_runtime
#     # print runtime
#     movie_run_time=""
#     for i in runtime:
#         if i.isdigit():
#             movie_run_time=movie_run_time+i
#     # print movie_run_time
#     # print runtime

  
#     details_dict={}
#     details_dict["name"]=movieName
#     details_dict["director"]= director_name
#     details_dict["country"]=country
#     details_dict["language"]=language_list
#     details_dict["poster_image_url"]=movie_poster_url
#     details_dict["bio"]=movie_bio
#     details_dict["runtime"]= movie_run_time
#     details_dict["genre"]= genre_list
#     return details_dict
# movie_details_data=scrape_movie_details(url_2)
# # pprint (movie_details_data)

# # fourth task completed############################

# top_10_movies_details=[]
# def get_movie_list_details(details,):
#     for index in details[0:10]:
#         # print index
#         url=index["movie_url"]
#         # print url
#         total=scrape_movie_details(url)
#         top_10_movies_details.append(total)

#     return(top_10_movies_details)

# data2=get_movie_list_details(total_data)
# # pprint (data2) 

# ############fifth task completed################

# language=[] 
# diffrent_launguage=[] 
# dublicate_launguages=[]
# launguage_dict={}

# def analyse_movies_language( movies_list):
#     for index in movies_list:
#         #  print index
#         movie_launguages=index['language']
#         language.append (movie_launguages)
#     # print language
#     for i in language:
#         for j in i:
#             diffrent_launguage.append(j)

#     # print diffrent_launguage
#     for index in diffrent_launguage:
#         if index not in dublicate_launguages:
#             dublicate_launguages.append(index)
#     # print dublicate_launguages

#     for i in dublicate_launguages:
#         count=0
#         for j in diffrent_launguage:
#             if i == j:
#                 count=count+1
#         launguage_dict[i]=count
#     # pprint (launguage_dict)
   
# analyse_movies_language(data2)

# ##############  six task completed  ####################
# directors_list=[]
# diffrent_directors=[]
# dublicate_directors_name=[]
# directors_dict={}
# def analyse_movies_directors(movies):
#     for index in movies:
#         # print index
#         movie_directors=index['director']
#         directors_list.append(movie_directors)
#     # print directors_list
#     for name in directors_list:
#         for j in name:
#             diffrent_directors.append(j)
#     # print diffrent_directors 
#     for i in diffrent_directors:
#         if i not in dublicate_directors_name:
#             dublicate_directors_name.append(i) 
#     # print dublicate_directors_name
#     for a in dublicate_directors_name:
#         count=0
#         for b in diffrent_directors:
#             if a == b:
#                 count=count+1 
#             directors_dict[a]=count
#     # pprint (directors_dict)

# analyse_movies_directors(data2)

# ####### seven task completed  ##############

# #####task_11#############
# genre_list=[]
# diffrent_genre=[]
# dublicate_genre=[]
# genre_dict={}

# def analyse_movies_genre(movies_list):
#     for name in movies_list:
#         # print (name)
#         movie_genre=name["genre"]
#         genre_list.append(movie_genre)
#     # print (genre_list)
#     for a in genre_list:
#         for b in a:
#             diffrent_genre.append(b)
#     # print diffrent_genre
#     for i in diffrent_genre:
#         if i not in dublicate_genre:
#             dublicate_genre.append(i)
#     # print dublicate_genre
#     for c in dublicate_genre:
#         count=0
#         for d in diffrent_genre:
#             if c == d:
#                 count=count+1
#             genre_dict[c]=count
#     # pprint (genre_dict)

# analyse_movies_genre(data2)
# ######eleven task completed















