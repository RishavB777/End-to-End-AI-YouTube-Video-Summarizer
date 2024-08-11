# End-to-End-AI-YouTube-Video-Summarizer
An end-to-end AI YouTube Video Summarizer

## Introduction
* Utilized the YouTube Transcript API in the back-end to retrieve captions from YouTube videos.
* Integrated Google Gemini Pro to generate detailed summaries based on the fetched captions.
* Used Streamlit for the front-end experience

## Libraries used
* youtube_transcript_api
* streamlit
* google-generativeai
* python-dotenv
* pathlib

## Setup
To run first of all, install all the requirements by running the following code on your terminal/command prompt:

```
pip install -r "requirements.txt"
```

After installing all the dependencies all that is left to do is run the app on streamlit using the following code on your terminal/command prompt:
```
streamlit run app.py
```

