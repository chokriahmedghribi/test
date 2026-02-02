import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from pathlib import Path

# Configuration de la page (doit être la première commande Streamlit)
st.set_page_config(
    layout="wide", 
    page_title="Mon Projet Arabe",
    initial_sidebar_state="expanded"
)

# Chargement CSS externe
def load_css():
    css_file = Path(__file__).parent / "styles.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        # CSS inline comme fallback
        st.markdown("""
        <style>
            /* Importation des polices */
            @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cairo:wght@400;700&display=swap');
            
            /* Variables CSS */
            :root {
                --primary-red: #8B0000;
                --secondary-red: #CC0000;
                --background-gray: #F0F2F6;
                --sidebar-white: #FFFFFF;
                --border-color: #ddd;
            }
            
            /* Global RTL et suppression Header */
            [data-testid="stHeader"] { display: none; }
            
            html, body, [data-testid="stAppViewContainer"] {
                direction: rtl;
                text-align: right;
                background-color: var(--background-gray);
            }
            
            /* Conteneur principal */
            .block-container {
                padding-top: 0 !important;
                padding-bottom: 0 !important;
            }
            
            [data-testid="stMainViewContainer"] {
                background-color: var(--background-gray);
                margin-right: 21rem;
                margin-left: 0;
                font-family: 'Amiri', serif;
            }
            
            /* Sidebar à droite, fond blanc */
            [data-testid="stSidebar"] {
                position: fixed;
                right: 0 !important;
                left: auto !important;
                background-color: var(--sidebar-white) !important;
                font-family: 'Cairo', sans-serif;
                border-left: 1px solid var(--border-color);
                min-width: 250px;
                max-width: 350px;
            }
            
            /* Correction padding sidebar */
            [data-testid="stSidebarUserContent"] {
                padding-top: 1rem !important;
                text-align: right;
            }
            
            /* Boutons sidebar */
            [data-testid="stSidebar"] .stButton > button {
                text-align: right !important;
                width: 100%;
                border: 1px solid var(--background-gray);
                margin-bottom: 5px;
                transition: all 0.3s ease;
            }
            
            [data-testid="stSidebar"] .stButton > button:hover {
                background-color: var(--background-gray);
            }
            
            /* Application des polices */
            [data-testid="stSidebar"] * {
                font-family: 'Cairo', sans-serif !important;
            }
            
            [data-testid="stMainViewContainer"] h1, h2, h3, p, span {
                font-family: 'Amiri', serif;
            }
            
            /* Titre encadré */
            .custom-title {
                background-color: var(--primary-red) !important;
                color: #FFFFFF !important;
                padding: 1.2rem;
                border-radius: 15px;
                text-align: center;
                font-family: 'Amiri', serif !important;
                font-size: clamp(24px, 2.5vw, 35px);
                font-weight: bold;
                margin-top: 1.2rem;
                margin-bottom: 1.8rem;
                border: 3px solid var(--secondary-red);
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }
            
            /* Responsive */
            @media (max-width: 991px) {
                [data-testid="stSidebar"] {
                    right: auto !important;
                    min-width: auto;
                }
                [data-testid="stMainViewContainer"] {
                    margin-right: 0;
                }
            }
            
            @media (max-width: 768px) {
                .custom-title {
                    padding: 0.8rem !important;
                    font-size: 1.4rem !important;
                }
            }
        </style>
        """, unsafe_allow_html=True)

# Initialisation session state
def init_session_state():
    default_values = {
        'page': 'home',
        'authenticated': False,
        'username': None
    }
    
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value

# Composants réutilisables
def display_title(text):
    """Affiche un titre stylisé"""
    st.markdown(f'<div class="custom-title">{text}</div>', unsafe_allow_html=True)

def sidebar_navigation():
    """Gère la navigation dans la sidebar"""
    with st.sidebar:
        # Logo avec fallback
        try:
            st.image("logo.png", width=150, use_container_width=True)
        except:
            st.markdown("### 🏷️ شعار المشروع")
        
        st.divider()
        
        # Boutons de navigation
        pages = {
            "الصفحة الرئيسية": "home",
            "الإحصائيات": "stats",
            "الإعدادات": "settings"
        }
        
        for label, page_key in pages.items():
            if st.button(label, use_container_width=True, key=f"btn_{page_key}"):
                st.session_state.page = page_key
                st.rerun()

# Pages de l'application
def home_page():
    """Page d'accueil"""
    display_title("مرحباً بك في الصفحة الرئيسية")
    st.info("هذا النص يظهر بخط Amiri الرائع وتصميم متناسق.")
    # Ajouter ici le contenu spécifique à la page d'accueil

def stats_page():
    """Page des statistiques"""
    display_title("لوحة الإحصائيات")
    st.info("هنا تظهر البيانات والرسوم البيانية.")
    # Ajouter ici les composants de statistiques

def settings_page():
    """Page des paramètres"""
    display_title("إعدادات النظام")
    st.info("يمكنك تغيير الخيارات هنا.")
    # Ajouter ici les contrôles des paramètres

# Mapper les pages aux fonctions
PAGE_MAP = {
    "home": home_page,
    "stats": stats_page,
    "settings": settings_page
}

# Fonction principale
def main():
    # Charger CSS
    load_css()
    
    # Initialiser session state
    init_session_state()
    
    # Afficher navigation sidebar
    sidebar_navigation()
    
    # Afficher la page active
    current_page = st.session_state.page
    if current_page in PAGE_MAP:
        PAGE_MAP[current_page]()
    else:
        # Fallback à la page d'accueil
        st.session_state.page = "home"
        home_page()

# Point d'entrée
if __name__ == "__main__":
    main()