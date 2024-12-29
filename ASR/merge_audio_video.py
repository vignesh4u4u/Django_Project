from moviepy.editor import VideoFileClip, AudioFileClip
video_file = "../Downloadfile/video.mp4"
audio_file = "../Downloadfile/crewAI Crash Course For Beginners-How To Create Multi AI Agent For Complex Usecases.m4a"
output_file = "merged_video.mp4"
video_clip = VideoFileClip(video_file)
audio_clip = AudioFileClip(audio_file)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

print("Merging completed. The output file is saved at:", output_file)

print("mergefile startded")
video = VideoFileClip(video_path)
audio = AudioFileClip(audio_path)
video = video.set_audio(audio)
final_video_path = os.path.join(save_path, f"{video_title}.mp4")
video.write_videofile(final_video_path, codec="libx264")