from task1 import movie_scrap
import json
import pprint
scrapped_data=movie_scrap()
# print(scrapped_data)
def group_by_year(movies):
    years=[]
    # list=[]
    for i in movies:
        # year=i["year"]
        if i["movie_year"] not in years:
            years.append(i["movie_year"])
            movie_dict={i:[]for i in years}
            for i in movies:
                year=i["movie_year"]    
                for x in movie_dict:
                    if (x)==(year):
                        movie_dict[x].append(i)
    with open("years data_task2.json","w")as file1:
        json.dump(movie_dict,file1,indent=5)
    return movie_dict
group_by_year(scrapped_data)