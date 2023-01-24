from pytube import YouTube

def Download_high_resolution(link):
    objeto = YouTube(link)
    objeto = objeto.streams.get_highest_resolution()
    try:
        objeto.download()
        print("The video was downloaded.")
    except:
        print("An error ocurred.")

def Download_audio_only(link):
    objeto = YouTube(link)
    objeto = objeto.streams.get_audio_only()
    try:
        objeto.download()
        print("The video was downloaded.")
    except:
        print("An error ocurred.")

def Download_low_resolution(link):
    objeto = YouTube(link)
    objeto = objeto.streams.get_lowest_resolution()
    try:
        objeto.download()
        print("The video was succesfully downloaded.")
    except:
        print("Somethig went wrong.")
while True: 
    link = input("Put the YouTube link here. URL:\n>>>")
    try:
        obj = YouTube(link)
        titulo = obj.title
        mode = input("Select a mode:\n-High resolution /.mp4 (H).\n-Low resolution /.mp4 (L).\n-Audio only /.mp3(A).\n>>>")
        if mode == "H":
            modo = "high Resolution"
        elif mode == "L":
            modo = "low resoltion"
        elif mode == "A":
            modo = "audio only"
        print('The video is titled: "'+ titulo + '".\nMode:"' + modo + '".')
        q1 = input( "Do you want to download it? (Y/N).")
        if q1 == "Y":
            break
        elif q1 == "N":
            "Canceled, try again."
        else:
            print("Something went wrong.")
    except:
        print("Something went wrong.")
if mode == "H":
    Download_high_resolution(link)
elif mode == "L":
    Download_low_resolution(link)
elif mode == "A":
    Download_audio_only(link)
