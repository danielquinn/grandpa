#!/usr/bin/env python3

video_template = """
  <div class="col-xs-12 col-sm-6 col-md-3 col-lg-2">
    <div class="box">
      <video id="my-video" class="video-js" controls preload="auto" width="320" height="240" poster="img/posters/{i:02}.jpg" data-setup="{{}}">
        <source src="vid/{i:02}.mp4" type="video/mp4">
        <p class="vjs-no-js">
          To view this video please enable JavaScript, and consider upgrading to a web browser that
          <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
        </p>
      </video>
    </div>
  </div>
"""
page_template = """
  <html>
    <head>
      <title></title>
      <link href="http://vjs.zencdn.net/5.8.8/video-js.css" rel="stylesheet">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/css/bootstrap.min.css" integrity="sha384-AysaV+vQoT3kOAXZkl02PThvDr8HYKPZhNT5h/CXfBThSRXQ6jW5DO2ekP5ViFdi" crossorigin="anonymous">
      <style>
        body {{
          background-color: #333333;
        }}
        .box {{
          padding: 0.5em;
        }}
        video {{
          width: 100%;
          height: 800px;
        }}
      </style>
    </head>
    <body>
      <div class="container-fluid">

        {}

        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>
        <script src="http://vjs.zencdn.net/5.8.8/video.js"></script>
      </div>
    </body>
  </html>
"""


videos = []
for i in range(38):
    videos.append(video_template.format(i=i))

print(page_template.format("\n".join(videos)))
