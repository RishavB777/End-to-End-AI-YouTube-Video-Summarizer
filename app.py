import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. 
You will be taking the transcript text and summarizing the entire video and
providing the important summary in points within 250 words. Please provide a detailed 
summary of the text provided here.
"""

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+transcript_text)
    return response.text

def extract_transcript(yt_video_url):
    try:
        video_id = yt_video_url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        # Since the API returns a list, we have to loop through the list to append it
        # one by one and get the whole string inside a variable
        transcript =""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    

st.title("YouTube Video Summarizer")
yt_link = st.text_input("Enter YouTube video link:")

if yt_link:
    video_id = yt_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Summary"):
    transcript_text = extract_transcript(yt_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Summary:")
        st.write(summary)