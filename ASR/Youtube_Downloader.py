from pydub import AudioSegment
from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

def convert_m4a_to_mp3(m4a_file, output_path):
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    mp3_file = os.path.join(output_path, os.path.basename(m4a_file).replace('.m4a', '.mp3'))
    audio.export(mp3_file, format="mp3")
    print(f"Converted: {mp3_file}")
    os.remove(m4a_file)
    print(f"Deleted original file: {m4a_file}")
    return mp3_file

def download_both_files(url, save_path):
    yt = YouTube(url)
    video_stream = yt.streams.filter(res="480p", progressive=False, file_extension='mp4').first()
    video_path = video_stream.download(output_path=save_path, filename="video.mp4")
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    audio_path = audio_stream.download(output_path=save_path)
    print(f"Downloaded Video: {yt.title}")
    return video_path, audio_path, yt.title

def merge_audio_and_video_file(url, save_path):
    #video_path, audio_path, video_title = download_both_files(url, save_path)
    #mp3_audio_file = convert_m4a_to_mp3(audio_path,save_path)
    video_file = r"D:\Pycharm_Projects\Django_Tutorial\ASR\Downloadfile\video.mp4"
    audio_file = r"D:\Pycharm_Projects\Django_Tutorial\ASR\Downloadfile\AWS DevOps Full Course in 36 Hrs  Part-1  AWS DevOps Tutorial for Beginners AWS DevOps Training .m4a"
    final_video_path = os.path.join(save_path, f"AWS DevOps Tutorial.mp4")
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(final_video_path, codec="libx264", audio_codec="aac")
    os.remove(video_path)
    os.remove(audio_file)
    print(f"Final video saved at: {final_video_path}")

video_url = 'https://www.youtube.com/watch?v=wfvDnniPFXY&t=39080s'
merge_audio_and_video_file(video_url, 'Downloadfile')
#download_both_files(video_url,'Downloadfile')
