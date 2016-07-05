import fresh_tomatoes
import media


''' Order of video info:
Title,
A very brief synopsis,
Poster image,
Trailer url,
Genre(s),
MPAA rating if a movie, or number of episodes/seasons if a tv show
'''

lola = media.Movie(
    "Run Lola Run",
    "Lola tries to beat the clock to help her boyfriend, while chance and choices affect the outcome.",
    "http://thetexastheatre.com/wp-content/uploads/2011/11/Run-Lola-Run-1999-movie-poster.jpg",
    "https://youtu.be/3ea0mG4ahRk",
    "action",
    "R"
    )

galaxy_quest = media.Movie(
    "Galaxy Quest",
    "The alumni cast of a TV series have to play their roles as the real thing when an alien race needs their help.",
    "http://crypticrock.com/wp-content/uploads/2016/01/51njhe6UBEL._SY355_.jpg",
    "https://www.youtube.com/watch?v=B34jbC43XzA",
    "comedy, spoof",
    "PG"
    )

miss_granny = media.Movie(
    "Miss Granny",
    "A woman in her 70s who magically finds herself in the body of her 20-year-old self.",
    "https://krilianeh.files.wordpress.com/2014/03/poster.jpg",
    "https://www.youtube.com/watch?v=FkWhntKKrIU",
    "comedy, family",
    "PG"
    )

alien = media.Movie(
    "Alien",
    "A commercial crew aboard the deep space towing vessel, Nostromo is on its way home when they pick up an SOS warning from a distant planet.",
    "http://ecx.images-amazon.com/images/I/31hbqR60nML.jpg",
    "https://www.youtube.com/watch?v=e0DFvWLXv9U",
    "sci-fi, suspense",
    "R"
    )

true_romance = media.Movie(
    "True Romance",
    "Clarence marries Alabama, steals cocaine from her pimp, and tries to sell it in Hollywood, while the owners of the coke try to reclaim it.",
    "http://i.jeded.com/i/true-romance.26061.jpg",
    "https://www.youtube.com/watch?v=_wNYNDzKpuQ",
    "black comedy, thriller, violent",
    "R"
    )

french_kiss = media.Movie(
    "French Kiss",
    "A woman flies to France to confront her straying fiance, but gets into trouble when the charming crook seated next to her uses her for smuggling.",
    "http://images.moviepostershop.com/french-kiss-movie-poster-1995-1020263414.jpg",
    "https://www.youtube.com/watch?v=eWCFoPUfm1Y",
    "comedy, romance",
    "PG-13"
    )

lego_movie = media.Movie(
    "The Lego Movie",
    "An ordinary Lego construction worker is thought to be the prophesied 'Special'.",
    "http://content9.flixster.com/movie/11/17/76/11177655_800.jpg",
    "https://www.youtube.com/watch?v=fZ_JOBCLF-I",
    "comedy, family, fast-paced",
    "PG"
    )

time_bandits = media.Movie(
    "Time Bandits",
    "A boy falls in with a gang of time-travelling thieves; a giddy fairy tale, a revisionist history lesson, and a satire of technology gone awry.",
    "http://thesefantasticworlds.com/wp-content/uploads/2014/02/time-bandits-movie-poster.jpg",
    "https://www.youtube.com/watch?v=NNO9apbGvzo",
    "dark comedy",
    "PG"
    )

flight_conchords = media.TV(
    "Flight of the Conchords",
    "Two shepherds-turned-musicians from New Zealand try to make it big as a folk duo in New York City.",
    "http://images.latinpost.com/data/images/full/64566/flight-of-the-conchords.jpg",
    "https://www.youtube.com/watch?v=srcc64JZmPw",
    "comedy, musical",
    "22 episodes in 2 seasons"
    )

firefly = media.TV(
    "Firefly",
    "Five hundred years in the future, a renegade crew aboard a small spacecraft tries to survive as they travel the fringes of the galaxy.",
    "https://liztellsfrank.files.wordpress.com/2013/05/firefly-poster1.jpg",
    "https://www.youtube.com/watch?v=g0O29rZiIRA",
    "action, sci-fi",
    "14 episodes in 1 season"
    )

movies_list = [time_bandits, lola, galaxy_quest, lego_movie, true_romance, alien, miss_granny, french_kiss]
tv_list = [flight_conchords, firefly]

# Use movies_list and tv_list to generate an HTML file and open it in
# a new browser tab.
fresh_tomatoes.open_videos_page(movies_list, tv_list)
