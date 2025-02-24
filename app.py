import streamlit as st
from diet_agent import get_diet_plan

st.title("🥗 Personalized Diet Planner AI")

# Collect user details
st.sidebar.header("Enter Your Details")
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25)
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=170)
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])
diet_preference = st.sidebar.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan", "Keto", "Paleo"])
allergies = st.sidebar.text_input("Allergies (if any)")
preferences = st.sidebar.text_input("Preferences (if any)")

# Generate diet plan
if st.sidebar.button("Generate Diet Plan"):
    user_input = f"""
    Age: {age} years
    Weight: {weight} kg
    Height: {height} cm
    Activity Level: {activity_level}
    Diet Preference: {diet_preference}
    Allergies: {allergies}
    Preferences:{preferences}
    Generate a personalized diet plan.
    Output Format="The Text should be less that 5 Lines","Provide a Detailed Table format of plan with time stamps"
    """
    diet_plan = get_diet_plan(user_input)
    st.subheader("Your Personalized Diet Plan 🍽️")
    if diet_plan is None:
      st.write("Clone and use with your api key.")
    st.write(diet_plan)
