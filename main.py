# import streamlit as st
# import subprocess

# def download_video_with_ytdlp(link):
#     try:
#         # Download video using yt-dlp
#         output_path = "downloaded_video.mp4"
#         command = ["yt-dlp", "-o", output_path, link]
#         subprocess.run(command, check=True)
#         return output_path
#     except Exception as e:
#         return f"Error: {e}"

# def main():
#     st.title("YouTube Video Downloader")

#     # Input for YouTube link
#     youtube_url = st.text_input("Enter YouTube Video Link:")

#     if st.button("Download Video"):
#         if youtube_url:
#             with st.spinner("Downloading..."):
#                 result = download_video_with_ytdlp(youtube_url)

#             if result and not result.startswith("Error"):
#                 st.success("Video downloaded successfully!")

#                 # Provide a download button for the user
#                 with open(result, "rb") as file:
#                     st.download_button(
#                         label="Download File",
#                         data=file,
#                         file_name="downloaded_video.mp4",
#                         mime="video/mp4"
#                     )
#             else:
#                 st.error(f"Failed to download video: {result}")
#         else:
#             st.warning("Please enter a valid YouTube link.")

# if __name__ == "__main__":
#     main()


import streamlit as st
import subprocess
import hashlib
from datetime import datetime

def generate_unique_filename(link):
    """Generate a unique filename based on the video link and timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    hashed_link = hashlib.md5(link.encode()).hexdigest()[:8]
    return f"video_{hashed_link}_{timestamp}.mp4"

def download_video_with_ytdlp(link):
    try:
        # Generate a unique filename for each video
        output_path = generate_unique_filename(link)

        # Download video using yt-dlp
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
                        file_name=result,
                        mime="video/mp4"
                    )
            else:
                st.error(f"Failed to download video: {result}")
        else:
            st.warning("Please enter a valid YouTube link.")

if __name__ == "__main__":
    main()
