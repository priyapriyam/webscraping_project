from task_5 import*
genre_list=[]
diffrent_genre=[]
dublicate_genre=[]
genre_dict={}

def analyse_movies_genre(movies_list):
    for name in movies_list:
        # print (name)
        movie_genre=name["genre"]
        genre_list.append(movie_genre)
    # print (genre_list)
    for a in genre_list:
        for b in a:
            diffrent_genre.append(b)
    # print diffrent_genre
    for i in diffrent_genre:
        if i not in dublicate_genre:
            dublicate_genre.append(i)
    # print dublicate_genre
    for c in dublicate_genre:
        count=0
        for d in diffrent_genre:
            if c == d:
                count=count+1
            genre_dict[c]=count
    return (genre_dict)

data_5=analyse_movies_genre(data2)
pprint (data_5)
######eleven task completed















