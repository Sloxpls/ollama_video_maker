import yt_dlp  # pip install yt-dlp
import os


def download_video(video_url):
    if not os.path.exists('temp'):
        os.makedirs('temp')

    # Set options for yt-dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio separately, then merge
        'outtmpl': 'temp/video',  # Output file template
        'noplaylist': True,  # Only download a single video
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return

    except Exception as e:
        print(f"Could not download Youtube video: {e}")
        return
