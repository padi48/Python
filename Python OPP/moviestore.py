#Movie store
import random
from datetime import date, timedelta

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return 'Full name: ' + self.firstname + ' ' + self.lastname + ' | Age: ' + str(self.age)

class Movies(Person):
    def __init__(self, firstname, lastname, age):
        super().__init__(firstname, lastname, age)
        self.movie_list = ['Spider Man', 'Men in Black', 'Grown Ups', 'Grown Ups 2', 'IT', 'Spongebob']

    def movies(self):
        print("Available movies right now:")
        print(self.movie_list)

    def pick_movie(self):
        print("Available movies right now:")
        print(self.movie_list)

        self.rented_movies = []

        self.pick = input("Name of your movie: ")
        if self.pick in self.movie_list:
            self.movie_list.remove(self.pick)
            self.rented_movies.append(self.pick)
            print("You picked {} as your movie!".format(self.pick))
            print("")
            print("Movies left:")
            print(self.movie_list)
        else:
            print("Please choose from the list!")

    def pick_another(self):
        x = input("Do you want to pick another movie?\n")
        if x == 'yes':
            self.pick_movie()
        elif x == 'no':
            None
        else:
            print("Please enter yes or no!")

    def show_movies(self):
        print(self.firstname + ' ' + self.lastname + ' has rented:')
        print(", ".join(self.rented_movies))

    def rent(self):
        self.start_rent = date.today()
        self.end_rent = date.today()+timedelta(days=30)

        return 'You rented the movie ' + str(self.start_rent.strftime("%x")) + ' and have to bring it back by ' + str(self.end_rent.strftime("%x"))

if __name__ == '__main__':
    t = Movies('Matthew', 'Pados', 18)
    print(t.__str__())
    t.pick_movie()
    t.pick_another()
    t.show_movies()
    print(t.rent())
