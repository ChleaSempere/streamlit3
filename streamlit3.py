import streamlit as st

import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
    
    # Importation du module
    from streamlit_option_menu import option_menu


# Création du menu qui va afficher les choix qui se trouvent dans la variable options
    selection = st.sidebar.selectbox(
            "Menu",
            ("Accueil", "Photos")
        )

# On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
        st.write("Bienvenue sur ma page !")
        st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGM5OWJ5Zng2bjB5ODZmampwZ29ybDVhdDduZGVmM3M5bDVpYzNtcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XD9o33QG9BoMis7iM4/giphy.webp")
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")
# ... et ainsi de suite pour les autres pages



if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')




  
