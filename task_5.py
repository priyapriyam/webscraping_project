from task_1 import total_data
from task_4 import*
from pprint import pprint

top_10_movies_details=[]
def get_movie_list_details(details):
    a=1
    for index in details:
        # print index
        url=index["movie_url"]
        # print url
        total=scrape_movie_details(url)
        top_10_movies_details.append(total)
        a=a+1
    return(top_10_movies_details)

data2=get_movie_list_details(total_data)
# pprint (data2) 

