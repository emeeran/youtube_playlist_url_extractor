from pytube import Playlist, YouTube

# Replace with your playlist URL
playlist_url = input("Enter the YouTube playlist URL: ")
file_name = input("Enter the file name: ")

# Create a playlist object
playlist = Playlist(playlist_url)

# Open a file for writing URLs and titles
with open(file_name, "w") as url_file:
    # Loop through videos in playlist and extract URLs and titles
    for video_url in playlist.video_urls:
        # Create a YouTube object for each video URL
        video = YouTube(video_url)
        # Extract the video title
        video_title = video.title
        # Write the URL and title to the file, separated by a comma
        url_file.write(f"{video_url}, {video_title}\n")

print(f"Extracted video URLs and titles from playlist and saved to {file_name}.txt")
