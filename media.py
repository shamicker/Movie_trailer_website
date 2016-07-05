import webbrowser


class Video():
    """ Create instance variables for a video.

    Attributes, in strings:
        title: The video's title
        general_synopsis: A one-line synopsis of the video
        general_image_url: The url of a poster image
        general_trailer_url: The url of a trailer
        genre: The genre description(s)
    """
    def __init__(self, title, general_synopsis, general_image_url, general_trailer_url, genre):
        self.title = title
        self.general_synopsis = general_synopsis
        self.poster_image_url = general_image_url
        self.trailer_youtube_url = general_trailer_url
        self.genre = genre

    def show_trailer(self):
        """ Open the trailer website in a new browser tab. """
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    """ Create instance variables for a movie.

    Inherits instance variables from class Video.

    Additional attributes:
        mpaa_rating: MPAA rating
    """
    def __init__(self, title, general_synopsis, general_image_url, general_trailer_url, genre, mpaa_rating):
        Video.__init__(self, title, general_synopsis, general_image_url, general_trailer_url, genre)
        self.mpaa_rating = mpaa_rating


class TV(Video):
    """ Create instance variables for a TV series.

    Inherits instance variables from class Video.

    Additional attributes:
        seasons_and_episodes: The total number of episodes in total number of seasons.
    """
    def __init__(self, title, general_synopsis, general_image_url, general_trailer_url, genre, seasons_and_episodes):
        Video.__init__(self, title, general_synopsis, general_image_url, general_trailer_url, genre)
        self.season_episode = seasons_and_episodes
