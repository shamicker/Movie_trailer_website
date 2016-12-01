import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Shauna's Faves</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha256-/SIrNqv8h6QGKDuNoLGA4iret+kyesCkHGzVUUV0shc=" crossorigin="anonymous"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
            text-align: center;
        }
        .video-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            display: block !important;
        }
        .video-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .details {
            height: 342px;
            width: 220px;
            position: absolute;
            top: 20px;
            left: 0;
            right: 0;
            margin: auto;
            opacity: 0;
            text-align: center;
        }
        .video-tile:hover .details {
            opacity: 1;
        }
        .video-tile:hover .image {
            opacity: .1;
        }
        .info {
            left: 0;
            right: 0;
            margin: 5px;
        }
        .genres {
            position: absolute;
            top: 10px;
        }
        .synopsis {
            position: absolute;
            top: 120px;
        }
        .rating {
            position: absolute;
            top: 300px;
        }
        .seasons {
            position: absolute;
            top: 280px;
        }
        .nav-tabs {
            margin-left: 10%;
            width: 80%;
            border-bottom: 1px solid orange;
            padding: 5px 10px 0;
        }
        .nav-tabs > li > a {
            color: orange;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px 10px 0 0;
        }
        .nav-tabs > li.active > a,
        .nav-tabs > li.active > a:hover,
        .nav-tabs > li.active > a:focus {
            color: orange;
            background: transparent;
            border-top: 1px solid orange;
            border-left: 1px solid orange;
            border-right: 1px solid orange;
            border-bottom: 1px solid black;
        }
        a:focus {
            outline: none;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.video-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                'id': 'trailer-video',
                'type': 'text-html',
                'src': sourceUrl,
                'frameborder': 0
            }));
        });
        // Animate in the videos when the page loads
        $(document).ready(function () {
            $('.video-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
            });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
    <body>
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
            <div class="modal-dialog">
                <div class="modal-content">
                    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                    </a>
                    <div class="scale-media" id="trailer-video-container">
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Page Content -->
        <div class="container tab-content">
            <!-- Nav Tabs -->
            <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
                <ul class="navbar-header nav nav-tabs">
                    <li class="navbar-right">
                        <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
                    </li>
                    <li class="active">
                        <a href="#movies" data-toggle="tab">Some Fave Movies</a>
                    </li>
                    <li class="">
                        <a href="#tvshows" data-toggle="tab">Some Fave TV</a>
                    </li>
                </ul>
            </div>
            <!-- Tab Contents -->
            <div id="movies" class="container active tab-pane">
                {movie_tiles}
            </div>
            <div id="tvshows" class="container tab-pane">
                {tv_tiles}
            </div>
        </div>
    </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 video-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img class="tile image" src="{poster_image_url}" width="220" height="342">
    <div class="tile details">
        <h4 class="genres info">Genre:<br>{genre}</h4>
        <h4 class="info synopsis">{general_synopsis}</h4>
        <h4 class="info rating">MPAA Rating: {mpaa_rating}</h4>
    </div>
    <h2>{video_title}</h2>
</div>
'''

# A single tv-show entry html template
tv_tile_content = '''
<div class="col-md-6 col-lg-4 video-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img class="tile image" src="{poster_image_url}" width="220" height="342">
    <div class="tile details">
        <h4 class="genres info">Labels:<br>{genre}</h4>
        <h4 class="info synopsis">{general_synopsis}</h4>
        <h4 class="info seasons">{seasons_and_episodes}</h4>
    </div>
    <h2>{video_title}</h2>
</div>
'''


def create_video_tiles_content(movie_and_tv_list):
    # The HTML content for the video-tile section of the page
    content = ''
    for video in movie_and_tv_list:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', video.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', video.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the video-tile content with its movie or tv content filled in
        try:
            tv = video.season_episode
        except AttributeError:
            content += movie_tile_content.format(
                trailer_youtube_id=trailer_youtube_id,
                video_title=video.title,
                general_synopsis=video.general_synopsis,
                poster_image_url=video.poster_image_url,
                genre=video.genre,
                mpaa_rating=video.mpaa_rating
            )
        else:
            content += tv_tile_content.format(
                trailer_youtube_id=trailer_youtube_id,
                video_title=video.title,
                general_synopsis=video.general_synopsis,
                poster_image_url=video.poster_image_url,
                genre=video.genre,
                seasons_and_episodes=video.season_episode
            )
    return content


def open_videos_page(movies, tv_shows):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_video_tiles_content(movies),
        tv_tiles=create_video_tiles_content(tv_shows))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # Open the output file in the browser, and in a new tab, if possible
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
