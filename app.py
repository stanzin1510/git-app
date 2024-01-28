import streamlit as st
st.title('Thiksay Monastry')
col1,col2 = st.columns(2)
with col1:
    st.image('thiksay monastry.png')
with col2:
    st.header('Thiksay Monastry is an Budddhist Monastry')
st.header('Mostly asked questions')
st.subheader('Why is thiksay monastry famous')
st.subheader('How old is thiksay Monastry')
st.subheader('What is the entry fees for Thiksay Monastry')

st.sidebar.title("Menu")
st.sidebar.markdown(
    """
    -Home
    -Contact
    -Career
    -Login
    """
)