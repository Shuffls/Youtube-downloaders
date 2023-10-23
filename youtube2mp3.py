from pytube import YouTube
from moviepy.editor import *
import os

# Define the path to the Music folder and the designated subfolder
music_folder = os.path.expanduser("~/Music/")
download_folder = os.path.join(music_folder, "YouTube_Downloads")

# Create the designated folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

url = input("Input url: ")
video = YouTube(url)
print(f"Title: {video.title}")
print("Downloading...")

# Download the audio to the designated folder
out_path = video.streams.filter(only_audio=True).first().download(output_path=download_folder)

# Convert the video to MP3 format using moviepy
video_clip = AudioFileClip(out_path)
mp3_path = os.path.join(download_folder, os.path.basename(out_path).replace(".mp4", ".mp3"))
video_clip.write_audiofile(mp3_path)

# Delete the original .mp4 file
os.remove(out_path)
print(f"Done! MP3 saved to: {mp3_path}")
