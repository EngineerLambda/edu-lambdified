## Education Lambdified - Powered by Gemini (Google)
Live URL of developed app: https://edu-lambdified.streamlit.app/
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
https://github.com/user-attachments/assets/78fb0e7f-4ab0-4c5f-ba5a-8afb1e020255


### 2. **Summarize documents and download (format preserved)**
###### About
This tool allows students (main target) or just anyone at all to be able to upload documents in (docx and pdf) format, and download a summarized version in the exact format they have uploaded.
###### Use case
Completing reading materials in a shorter time, while not missing the important points

###### Future additions
* Have support for more file formats (e.g pptx)
* Have support for longer documents

###### Sample

https://github.com/user-attachments/assets/bcd6e97b-5e59-4850-ac99-d0c4b48448b0


### 3. **Actively Practice documents with AI**
###### About
This tool allows students to practice their documents, it creates a CBT-standard simulation, where they get to test how much information they are able to remember after reading.

###### Use case
Good way to practice for exams that requires high precision answers

###### Future additions
* Support longer documents
* Support more document formats

###### Sample

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

https://github.com/user-attachments/assets/b0ca65df-fc0e-4b7c-a091-128c98d9235d


### 5. **Capture and Ask**
###### About
This tool allows students to Upload images and get AI guides
###### Use case
This is good for when you have complicated equations and diagrams that you find hard to understand, whether in hard or soft copy materials, just capture (camera or screenshot) and ask AI, interactively.
###### Future additions
Allow upload of some other media files; gif, videos, ...
###### Sample

https://github.com/user-attachments/assets/81d32ac8-7826-4957-8777-b7e3a2539827

Technologies used:
* Python
* Langchain
* Google Gemini LLMs (Gemini Pro and Gemini 1.5 Flash)