# 🎓 IRGIB CONNECT AI

### Assistant conversationnel intelligent pour IRGIB Africa

## 📌 Présentation du projet

IRGIB CONNECT AI est un assistant conversationnel intelligent conçu pour accompagner les étudiants d'IRGIB Africa dans leurs démarches et leurs recherches d'informations universitaires.

Il permet aux étudiants d'obtenir des réponses concernant les horaires, les inscriptions, la bibliothèque, les salles de cours et les examens.

## 🎯 Objectifs

- Faciliter l'accès aux informations universitaires.
- Améliorer l'expérience des étudiants.
- Automatiser les réponses aux questions fréquentes.
- Orienter les étudiants vers le service administratif lorsque cela est nécessaire.

## ✨ Fonctionnalités

- Détection des intentions des utilisateurs.
- Reconnaissance des questions en langage naturel.
- Classification automatique des intentions avec Machine Learning.
- Réponses automatiques aux questions fréquentes.
- Gestion du contexte de conversation.
- Mémorisation du prénom de l'utilisateur.
- Gestion des questions non reconnues.
- Orientation vers un interlocuteur humain.
- Enregistrement des conversations dans une base de données SQLite.
- Gestion et suppression de l'historique des conversations.
- API REST avec Flask.
- Évaluation des performances du modèle.

## 🧠 Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Langage de programmation |
| Scikit-learn | Classification des intentions |
| TF-IDF | Transformation des textes en vecteurs |
| Logistic Regression | Modèle de classification |
| Streamlit | Interface conversationnelle |
| Flask | API REST du chatbot |
| SQLite | Stockage des conversations |
| Git | Gestion des versions |
| GitHub | Hébergement du code source |

## 🏗️ Architecture du projet

```text
IRGIB_CHATBOT/
│
├── chatbot.py
├── modele_ml.py
├── evaluation.py
├── app.py
├── api.py
├── database.py
├── multilingual.py
├── requirements.txt
├── README.md
└── .gitignore
```

La base de données `irgib_connect.db` est créée localement par le programme.

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/IssoufouAllade/IRGIB-CONNECT-AI.git
```

### 2. Entrer dans le dossier

```bash
cd IRGIB-CONNECT-AI
```

### 3. Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

## ▶️ Lancement du projet

### Interface Streamlit

```bash
python -m streamlit run app.py
```

### API Flask

```bash
python api.py
```

L'API fonctionne localement sur le port 5000.

## 🧪 Évaluation

Le projet comprend un module d'évaluation permettant de tester la capacité du chatbot à reconnaître les intentions des utilisateurs et à gérer les questions non reconnues.

Pour lancer les tests :

```bash
python evaluation.py
```

## 👥 Équipe du projet

- Issoufou Allade
- Chabi Rayan
- Effiboley Mael

## 📚 Cadre académique

Projet réalisé dans le cadre des travaux pratiques de la filière Technologies de l'Information et de la Communication (TIC) à IRGIB Africa.

## 📄 Licence

Projet académique — IRGIB CONNECT AI.