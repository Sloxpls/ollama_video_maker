# own libs
from llama_api import generate_script  # takes one parameter (prompt)
from get_youtube_videos import download_video  # takes one parameter (video_url)
from stt import generate_transcript  # takes one parameter (video_file)

# external libs
import re

"""
****************************
mr hugo homosexual behöver hjälpa mig med detta skit riktigt helvete med all ai!
****************************
"""
def main() -> None:
    youtube_video_link = "https://www.youtube.com/watch?v=cXzlxlDBYy0"
    download_video(youtube_video_link)
    respond_list = []
    transcript = generate_transcript("temp/video.mkv")
    for blocks in transcript:
        prompt = (
                "Crete motivational quotes from this transcription, give me them back in a json format with time staps of start and end of qouts: " + str(blocks)
                )
        respond = generate_script(prompt)
        respond_list.append(respond)
    print(respond_list)
    """ 
    prompt = "Convert the following extracted quotes into a Python list, with no additional information or formatting. Just return the list:\n\n" + str(respond_list)
    respond = generate_script(prompt)
    print(respond)
    """



if __name__ == "__main__":
    main()

