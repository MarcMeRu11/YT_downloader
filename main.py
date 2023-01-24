from pytube import YouTube

def Download_high_resolution(link):
    objeto = YouTube(link)
    objeto = objeto.streams.get_highest_resolution()
    try:
        objeto.download()
        print("The video was downloaded.")
    except:
        print("An error ocurred.")

link = input("Put the YouTube link here. URL:")
Download_high_resolution(link)