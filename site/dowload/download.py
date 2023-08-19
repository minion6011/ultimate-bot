from flask import Flask, request, send_file #d

import pytube #d

import random 
from random import choice

import os

app = Flask(__name__)

html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Input e Download</title>
</head>
<body>
    <form action="/process" method="post">
        <label for="user_input">Inserisci del testo:</label>
        <textarea id="user_input" name="user_input"></textarea>
        <button type="submit">Elabora e Scarica</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return html_form

@app.route('/process', methods=['POST'])
def process():
	url = request.form['user_input']
	try:
		if url.startswith("https://youtu.be/"):
			share_video_id = url.replace("https://youtu.be/", "")
			share_video_url = "youtube.com/watch?v=" + f"{share_video_id}"
			
			#find-video
			video = pytube.YouTube(share_video_url)
			
			#title-file
			number = random.randint(1, 100000)
			extension = "mp4"
			file_name = f"{number}.{extension}"
			#video.streams.get_highest_resolution().download(filename=file_name)
			#download
			video.streams.first().download(filename=file_name)
			
			filename = f"{file_name}"
			return send_file(filename, as_attachment=True)
		else:
			#find-video
			video = pytube.YouTube(url)
			
			#title-file
			number = random.randint(1, 100000)
			extension = "mp4"
			file_name = f"{number}.{extension}"
			#video.streams.get_highest_resolution().download(filename=file_name)
			
			#download
			video.streams.first().download(filename=file_name)
			
			
			filename = f"{file_name}"
			return send_file(filename, as_attachment=True)
	except:
		print("e")

if __name__ == '__main__':
    app.run()
