from pytube import YouTube

url = (input("paste the YT url: "))

yt_video = YouTube(url)

yt_video = yt_video.streams.get_highest_resolution()

yt_video.download();

print("download fertig")
