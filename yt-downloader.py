import pytube
from pytube import YouTube
from pytube.exceptions import *
import time
from moviepy.editor import *

# downloading audio function


def download_audio(url):
    print("Downloading...")
    try:
        start_time = time.time()
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        filename = yt.title + ".mp3"
        audio.download(filename=filename)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Downloaded in", round(execution_time, 2), "seconds")
    except Exception as e:
        print("Error: Downloading file stopped: ", e)

# downloading video function


def download_video(url, resolution):
    print("Downloading...")
    try:
        start_time = time.time()
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution, progressive=True).first()
        title = video.title
        print("Downloading video in resolution {}: {}".format(resolution, title))
        video.download()
        end_time = time.time()
        execution_time = end_time - start_time
        print("Downloaded in", round(execution_time, 2), "seconds")
    except Exception as e:
        print("Error: Downloading file stopped: ", e)

# showing video resolution options


def show_available_resolutions(url):
    try:
        yt = YouTube(url)
        print("Available video resolutions:")
        for stream in yt.streams.filter(progressive=True):
            print(stream.resolution)
    except Exception as e:
        print("Error: Downloading video resolutions stopped: ", e)


while True:
    url = input("Give me a link to the YouTube video: ")
    mode = input(
        "Choose what you want to get: \n1# AUDIO FILE\n2# VIDEO FILE\n3# FINISH PROGRAM\nDecision: ")
    if mode == '1':
        download_audio(url)
        continue
    elif mode == '2':
        show_available_resolutions(url)
        resolution = input("Choose video resolution: ")
        download_video(url, resolution)
        continue
    elif mode == '3':
        break
    else:
        print("Wrong choice")
        continue
