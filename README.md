# 📊 PFA - Automatisation des Ventes

## 📝 Description
Ce projet Python permet d'automatiser l'analyse des ventes d'une entreprise de e-commerce à partir d'un fichier CSV généré automatiquement par le programme.

## 🚀 Fonctionnalités
- ✅ Génération automatique du fichier `ventes.csv`
- ✅ Lecture du fichier `ventes.csv`
- ✅ Calcul du chiffre d'affaires brut
- ✅ Application des remises
- ✅ Calcul du CA net
- ✅ Calcul de la TVA
- ✅ Calcul du CA total
- ✅ Identification du produit le plus rentable
- ✅ Export des résultats dans `resultats_final.csv`
- ✅ Visualisation graphique avec Matplotlib

## ⚙️ Prérequis
- 🐍 Python 3 installé
- 💻 VS Code recommandé

## 🛠️ Installation
### 1️⃣ Créer un environnement virtuel
python -m venv .venv
### 2️⃣Activer l'environnement :
.\.venv\Scripts\activate
### 3️⃣Installer les dépendances :
pip install -r requirements.txt

## ▶️ Utilisation
### 1️⃣ Lancer le programme :
python main.py

### 2️⃣ Entrer le nombre de lignes à générer lorsque le programme le demande

### 3️⃣ Le programme génère automatiquement le fichier ventes.csv, effectue les calculs, puis crée le fichier resultats_final.csv

## 📂 Structure du projet
- main.py : script principal 
- ventes.csv : fichier de ventes généré automatiquement 
- resultats_final.csv : résultats générés 
- requirements.txt : dépendances 
- README.md : documentation*

## 📌 Exemple de résultat
Le programme génère un fichier ventes.csv, calcule le chiffre d'affaires brut, le CA net, la TVA et le CA total, puis affiche le produit le plus rentable et crée un fichier CSV contenant les résultats.

## 👨‍💻 Auteur
 Sayadi Leila / Balti Chahd / Akermi Amine (Grp 7)