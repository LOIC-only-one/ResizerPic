# README 📄

## Description 🖼️

Ce projet est un script Python permettant de traiter des images en supprimant leur arrière-plan et en effectuant un découpage autour des visages détectés. Il utilise les bibliothèques `rembg`, `Pillow`, et `OpenCV` pour effectuer ces opérations.

## Fonctionnalités ✨

- 🧹 Suppression de l'arrière-plan des images.
- 👤 Détection de visages dans les images.
- ✂️ Découpage des images autour des visages détectés avec une marge configurable.

## Prérequis 📋

- 🐍 Python 3.7 ou supérieur.
- 📦 Les bibliothèques suivantes doivent être installées :
    - `rembg`
    - `Pillow`
    - `opencv-python`
    - `numpy`

## Installation ⚙️

1. Clonez ce dépôt :
     ```bash
     git clone <URL_DU_DEPOT>
     cd <NOM_DU_DEPOT>
     ```

2. Installez les dépendances :
     ```bash
     pip install -r requirements.txt
     ```

3. 📥 Téléchargez le modèle U2Net et placez-le à l'emplacement spécifié dans le script (`MODEL_PATH`).

## Utilisation 🚀

1. Modifiez les chemins dans le script pour correspondre à vos fichiers :
     - `INPUT_FILE` : Chemin de l'image d'entrée.
     - `OUTPUT_DIR` : Répertoire de sortie.
     - `MODEL_PATH` : Chemin vers le modèle U2Net.

2. Exécutez le script :
     ```bash
     python script.py
     ```

3. 📂 Les résultats seront enregistrés dans le répertoire de sortie spécifié.

## Structure du Projet 🗂️

```
.
├── script.py          # Script principal
├── requirements.txt   # Liste des dépendances
└── README.md          # Documentation
```

## Journalisation 📝

Le script génère des logs pour suivre les étapes du traitement. Les messages incluent :
- ℹ️ Informations sur le traitement des images.
- ⚠️ Avertissements si aucun visage n'est détecté.
- ❌ Erreurs en cas de problème.

## Limitations ⚠️

- Le script ne traite qu'une seule image à la fois.
- La détection des visages peut échouer si l'image est de mauvaise qualité ou si les visages sont partiellement visibles.

## Contribuer 🤝

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour signaler des problèmes.

## Licence 📜

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.
