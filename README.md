# PFA - Automatisation des Ventes

## Description
Ce projet Python permet d'automatiser l'analyse des ventes d'une entreprise de e-commerce à partir d'un fichier CSV.

## Fonctionnalités
- Lecture du fichier ventes.csv
- Calcul du chiffre d'affaires brut
- Application des remises
- Calcul du CA net
- Calcul de la TVA
- Calcul du CA total
- Identification du produit le plus rentable
- Export des résultats dans resultats_final.csv
- Visualisation graphique avec Matplotlib

## Prérequis
- Python 3 installé
- VS Code recommandé

## Installation
1. Créer un environnement virtuel :
   python -m venv .venv

2. Activer l'environnement :
   .\.venv\Scripts\activate

3. Installer les dépendances :
   pip install -r requirements.txt

## Utilisation
1. Ajouter ou modifier le fichier ventes.csv
2. Lancer le programme :

   python main.py

## Structure du projet
- main.py : script principal
- ventes.csv : données d'entrée
- resultats_final.csv : résultats générés
- requirements.txt : dépendances
- README.md : documentation

## Exemple de résultat
Le programme affiche le chiffre d'affaires total et le produit le plus rentable, puis génère un fichier CSV contenant les résultats.

## Auteur
- Sayadi Leila / Balti Chahd / Akermi Amine (Grp 7)