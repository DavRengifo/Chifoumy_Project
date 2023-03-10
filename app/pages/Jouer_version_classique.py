#===============================================================================

import random
import streamlit as st
from chifoumy.interface.detection import picture_to_df
from chifoumy.ml_logic.registry import load_pipeline
#from chifoumy.interface.utils import create_key

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

MAX_SCORE = 3

def scoring(machine_gesture, user_gesture):
    """
    0: pierre,
    1: feuille,
    2: ciseaux,
    """
    if user_gesture==machine_gesture:
        return "null"
    elif user_gesture==0 and machine_gesture==2:
        return "user"
    elif user_gesture == 1 and machine_gesture == 0:
        return "user"
    elif user_gesture == 2 and machine_gesture == 1:
        return "user"
    else:
        return "machine"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Jouons contre la machine !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

#-------------------------------------------------------------------------------

file = open("scores.txt", "r")
for line in file:
    tab = line.split(",")
    user_score = int(tab[0])
    machine_score = int(tab[1])
file.close()

picture = None
placeholder1 = st.empty()
picture = placeholder1.camera_input("", key=666)
if picture:
    df = picture_to_df(picture)

    if type(df) == type("toto"):
        st.write("Problème dans l'acquisition photo.")
    else:
        my_pipeline = load_pipeline()
        target = my_pipeline.predict(df)
        target = target[0]
        html_user_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
        html_user_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
        html_user_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
        #----

        user_dict = {0: html_user_pierre, 1: html_user_feuille, 2: html_user_ciseaux}
        user_gesture = user_dict[target]

        #----------------
        # Jeu de l'IA
        machine_play = random.randint(0, 2)
        html_machine_pierre ="<div style='color:#E37B01;font-size:30px'>Geste machine : pierre</div>"
        html_machine_feuille ="<div style='color:#AEC90E;font-size:30px'>Geste machine : feuille</div>"
        html_machine_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Geste machine : ciseaux</div>"
        machine_dict = {0: html_machine_pierre, 1: html_machine_feuille, 2: html_machine_ciseaux}
        machine_gesture = machine_dict[machine_play]

        #----------------

        # scoring
        result = scoring(machine_play, target)
        if result=="machine":
            machine_score += 1
        elif result=="user":
            user_score += 1
        elif result=="null":
            pass
        user_html = f"<div style='color:#44B7E3;font-size:30px'>🙂 Score du joueur : {user_score}</div>"
        machine_html = f"<div style='color:#44B7E3;font-size:30px'>🤖 Score de la machine : {machine_score}</div>"
        file = open("scores.txt", "w")
        file.write(f"{user_score},{machine_score}")
        file.close()

        #-------------------------------------------------------------------

        # Affichage amélioré
        IMAGE_PIERRE_PATH = "https://www.bejian.fr/chifoumy/images/"
        machine_image_dict = {0: "logo_rock_machine.png",1: "logo_paper_machine.png",2: "logo_scissors_machine.png"}
        human_image_dict = {0: "logo_rock_human.png",1: "logo_paper_human.png",2: "logo_scissors_human.png"}
        image_user = IMAGE_PIERRE_PATH + human_image_dict[target]
        image_machine = IMAGE_PIERRE_PATH + machine_image_dict[machine_play]
        big_html = f"""
        <div style="display:flex;justify-content:center;align-items:center;width:100%;height:100%">
        <table>
        <tr>
            <th style='text-align:center;font-size:30px'>🙂 Humain</th>
            <th style='text-align:center;font-size:30px'>🤖 Machine</th>
        </tr>
        <tr>
            <td><img src='{image_user}' width='300'></td>
            <td><img src='{image_machine}' width='300'></td>
        </tr>
        <tr>
            <td style='text-align:center;font-size:50px;color:#44B7E3'>{user_score}</td>
            <td style='text-align:center;font-size:50px;color:#44B7E3'>{machine_score} </td>
        </tr>
        </table>
        </div>
        <br>
        """
        st.markdown(big_html, unsafe_allow_html=True)

        #-------------------------------------------------------------------

        if machine_score==MAX_SCORE:
            final_html = f"<div style='color:#FF036A;font-size:30px'>➡️ Victoire de la machine !</div>"
            st.markdown(final_html, unsafe_allow_html=True)
        if user_score==MAX_SCORE:
            final_html = f"<div style='color:#FF036A;font-size:30px'>➡️ Victoire de l'humain !</div>"
            st.markdown(final_html, unsafe_allow_html=True)
