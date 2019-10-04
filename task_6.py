from task_5 import*
language=[] 
diffrent_launguage=[] 
dublicate_launguages=[]
launguage_dict={}

def analyse_movies_language( movies_list):
    for index in movies_list:
        #  print index
        movie_launguages=index['language']
        language.append (movie_launguages)
    # print language
    for i in language:
        for j in i:
            diffrent_launguage.append(j)

    # print diffrent_launguage
    for index in diffrent_launguage:
        if index not in dublicate_launguages:
            dublicate_launguages.append(index)
    # print dublicate_launguages

    for i in dublicate_launguages:
        count=0
        for j in diffrent_launguage:
            if i == j:
                count=count+1
        launguage_dict[i]=count
    # pprint (launguage_dict)
   
analyse_movies_language(data2)