import os
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process
import streamlit as st

# Initialize the model
model = Ollama(model="llama3")
is_verbose = False

# Set environment variables
os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'llama-3.1-8b-instant'
os.environ["OPENAI_API_KEY"] = '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'

# Title of the app
st.title("Academic Support Tool")

# Create input fields for each question
student_id = st.text_input("1. Student ID:")
name = st.text_input("2. Name:")
learning_style = st.selectbox("3. Learning Style:", options=["Visual", "Auditory", "Kinesthetic"])
diversity_factor = st.selectbox("4. Diversity Factors:", options=["English", "Hispanic", "Other"])
engagement_level = st.selectbox("5. Engagement Level:", options=["High", "Medium", "Low"])
performance_metrics = st.number_input("6. Performance Metrics (out of 100):", min_value=0, max_value=100)
motivation_level = st.selectbox("7. Motivation Level:", options=["Very Motivated", "Somewhat Motivated", "Not Motivated"])
challenges_faced = st.text_area("8. Challenges Faced:")
parental_involvement = st.selectbox("9. Parental Involvement:", options=["High", "Medium", "Low"])
extracurricular_activities = st.text_input("10. Extracurricular Activities:")
social_interaction_preference = st.selectbox("11. Social Interaction Preference:", options=["Group", "Individual"])
learning_environment = st.selectbox("12. Learning Environment:", options=["Quiet", "Collaborative", "Structured"])
study_habits = st.text_area("13. Study Habits:")
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
    
     # Create prompt for LLaMA
    prompt = (
        f"I am {student_info['name']}. My learning style is {student_info['learning_style']}. "
        f"My diversity factor is {student_info['diversity_factor']}. "
        f"My engagement level is {student_info['dengagement_level']}"
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

    guru = Agent(
        role="Academic Support Tool for Students",
        goal="To understand the needs of students and help them with personalised solution",
        backstory="You are an AI assistant whose only job is to understand the individual needs of the students and provide them with a personalised solution to make them successful in their life",
        verbose=True,
        allow_delegation=False,
        llm=model
    )

    response = Task(
        description=f"Respond to the prompt: '{prompt}' based on the metrics provided by the student.",
        agent=guru,
        expected_output="Give a suitable and personalised solution to each student"
    )

    crew = Crew(
        agents=[guru],  # Wrap the agent in a list
        tasks=[response],  # Wrap the task in a list
        verbose=1,
        process=Process.sequential
    )

    output = crew.kickoff()
    print("Crew Output:", output)
    st.write(output)  # Display the output in the Streamlit app
