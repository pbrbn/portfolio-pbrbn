import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer

#Projets
from projets.hyge import hyge_page
from projets.tripadvisor import tripadvisor_page
from projets.smartrescue import smartrescue_page
from projets.package_mnlm import mnlm_page


# --------- CONFIGURATION DE LA PAGE -----------
st.set_page_config(
    page_title="Portfolio Pierre BOURBON",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Masquer le menu de navigation auto-généré par Streamlit
hide_menu = """
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)


def main():
    # --------- MENU LATÉRAL -----------
    st.sidebar.title("📁 Menu de navigation")

    if st.sidebar.button("🚀 Accueil"):
        st.session_state["page"] = "🚀 Accueil"

    if st.sidebar.button("💪 Projet Hygé - Data Management"):
        st.session_state["page"] = "💪 Projet Hygé - Data Management"

    if st.sidebar.button("🍴 Projet TripAdvisor - NLP"):
        st.session_state["page"] = "🍴 Projet TripAdvisor - NLP"

    if st.sidebar.button("🚑 Projet SmartRescue - GenAI / RAG"):
        st.session_state["page"] = "🚑 Projet SmartRescue - GenAI / RAG"  

    if st.sidebar.button("📊 Projet Package R - MNLM"):
        st.session_state["page"] = "📊 Projet Package R - MNLM"   

    #Page par défaut
    if "page" not in st.session_state:
        st.session_state["page"] = "🚀 Accueil"

    # --------- PAGE ACCUEIL -----------
    if st.session_state["page"] == "🚀 Accueil":
        st.title("👋 Bienvenue sur mon Portfolio")
        st.write("Je m'appelle Pierre BOURBON et je suis Data Scientist. Ostéopathe de formation, j’ai découvert la Data Science au travers du projet Hygé (que vous pourrez retrouver dans mes projets). \n\n")
        st.write("J'ai décidé en 2023 de me spécialiser en Data Science. Pour se faire, je me suis formé dans un premier temps en auto didacte, puis à travers un premier bootcamp chez Jedha. Enfin, en 2024 j'ai intégré le Master 2 - Statistiques et Informatique pour la Science des Données (SISE) à l'université Lumière Lyon 2 afin de terminer ma formation.")
        st.write("Fort de mes expériences passées, en libéral et en entrepreneuriat, j’ai construis mon parcours en mettant au premier plan ma curiosité et ma persévérance. Mon profil est atypique, mêlant chefferie de projet, santé et Data Science.\n\n")


        st.header("📄 Mon CV")
        pdf_path = "assets/CV_Pierre BOURBON.pdf"
        with open(pdf_path, "rb") as f:
            pdf_file = f.read()
            pdf_viewer(pdf_file)
        
        st.header("📩 Me Contacter")
        st.write("📧 Email : contact@monportfolio.com")
        st.write("🔗 [LinkedIn](https://fr.linkedin.com/in/pierre-bourbon-7b6b7012a)")
        st.write("📂 [GitHub](https://github.com/pbrbn)")

    # --------- PROJETS (Appel des fichiers) -----------
    elif st.session_state["page"] == "💪 Projet Hygé - Data Management":
        hyge_page()

    elif st.session_state["page"] == "🍴 Projet TripAdvisor - NLP":
        tripadvisor_page()

    elif st.session_state["page"] == "🚑 Projet SmartRescue - GenAI / RAG":
        smartrescue_page()

    elif st.session_state["page"] == "📊 Projet Package R - MNLM":
        mnlm_page()

    # --------- PIED DE PAGE -----------
    st.sidebar.markdown("---")
    st.sidebar.write("© 2025 - Portfolio Data Pierre Bourbon")

if __name__ == "__main__":
    main()