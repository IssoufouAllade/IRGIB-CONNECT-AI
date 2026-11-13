from flask import Flask, request, jsonify
from chatbot import repondre

app = Flask(__name__)

# Limite maximale des requêtes
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024

@app.route("/", methods=["GET"])
def accueil():
    return jsonify({
        "projet": "IRGIB CONNECT AI",
        "message": "API du chatbot universitaire opérationnelle"
    })


@app.route("/chat", methods=["POST"])
def chat():

    donnees = request.get_json(silent=True)

    if not isinstance(donnees, dict):
        return jsonify({
            "erreur": "Format JSON invalide."
        }), 400

    message = donnees.get("message", "")

    if not isinstance(message, str):
        return jsonify({
            "erreur": "Le message doit être du texte."
        }), 400

    message = message.strip()

    if not message:
        return jsonify({
            "erreur": "Veuillez saisir une question."
        }), 400

    if len(message) > 500:
        return jsonify({
            "erreur": "Votre message dépasse la limite de 500 caractères."
        }), 400

    try:
        reponse = repondre(message)

        return jsonify({
            "question": message,
            "reponse": reponse
        }), 200

    except Exception:
        app.logger.exception("Erreur lors du traitement du message")

        return jsonify({
            "erreur": "Une erreur est survenue. Veuillez réessayer."
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)