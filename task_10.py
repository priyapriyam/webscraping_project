from task_8 import*
from task_7 import*
directors_list=[]
diffrent_directors=[]
launage_count={}

def analyse_language_and_directors(movies_list,directors):
    for index in directors[0:100]:
        language_list=[]
        directors_dict={}
        director_language_count={}
        dublicate_launguage=[]
        for i in movies_list[0:100]:
            if index in i["director"]:
                language_list.extend(i["language"])
        # print (index,language_list)
        
        directors_dict={}
        for a in language_list:
                if a not in dublicate_launguage:
                        dublicate_launguage.append(a)
        # print dublicate_launguage

        for language in dublicate_launguage:
                count=0
                for b  in language_list:
                        if language == b:
                            count=count+1 
                directors_dict[language]=count
                # pprint (directors_dict)
        launage_count[index]=directors_dict
    return launage_count
director_language_data=analyse_language_and_directors(movies_details_chaching,sorted_directors_list)
pprint (director_language_data)