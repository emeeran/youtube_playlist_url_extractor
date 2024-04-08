from pytube import Playlist

# Replace with your playlist URL
playlist_url = input("Enter the YouTube playlist URL: ")
file_name = input("Enter the file name (without extension): ")

# Ensure the file name includes the ".txt" extension
file_name_with_extension = f"{file_name}.txt"

try:
    # Create a playlist object
    playlist = Playlist(playlist_url)

    # Open a file for writing URLs and titles with UTF-8 encoding
    with open(file_name_with_extension, "w", encoding="utf-8") as url_file:
        # Loop through videos in playlist and directly write titles and URLs
        for video in playlist.videos:
            url_file.write(f"{video.title}\n{video.watch_url}\n\n")

    print(f"Extracted video URLs and titles from playlist and saved to {file_name_with_extension}")

except Exception as e:
    print("An error occurred:", e)
