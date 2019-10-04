from task_5 import*
directors_list=[]
diffrent_directors=[]
dublicate_directors_name=[]
directors_dict={}

def getDirector(movies):
    for index in movies:
        # print index
        movie_directors=index['director']
        directors_list.append(movie_directors)
    return directors_list
total_directors=getDirector(data2)
# print total_directors

def diff_directors(director_list):
    for name in director_list:
        for j in name:
            diffrent_directors.append(j)
    return diffrent_directors
directors_data=diff_directors(total_directors)
# print  directors_data

def dublicate_directors(directors_name):
    for i in directors_name:
        if i not in dublicate_directors_name:
            dublicate_directors_name.append(i) 
    return dublicate_directors_name
sorted_directors_list=dublicate_directors(directors_data)
# print sorted_directors_list

def analyse_movies_directors(main_directors,directors):
   for a in main_directors:
        count=0
        for b in directors:
            if a == b:
                count=count+1 
            directors_dict[a]=count
        return (directors_dict)
data_4=analyse_movies_directors(sorted_directors_list,directors_data)
# pprint (data_4)

# ####### seven task completed  ##############

