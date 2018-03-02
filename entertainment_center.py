import media
import fresh_tomatoes

contact = media.Movie("Contact",
                          "https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",
                          "https://www.youtube.com/watch?v=d9C2cF3KvP8")

matrix = media.Movie("The Matrix",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

the_dish = media.Movie("The Dish",
                           "https://upload.wikimedia.org/wikipedia/en/4/4a/Thedish_poster.jpg",
                           "https://www.youtube.com/watch?v=2TAqXENo1rA")

toy_story = media.Movie("Toy Story" ,
                            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg" ,
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar" ,
                            "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg" ,
                            "https://www.youtube.com/watch?v=5PSNL1qE6VY")


beautiful_mind = media.Movie("A Beautiful Mind" ,
                             "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg" ,
                             "https://www.youtube.com/watch?v=WFJgUm7iOKw")

# Store the Movie objects in a list.
movies = [contact, matrix, the_dish, toy_story, avatar , beautiful_mind]

# Open the movie website in the user's browser, featuring the movies above.
fresh_tomatoes.open_movies_page(movies)