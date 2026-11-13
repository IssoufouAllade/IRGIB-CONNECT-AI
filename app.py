import streamlit as st

from chatbot import repondre
from database import (
    creer_base,
    enregistrer_echange,
    recuperer_historique,
    supprimer_historique
)

# Initialisation de la base de données
creer_base()

# Configuration de la page
st.set_page_config(
    page_title="IRGIB CONNECT AI - Assistant universitaire IRGIB Africa",
    page_icon="🎓",
    layout="centered"
)

# Titre
st.title("🎓 IRGIB CONNECT AI")
st.subheader("Assistant intelligent d'IRGIB Africa")


st.text(
    "IRGIB CONNECT AI est un assistant conversationnel "
    "universitaire dédié à IRGIB Africa au Bénin. "
    "Il aide les étudiants à obtenir des informations "
    "sur les horaires, les inscriptions, la bibliothèque, "
    "les salles de cours et les examens."
)
st.divider()

# Initialisation de l'historique
if "historique" not in st.session_state:
    st.session_state.historique = []

# Affichage des anciens messages
for role, texte in st.session_state.historique:
    with st.chat_message(role):
        st.write(texte)
st.caption(
    "Information : les échanges sont enregistrés "
    "dans une base de données pour assurer le suivi "
    "et l'amélioration du chatbot. Évitez de communiquer "
    "des informations personnelles ou confidentielles."
)

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
        
    # Enregistrer la conversation dans SQLite
        enregistrer_echange(message, reponse)

    # Afficher la réponse
    with st.chat_message("assistant"):
        st.write(reponse)

    # Sauvegarder les messages dans l'historique
    st.session_state.historique.append(("user", message))
    st.session_state.historique.append(("assistant", reponse))

# Suppression de l'historique
st.subheader("Gestion de l'historique")

confirmation = st.checkbox(
    "Je confirme vouloir supprimer toutes les conversations enregistrées."
)

if st.button(
    "Supprimer définitivement",
    disabled=not confirmation
):
    supprimer_historique()
    st.session_state.historique = []

    st.success("Historique supprimé avec succès.")
    st.rerun()


# Pied de page
st.divider()
st.caption("IRGIB CONNECT AI | Assistant universitaire | IRGIB Africa")


