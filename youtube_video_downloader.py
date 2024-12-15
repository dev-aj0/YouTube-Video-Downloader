import yt_dlp

def download_youtube_video():
    video_url = input("Enter the YouTube video link: ")
    ydl_opts = {
        'format': 'best',  # Download the best available quality
        'outtmpl': '%(title)s.%(ext)s'  # Save the file with the video title as the filename
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
