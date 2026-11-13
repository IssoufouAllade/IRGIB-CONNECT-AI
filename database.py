import sqlite3
from datetime import datetime

DB_NAME = "irgib_connect.db"


def creer_base():
    connexion = sqlite3.connect(DB_NAME)
    curseur = connexion.cursor()

    curseur.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            reponse TEXT NOT NULL,
            date_creation TEXT NOT NULL
        )
    """)

    connexion.commit()
    connexion.close()


def enregistrer_echange(question, reponse):
    connexion = sqlite3.connect(DB_NAME)
    curseur = connexion.cursor()

    curseur.execute("""
        INSERT INTO conversations
        (question, reponse, date_creation)
        VALUES (?, ?, ?)
    """, (
        question,
        reponse,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connexion.commit()
    connexion.close()


def recuperer_historique(limite=50):
    connexion = sqlite3.connect(DB_NAME)
    curseur = connexion.cursor()

    curseur.execute("""
        SELECT question, reponse, date_creation
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
    """, (limite,))

    resultats = curseur.fetchall()
    connexion.close()

    return resultats

def supprimer_historique():
    connexion = sqlite3.connect(DB_NAME)
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM conversations")

    connexion.commit()
    connexion.close()