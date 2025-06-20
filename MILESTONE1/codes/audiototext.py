import speech_recognition as sr
from moviepy.editor import AudioFileClip
import os
# Function to convert mp3 to wav using moviepy
def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    if not os.path.exists(mp3_file_path):
        raise FileNotFoundError(f"Audio file not found: {mp3_file_path}")
    
    audio_clip = AudioFileClip(mp3_file_path)
    audio_clip.write_audiofile(wav_file_path)

# Function to convert audio file to text
def audio_to_text(wav_file):
    r = sr.Recognizer()
    try:
        # Load the wav file
        with sr.AudioFile(wav_file) as source:
            # Adjust for ambient noise and record the audio
            r.adjust_for_ambient_noise(source)
            audio_data = r.record(source)
            
            # Recognize the speech using Google Web Speech API
            text = r.recognize_google(audio_data)
            return text
    
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)
    
    except sr.UnknownValueError:
        return "Audio not understandable"

# Function to save transcription to a text file
def save_transcription_to_file(text, file_path):
    with open(file_path, "w") as text_file:
        text_file.write(text)

# Path to the mp3 file
mp3_file_path = "Meeting-Summarizer-and-plan-of-action-generator-using-NLP_oct_2024\\MILESTONE1\\audioandvideo\\audio.mp3"  # Replace with your mp3 file path
wav_file_path = "converted_audio.wav"
transcription_file_path = "transcription1.txt"

# Convert mp3 to wav
convert_mp3_to_wav(mp3_file_path, wav_file_path)

# Convert the wav file to text
transcription = audio_to_text(wav_file_path)

# Save the transcription to a text file
if transcription:
    save_transcription_to_file(transcription, transcription_file_path)
    print(f"Transcription saved to {transcription_file_path}")
else:
    print("No transcription to save.")