import argparse
import os
from pytube import YouTube

parser = argparse.ArgumentParser(description='Baixa um video do youtube na maior qualidade disponivel.')
parser.add_argument('youtube_url', help='youtube url')
args = parser.parse_args()

yt = YouTube(args.youtube_url)
video_filename = yt.streams.filter(file_extension='mp4').get_highest_resolution().download()
os.rename(video_filename, yt.title + '.mp4')
