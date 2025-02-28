import yt_dlp
import os

def download_audio_from_file():
    links_file = './links.txt'

    # Set the destination folder
    destination = r'C:\Example\example'
    if not os.path.isfile(links_file):
        print(f"File '{links_file}' not found.")
        return

    try:
        with open(links_file, 'r') as file:
            links = file.readlines()

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for link in links:
                link = link.strip()
                if link:  # Check if the link is not empty
                    print(f"Downloading {link}...")
                    ydl.download([link])

        print(f"Download complete! Files saved in: {destination}")
    except Exception as e:
        print(f"An error occurred: {e}")
download_audio_from_file()
