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
    # youtube_video_link = ""
    # download_video(youtube_video_link)
    respond_list = []
    transcript = generate_transcript("temp/video.webm")
    for blocks in transcript:
        prompt = (
                "Extract the most important and insightful quotes from the following transcript. "
                "Each quote should be self-contained and make sense without additional context. "
                "The quotes can come from different parts of the transcript and may span across multiple segments if needed. "
                "Ensure that the quotes are meaningful and can stand alone as impactful statements. "
                "Here is the transcript: " + str(blocks)
                )
        respond = generate_script(prompt)
        respond_list.append(respond)

    prompt = "Convert the following extracted quotes into a Python list, with no additional information or formatting. Just return the list:\n\n" + str(respond_list)
    respond = generate_script(prompt)
    print(respond)


if __name__ == "__main__":
    main()

