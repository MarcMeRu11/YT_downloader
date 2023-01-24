from pytube import YouTube

def Download(link,mode):
    objeto = YouTube(link)
    if mode == "H":
        objeto = objeto.streams.get_highest_resolution()
    elif mode == "L": 
        objeto = objeto.streams.get_lowest_resolution()
    elif mode == "A":
        objeto = objeto.streams.get_audio_only()
    try:
        objeto.download()
        print("The video was downloaded.")
    except:
        print("An error ocurred.")

while True: 
    link = input("Put the YouTube link here. URL:")
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
        segundos = obj.length
        minutos = int(segundos / 60)
        segundos -= minutos * 60
        print('The video is titled: "'+ titulo + '".\nMode:"' + modo + '".\nThe length is:', str(minutos)+":"+str(segundos),"minutes.")
        q1 = input( "Do you want to download it? (Y/N).\n>>>")
        if q1 == "Y":
            break
        elif q1 == "N":
            "Canceled, try again."
        else:
            print("Something went wrong.")
    except:
        print("Something went wrong.")
Download(link,mode)
