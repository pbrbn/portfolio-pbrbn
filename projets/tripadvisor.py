import streamlit as st

def tripadvisor_page():
    # Affichage du logo
    st.image("assets/tripadvisor_logo.png", width=200)

    # Titre et présentation du projet
    st.title("🍴 TripAdvisor - NLP")
    st.write("Projet réalisé dans le cadre du cours de **Natural Language Processing** du Master 2 - SISE.")

    # Descriptif du projet
    st.header("📌 Description du projet")
    st.write(
        "Dans un monde où l'expérience client est essentielle, **NLP-Projet-SISE** révolutionne la manière dont nous comprenons "
        "les retours des utilisateurs. Cette application de **traitement du langage naturel (NLP)** se spécialise dans l'extraction, "
        "l'analyse et la visualisation des données provenant des **avis utilisateurs** des restaurants sur TripAdvisor, offrant ainsi des "
        "insights précieux pour améliorer la qualité des services et l'engagement client."
        
        "\n\nGrâce à l'exploitation des techniques avancées de **NLP**, l'application permet d'extraire des informations pertinentes à partir de "
        "milliers d'avis en ligne, permettant ainsi aux restaurateurs d'identifier les tendances, les points forts et les axes d'amélioration "
        "en un clin d'œil. Les données collectées sont ensuite stockées dans une **base de données SQLite** pour une gestion optimale et une analyse "
        "rapide."
        
        "\n\nCe projet, développé en **Python**, utilise des bibliothèques puissantes telles que **spaCy**, **pandas**, et **Streamlit** pour rendre "
        "les données facilement accessibles et compréhensibles à travers des visualisations interactives. Les données utilisées proviennent du **scraping** "
        "du site **TripAdvisor**, ainsi que de l'**open data de l'INSEE**, garantissant des analyses complètes et détaillées."
        
        "\n\nL'impact de cette application est double :\n"
        "- **Amélioration continue des services** : Les restaurateurs peuvent facilement identifier les points d'amélioration à partir des retours des clients.\n"
        "- **Prise de décision éclairée** : L'analyse des avis permet de mieux orienter les stratégies de marketing et de service, avec des données fiables et précises."
    )
    

    # Ton rôle dans le projet
    st.header("👨‍💻 Mon rôle dans le projet")
    st.write(
        "- **Développement et maintenance du web scraping** 🧑‍💻\n"
        "- **Analyse des avis via Machine Learning** 🤖\n"
        "- **Prétraitement et nettoyage des données** 🧹"
    )

    # Fonctionnalités principales
    st.header("⚙️ Fonctionnalités principales")
    st.markdown("""
    - **📝 Scraping** : Extraction des informations des restaurants et des avis depuis TripAdvisor.
    - **🔍 Prétraitement des données** : Analyse textuelle avec **spaCy** et **NLTK**.
    - **💾 Stockage des données** : Gestion des données dans une **base SQLite**.
    - **📊 Visualisation des données** : Tableaux et graphiques interactifs via **Streamlit**.
    """)

    # Lien GitHub
    st.header("👉 GitHub")
    st.markdown("""
    - [Lien vers le repository](https://github.com/pbrbn/NLP-Projet-SISE/)
    """)

    # Ajout d'un footer
    st.markdown("---")
    st.write("📌 **Projet réalisé dans le cadre du Master 2 - SISE** | © 2024")