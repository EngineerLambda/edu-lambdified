import os
import streamlit as st


cwd = os.getcwd()

welcome_page = st.Page(page=os.path.join(cwd, "welcome.py"), title="Welcome page", icon="👋")
youtube_rag = st.Page(page=os.path.join(cwd, "youtube_rag.py"), title="Chat with Youtube videos", icon="⏯️")
summarizer_py = st.Page(page=os.path.join(cwd, "summarizer.py"), title="Summarize documents and download (format preserved)", icon="🗒️")
qa_session = st.Page(page=os.path.join(cwd, "qa_app.py"), title="Actively Practice documents with AI", icon="✍")
gpa_calculator = st.Page(page=os.path.join(cwd, "gpa_calculator.py"), title="Calculate GPA and get AI guidance", icon="📱")
image_explain = st.Page(page=os.path.join(cwd, "image_explain.py"), title="Capture and Ask", icon="🖼️")

pg = st.navigation(pages=[welcome_page, youtube_rag, summarizer_py, qa_session, gpa_calculator, image_explain])

pg.run()