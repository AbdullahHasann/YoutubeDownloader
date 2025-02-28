import yt_dlp
import os

# Function to download mp4 using yt-dlp
def download_video_from_file():
    # File containing YouTube links
    links_file = './linksmp4.txt'

    # Set the destination folder
    destination = r'C:\Example\example'

    # Check if the links file exists
    if not os.path.isfile(links_file):
        print(f"File '{links_file}' not found.")
        return

    try:
        # Read links from the file
        with open(links_file, 'r') as file:
            links = file.readlines()

        ydl_opts = {
            'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',  # Best video + best audio in MP4
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for link in links:
                link = link.strip()  # Remove any extra whitespace
                if link:  # Check if the link is not empty
                    print(f"Downloading {link}...")
                    ydl.download([link])

        print(f"Download complete! Files saved in: {destination}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
download_video_from_file()
