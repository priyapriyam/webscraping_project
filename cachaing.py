from task_1 import total_data
from task_5 import*
from pprint import pprint
import pathlib
import requests
import json


diffrent_id=[]
def store_data(details):
    for index in details[0:10]:
        a= index['movie_url']
        split_list=a.split('/')
        # print split_list
        id_number=split_list[4]
        diffrent_id.append(id_number)
    return diffrent_id
a=store_data(total_data)
# pprint (a)

def writting_data(file,data):
        with open(file,"w") as file1:
                file1.write (json.dumps(data))

        # file1.close()
def data_read(file):
    myFile=open(file,"r")
    myObject=myFile.read()

    myData=json.loads(myObject)
    return (myData)
    myFile.close()
def movie_details(movie_list,movie_id):
        
        for index in range(len(movie_list)):
                json_file="json_files/"+movie_id[index]+".json"
                print json_file
                filename=pathlib.Path(json_file)
                if filename.exists():
                        read_data = data_read(json_file)
                        
                        print "file is readable " 
                        return read_data              
                else:
                        data=writting_data(json_file,movie_list[index])
                        print "file is wrrithing"
                        return data


b=movie_details(data2,a)
pprint(b)



