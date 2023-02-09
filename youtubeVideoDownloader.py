from pytube import YouTube


def video_download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("There has been an error")
    print("Video downloaded successfully")


link = input("Put the link here, URL: ")
video_download(link)
