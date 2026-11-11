import streamlit as st
from chatbot import repondre

# Configuration de la page
st.set_page_config(
    page_title="IRGIB CONNECT AI",
    page_icon="🎓",
    layout="centered"
)

# Titre
st.title("🎓 IRGIB CONNECT AI")
st.subheader("Assistant intelligent d'IRGIB Africa")

st.write(
    "Bienvenue ! Je suis votre assistant universitaire. "
    "Posez-moi vos questions sur les horaires, les inscriptions, "
    "la bibliothèque, les salles et les examens."
)

st.divider()

# Initialisation de l'historique
if "historique" not in st.session_state:
    st.session_state.historique = []

# Affichage des anciens messages
for role, texte in st.session_state.historique:
    with st.chat_message(role):
        st.write(texte)

# Zone de saisie
message = st.chat_input("Écrivez votre question ici...")

if message:
    # Afficher le message utilisateur
    with st.chat_message("user"):
        st.write(message)

    # Obtenir la réponse du chatbot
    try:
        reponse = repondre(message)
    except Exception:
        reponse = (
            "Désolé, une erreur est survenue. "
            "Veuillez réessayer ou contacter un responsable."
        )

    # Afficher la réponse
    with st.chat_message("assistant"):
        st.write(reponse)

    # Sauvegarder les messages dans l'historique
    st.session_state.historique.append(("user", message))
    st.session_state.historique.append(("assistant", reponse))

# Bouton pour effacer la conversation
if st.button("Effacer la conversation"):
    st.session_state.historique = []
    st.rerun()

# Pied de page
st.divider()
st.caption("IRGIB CONNECT AI | Assistant universitaire | IRGIB Africa")


