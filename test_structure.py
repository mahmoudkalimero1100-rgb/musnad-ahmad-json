import json

# Ouvre ton gros fichier en mode lecture avec l'encodage UTF-8 (indispensable pour l'arabe)
with open('musnadahmad_complet_chapitres.json', 'r', encoding='utf-8') as file:
    # Charge le JSON dans la mémoire (ça peut prendre 1 ou 2 secondes)
    data = json.load(file)
    
    # Affiche le tout premier élément de la liste, bien formaté
    print(json.dumps(data[0], indent=4, ensure_ascii=False))