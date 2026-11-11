import re
import unicodedata

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Normalisation des messages
def normaliser(texte):
    texte = texte.lower().strip()
    texte = unicodedata.normalize("NFD", texte)

    texte = ''.join(
        c for c in texte
        if unicodedata.category(c) != 'Mn'
    )

    texte = re.sub(r"[^a-z0-9' ]", ' ', texte)

    return re.sub(r'\s+', ' ', texte)

exemples = {
    "salutation": [
        "bonjour",
        "salut",
        "bonsoir",
        "hello",
        "salut comment allez vous",
        "bonjour comment allez vous",
        "coucou",
        "bonsoir a tous",
        "salut comment ca va",
        "heureux de vous rencontrer",
        "je viens vous saluer",
        "salut tout le monde",
        "je vous souhaite une bonne journee",
        "bonsoir comment allez vous aujourd hui",
        "coucou assistant j ai une question",
        "bonjour je suis nouveau ici",
        "salut assistant",
        "bonsoir je voudrais un renseignement",
        "hello je suis etudiant",
        "salut je viens demander une information",
        "bonjour je suis nouveau a l'universite",
    ],
    "horaires": [
        "je veux connaitre les horaires de mes cours",
        "quel est mon emploi du temps",
        "a quelle heure commencent les cours",
        "je cherche mon planning",
        "on a quel cours a 8h ou 9h",
        "je voudrais consulter mon emploi du temps",
        "quels cours avons nous demain",
        "quand commencent les cours",
        "je veux connaitre les heures de cours",
        "mon planning de la semaine",
        "je dois venir a quelle heure",
        "quel est le programme des cours aujourd hui",
        "quand commence ma journee de cours",
        "je voudrais voir les horaires de demain",
        "est ce que les cours ont deja commence",
        "je voudrais connaitre les cours de la journee",
        "quels sont les enseignements prevus demain",
        "je cherche les heures de mes differentes matieres",
        "quand est ce que notre premiere seance commence",
        "je veux voir le programme de la prochaine semaine",
        "je veux connaitre les heures de mes cours",
        "quel est mon emploi du temps aujourd hui",
        "quels cours sont prevus demain",
        "je voudrais connaitre les heures de debut des cours",
        "ou puis je consulter mon planning",
        "je voudrais savoir a quelle heure les cours debutent",
        "quel est l'horaire de nos prochaines seances",
        "les cours commencent a quelle heure le matin",
        "je voudrais connaitre mon emploi du temps",
        "je veux connaitre mon emploi de temps",
        "je voudrais connaitre mes horaires",
        "je veux savoir quand j'ai cours",
        "quel est mon planning de cours",
        "je cherche mon emploi du temps",
        "je voudrais connaitre mon empoi de temp",
        "à quelle heure dois-je être en classe",
        "à quelle heure commence ma première séance",
        "quand débute le premier cours",
        "je voudrais connaître l'heure de mes cours",
        "à quel moment commence la journée de cours",
    ], 
    "inscription": [
        "je veux m'inscrire a IRGIB Africa",
        "quels sont les documents pour inscription",
        "comment faire pour m'inscrire",
        "quelles sont les conditions d'admission",
        "je veux deposer mon dossier",
        "comment obtenir le formulaire d'inscription",
        "je souhaite rejoindre IRGIB Africa",
        "quelles pieces faut il fournir",
        "ou deposer mon dossier d'admission",
        "les inscriptions sont elles ouvertes",
        "combien coutent les frais de scolarite",
        "je veux connaitre les frais universitaires",
        "quel est le prix de la formation",
        "je souhaite devenir etudiant dans votre ecole",
        "comment faire une demande d admission",
        "quelles sont les etapes pour rejoindre votre etablissement",
        "je voudrais deposer ma candidature",
        "comment obtenir les informations sur les inscriptions",
        "je veux faire mon inscription",
        "quelles sont les conditions pour etre admis",
        "comment obtenir un dossier d inscription",
        "je souhaite devenir etudiant a IRGIB Africa",
        "quels documents dois je fournir pour entrer a l ecole",
        "je voudrais déposer mon dossier pour entrer a l'ecole",
        "quelles formalites dois je remplir pour etre etudiant",
        "comment obtenir les informations sur les admissions",
        "je souhaite faire une demande d'admission",
        "quels documents sont necessaires pour rejoindre l'ecole",
        "je voudrais connaitre les etapes pour m'inscrire",
        "comment faire pour integrer IRGIB Africa",
        "je veux connaitre la procedure pour devenir etudiant",
        "comment transmettre mon dossier de candidature",
       "je voudrais connaitre les modalites pour candidater",
       "quelles sont les modalites pour presenter une candidature",
       "je souhaite connaitre les procedures pour rejoindre l'ecole",
       "comment puis-je faire parvenir mes documents",
       "quelles demarches effectuer pour etre admis",
       "je voudrais deposer une demande pour integrer l'universite",
       "quand ouvrent les inscriptions pour les nouveaux etudiants",
       "quelle est la periode de depot des dossiers",
       "a partir de quand peut on faire une demande d'admission",
       "quand commencent les procedures pour rejoindre l'etablissement",
        
    ],
    "bibliotheque": [
        "ou se trouve la bibliotheque",
        "je cherche des livres",
        "avez vous de la documentation",
        "je veux consulter des livres",
        "ou trouver les documents pour les etudiants",
        "comment emprunter un livre",
        "je voudrais acceder a la bibliotheque",
        "ou puis je trouver des ouvrages",
        "est ce que la bibliotheque est ouverte",
        "je cherche un livre pour mes recherches",
        "je souhaite consulter des ouvrages",
        "puis je lire des livres a la bibliotheque",
        "je voudrais faire une recherche a la bibliotheque",
        "est ce possible de consulter un livre sur place",
        "je voudrais acceder aux livres disponibles",
        "comment trouver un document pour mes etudes",
        "je souhaite consulter les ouvrages de l ecole",
        "est ce que je peux emprunter des documents",
        "ou puis je lire tranquillement mes livres",
        "je voudrais emprunter un ouvrage",
        "comment acceder aux ressources de la bibliotheque",
        "je cherche des livres pour mes etudes",
        "est ce que je peux consulter les livres",
        "ou trouver des documents pour mes recherches",
        "je voudrais consulter des livres a la bibliotheque",
        "comment acceder aux ressources documentaires",
        "est ce que la bibliotheque propose des ouvrages",
        "je cherche des livres pour mes recherches",
        "quels services sont disponibles au centre documentaire",
        "comment effectuer une recherche dans la bibliotheque",
        "est ce que les etudiants peuvent lire dans la bibliotheque",
        "je souhaite trouver des documents pour mes travaux",
        "quels sont les possibilites de lecture sur place",

    ],
    "salles": [
        "ou se trouve ma salle de cours",
        "dans quelle salle avons nous cours",
        "je cherche la salle informatique",
        "comment trouver ma salle de classe",
        "ou se trouve mon local",
        "comment trouver la salle ou nous avons cours",
        "je ne connais pas ma salle de classe",
        "quelle salle est reservee aux etudiants",
        "comment acceder aux salles de cours",
        "je cherche l'amphitheatre",
        "ou se trouve notre amphitheatre",
        "je ne trouve pas le batiment de ma classe",
        "je cherche ou se trouve mon amphitheatre",
        "comment trouver le local de mon prochain cours",
        "pouvez vous m indiquer le lieu de notre seance",
        "ou se trouve ma salle de cours",
        "je cherche le local ou nous avons cours",
        "comment trouver mon amphitheatre",
        "ou se situe le laboratoire informatique",
        "je voudrais connaitre le numero de ma salle",
        "je voudrais savoir dans quel batiment se trouve ma classe",
        "comment acceder a notre salle de cours",
        "je cherche la salle ou se tient notre cours",
        "pouvez vous me renseigner sur les locaux de l'ecole",
        "ou se trouve la salle ou nous avons cours aujourd'hui",
        "comment retrouver la salle attribuee a ma classe",
        "je voudrais connaitre l'emplacement de notre salle",
        "comment trouver la salle de mon prochain cours",
        "je cherche le local ou se deroule mon cours",
        "ou se trouve la salle informatique",
        "dans quel batiment se passent les cours",
        "comment connaitre le numero de ma salle",
        "ou pouvons nous nous reunir pour le cours",
        "comment localiser la classe ou se deroule ma seance",
        "je voudrais savoir ou retrouver mes camarades pour le cours",
        "quel est le lieu de notre prochain enseignement",

    ]    ,
    "examens": [
        "quand auront lieu les examens",
        "je veux connaitre le calendrier des examens",
        "quelle est la date de mon examen",
        "quelles sont les dates des epreuves",
        "comment consulter mes resultats",
        "comment connaitre la date des examens",
        "quand se derouleront les epreuves",
        "ou trouver le programme des examens",
        "je voudrais consulter mes notes",
        "comment savoir si je suis admis",
        "a quelle periode se deroulent les examens",
        "je voudrais savoir quand auront lieu les compositions",
        "quelle est la periode des evaluations",
        "comment connaitre le calendrier des epreuves",
        "je cherche les dates de mes examens",
        "quand les resultats des examens seront ils disponibles",
        "quand commencent les examens",
        "je voudrais connaitre le calendrier des epreuves",
        "comment consulter les dates des examens",
        "a quelle date aura lieu mon prochain examen",
        "ou puis je voir le programme des evaluations",
        "je voudrais connaitre le calendrier des compositions",
        "quand auront lieu les examens de fin de semestre",
        "comment consulter les resultats de mes examens",
        "je cherche les dates des prochaines evaluations",
        "quand est prevue la prochaine session d'examens",
        "comment connaitre les dates des examens",
        "quand commencent les evaluations",
        "je voudrais consulter le programme des epreuves",
        "a quelle date se terminent les compositions",
        "ou trouver les informations sur les examens",
        "comment acceder aux notes obtenues aux examens",
        "ou consulter les notes publiees par l'administration",
        "je voudrais connaitre mes resultats academiques",
        "comment savoir si les resultats des compositions sont disponibles",

    ],
    "inconnu": [
        "quel temps fera t il demain",
        "comment preparer du riz",
        "qui va gagner le prochain match",
        "comment reparer une voiture",
        "quelle est la capitale du japon",
        "donne moi une recette de gateau",
        "combien coute un telephone",
        "raconte moi une blague",
        "comment jouer au football",
        "quelle est la meteo aujourd hui"

    ],
    "remerciement": [
        "merci",
        "merci beaucoup",
        "je vous remercie",
        "c'est gentil merci",
        "je te remercie",
        "merci pour votre aide",
        "super merci",
        "d'accord merci",
        "je vous remercie beaucoup",
        "merci pour les informations",
        "je vous remercie",
        "je vous remercie sincèrement",
        "un grand merci",
        "merci infiniment",
        "je tiens à vous remercier",
        "merci pour votre réponse",
        "c'est très gentil",
        "je vous suis reconnaissant",
        "merci pour ces informations",
        "vraiment merci",
        "je vous exprime toute ma gratitude",
        "je tiens à vous exprimer mes remerciements",
        "je vous adresse mes remerciements",
        "je vous suis profondément reconnaissant",
        "toute ma reconnaissance pour votre aide",
        "je tiens a vous dire merci",
        "je vous remercie pour votre disponibilite",
        "je suis tres content de votre assistance",
        "merci pour le temps que vous m'avez consacre",
        "j'apprecie beaucoup votre soutien",
    ],

}
# Préparation des données d'entraînement

