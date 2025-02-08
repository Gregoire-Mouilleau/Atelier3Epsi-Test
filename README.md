# 📌 Projet Pokedex - Test de Charge avec Locust

## 🚀 Description du Projet
Ce projet est une **application web Pokedex** qui affiche les **150 premiers Pokémon** en récupérant les données depuis **PokeAPI**. L'objectif de cet atelier est d'effectuer des **tests de charge** avec **Locust** afin d'analyser les performances du site et d'identifier les points d'amélioration.

## 📂 Structure du Projet
- **index.html** → Page principale du Pokedex
- **style.css** → Feuille de style pour le design
- **script.js** → Script qui récupère et affiche les Pokémon
- **test/load/** → Dossier contenant les tests de charge avec Locust

## ⚙️ Installation et Exécution
### 🔹 Étape 1 : Cloner le projet
```bash
git clone https://github.com/Gregoire-Mouilleau/Atelier3Epsi-Test.git
```

### 🔹 Étape 2 : Lancer un serveur local
```bash
python -m http.server
```
📌 Ouvrir **http://localhost:8000** dans le navigateur.

### 🔹 Étape 3 : Installation de Locust
```bash
cd test/load
python -m venv env
source env/bin/activate
pip install locust
pip freeze > requirements.txt
```

### 🔹 Étape 4 : Exécution des tests de charge
```bash
locust
```
📌 Ouvrir **http://localhost:8089** et lancer les tests.

## 🔍 Problèmes Connus et Solutions
### 1️⃣ **Temps de chargement élevé pour les 150 Pokémon**
- **Cause** : Le script `script.js` effectue **150 requêtes** vers **PokeAPI**, ralentissant l'affichage.
- ✅ **Solution** : Charger les Pokémon progressivement (par groupes de 10 ou 20) et mettre en cache les données.

### 2️⃣ **Dépendance à l’API externe**
- **Cause** : Si **PokeAPI** est lent ou hors ligne, l’application devient inutilisable.
- ✅ **Solution** : Sauvegarder les données Pokémon en cache (`localStorage`) pour éviter les requêtes répétées.

### 3️⃣ **Problèmes de chargement des fichiers statiques**
- **Cause** : `style.css` et `script.js` peuvent ralentir le rendu.
- ✅ **Solution** : Activer le cache navigateur ou héberger ces fichiers sur un **CDN**.

## 📊 Résultats des Tests
- **La page d’accueil se charge rapidement (médian ~9ms).**
- **Certains Pokémon (ID 100-150) prennent plus de temps à charger (~80ms).**
- **Les requêtes vers PokeAPI peuvent atteindre 360ms sous forte charge.**

📌 Ces résultats montrent qu’une **optimisation côté client** (caching, lazy loading) est nécessaire.

## 📌 Historisation
Les tests et optimisations ont été **versionnés avec Git** pour suivre l’évolution des performances.
```bash
git add .
git commit -m "Ajout des tests de charge avec Locust"
git push origin main
```
