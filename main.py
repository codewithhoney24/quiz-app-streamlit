import streamlit as st
import random
import time

# Custom styling for better UI
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(65deg, #D8BFD8, #B0E0E6);
        }
        .gradient-text {
            background: linear-gradient(45deg, #FF00FF, #0000FF, #000000, #00FF00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .stButton > button {
            background: linear-gradient(45deg, #E6E6FA, #ADD8E6);
            color: #00008B;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px;
            border: none;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background: linear-gradient(45deg, #D8BFD8, #B0E0E6);
            color: black;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with proper icon styling
st.markdown("<h1>🤖 <span class='gradient-text'>AGI Knowledge Quiz</span> 🧠</h1>", unsafe_allow_html=True)

# Define quiz questions
questions = [
    {"question": "🔍 What does AGI stand for?", 
     "options": ["Advanced General Intelligence", "Artificial General Intelligence", "Automated Global Interaction", "Augmented General Intelligence"], 
     "answer": "Artificial General Intelligence"},
    
    {"question": "🎯 Which of the following is a key goal of AGI?", 
     "options": ["Mimic human-like decision making", "Perform only specific tasks", "Enhance existing narrow AI", "Run on quantum computers only"], 
     "answer": "Mimic human-like decision making"},
    
    {"question": "🧑‍🔬 Which scientist is known for his contributions to AI and AGI research?", 
     "options": ["Alan Turing", "Albert Einstein", "Isaac Newton", "Marie Curie"], 
     "answer": "Alan Turing"},
    
    {"question": "🤔 What is a major challenge in achieving AGI?", 
     "options": ["Creating self-awareness", "Improving hardware only", "Replacing human workers", "Coding in Python"], 
     "answer": "Creating self-awareness"},
    
    {"question": "🔄 What distinguishes AGI from Narrow AI?", 
     "options": ["AGI can perform multiple tasks flexibly", "AGI uses machine learning", "AGI is faster", "AGI is built using Python"], 
     "answer": "AGI can perform multiple tasks flexibly"},
    
    {"question": "🧠 Which field is closely related to AGI?", 
     "options": ["Cognitive Science", "Astrophysics", "Chemistry", "Linguistics"], 
     "answer": "Cognitive Science"},
    
    {"question": "⚠️ What is a common fear about AGI?", 
     "options": ["Job loss", "Conscious AI taking over", "Slower computers", "Higher electricity bills"], 
     "answer": "Conscious AI taking over"},
    
    {"question": "🧩 What is an essential component of AGI?", 
     "options": ["Reasoning and problem-solving", "Fast computing only", "Cloud storage", "Pre-written commands"], 
     "answer": "Reasoning and problem-solving"},
    
    {"question": "💻 Which programming language is often used in AGI research?", 
     "options": ["Python", "Swift", "HTML", "CSS"], 
     "answer": "Python"},
    
    {"question": "🎯 What is the ultimate goal of AGI?", 
     "options": ["Achieve human-level intelligence", "Automate industries", "Replace search engines", "Enhance social media"], 
     "answer": "Achieve human-level intelligence"}
]

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

# Check if the quiz is completed
if st.session_state.question_index < len(questions):
    question = questions[st.session_state.question_index]
    
    # Display the question
    st.subheader(question["question"])
    
    # Create radio buttons for options
    selected_option = st.radio("Choose your answer:", question["options"], key=f"quiz_q{st.session_state.question_index}")
    
    # Submit button
    if st.button("🚀 Submit Answer"):
        if selected_option == question["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is: {question['answer']}")
        
        time.sleep(1)
        st.session_state.question_index += 1
        st.rerun()
else:
    # Display Final Score
    st.subheader("🎉 Quiz Completed!")
    st.write(f"🏆 Your Final Score: **{st.session_state.score} / {len(questions)}**")
    
    if st.session_state.score >= 9:
        st.markdown("<h2>🌟 Congratulations! You are an AGI expert! 🎊</h2>", unsafe_allow_html=True)
        st.balloons()
        st.success("🌟 Congratulations! You are an AGI expert! 🎊")  

    # Restart button should only appear after the quiz is complete
    if st.button("🔄 Restart Quiz"):
        st.session_state.clear()
        st.rerun()

  # Footer
st.markdown("<h6 style='text-align: center; margin-top: 40px;'>🚀 Built by <span class='gradient-text'>Nousheen Atif</span> 💡</h6>", unsafe_allow_html=True)
