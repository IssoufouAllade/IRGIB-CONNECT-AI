# 🎓 IRGIB CONNECT AI

### Assistant conversationnel intelligent pour IRGIB Africa

## 📌 Présentation du projet

IRGIB CONNECT AI est un assistant conversationnel intelligent conçu pour accompagner les étudiants d'IRGIB Africa dans leurs démarches et leurs recherches d'informations universitaires.

Il permet aux étudiants d'obtenir des réponses concernant les horaires, les inscriptions, la bibliothèque, les salles de cours et les examens.

## 🎯 Objectifs

- Faciliter l'accès aux informations universitaires.
- Améliorer l'expérience des étudiants.
- Automatiser les réponses aux questions fréquentes.
- Orienter les étudiants vers le service administratif lorsque nécessaire.

## ✨ Fonctionnalités

- Détection automatique des intentions.
- Compréhension des questions en langage naturel.
- Classification des intentions avec Machine Learning.
- Gestion du contexte conversationnel.
- Mémorisation de certaines informations de conversation.
- Réponses de secours lorsque la question n'est pas comprise.
- Interface web interactive.
- API REST avec Flask.
- Journalisation des intentions et des niveaux de confiance.

## 🛠️ Technologies utilisées

- Python
- Streamlit
- Flask
- Scikit-learn
- TF-IDF
- Logistic Regression
- Git et GitHub

## 📂 Structure du projet

```text
IRGIB-CONNECT-AI/
│
├── api.py
├── app.py
├── chatbot.py
├── evaluation.py
├── modele_ml.py
├── .gitignore
└── README.md
```

## 🚀 Installation

Cloner le projet :

```bash
git clone https://github.com/IssoufouAllade/IRGIB-CONNECT-AI.git
```

Entrer dans le dossier :

```bash
cd IRGIB-CONNECT-AI
```

Installer les dépendances :

```bash
pip install streamlit flask scikit-learn
```

## ▶️ Lancement de l'application

### Interface web Streamlit

```bash
streamlit run app.py
```

### API REST Flask

```bash
flask --app api run
```

L'API sera accessible localement à l'adresse :

`http://127.0.0.1:5000`

## 👥 Équipe du projet

- Issoufou Allade
- Chabi Rayan
- Effiboley Mael

## 🎓 Contexte académique

Projet réalisé dans le cadre des travaux pratiques de la filière TIC.

**Établissement : IRGIB Africa**

---

*IRGIB CONNECT AI — L'information universitaire à portée de conversation.*
