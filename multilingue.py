# Dictionnaire multilingue IRGIB CONNECT AI

EXPRESSIONS = {
    "anglais": {
        "hello": "bonjour",
        "hi": "bonjour",
        "good morning": "bonjour",
        "good afternoon": "bonjour",
        "thank you": "merci",
        "thanks": "merci",

        "what are the opening hours": "horaires",
        "what time does the university open": "horaires",
        "how can i register": "comment faire une inscription",
        "how do i enroll": "comment faire une inscription",
        "what are the admission requirements": "quelles sont les conditions d'inscription",
        "what documents do i need to enroll": "quels documents faut-il pour l'inscription",

        "where is the library": "où se trouve la bibliothèque",
        "where can i find the library": "où se trouve la bibliothèque",
        "where is the classroom": "où se trouve la salle de cours",
        "where are the exams": "quand ont lieu les examens"
    }
}

def detecter_langue(message):
    message = message.lower().strip()

    for expression in EXPRESSIONS["anglais"]:
        if expression in message:
            return "anglais"

    return "francais"


def traduire_question(message):
    message = message.lower().strip()

    for anglais, francais in EXPRESSIONS["anglais"].items():
        if anglais in message:
            return francais

    return message