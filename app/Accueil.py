#===============================================================================

import streamlit as st
from PIL import Image

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

html_title = "<h1 style='color:#FF036A;text-align:left;font-size:90px'>Projet Chifoumy</h1>"
st.markdown(html_title, unsafe_allow_html=True)
image_path = IMAGE_PATH + "chifoumi__ter.jpg"
chifoumi_image = Image.open(image_path)
picture = st.image(chifoumi_image, width=600)
#button_play = st.button("Jouer")

#===============================================================================

#st.write(create_key())

