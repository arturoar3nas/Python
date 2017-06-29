import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story stupid",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Toy_Story.svg/245px-Toy_Story.svg.png",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "blue people",
                     "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Avatar-Logo-avatar.svg/300px-Avatar-Logo-avatar.svg.png",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

ring_comunity = media.Movie("Ring Comunity",
                            "Frodo begin travel",
                            "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                            "https://www.youtube.com/watch?v=yZL3x8XE0hU")
two_towers = media.Movie("Two Towers",
                         "Gandalf return",
                         "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
                         "https://www.youtube.com/watch?v=ve5HZfrrUqc")
return_king = media.Movie("Return Of The King",
                          "the ring is distroy",
                          "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                          "https://www.youtube.com/watch?v=KOQSQaGgJxs")

movies = [toy_story,avatar,ring_comunity,two_towers,return_king]
fresh_tomatoes.open_movies_page(movies)
