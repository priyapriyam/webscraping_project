from task_1 import *

years_list=[]
def movie_years(years):
    for i in range(len(years)):
        years_list.append (years[i]["movie_year"]) 
    return years_list 
year_data=movie_years(total_data)
# print year_data

dublicates=[]
def dublicate_years(movie_year):
    for index in range(len(movie_year)):
        if movie_year[index] not in dublicates:
            dublicates.append(years_list[index])
    dublicates.sort()
    # print dublicates
    return dublicates
diffrent_years=dublicate_years(year_data)
#  print b 
year_dic={}
def group_by_year(movies,movie_data):
    for i in range(len(movies)):
        year_data= movies[i]
        year_dic[year_data]=[]
    # print year_dic 
    for i in year_dic:
        # print i
        for j in total_data:
            # print j
            if i == j["movie_year"]:
                (year_dic[i]).append (j)
    return (year_dic)                                                                                                                                                                                                                                                                                                                                              
data=group_by_year(diffrent_years,year_data)
# pprint (data)
    