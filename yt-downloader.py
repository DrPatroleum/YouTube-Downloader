import pytube
from pytube import YouTube
from pytube.exceptions import *
import time
from moviepy.editor import *

# funkcja do pobierania audio


def download_audio(url):
    print("Trwa pobieranie...")
    try:
        start_time = time.time()
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        filename = yt.title + ".mp3"
        audio.download(filename=filename)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Pomyślnie pobrano w czasie", round(execution_time, 2), "sekund")
    except Exception as e:
        print("Błąd: Nie udało się pobrać pliku audio: ", e)

# funkcja do pobierania wideo


def download_video(url, resolution):
    print("Trwa pobieranie...")
    try:
        start_time = time.time()
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution, progressive=True).first()
        title = video.title
        print("Pobieranie wideo w rozdzielczości {}: {}".format(resolution, title))
        video.download()
        end_time = time.time()
        execution_time = end_time - start_time
        print("Pomyślnie pobrano w czasie", round(execution_time, 2), "sekund")
    except Exception as e:
        print("Błąd: Nie udało się pobrać pliku wideo: ", e)

# funkcja do wyświetlania dostępnych rozdzielczości wideo


def show_available_resolutions(url):
    try:
        yt = YouTube(url)
        print("Dostępne rozdzielczości wideo:")
        for stream in yt.streams.filter(progressive=True):
            print(stream.resolution)
    except Exception as e:
        print("Błąd: Nie udało się pobrać dostępnych rozdzielczości: ", e)


while True:
    url = input("Podaj URL do filmu na YouTube: ")
    mode = input(
        "Wybierz tryb pobierania: \n1# AUDIO\n2# WIDEO\n3# KONIEC\nWybieram: ")
    if mode == '1':
        download_audio(url)
        continue
    elif mode == '2':
        # wyświetlanie dostępnych rozdzielczości wideo
        show_available_resolutions(url)
        resolution = input("Wybierz rozdzielczość wideo: ")
        download_video(url, resolution)
        continue
    elif mode == '3':
        break
    else:
        print("Nieprawidłowy wybór")
        continue
