import streamlit as st
import os

base = os.path.join(os.getcwd(), "sample_vids")

def vid_name(name):
    return os.path.join(base, name)

st.set_page_config(page_title="Welcome Page", page_icon="👋")
part_1 = """
## Education Lambdified - Powered by Gemini (Google)
This is an AI solution to some of the problems faced by students in school. It focuses on four solutions:
1. Chat with Youtube videos
2. Summarize documents and download
3. Actively Practice documents with AI
4. Calculate GPA and get AI guidance

### 1. **Chat with Youtube videos**
###### About
This AI soloution makes use of Youtube video URL to obtain the video transcript, then processes it, to provide a custom question-answering AI chatbot. It also add the video summary on the side bar, just so users can have an idea on what questions to ask.
###### Use case
It saves one the stress of having to watch an entire video just to find a simple information.

###### Future additions
* Being able to upload your own video file to do just the same thing.
* Support longer videos

###### Sample
"""
st.markdown(part_1)
st.video(vid_name("youtube_rag.mp4"))

part_2 = """
### 2. **Summarize documents and download (format preserved)**
###### About
This tool allows students (main target) or just anyone at all to be able to upload documents in (docx and pdf) format, and download a summarized version in the exact format they have uploaded.
###### Use case
Completing reading materials in a shorter time, while not missing the important points

###### Future additions
* Have support for more file formats (e.g pptx)
* Have support for longer documents

###### Sample
"""
st.markdown(part_2)
st.video(vid_name("summarizer.mp4"))

part_3 = """
### 3. **Actively Practice documents with AI**
###### About
This tool allows students to practice their documents, it creates a CBT-standard simulation, where they get to test how much information they are able to remember after reading.

###### Use case
Good way to practice for exams that requires high precision answers

###### Future additions
* Support longer documents
* Support more document formats
* Use a better LLM with reliable JSON output
###### Sample
"""
st.markdown(part_3)


part_4 = """
### 4. **Calculate GPA and get AI guidance**
###### About
This tool allows students to track progress by calculating their gpa/cgpa based on both 4.0 and 5.0 system, together with AI recommendation on how to get their grades up.
It is divided into two sections:
* New: This helps to compute GPA for a single semester
* Old: This helps to calulculate cummulative GPA (CGPA) for all completed semesters using previous CGPA and number of units previously done.
###### Use case
Calculating CGPA before a new semester considering each of the new courses to be done, to be able to set minimum grade for each course, depending on a target goal. I have personally tried this in school and it helped all the time.

###### Future additions
Allow upload of result documents (pdf) or image (screenshot) to calculate CGPA.

###### Sample
"""
st.markdown(part_4)
st.video(vid_name("gpa_calculator.mp4"))


part_5 = """
### 5. **Capture and Ask**
###### About
This tool allows students to Upload images and get AI guides
###### Use case
This is good for when you have complicated equations and diagrams that you find hard to understand, whether in hard or soft copy materials, just capture (camera or screenshot) and ask AI, interactively.
###### Future additions
Allow upload of some other media files; gif, videos, ...
###### Sample
"""
st.markdown(part_5)
st.video(vid_name("capture.mp4"))
