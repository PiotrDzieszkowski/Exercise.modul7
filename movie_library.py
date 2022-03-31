from random import randrange, random, randint
from datetime import date

class MovieLibrary:
    def __init__(self, title, publishment_year, type_of, num_of_plays):
        self.title = title
        self.publishment_year = publishment_year
        self.type_of = type_of
        self.num_of_plays = num_of_plays
        
    def play(self,plays= 1):
        self.num_of_plays+= plays

    def __str__(self):
        return (f"{self.title} ({self.publishment_year})")
    def add(self):
        try:
            custom_list = [self.title,self.publishment_year,self.type_of,self.episode_num, self.season_num,self.num_of_plays]
            General_list.append(custom_list)
            
        except:
            custom_list = [self.title,self.publishment_year,self.type_of,self.num_of_plays]
            General_list.append(custom_list)
    
        
class SerialLibrary(MovieLibrary):
    def __init__(self, title, publishment_year, type_of, num_of_plays, episode_num, season_num):
        super().__init__(title, publishment_year, type_of, num_of_plays)
        self.episode_num = episode_num
        self.season_num = season_num

    def __str__(self):
        if self.episode_num <10:
            self.episode_num = "0" + str(self.episode_num)
        if self.season_num <10:
            self.season_num = "0" + str(self.season_num)
        return(f"{self.title} S{self.season_num} E{self.episode_num}")

    
        



def get_movies():
    movie_list = []
    for movie in General_list:
        if len(movie) < 5:
            movie_list.append(movie)
            movie_list = sorted(movie_list)
    print(movie_list)

def get_serials():
    serial_list = []
    for serial in General_list:
        if len(serial) > 4:
            serial_list.append(serial)
            serial_list = sorted(serial_list)
    print(serial_list)

def search():
    search_phrase = input("Please type the serial or movie name:")
    for search_object in General_list:               
        if search_object[0].lower() == search_phrase.lower():                
            print(search_object)

def generate_views():
    items_number = len(General_list)-1
    rnd_number = randint(0,items_number)
    list_len = len(General_list[rnd_number])-1
    rnd_views = randint(0,101)

    General_list[rnd_number][list_len] = rnd_views
    print(General_list[rnd_number])
def generate_views_x10():

    for x in range(0,10):
        generate_views()


def top_titles():
    the_best_rank = input("Choose from 1 to 10, the number of top titles to be shown:")
    content_type = input("Put serial or movie, to select category to be shown:")
    best = int(the_best_rank)
    if content_type.lower() == "serial":
        
        serial_rank = {}
        for serials in General_list:
            if len(serials) == 6:
                
                serial_rank.setdefault("Number",{}).setdefault(serials[5],{})
                serial_rank["Number"][serials[5]] = serials[0]
    

        if best <= len(serial_rank["Number"].keys()):
            temp = sorted(serial_rank["Number"].keys(),reverse=True)
            
            for num in range(best):
           
                print(serial_rank["Number"][temp[num]])
        else:
            print("Number of selected top serials exceed the available list.")

    elif content_type.lower() == "movie":
        
        movie_rank = {}
        for movies in General_list:
            if len(movies) == 4:
                
                movie_rank.setdefault("Number",{}).setdefault(movies[3],{})
                movie_rank["Number"][movies[3]] = movies[0]
    

        if best <= len(movie_rank["Number"].keys()):
            temp = sorted(movie_rank["Number"].keys(),reverse=True)            
            for num in range(best):
           
                print(movie_rank["Number"][temp[num]])
        else:
            print("Number of selected top movies exceed the available list.")
    else:
        print("Selected criteria is outside of the list.")
    
def add_series():
        
        title_input = str(input("Put the name of the serial:"))
        publishment_year_input = str(input("Put the year of publishment:"))
        type_of_input = str(input("Put the type of serial:"))
        episode_num_input = int(input("Type the number of episodes:"))
        season_num_input = int(input("Type the number of season to be added:"))

        for num in range(1,episode_num_input+ 1):
            General_list.append([title_input,publishment_year_input,type_of_input,num,season_num_input,0])




        
    
    


    
current_date = date.today()
formatted_date = date.strftime(current_date, "%d.%m.%Y")


        
            
            
General_list = []

