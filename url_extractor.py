import os
from pytube import Playlist

def scrape_playlist(playlist_url, file_name):
    playlist = Playlist(playlist_url)
    os.makedirs('scraped_data', exist_ok=True)
    file_path = os.path.join('scraped_data', f"{file_name}.txt")

    with open(file_path, "w", encoding="utf-8") as url_file:
        for video in playlist.videos:
            url_file.write(f"{video.title}\n{video.watch_url}\n\n")

    print(f"Extracted video URLs and titles from playlist and saved to {file_path}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    file_name = input("Enter the file name (without extension): ")

    scrape_playlist(playlist_url, file_name)
