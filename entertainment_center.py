# in python you import the file name that contains the class, classes are not the same name as the file
import media
import fresh_tomatoes

""" this module creates movie objects and calls fresh_tomatoes.open_movies_page """

# create the toy_story movie instance
toy_story = media.Movie("Toy Story",
                        "movie about toys that are magic",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# create the school_of_rock movie instance
school_of_rock = media.Movie("School of Rock",
                             "kids rocking with jeff black",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# create ratatouille movie instance
ratatouille = media.Movie("Ratatouille", "rodents make food",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=e8GBfNo3IHY")

# create the midnight in paris movie instance
midnight_in_paris = media.Movie("Midnight in Paris", "weird movie with owen wilson in paris",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

# this array is passed into the marc_movies class,
movies = [toy_story, school_of_rock, ratatouille, midnight_in_paris]

# this is the function call which will create the html page, and then loads it
fresh_tomatoes.open_movies_page(movies)
