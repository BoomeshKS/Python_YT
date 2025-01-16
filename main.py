import streamlit as st
import subprocess

def download_video_with_ytdlp(link):
    try:
        # Download video using yt-dlp
        output_path = "downloaded_video.mp4"
        command = ["yt-dlp", "-o", output_path, link]
        subprocess.run(command, check=True)
        return output_path
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("YouTube Video Downloader")

    # Input for YouTube link
    youtube_url = st.text_input("Enter YouTube Video Link:")

    if st.button("Download Video"):
        if youtube_url:
            with st.spinner("Downloading..."):
                result = download_video_with_ytdlp(youtube_url)

            if result and not result.startswith("Error"):
                st.success("Video downloaded successfully!")

                # Provide a download button for the user
                with open(result, "rb") as file:
                    st.download_button(
                        label="Download File",
                        data=file,
                        file_name="downloaded_video.mp4",
                        mime="video/mp4"
                    )
            else:
                st.error(f"Failed to download video: {result}")
        else:
            st.warning("Please enter a valid YouTube link.")

if __name__ == "__main__":
    main()
