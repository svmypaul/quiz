import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import random
import pandas as pd

def load_questions(file):
    df = pd.read_excel(file, engine='openpyxl')
    questions = df.to_dict(orient='records')  # Convert to list of dictionaries
    random.shuffle(questions)
    return questions

file = st.file_uploader('upload your file')

# Define questions and answers
# questions = [
#     {
#         "question": "What is the capital of France?",
#         "answer": "Paris"
#     },
#     {
#         "question": "What is 2 + 2?",
#         "answer": "4"
#     },
#     {
#         "question": "What is the largest ocean on Earth?",
#         "answer": "Pacific"
#     }
# ]
startBtn = st.button('Start')

        
if startBtn and file is not None:

    st.session_state.questions = load_questions(file)
    st.session_state.quiz_started = True
    

st.title("Quiz App")

if 'quiz_started' in st.session_state and st.session_state.quiz_started:
    questions = st.session_state.questions
    
    for current_question in range(len(questions)):
    # Display the current question
        st.text(questions[current_question]["question"])

        # Button to view the answer
        if st.button('View Answer', key=f'view_{current_question}'):
            st.info(questions[current_question]["answer"])


    if st.button('Reload'):
        random.shuffle(questions)
        # streamlit_js_eval(js_expressions="parent.window.location.reload()")