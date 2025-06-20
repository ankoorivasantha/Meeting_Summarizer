import moviepy.editor as mp
from tkinter.filedialog import askopenfilename

def extract_audio():
    video_path = askopenfilename(title="Select Video File")
    if video_path:
        try:
            with mp.VideoFileClip(video_path) as video:
                audio = video.audio
                audio.write_audiofile("audio.mp3")
            print("Audio extraction completed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("No file selected.")

if __name__ == "__main__":
    extract_audio()
