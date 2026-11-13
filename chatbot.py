import re
import unicodedata
import logging
from modele_ml import detecter_intention_ml
from multilingue import detecter_langue, traduire_question

# Configuration de la journalisation
logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
    force=True
)

def normaliser(texte):
    # 1. Transformer en minuscules
    texte = texte.lower()

    # 2. Supprimer les espaces au début et à la fin
    texte = texte.strip()

    # 3. Décomposer les caractères accentués
    texte = unicodedata.normalize('NFD', texte)

    # 4. Supprimer les accents
    texte = ''.join(
        c for c in texte
        if unicodedata.category(c) != 'Mn'
    )

    # 5. Remplacer la ponctuation par des espaces
    texte = re.sub(r"[^a-z0-9' ]", ' ', texte)

    # 6. Supprimer les espaces multiples
    return re.sub(r'\s+', ' ', texte)


BASE = {
    "salutation": {
        "mots": ["bonjour", "salut", "bonsoir", "hello", "salutation", "salutations"],
        "reponse": "Bonjour ! Bienvenue sur l'assistant universitaire d'IRGIB Africa."
    },

    "horaires": {
        "mots": [
    "horaire",
    "horaires",
    "emploi",
    "temps",
    "heure",
    "heures",
    "planning",
    "9h",
    "8h",
    
],
        "reponse": "Je peux vous aider à consulter votre emploi du temps. Quelle est votre classe ?"
    },

    "inscription": {
        "mots": ["inscription", "inscrire", "m'inscrire", "inscris", "dossier", "documents", "admission", "admissions", "conditions"],
        "reponse": "Je peux vous renseigner sur les conditions et les documents d'inscription."
    },

    "bibliotheque": {
        "mots": ["bibliotheque", "livre", "livres", "documentation", "document"],
        "reponse": "Je peux vous renseigner sur la bibliothèque et les documents disponibles."
    },

    "salles": {
        "mots": ["salle", "classe", "local", "informatique"],
        "reponse": "Je peux vous aider à trouver votre salle de cours."
    },

    "examens": {
    "mots": [
        "examen",
        "examens",
        "exam",
        "exam1",
        "exams",
        "calendrier",
        "epreuves",
        "resultats"
    ],
    "reponse": "Je peux vous renseigner sur le calendrier des examens."
},
    
    "inconnu": {
        "mots": [],
        "reponse": "Je n'ai pas compris votre demande. Pouvez-vous reformuler ou contacter le service administratif ?"
    }
}
REPONSES_ANGLAIS = {
    "salutation": "Hello! Welcome to IRGIB CONNECT AI. How can I help you?",

    "horaires": "I can help you find information about your class schedule. Which class are you in?",

    "inscription": "I can provide information about admission requirements and registration documents.",

    "bibliotheque": "I can provide information about the library and available documents.",

    "salles": "I can help you find information about your classroom.",

    "examens": "I can provide information about the examination schedule.",

    "remerciement": "You're welcome! I'm happy to help you.",

    "inconnu": "I did not understand your question. Could you please rephrase it?"
}
contexte = {
    "prenom": None,
    "classe": None,
    "derniere_intention": None,
    "attente": None
}
def detecter_intention(message):
    texte = normaliser(message)

    if "comment allez vous" in texte or "comment ca va" in texte:
        return "salutation"

    mots = set(texte.split())
    meilleure = "inconnu"
    score_max = 0

    for nom, infos in BASE.items():
        # Priorité à l'intention salles
        if "salle" in mots or "salles" in mots:
            return "salles"
        score = len(mots & set(infos["mots"]))

        if score > score_max:
            meilleure = nom
            score_max = score

    return meilleure
def repondre(message):
    texte = normaliser(message)

        # Orientation vers un humain
    mots_humain = ["humain", "responsable", "administratif", "agent"]

    if any(mot in texte.split() for mot in mots_humain):
        return "Je vous invite à contacter le service administratif d'IRGIB Africa pour obtenir une assistance humaine."
    
            # Vérifier si le chatbot attend le nom de la classe
    if contexte["attente"] == "classe":

        if "mobile" in texte or "telephone" in texte:
            contexte["derniere_intention"] = "horaires"
            return "Oui ! Vous pourrez consulter votre emploi du temps sur téléphone. Pour connaître votre planning précis, indiquez votre classe."

        intention_message = detecter_intention(message)

        if intention_message == "inconnu":
            contexte["classe"] = message.strip()
            contexte["attente"] = None
            return f"Merci ! Je vais rechercher l'emploi du temps de {contexte['classe']}."

        else:
            contexte["attente"] = None
    
    
    # Mémoriser le prénom de l'étudiant
    if "je m'appelle" in texte:
        contexte["prenom"] = texte.split("je m'appelle")[-1].strip().capitalize()
        prenom = contexte["prenom"]
        return f"Enchanté {prenom} !"
    
        # Gérer une relance sur l'emploi du temps
    if contexte["derniere_intention"] == "horaires":
        if "mobile" in texte or "telephone" in texte:
            return "Vous parlez toujours de votre emploi du temps. Vous souhaitez le consulter sur téléphone."

    # Détecter l'intention
    langue = detecter_langue(message)

    message_modele = traduire_question(message) if langue == "anglais" else message

    intention, confiance = detecter_intention_ml(message_modele, seuil=0.32)
    logging.info(
        "intention=%s confiance=%.2f",
        intention,
        confiance
)
    if langue == "anglais":
        return REPONSES_ANGLAIS.get(intention, REPONSES_ANGLAIS["inconnu"])
    
    if intention == "remerciement":
        return "Avec plaisir ! Je reste disponible si vous avez d'autres questions."

    # Mémoriser la dernière intention
    contexte["derniere_intention"] = intention

    if intention == "salutation" and contexte["prenom"]:
        return f"Bonjour {contexte['prenom']} ! Comment puis-je vous aider ?"

    if intention == "horaires":
        contexte["attente"] = "classe"
        return "Pour quelle classe souhaitez-vous consulter les horaires ?"

    # Réponse par défaut
    if intention == "inconnu":
        logging.warning("Question non comprise par le chatbot")
        return BASE["inconnu"]["reponse"]

    # Retourner la réponse correspondante
    return BASE[intention]["reponse"]
if __name__ == "__main__":

    print("===================================")
    print("   ASSISTANT UNIVERSITAIRE IRGIB")
    print("===================================")
    print("Bonjour ! Comment puis-je vous aider ?")
    print("Tapez 'quitter' pour terminer la conversation.")

    while True:
        message = input("\nVous : ")

        if message.lower().strip() == "quitter":
            print("Assistant : Au revoir ! À bientôt.")
            break

        reponse = repondre(message)

        print("Assistant :", reponse)