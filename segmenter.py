from pydub import AudioSegment
from pydub.utils import make_chunks
import os

def cmd_segmentor():
    exists = True
    i = 0  # not so efficient as per reference
    while exists:
        if os.path.exists(f"chunk temp/chunk{i}.wav"):
            os.remove(f"chunk temp/chunk{i}.wav")
            i += 1
        else:
            exists = False


    exists = True
    i = 1  # not so efficient as per reference
    while exists:
        if os.path.exists(f"Proto/recording{i}.wav"):
            i += 1
        else:
            exists = False
    song = f'Proto/recording{i-1}.wav'

    myaudio = AudioSegment.from_file(song, "wav")
    chunk_length_ms = 1000  # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms)  # Make chunks of one sec

    # Export all of the individual chunks as wav files

    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.wav".format(i)
        print("exporting", chunk_name)
        chunk.export(f'chunk temp/{chunk_name}', format="wav")

