import streamlit as st
from streamlit_option_menu import option_menu
import json
import os

# Configurazione pagina
st.set_page_config(page_title="Parete da Arrampicata", layout="wide")

# --- CSS PERSONALIZZATO ---
st.markdown("""
<style>
/* Sfondo a gradiente */
.stApp {
    background: linear-gradient(to bottom, #ffffff, #ffa500, #ffd700);
    font-family: 'Helvetica Neue', sans-serif;
}
/* Stile titoli */
h1, h2, h3 {
    color: #222222;
}
/* Stile sezioni */
.section {
    padding: 50px;
    border-radius: 20px;
    margin-bottom: 50px;
    background-color: #ffffffcc;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
}
/* Stile immagine home */
img {
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- MENU DI NAVIGAZIONE ---
with st.sidebar:
    selected = option_menu(
        menu_title="Navigazione",
        options=["Home", "Galleria", "Video", "Specifiche", "Contatti"],
        icons=["house", "camera", "film", "gear", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# --- HOME ---
if selected == "Home":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.title("🏔️ Climb Up - La Parete d'Arrampicata su Misura")
    st.image("media/copertina.PNG", use_container_width=True)

    st.subheader("Poco spazio, infiniti metri")
    st.write("""
        Siamo un team che lavora insieme da anni con la passione per la montagna 
        e l’arrampicata.  
        **Climb-Up** è una parete mobile d’arrampicata che adegua la propria 
        velocità di discesa in funzione del peso e delle abilità dell’utente.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- GALLERIA ---
elif selected == "Galleria":
    st.markdown('<div class="section" style="background-color: #ffa500cc;">', unsafe_allow_html=True)
    st.title("📸 Galleria Fotografica")

    cols = st.columns(3)
    immagini = [
        "media/foto1.PNG",
        "media/foto2.PNG",
        "media/foto3.PNG",
        "media/foto4.PNG",
        "media/foto5.PNG",
        "media/foto6.PNG",
    ]

    for i, img in enumerate(immagini):
        with cols[i % 3]:
            st.image(img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- VIDEO ---
elif selected == "Video":
    st.markdown('<div class="section" style="background-color: #ffd700cc;">', unsafe_allow_html=True)
    st.title("🎥 Video Dimostrativo")
    st.write("Guarda Climb Up in azione:")

    video_file = open('media/video_presentazione.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SPECIFICHE ---
elif selected == "Specifiche":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.title("🔧 Specifiche Tecniche")
    
    st.subheader("Dimensioni e Struttura")
    st.write("""
    - **Altezza standard:** 3 metri  
    - **Larghezza:** 2,5 metri modulare  
    - **Materiale:** Legno marino + Acciaio zincato  
    - **Resistenza:** Certificata fino a 150kg per modulo
    """)

    st.subheader("Installazione")
    st.write("""
    Climb Up può essere installata sia in ambienti interni che esterni, grazie ai materiali trattati per resistere agli agenti atmosferici.
    Il montaggio avviene in sole 2 ore senza bisogno di interventi murari permanenti.
    """)

    st.subheader("Personalizzazioni disponibili")
    st.write("""
    - Varie tipologie di prese
    - Inclinazione regolabile
    - Branding personalizzato
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CONTATTI ---
elif selected == "Contatti":
    st.markdown('<div class="section" style="background-color: #ffa500cc;">', unsafe_allow_html=True)
    st.title("📞 Contattaci")

    st.write("Siamo a tua disposizione per qualsiasi informazione o preventivo.")
    
    with st.form(key='contact_form'):
        name = st.text_input("Nome")
        email = st.text_input("Email")
        message = st.text_area("Messaggio")
        submit_button = st.form_submit_button(label='Invia')

        if submit_button:
            # Creiamo un dizionario con i dati
            new_contact = {
                "nome": name,
                "email": email,
                "messaggio": message
            }

            # Controlliamo se esiste già il file JSON
            if os.path.exists('contatti.json'):
                with open('contatti.json', 'r', encoding='utf-8') as f:
                    contacts = json.load(f)
            else:
                contacts = []

            # Aggiungiamo il nuovo contatto
            contacts.append(new_contact)

            # Salviamo il file aggiornato
            with open('contatti.json', 'w', encoding='utf-8') as f:
                json.dump(contacts, f, ensure_ascii=False, indent=4)

            st.success("✅ Messaggio inviato con successo! Ti contatteremo a breve.")

    st.markdown(""" 
    ---
    📧 Email:   
    📱 Telefono: +39 123 456 789
    """)
    st.markdown('</div>', unsafe_allow_html=True)