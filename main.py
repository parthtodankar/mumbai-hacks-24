import os
from langchain_community.llms import Ollama
import streamlit as st

# Set environment variables
os.environ["OpenAi_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["Llama_MODEL_NAME"] = 'llama-3.1-8b-instant'
os.environ["GROQ_API_KEY"] = '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'

# Initialize the model
model = Ollama(model="llama3.2")

# Title of the app
st.title("Academic Support Tool \n by Team [Matrix] at Mumbai Hacks 24")

# Create input fields for each question
student_id = st.text_input("1. Student ID:")
name = st.text_input("2. Name:")
learning_style = st.selectbox("3. Learning Style:", options=["Visual", "Auditory", "Kinesthetic"])
diversity_factor = st.selectbox("4. Diversity Factors:", options=["English", "Hispanic", "Learning and Physical Abilities", "Gender Identity", "Mental Health", "Geographic Location"])
engagement_level = st.selectbox("5. Engagement Level:", options=["High", "Medium", "Low"])
performance_metrics = st.number_input("6. Performance Metrics (out of 100):", min_value=0, max_value=100)
motivation_level = st.selectbox("7. Motivation Level:", options=["Very Motivated", "Somewhat Motivated", "Not Motivated"])
challenges_faced = st.text_area("8. Challenges Faced:")
parental_involvement = st.selectbox("9. Parental Involvement:", options=["High", "Medium", "Low"])
extracurricular_activities = st.text_input("10. Extracurricular Activities:")
social_interaction_preference = st.selectbox("11. Social Interaction Preference:", options=["Group", "Individual"])
learning_environment = st.selectbox("12. Learning Environment:", options=["Quiet", "Collaborative", "Structured"])
study_habits = st.selectbox("13. Study Habits:", options=["Daily Review", "Last-minute cramming", "Mind Mapping", "Flashcards"])
peer_relationships = st.selectbox("14. Peer Relationships:", options=["Positive", "Neutral", "Negative"])

# Button to submit the questionnaire
if st.button("Submit"):
    # Store answers as variables
    student_info = {
        "student_id": student_id,
        "name": name,
        "learning_style": learning_style,
        "diversity_factor": diversity_factor,
        "engagement_level": engagement_level,
        "performance_metrics": performance_metrics,
        "motivation_level": motivation_level,
        "challenges_faced": challenges_faced,
        "parental_involvement": parental_involvement,
        "extracurricular_activities": extracurricular_activities,
        "social_interaction_preference": social_interaction_preference,
        "learning_environment": learning_environment,
        "study_habits": study_habits,
        "peer_relationships": peer_relationships
    }
    
    prompt = (
        f"I am {student_info['name']}. My learning style is {student_info['learning_style']}. "
        f"My diversity factor is {student_info['diversity_factor']}. "
        f"My engagement level is {student_info['engagement_level']}"
        f"My performance metrics are {student_info['performance_metrics']}/100"
        f"My motivation level is {student_info['motivation_level']}"
        f"Challenges I face are {student_info['challenges_faced']}"
        f"My parental involvement is {student_info['parental_involvement']}"
        f"My extracuricular activities are {student_info['extracurricular_activities']}"
        f"My social interaction preference is {student_info['social_interaction_preference']}"
        f"My learning environment is {student_info['learning_environment']}"
        f"My study habit is {student_info['study_habits']}"
        f"My peer relationship is {student_info['peer_relationships']}"
        "Give me a solution to improve myself academically."
    )
    try:
        # Use invoke instead of generate
        response = model.invoke(prompt)
        
        # Display the output in the Streamlit app
        st.write("Personalized Academic Solution:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


footer_html = """<div style='text-align: center;'>
  <p>Developed with ❤️ by team [Matrix] (Parth and Neel)</p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)
