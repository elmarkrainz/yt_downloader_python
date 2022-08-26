from pytube import YouTube

url = 'https://www.youtube.com/watch?v=9ZBmn5AzbPE'
print (url)

yt_video = YouTube(url)
print(yt_video.title)

yt_video = yt_video.streams.get_highest_resolution()
yt_video.download()

print('your video is downloaded successfully')
