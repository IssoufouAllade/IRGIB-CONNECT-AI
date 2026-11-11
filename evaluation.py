from modele_ml import detecter_intention_ml

tests = [
    # Salutations
    ("Coucou, je viens demander un renseignement", "salutation"),
    ("Salut, j'ai besoin d'aide", "salutation"),
    ("Bonsoir à toute l'équipe", "salutation"),
    ("Hello, je suis étudiant ici", "salutation"),
    ("Bonjour, je voudrais poser une question", "salutation"),

    # Horaires
    ("À quel moment commencent nos activités demain ?", "horaires"),
    ("Je voudrais connaître mes heures de cours", "horaires"),
    ("Quels enseignements sont prévus cette semaine ?", "horaires"),
    ("À quelle heure dois-je être en classe ?", "horaires"),
    ("Je veux consulter mon programme hebdomadaire", "horaires"),

    # Inscriptions
    ("Je souhaite intégrer votre établissement", "inscription"),
    ("Comment puis-je soumettre ma candidature ?", "inscription"),
    ("Quels papiers faut-il préparer pour l'admission ?", "inscription"),
    ("Je voudrais connaître la procédure d'inscription", "inscription"),
    ("Quand peut-on commencer les démarches d'admission ?", "inscription"),

    # Bibliothèque
    ("Je cherche un ouvrage pour étudier", "bibliotheque"),
    ("Peut-on accéder aux livres de l'école ?", "bibliotheque"),
    ("Je voudrais consulter des documents", "bibliotheque"),
    ("Où puis-je faire une recherche documentaire ?", "bibliotheque"),
    ("Est-ce qu'on peut lire sur place ?", "bibliotheque"),

    # Salles
    ("Je ne connais pas le local de mon cours", "salles"),
    ("Où devons-nous nous réunir pour le cours ?", "salles"),
    ("Je cherche le bâtiment des étudiants", "salles"),
    ("Dans quel amphithéâtre se déroule la séance ?", "salles"),
    ("Je voudrais localiser notre classe", "salles"),

    # Examens
    ("À quelle date auront lieu les épreuves finales ?", "examens"),
    ("Je voudrais connaître le calendrier des évaluations", "examens"),
    ("Quand seront organisées les compositions ?", "examens"),
    ("Où peut-on consulter les résultats scolaires ?", "examens"),
    ("Comment connaître les dates des contrôles ?", "examens"),
]

reussites = 0
resultats_intents = {}
erreurs = []

print("\n===== ÉVALUATION DU CHATBOT =====\n")

for phrase, attendu in tests:
    obtenu, confiance = detecter_intention_ml(
        phrase,
        seuil=0.25
    )

    correct = obtenu == attendu
    if not correct:
        erreurs.append((phrase, attendu, obtenu, confiance))


    if attendu not in resultats_intents:
        resultats_intents[attendu] = {
            "total": 0,
            "reussites": 0
        }

    resultats_intents[attendu]["total"] += 1

    if correct:
        reussites += 1
        resultats_intents[attendu]["reussites"] += 1

    print(f"Phrase : {phrase}")
    print(f"Attendu : {attendu}")
    print(f"Obtenu : {obtenu}")
    print(f"Confiance : {confiance:.2%}")
    print(f"Résultat : {'SUCCÈS' if correct else 'ÉCHEC'}")
    print("-" * 40)

taux = (reussites / len(tests)) * 100

print("\n===== BILAN FINAL =====")
print(f"Nombre de tests : {len(tests)}")
print(f"Réussites : {reussites}")
print(f"Échecs : {len(tests) - reussites}")
print(f"Taux de compréhension : {taux:.2f}%")
print("\n===== BILAN PAR INTENTION =====")

for intention, resultats in resultats_intents.items():
    total = resultats["total"]
    bonnes_reponses = resultats["reussites"]
    taux_intention = (bonnes_reponses / total) * 100

    print(f"\nIntention : {intention}")
    print(f"Tests : {total}")
    print(f"Réussites : {bonnes_reponses}")
    print(f"Taux : {taux_intention:.2f}%")

print("\n===== ANALYSE DES ERREURS =====")

for phrase, attendu, obtenu, confiance in erreurs:
    print(f"\nPhrase : {phrase}")
    print(f"Attendu : {attendu}")
    print(f"Obtenu : {obtenu}")
    print(f"Confiance : {confiance:.2%}")

print("\n===== TESTS HORS SUJET =====")

tests_hors_sujet = [
    "Quel temps fera-t-il demain ?",
    "Comment préparer du riz ?",
    "Qui va gagner le prochain match ?",
    "Comment réparer une voiture ?",
    "Quelle est la capitale du Japon ?"
]
for phrase in tests_hors_sujet:
    obtenu, confiance = detecter_intention_ml(
        phrase,
        seuil=0.25
    )

    print(f"\nPhrase : {phrase}")
    print(f"Intention détectée : {obtenu}")
    print(f"Confiance : {confiance:.2%}")

    if obtenu == "inconnu":
        print("Résultat : SUCCÈS")
    else:
        print("Résultat : ÉCHEC")

# ==========================================
# TESTS INDEPENDANTS
# ==========================================

tests_independants = [
    ("salutation", "Bonsoir, je viens demander un renseignement."),
    ("salutation", "Salut, j'ai une petite question."),

    ("horaires", "À quelle heure débute ma première séance ?"),
    ("horaires", "Quand dois-je venir en cours cette semaine ?"),

    ("inscription", "Quels papiers faut-il fournir pour intégrer l'école ?"),
    ("inscription", "Comment déposer mon dossier de candidature ?"),

    ("bibliotheque", "Est-ce que je peux consulter des ouvrages sur place ?"),
    ("bibliotheque", "Je cherche un document dans le centre de lecture."),

    ("salles", "Dans quel local se déroule le cours de TIC ?"),
    ("salles", "Je cherche la salle où nous avons cours."),

    ("examens", "Où puis-je consulter le calendrier des épreuves ?"),
    ("examens", "À quelle période auront lieu les évaluations ?"),

    ("remerciement", "Je vous suis très reconnaissant."),
    ("remerciement", "Recevez mes sincères remerciements.")
]

reussites_independantes = 0

print("\n========== TESTS INDEPENDANTS ==========\n")

for intention_attendue, phrase in tests_independants:

    intention_predite, confiance = detecter_intention_ml(
        phrase, seuil=0.32
    )

    resultat = "REUSSI" if intention_predite == intention_attendue else "ECHEC"

    if resultat == "REUSSI":
        reussites_independantes += 1

    print(f"Phrase : {phrase}")
    print(f"Attendu : {intention_attendue}")
    print(f"Détecté : {intention_predite}")
    print(f"Confiance : {confiance:.2%}")
    print(f"Résultat : {resultat}")
    print("-" * 45)

total = len(tests_independants)

print("\n========== BILAN INDEPENDANT ==========")
print(f"Réussites : {reussites_independantes}/{total}")
print(f"Taux de réussite : {reussites_independantes / total * 100:.2f}%")