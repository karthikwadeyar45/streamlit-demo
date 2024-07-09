# To run this app --> streamlit run app.py
import streamlit as st

st.title('Streamlit Web Application Demo')
st.header('Heading Streamlit')
st.subheader('Sub-Heading Streamlit')
st.text('This is a simple text')
st.success("Success")
st.warning("Warning")
st.info("Information")
st.error("Error")
if st.checkbox('Select/Unselect'):
    st.text('Checkbox is selected')
else:
    st.text('Checkbox is not selected')

state = st.radio('Select your state', ('Maharashtra', 'Karnataka', 'Tamil Nadu'))

if state == 'Karnataka':
    st.success("That's my state as well")

occupation = st.selectbox('Select your occupation', ['Student', 'Data Scientist', 'Web Developer', 'Doctor'])
st.text(f'You selected {occupation}')

if st.button('Click Me'):
    st.error('Button is clicked')

st.sidebar.header("Heading of Sidebar")
st.sidebar.text("Created by Karthik")