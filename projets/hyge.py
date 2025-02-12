import streamlit as st

def hyge_page():
    # Affichage du logo
    st.image("assets/hyge_logo.png", width=200)

    # Titre et présentation du projet
    st.title("🌟 Hygé - Le Partenaire Santé au Travail")
    st.write("Projet entrepreneurial développé de 2021 à 2023, **Hygé** révolutionne la gestion de la qualité de vie au travail.")

    # Descriptif du projet
    st.header("📌 Description du projet")
    st.write(
        "Le bien-être au travail est devenu une priorité après le COVID, **Hygé** se positionne comme la solution ultime pour diagnostiquer, traiter et prédire les **Troubles Musculo-Squelettiques (TMS)**. Cette application web, développée avec **Ksaar**, permet aux collaborateurs de répondre à des questionnaires sur leur hygiène de vie, leur stress au travail, et bien plus encore. Les dirigeants, quant à eux, bénéficient de dashboards intuitifs pour piloter efficacement la qualité de vie au travail."

        "\n\nGrâce à des techniques avancées de **Machine Learning**, Hygé identifie les risques de développement de TMS chez les collaborateurs, offrant ainsi des insights précieux pour améliorer leur bien-être."
        "\n\nCe projet, a été développé avec des outils **NoCode** pour rendre les données facilement accessibles et compréhensibles à travers des visualisations interactives. Les données utilisées proviennent de questionnaires détaillés et de sources fiables, garantissant des analyses complètes et détaillées."

        "\n\nL'impact de cette application est double :\n"
        "- **Amélioration continue du bien-être** : Les collaborateurs bénéficient de recommandations personnalisées pour améliorer leur hygiène de vie et réduire les risques de TMS.\n"
        "- **Prise de décision éclairée** : Les dirigeants peuvent orienter leurs stratégies de gestion du bien-être au travail avec des données fiables et précises."
    )

    # Ton rôle dans le projet
    st.header("👨‍💻 Mon rôle dans le projet")
    st.write(
        "- **Réalisation du business plan** (pré-incubation à l'EM Lyon) 📈\n"
        "- **Lien entre les objectifs business et les besoins techniques** du Data Scientist 🔗\n"
        "- **Mise en place du data management** pour garantir la qualité et la fiabilité des données 📊\n"
        "- **Supervision du développement de la web app**, de la conception à la mise en production 🛠️"
    )

    # Fonctionnalités principales
    st.header("⚙️ Fonctionnalités principales")
    st.markdown("""
    - **📝 Questionnaires interactifs** : Collecte d'informations sur l'hygiène de vie et le stress au travail.
    - **🔍 Analyse des données** : Utilisation de techniques de Machine Learning pour identifier les risques de TMS.
    - **📊 Visualisation des données** : Dashboards intuitifs et interactifs via Ksaar.
    """)

    # Ajout d'un footer
    st.markdown("---")
    st.write("📌 **Projet entrepreneurial** | 2021-2023")