from pytube import YouTube
from sys import argv

#enter link as the command line argument

link = input("Enter link: ") 
yt = YouTube(link)
#print(yt.title)

stream = yt.streams.get_highest_resolution()
stream.download()
