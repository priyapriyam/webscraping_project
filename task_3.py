from task_1 import*
from task_2 import diffrent_years
new_list=[]
new=[]
new1=[]
new2=[]
new_dict={}
def group_by_decade(years,movies):
    for index in years:
        modules=index%10
        year=index-modules
        range=year+10
        if range not in new1:
            decade=range-10
            new.append(decade)
            new1.append(range)
    # print (new1)
    # print new
    for i in new:
        key=i
        new_dict[key]=[]
    for i in new_dict:
        for j in total_data:
            if i < j["movie_year"] and (i+10)>j["movie_year"]:
                (new_dict[i]).append (j)
    return (new_dict)
data_3=group_by_decade(diffrent_years,total_data) 
# pprint (data_3)


#third task completed########################

