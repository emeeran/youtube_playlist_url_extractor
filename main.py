from pytube import Playlist, YouTube

# Replace with your playlist URL
playlist_url = input("Enter the YouTube playlist URL: ")
file_name = input("Enter the file name: ")

# Ensure the file name includes the ".txt" extension
file_name_with_extension = f"{file_name}.txt"

# Create a playlist object
playlist = Playlist(playlist_url)

# Open a file for writing URLs and titles with UTF-8 encoding
with open(file_name_with_extension, "w", encoding="utf-8") as url_file:
    # Loop through videos in playlist and extract URLs and titles
    for video_url in playlist.video_urls:
        # Create a YouTube object for each video URL
        video = YouTube(video_url)
        # Extract the video title
        video_title = video.title
        # Write the title on a new line, followed by the URL, and then an empty line
        url_file.write(f"{video_title}\n{video_url}\n\n")

print(f"Extracted video URLs and titles from playlist and saved to {file_name_with_extension}")
