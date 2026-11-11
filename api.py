from flask import Flask, request, jsonify
from chatbot import repondre

# Création de l'application Flask
app = Flask(__name__)

# Route d'accueil
@app.route("/", methods=["GET"])
def accueil():
    return jsonify({
        "projet": "IRGIB CONNECT AI",
        "message": "API du chatbot universitaire opérationnelle"
    })

# Route pour envoyer une question au chatbot
@app.route("/chat", methods=["POST"])
def chat():
    donnees = request.get_json(silent=True) or {}

    message = donnees.get("message", "").strip()

    if not message:
        return jsonify({
            "erreur": "Veuillez saisir une question."
        }), 400

    reponse = repondre(message)

    return jsonify({
        "question": message,
        "reponse": reponse
    })

# Lancement du serveur
if __name__ == "__main__":
    app.run(debug=True, port=5000)