
import streamlit as st

def mnlm_page():
    # Affichage du logo
    st.image("assets/R_logo.png", width=200)

    # Titre et présentation du projet
    st.title("🍴 Package R - Multinomial Logistic Regression tailored for Mixed datasets")
    st.write("Projet réalisé dans le cadre du cours de **Programmation R** du Master 2 - SISE.")

    # Descriptif du projet
    st.header("📌 Description du projet")
    st.write(
        "**mnlmixte** est un package R innovant conçu pour effectuer des régressions logistiques multinomiales adaptées aux ensembles de données mixtes, c'est-à-dire composés à la fois de variables catégorielles et numériques. Ce package permet de réaliser des tâches de classification sur des ensembles de données variés, tout en optimisant la vitesse d'exécution grâce à son support de **traitement parallèle**."
        
        "\n\nL'objectif principal de **mnlmixte** est de simplifier l'analyse de données complexes en permettant aux utilisateurs de mener des régressions logistiques multinomiales sur des ensembles de données hétérogènes, tout en automatisant certaines étapes cruciales telles que la sélection des variables et l'évaluation des performances."
        
        "\n\nLes principales fonctionnalités du package sont :\n"
        "- **Régression logistique multinomiale** : Effectuer des tâches de classification sur des ensembles de données mixtes (catégorielles et numériques).\n"
        "- **Sélection de variables** : Identifier automatiquement les variables les plus importantes à l'aide de tests statistiques (ex : Chi-deux).\n"
        "- **Traitement parallèle** : Exploiter les cœurs multiples pour entraîner le modèle de manière plus efficace sur de grands ensembles de données.\n"
        "- **Exportation du modèle** : Exporter les modèles entraînés au format **PMML** pour faciliter le partage et le déploiement.\n"
        "- **Outils de visualisation** : Afficher l'importance des variables, les courbes de perte et les courbes ROC-AUC pour une meilleure interprétation des résultats.\n"
        "- **Métriques d'évaluation** : Calculer la précision, le rappel, le score F1, la précision globale (accuracy) et l'AUC sur les ensembles de test."
        
        "\n\nEn résumé, **mnlmixte** est un outil puissant et flexible qui permet aux analystes et aux chercheurs d’effectuer des régressions logistiques multinomiales sur des ensembles de données mixtes, tout en optimisant la performance du calcul grâce au traitement parallèle."
    )