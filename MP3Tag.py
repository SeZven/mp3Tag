import os
import eyed3


PATH = "" # Path to .mp3 files

def main():
    for root,dirs,files, in os.walk(PATH):
        for name in files:
            if name.endswith(".mp3"): # name = "artist - title.mp3"
                artist, title = name.split(" - ")
                title = title.removesuffix(".mp3")
                audiofile = eyed3.load(f"{PATH}\{name}")
                audiofile.tag.artist = artist
                audiofile.tag.title = title
                audiofile.tag.save()
                

main()


