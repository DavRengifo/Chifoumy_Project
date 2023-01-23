import streamlit as st

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Administration</h1>"
st.markdown(html_title, unsafe_allow_html=True)

#-------------------------------------------------------------------------------

button = st.button("Réinitialiser les scores")

if button:
    file = open("scores.txt", "w")
    file.write("0,0")
    file.close()
    st.write("✅ Scores réinitialisés à zéro.")
