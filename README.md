\# Musnad Ahmad - JSON Export



Ce dépôt a pour but de structurer et de formater les données du \*\*Musnad Ahmad\*\* (Édition Darussalam, + de 27 000 hadiths) afin de faciliter leur intégration dans des plateformes open source comme \[Sunnah.com](https://sunnah.com).



\## Contexte

Actuellement, la numérisation et la traduction du Musnad Ahmad sur Sunnah.com stagnent à environ 4%. L'objectif de ce projet est de fournir un dataset complet et pré-formaté pour accélérer ce travail via une approche d'ingénierie des données (ETL).



\## Source des données

\* \*\*Édition :\*\* Darussalam (Standard de numérotation)

\* \*\*Extraction :\*\* Les données brutes ont été générées à partir de Hadithhub.



\## Structure du dépôt

\* `/data/raw/` : Contient l'export JSON brut original.

\* `/data/formatted/` : (À venir) Contient les données nettoyées et divisées par livres/chapitres, mappées sur le schéma de données de Sunnah.com.

\* `/scripts/` : (À venir) Scripts de transformation et de parsing (JSON vers JSON standardisé).



\## Prochaines étapes

1\. Développer un script de transformation pour mapper les clés actuelles vers le schéma de Sunnah.com (`collectionID`, `bookID`, `hadithNumber`, `arabicText`, etc.).

2\. Découper le fichier brut massif en fichiers JSON plus petits, classés par "Livres" (Kutub).

3\. Soumettre des Pull Requests incrémentales à l'équipe de Sunnah.com.

