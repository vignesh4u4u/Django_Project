from pydub import AudioSegment
import os

def convert_m4a_to_mp3(m4a_file, output_path):
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    mp3_file = output_path + m4a_file.replace('.m4a', '.mp3')
    audio.export(mp3_file, format="mp3", bitrate="192k")
    print(f"Converted: {mp3_file}")
    os.remove(m4a_file)
    print(f"Deleted original file: {m4a_file}")



output_path = r"../Downloadfile/Rick Astley - Never Gonna Give You Up (Official Music Video).m4a"
convert_m4a_to_mp3(output_path, "./")