movie_1 = MovieLibrary(title= "Shrek", publishment_year= 2005, type_of= "comedy",num_of_plays= 11)
movie_2 = MovieLibrary(title= "Independent Day", publishment_year= 2007, type_of= "action",num_of_plays= 17)
movie_3 = MovieLibrary(title="Toy Story",publishment_year= 2002,type_of= "comedy",num_of_plays= 18)
movie_4 = MovieLibrary(title="Scary Film",publishment_year= 1999,type_of= "comedy",num_of_plays= 64)
movie_5 = MovieLibrary(title="Inception",publishment_year= 2016,type_of= "fantasy",num_of_plays= 111)
movie_6 = MovieLibrary(title="Capitan America",publishment_year= 2013,type_of= "fantasy",num_of_plays= 99)
movie_7 = MovieLibrary(title="Hulk",publishment_year= 2009,type_of= "fantasy",num_of_plays= 87)
movie_8 = MovieLibrary(title="Saw 1",publishment_year= 2003,type_of= "horror",num_of_plays= 54)
movie_9 = MovieLibrary(title="American Pie",publishment_year= 2004,type_of= "comedy",num_of_plays= 72)
movie_10 = MovieLibrary(title="American Pie 2",publishment_year= 2006,type_of= "comedy",num_of_plays= 74)
movie_11 = MovieLibrary(title="American Pie 3",publishment_year= 2007,type_of= "comedy",num_of_plays= 64)
movie_12 = MovieLibrary(title="American Beauty",publishment_year= 2009,type_of= "dramat",num_of_plays= 93)
movie_13 = MovieLibrary(title="Friday 13th",publishment_year= 2005,type_of= "horror",num_of_plays= 120)
movie_14 = MovieLibrary(title="Chucky",publishment_year= 1998,type_of= "horror",num_of_plays= 150)
movie_15 = MovieLibrary(title="Freddy vs Jason",publishment_year= 2014,type_of= "horror",num_of_plays= 94)

serial_1 = SerialLibrary(title= "The Walking Dead",publishment_year= 2010,type_of= "action",episode_num= 10,season_num= 1,num_of_plays= 7)
serial_2 = SerialLibrary(title= "The suits",publishment_year= 2012,type_of= "fantasy",episode_num= 5,season_num= 11,num_of_plays= 11)
serial_3 = SerialLibrary(title= "Big Bang Theory",publishment_year= 2012,type_of= "fantasy",episode_num= 10,season_num= 7,num_of_plays= 15)
serial_4 = SerialLibrary(title= "Game of Thrones",publishment_year= 2012,type_of= "fantasy",episode_num= 3,season_num= 4,num_of_plays= 26)
serial_5 = SerialLibrary(title= "Shields",publishment_year= 2011,type_of= "fantasy",episode_num= 5,season_num= 1,num_of_plays= 44)
serial_6 = SerialLibrary(title= "Arrow",publishment_year= 2014,type_of= "fantasy",episode_num= 16,season_num= 7,num_of_plays= 33)
serial_7 = SerialLibrary(title= "American Horror Story",publishment_year= 2016,type_of= "horror",episode_num= 13,season_num= 4,num_of_plays= 55)
serial_8 = SerialLibrary(title= "TY",publishment_year= 2019,type_of= "thriller",episode_num= 10,season_num= 2,num_of_plays= 48)
serial_9 = SerialLibrary(title= "Narcos",publishment_year= 2018,type_of= "document",episode_num= 10,season_num= 4,num_of_plays= 116)
serial_10 = SerialLibrary(title= "Black Mirror",publishment_year= 2015,type_of= "fantasy",episode_num= 9,season_num= 2,num_of_plays= 200)


movie_collection = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6, movie_7, movie_8, movie_9, movie_10, movie_11, movie_12, movie_13, movie_14, movie_15]
serial_collection = [serial_1, serial_2, serial_3, serial_4, serial_5, serial_6, serial_7, serial_8, serial_9, serial_10]

for movie in movie_collection: # filling the list library with movies
    movie.play()
    movie.add()

for serial in serial_collection: # filling the movie library with series
    serial.play()
    serial.add()


add_series() # adding whole series based on inputted parameters
generate_views() # generate random amount of views
generate_views_x10() # generate random amount of views 10 times



print("The most popular movies of the day :" + str(formatted_date)))
top_titles()