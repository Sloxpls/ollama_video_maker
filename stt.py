import whisper


def generate_transcript(video_file):
    model = whisper.load_model("base")
    result = model.transcribe(video_file)
    result = prepare_transcript(result)
    result = cut_down_transcript_to_words(result)
    return result


def prepare_transcript(result):
    transcript = []
    for segment in result["segments"]:
        cut_down_segment = {
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        }
        transcript.append(cut_down_segment)

    return transcript


def cut_down_transcript_to_words(segments, max_words=500):
    total_words = 0
    current_chunk = []
    chunks = []

    for i, segment in enumerate(segments):
        num_words = len(segment["text"].split())
        if total_words + num_words > max_words:
            chunks.append(current_chunk)
            current_chunk = []
            total_words = 0

        current_chunk.append(segment)
        total_words += num_words

    if current_chunk:
        chunks.append(current_chunk)

    return chunks
