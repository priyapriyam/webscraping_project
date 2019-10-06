from task_1 import*
import requests
from bs4 import BeautifulSoup 
from pprint import pprint
import copy

cast_url="https://www.imdb.com/title/tt0066763/"
# pprint(cast_url)

def scrape_movie_cast(movie_caste_url):
	request_1=requests.get(movie_caste_url)
	# print request_1
	soup_2=BeautifulSoup(request_1.text,"html5lib")
	# pprint(soup_2)
	main_class= soup_2.find("table",class_="cast_list")
	# print main_class
	tags=main_class.findAll("td",class_="")
	cast_list=[]

	for i in tags:
		# print i
		name=i.find("a").get_text().strip(" ")
		imdb_id=i.find("a")["href"][6:15]
		cast_dict={"name":name,"id":imdb_id}
		
		cast_list.append(cast_dict)
	print cast_list
scrape_movie_cast(cast_url)