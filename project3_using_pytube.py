import pytube 

video_url = "https://www.youtube.com/watch?v=B5p67d39uk4"  
# Example video URL
yt = pytube.YouTube(video_url)

stream = yt.streams.get_highest_resolution()
output_path = "D:/yt"  
# Example output directory
stream.download(output_path)
