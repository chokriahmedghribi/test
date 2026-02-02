import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader



# 1. Configuration de la page
st.set_page_config(layout="wide", page_title="Mon Projet Arabe")

# 2. Injection de CSS corrigé
st.markdown("""
    <style>
        /* Importation des polices */
        @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cairo:wght@400;700&display=swap');

        /* Global RTL et suppression Header */
        [data-testid="stHeader"] {
            display: none;
        }

        html, body, [data-testid="stAppViewContainer"] {
            direction: rtl;
            text-align: right;
            background-color: #F0F2F6; /* Couleur grise de fond */
        }

        /* Conteneur principal */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
        }

        [data-testid="stMainViewContainer"] {
            background-color: #F0F2F6;
            margin-right: 21rem;
            margin-left: 0;
            font-family: 'Amiri', serif;
        }

        /* Sidebar à droite, fond blanc */
        [data-testid="stSidebar"] {
            position: fixed;
            right: 0 !important;
            left: auto !important;
            background-color: #FFFFFF !important;
            font-family: 'Cairo', sans-serif;
            border-left: 1px solid #ddd;
        }

        /* Correction padding sidebar */
        [data-testid="stSidebarUserContent"] {
            padding-top: 1rem !important;
            text-align: right;
        }
            /* --- CONFIGURATION MOBILE (Écrans réduits) --- */
        @media (max-width: 991px) {
            [data-testid="stSidebar"] {
                right: auto !important; /* Streamlit gère l'ouverture auto */
            }
            [data-testid="stMainViewContainer"] {
                margin-right: 0;
            }
            .custom-title {
                font-size: 24px !important; /* Titre plus petit sur mobile */
                padding: 10px !important;
            }
        }

        /* Application des polices aux éléments */
        [data-testid="stSidebar"] * {
            font-family: 'Cairo', sans-serif !important;
        }
        
        [data-testid="stMainViewContainer"] h1, h2, h3, p, span {
            font-family: 'Amiri', serif;
        }

        /* Style spécifique pour les boutons de la sidebar */
        [data-testid="stSidebar"] button {
            text-align: right !important;
            width: 100%;
            border: 1px solid #f0f2f6;
            margin-bottom: 5px;
        }

        /* LE TITRE ENCADRÉ ROUGE */
        .custom-title {
            background-color: #8B0000 !important;
            color: #FFFFFF !important;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-family: 'Amiri', serif !important;
            font-size: 35px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 30px;
            border: 3px solid #CC0000;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Fonction pour le titre
def display_title(text):
    st.markdown(f'<div class="custom-title">{text}</div>', unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    try:
        st.image("logo.png", width=150)
    except:
        st.markdown("### 🏷️ شعار المشروع")
    
    st.markdown("---")
    
    if st.button("الصفحة الرئيسية"):
        st.session_state.page = "home"
    if st.button("الإحصائيات"):
        st.session_state.page = "stats"
    if st.button("الإعدادات"):
        st.session_state.page = "settings"

# Initialisation de la navigation
if 'page' not in st.session_state:
    st.session_state.page = "home"

# 4. Contenu Principal
if st.session_state.page == "home":
    display_title("مرحباً بك في الصفحة الرئيسية")
    st.info("هذا النص يظهر بخط Amiri الرائع وتصميم متناسق.")
    
elif st.session_state.page == "stats":
    display_title("لوحة الإحصائيات")
    st.info("هنا تظهر البيانات والرسوم البيانية.")

elif st.session_state.page == "settings":
    display_title("إعدادات النظام")
    st.info("يمكنك تغيير الخيارات هنا.")