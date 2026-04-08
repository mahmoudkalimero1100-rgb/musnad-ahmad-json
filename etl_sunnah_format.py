import json
import os
import re

# 1. Configuration des chemins
DOSSIER_SOURCE = 'musnadahmad_complet_chapitres.json'
DOSSIER_CIBLE = 'data/formatted/'

# Création du dossier cible s'il n'existe pas
os.makedirs(DOSSIER_CIBLE, exist_ok=True)

def extraire_numero_hadith(texte):
    """Extrait le numéro du hadith depuis la chaîne 'Musnad Ahmad - Hadith X'"""
    match = re.search(r'\d+', texte)
    return int(match.group()) if match else None

def transformer_donnees():
    print("Chargement du gros fichier JSON en mémoire...")
    with open(DOSSIER_SOURCE, 'r', encoding='utf-8') as f:
        donnees_brutes = json.load(f)

    # Dictionnaire pour regrouper les hadiths par chapitre (livre)
    livres = {}

    print(f"{len(donnees_brutes)} hadiths trouvés. Début du formatage...")

    for item in donnees_brutes:
        chapitre_id = item.get("numeroChapitre")
        
        # Formatage selon les standards Sunnah.com
        hadith_formate = {
            "collection": "ahmad",
            "bookNumber": str(chapitre_id),
            "chapterTitleArabic": item.get("chapitreArabe", "").strip(),
            "chapterTitleFrench": item.get("chapitreFrancais", "").strip(),
            "hadithNumber": str(extraire_numero_hadith(item.get("sourceFrancais", ""))),
            "arabicText": item.get("arabe", "").strip(),
            "frenchText": item.get("francais", "").strip() if item.get("francais") != "Traduction indisponible." else "",
            "reference": {
                "book": str(chapitre_id),
                "hadith": str(extraire_numero_hadith(item.get("sourceFrancais", "")))
            }
        }

        # Si le chapitre n'existe pas encore dans notre dictionnaire, on le crée
        if chapitre_id not in livres:
            livres[chapitre_id] = []
            
        livres[chapitre_id].append(hadith_formate)

    # Sauvegarde des données découpées par livre
    print("Découpage et sauvegarde des fichiers...")
    for chapitre_id, liste_hadiths in livres.items():
        nom_fichier = f"{DOSSIER_CIBLE}book_{chapitre_id}.json"
        
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            # On sauvegarde avec une indentation propre pour faciliter la relecture (Code Review)
            json.dump(liste_hadiths, f, ensure_ascii=False, indent=4)
            
    print(f"Succès ! Les données ont été formatées et divisées en {len(livres)} fichiers dans le dossier {DOSSIER_CIBLE}")

if __name__ == "__main__":
    transformer_donnees()