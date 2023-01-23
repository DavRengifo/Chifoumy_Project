#===============================================================================

import streamlit as st
from PIL import Image

#-------------------------------------------------------------------------------

from chifoumy.interface.detection import take_a_picture, picture_to_df
from chifoumy.interface.utils import create_key
from chifoumy.ml_logic.registry import load_pipeline

#===============================================================================

IMAGE_PATH = "data_images/ciseaux/"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Alimentons le dataset « ciseaux » !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

#-------------------------------------------------------------------------------

picture = None
picture = take_a_picture(key=6453)
if picture:
    button1 = st.button("Sauvegarder la photo", key=1)
    if button1:
        df = picture_to_df(picture)
        if type(df) == type("toto"):
            st.write("Problème dans l'acquisition photo.")
        else:
            st.write("✅ Acquisition photo OK")
            #----
            my_pipeline = load_pipeline()
            target = my_pipeline.predict(df)
            target = target[0]
            #----
            html_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
            html_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
            html_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
            chifoudict = {0: html_pierre, 1: html_feuille, 2: html_ciseaux}
            texte_pierre = "Votre geste : pierre"
            texte_feuille = "Votre geste : feuille"
            texte_ciseaux = "Votre geste : ciseaux"
            simpledict = {0: texte_pierre, 1: texte_feuille, 2: texte_ciseaux}
            html_gesture = chifoudict[target]
            texte_gesture = simpledict[target]
            st.write(f"✅ {texte_gesture}")
            #----
            file_name = IMAGE_PATH + "image_" + str(create_key()) + ".png"
            img_pil = Image.open(picture)
            img_pil.save(file_name)
            st.write(f"✅ Sauvegarde de la photo '{file_name}'.")
