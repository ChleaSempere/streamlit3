import streamlit as st
from streamlit_authenticator import Authenticate
# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,  # Sera géré automatiquement
            'logged_in': False,  # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,  # Sera géré automatiquement
            'logged_in': False,  # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "nom_du_cookie",  # Le nom du cookie, un str quelconque
    "cle_du_cookie",  # La clé du cookie, un str quelconque
    30  # Le nombre de jours avant que le cookie expire
)
# Connexion utilisateur
authenticator.login()
def accueil():
    st.title("Bienvenue sur la page d'accueil")
    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGM5OWJ5Zng2bjB5ODZmampwZ29ybDVhdDduZGVmM3M5bDVpYzNtcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XD9o33QG9BoMis7iM4/giphy.webp") # Lien vers le GIF
def photos_chat():
    st.subheader("Les photos des animaux")
    # Créer des colonnes pour afficher les images sur la même ligne
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.image("https://static.streamlit.io/examples/owl.jpg")
if st.session_state["authentication_status"]:
    # Le bouton de déconnexion au-dessus du menu
    authenticator.logout("Déconnexion")
    # Menu dans la barre latérale, seulement si connecté
    option = st.sidebar.selectbox(
        "Menu",
        ["Accueil", "Les photos de mes animaux"]
    )
    # Affichage du contenu selon l'option sélectionnée
    if option == "Accueil":
        accueil()
    elif option == "Les photos de mon chat":
        photos_chat()
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