textes = []
etiquettes = []

for intention, phrases in exemples.items():
    for phrase in phrases:
        textes.append(normaliser(phrase))
        etiquettes.append(intention)


# Transformation des phrases en données numériques

vectoriseur = TfidfVectorizer(ngram_range=(1, 2))

X = vectoriseur.fit_transform(textes)

# Création et entraînement du modèle

modele = LogisticRegression(max_iter=1000)

modele.fit(X, etiquettes)

# Détection de l'intention avec le modèle ML

def detecter_intention_ml(message, seuil=0.45):

    X_message = vectoriseur.transform([normaliser(message)])

    probabilites = modele.predict_proba(X_message)[0]

    indice = probabilites.argmax()

    confiance = float(probabilites[indice])

    if confiance < seuil:
        return "inconnu", confiance

    return modele.classes_[indice], confiance

if __name__ == "__main__":

    tests = [
        ("Salut, je suis nouveau ici", "salutation"),
        ("A quelle heure dois-je venir demain", "horaires"),
        ("Je souhaite faire mon admission", "inscription"),
        ("La bibliothèque possède-t-elle des manuels", "bibliotheque"),
        ("Dans quel bâtiment se trouve notre classe", "salles"),
        ("A quelle période passent les étudiants", "examens"),
        ("Je voudrais connaître les frais de scolarité", "inscription"),
        ("Peut-on consulter les livres sur place", "bibliotheque"),
        ("Je suis perdu, je cherche mon amphithéâtre", "salles"),
        ("Quand seront publiées les notes", "examens")
    ]

    for seuil in [0.25]:

        reussites = 0

        print(f"\n========== SEUIL {seuil} ==========")

        for message, attendu in tests:

            obtenu, confiance = detecter_intention_ml(message, seuil)

            if obtenu == attendu:
                reussites += 1

            print(f"{message}")
            print(f"Attendu : {attendu} | Obtenu : {obtenu}")
            print(f"Confiance : {confiance:.2%}")
            print("------------------------------")

        taux = reussites / len(tests) * 100

        print(f"TOTAL : {reussites}/10")
        print(f"TAUX DE RÉUSSITE : {taux:.0f}%")