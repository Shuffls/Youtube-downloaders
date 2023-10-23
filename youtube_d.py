import pytube

vid_url = input("Input your youtube URL: ")
yt = pytube.YouTube(vid_url)


stream = yt.streams.get_highest_resolution()
stream.download()