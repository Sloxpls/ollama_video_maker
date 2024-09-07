import yt_dlp as ydl
import os

def download_video(video_url):
    if not os.path.exists('temp'):
        os.makedirs('temp')

    # Set options for yt-dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio separately, then merge
        'outtmpl': 'temp/video.%(ext)s',  # Output file template with extension
        'noplaylist': True,  # Only download a single video
    }

    # Instantiate and execute the download process
    with ydl.YoutubeDL(ydl_opts) as ydl_instance:
        ydl_instance.download([video_url])
