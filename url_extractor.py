import os
from pytube import Playlist

def scrape_playlist(playlist_url, file_name):
    """
    Scrape video URLs and titles from a YouTube playlist and save them to a file in the 'scraped_data' directory.

    Parameters:
    playlist_url (str): The URL of the YouTube playlist.
    file_name (str): The name of the file to save the scraped data to, without extension.
    """
    try:
        # Create a playlist object
        playlist = Playlist(playlist_url)

        # Ensure the 'scraped_data' directory exists
        if not os.path.exists('scraped_data'):
            os.makedirs('scraped_data')

        # Ensure the file name includes the ".txt" extension
        file_name_with_extension = f"{file_name}.txt"
        # Specify the full path to the file within the 'scraped_data' directory
        file_path = os.path.join('scraped_data', file_name_with_extension)

        # Open a file for writing URLs and titles with UTF-8 encoding
        with open(file_path, "w", encoding="utf-8") as url_file:
            # Loop through videos in playlist and directly write titles and URLs
            for video in playlist.videos:
                url_file.write(f"{video.title}\n{video.watch_url}\n\n")

        print(f"Extracted video URLs and titles from playlist and saved to {file_path}")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Replace with your playlist URL
    playlist_url = input("Enter the YouTube playlist URL: ")
    file_name = input("Enter the file name (without extension): ")

    scrape_playlist(playlist_url, file_name)
