from task_1 import total_data
from task_4 import*
from pprint import pprint
import pathlib
import requests
import json
import time
import random


diffrent_id=[]
urlList=[]
dict={}
def store_data(details):
    for index in details:
        a= index['movie_url']
        split_list=a.split('/')
        urlList.append(a)
        # print split_list
        id_number=split_list[4]
        diffrent_id.append(id_number)
    dict["url"]=urlList
    dict["id"]=diffrent_id
    return dict
a=store_data(total_data)
# pprint (a)


def writting_data(data,file):
        with open(file,"w") as file1:
                file1.write (json.dumps(data))

        # file1.close()
def data_read(file):
    myFile=open(file,"r")
    myObject=myFile.read()

    myData=json.loads(myObject)
    return (myData)
#     myFile.close()

whole_data=[]
def movie_details(movie_id):
        random_number=random.randint(1,3)
        urls=movie_id["url"]
        id_list=movie_id["id"]
        for index in range(len(urls)):
                data1=urls[index]
                dict_data=scrape_movie_details(data1)
                json_file="json_files/"+id_list[index]+".json"
                
                filename=pathlib.Path(json_file)

                if filename.exists():
                        read_data = data_read(json_file)
                        
                
                        # print "file is readable " 
                        whole_data.append(read_data)              
                else:
                        
                        data=writting_data(dict_data,json_file)
                        time.sleep(random_number)
                        # print "file is wrrithing"
                        # return data
        return whole_data


movies_details_chaching=movie_details(a)
# pprint(movies_details_chaching)



