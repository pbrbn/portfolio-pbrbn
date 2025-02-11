import streamlit as st

def smartrescue_page():
    # Affichage du logo
    st.image("assets/smartrescue_logo.png", width=200)

    # Titre et présentation du projet
    st.title("🚑 Smart Rescue - Gen AI / RAG")
    st.write("Projet réalisé dans le cadre du cours de **Generative AI** du Master 2 - SISE.")

    # Descriptif du projet
    st.header("📌 Description du projet")
    st.write(
        "Dans des situations d'urgence, chaque seconde compte. **SmartRescue** est une application révolutionnaire conçue pour soutenir "
        "les opérateurs d'urgence grâce à l'intégration d'un **LLM (Large Language Model)** et d'un **RAG (Retrieval-Augmented Generation)**. "
        "Cette technologie de pointe permet de fournir une **assistance rapide et précise**, aidant les opérateurs à prendre des décisions éclairées "
        "en temps réel, et ce, à chaque appel d'urgence."
        
        "\n\nAvec **SmartRescue**, les opérateurs bénéficient d'un assistant intelligent qui analyse instantanément les informations pertinentes, "
        "fournit des suggestions basées sur des données réelles et aide à prioriser les actions à entreprendre. Le système utilise des **modèles de langage avancés** pour "
        "soutenir la prise de décision, offrant une réponse rapide et fiable dans des moments critiques."
        
        "\n\nLes avantages de cette technologie sont multiples :\n"
        "- **Assistance en temps réel** : Le LLM et le RAG permettent aux opérateurs d’avoir une réponse immédiate et pertinente.\n"
        "- **Amélioration de la prise de décision** : La technologie aide à analyser rapidement des informations complexes pour orienter les actions.\n"
        "- **Optimisation des ressources** : En accélérant les processus de décision, SmartRescue permet de mieux gérer les ressources humaines et matérielles lors des interventions.\n"
        
        "\n\nEn résumé, **SmartRescue** transforme l’approche des interventions d’urgence, en alliant l’intelligence humaine et l’intelligence artificielle pour sauver des vies plus rapidement et plus efficacement."
    )

    # Rôle
    st.header("👨‍💻 Mon rôle dans le projet")
    st.write(
        "- **Développement de la sécurité du RAG** 🔐\n"
        "- **Détection des documents pertinents dans ChromaDB** 🔎\n"
        "- **Analyse des comportements utilisateurs** 📊\n"
    )

    # Fonctionnalités principales
    st.header("⚙️ Fonctionnalités principales")
    st.markdown("""
    - **📞 Aide téléphonique** : Enregistrement des conversations et assistance en temps réel via LLM.
    - **📊 Dashboard** : Suivi des métriques du système RAG (**coût, latence, impact environnemental**).
    - **🔧 Admin** : 
        - Suivi des logs d'utilisation 📜  
        - Surveillance des appels API 🔄  
        - Génération de rapports de sécurité 🔍  
        - Configuration des clés API 🔑  
    """)

    # Lien GitHub
    st.header("👉 GitHub")
    st.markdown("""
    - [Lien vers le repository](https://github.com/maxenceLIOGIER/SmartRescue)
    """)

    # Ajout d'un footer
    st.markdown("---")
    st.write("📌 **Projet réalisé dans le cadre du Master 2 - SISE** | © 2024")