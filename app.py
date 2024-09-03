import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import random
import pandas as pd
from gtts import gTTS
import io

def load_questions(file):
    df = pd.read_excel(file, engine='openpyxl')
    questions = df.to_dict(orient='records')  # Convert to list of dictionaries
    random.shuffle(questions)
    return questions

def text_speech(text):
    myobj = gTTS(text=text, lang='en', slow=True)  ## converting audio format
    audio_bytes = io.BytesIO()
    myobj.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes



file = st.file_uploader('upload your file')


startBtn = st.button('Start')

        
if startBtn and file is not None:

    st.session_state.questions = load_questions(file)
    st.session_state.quiz_started = True
    

st.title("Quiz App")

if 'quiz_started' in st.session_state and st.session_state.quiz_started:
    questions = st.session_state.questions
    
    for current_question in range(len(questions)):
        col1, col2 = st.columns(2)
    # Display the current question
        with col1:
            st.markdown(f'<p style="color:red;">{questions[current_question]["question"]}</p>', unsafe_allow_html=True)
        with col2:
            st.audio(text_speech(questions[current_question]["question"]), format='audio/mp3')
        # Button to view the answer
        if st.button('View Answer', key=f'view_{current_question}'):
            col1, col2 = st.columns(2)
            st.text(f"Sentence: {questions[current_question]["Sentence"]}")
            st.markdown("---")
            with col1:
                st.success(questions[current_question]["answer"])
            with col2:
                st.audio(text_speech(questions[current_question]["answer"]), format='audio/mp3')  # playing audio


    if st.button('Reload'):
        random.shuffle(questions)
        # streamlit_js_eval(js_expressions="parent.window.location.reload()")