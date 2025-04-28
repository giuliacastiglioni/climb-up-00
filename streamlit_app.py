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
        options=["Home", "Galleria", "Video", "Specifiche","Questionario", "Contatti"],
        icons=["house", "camera", "film", "gear","clipboard-check", "envelope"],
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
    - **Funzionamento senza alimentazione elettrica** 
    - **Fotocellule di sicurezza**  
    - **Appoggi fissi**
    - **Inclinazione parete:** -37°/+37°
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

            contacts = []
            if os.path.exists('contatti.json'):
                if os.path.getsize('contatti.json') > 0:
                    with open('contatti.json', 'r', encoding='utf-8') as f:
                        contacts = json.load(f)

            # Aggiungiamo il nuovo contatto
            contacts.append(new_contact)

            # Salviamo il file aggiornato
            with open('contatti.json', 'w', encoding='utf-8') as f:
                json.dump(contacts, f, ensure_ascii=False, indent=4)

            st.success("✅ Messaggio inviato con successo! Ti contatteremo a breve.")

    st.markdown(""" 
    ---
    📧 Email:  INSERIRE NOSTRA 
    📱 Telefono: +39 INSERIRE NOSTRO
    """)
    st.markdown('</div>', unsafe_allow_html=True)


    # --- QUESTIONARIO ---
elif selected == "Questionario":
    st.markdown('<div class="section" style="background-color: #fffacd;">', unsafe_allow_html=True)  # colore giallo chiaro
    st.title("📝 Questionario Conoscitivo")

    st.write("Compila questo breve questionario per aiutarci a capire meglio le tue esigenze!")

    with st.form(key='questionnaire_form'):
        risposta1 = st.text_area("1) Che macchinari utilizzate già?")
        risposta2 = st.text_area("2) Che tipologie di pazienti avete?")
        risposta3 = st.text_area("3) Che esercizi hai bisogno di fare?")
        risposta4 = st.text_area("4) Che problematiche principali affrontate di solito?")
        risposta5 = st.text_area("5) Avete macchinari simili a quello che offriamo? Quali sono le loro limitazioni?")
        risposta6 = st.text_area("6) Quali caratteristiche ritenete più importanti in un macchinario di riabilitazione?")
        risposta7 = st.text_area("7) Qual è il vostro volume di pazienti?")
        risposta8 = st.text_area("8) Quali tipi di trattamenti riabilitativi sono più richiesti?")
        risposta9 = st.text_area("9) Qual è il budget disponibile per l'acquisto di nuovi macchinari?")
        risposta10 = st.text_area("10) Come valutate l'efficacia dei vostri attuali dispositivi riabilitativi?")
        risposta11 = st.text_area("11) Avete bisogno di funzionalità specifiche da implementare?")
        risposta12 = st.text_area("12) Climb-Up può essere un macchinario utile?")
        risposta13 = st.text_area("13) Avete bisogno di formazione per l'uso del nuovo macchinario?")
        risposta14 = st.text_area("14) Come pensate che il nuovo macchinario possa migliorare l'esperienza del paziente clinici?")

        submit_questionnaire = st.form_submit_button(label='Invia Questionario')

        if submit_questionnaire:
            import json
            import os
            from datetime import datetime

            # Prepariamo i dati
            new_response = {
                "data_invio": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "risposte": {
                    "domanda_1": risposta1,
                    "domanda_2": risposta2,
                    "domanda_3": risposta3,
                    "domanda_4": risposta4,
                    "domanda_5": risposta5,
                    "domanda_6": risposta6,
                    "domanda_7": risposta7,
                    "domanda_8": risposta8,
                    "domanda_9": risposta9,
                    "domanda_10": risposta10,
                    "domanda_11": risposta11,
                    "domanda_12": risposta12,
                    "domanda_13": risposta13,
                    "domanda_14": risposta14,
                }
            }

            questionari = []
            if os.path.exists('questionari.json'):
                if os.path.getsize('questionari.json') > 0:
                    with open('questionari.json', 'r', encoding='utf-8') as f:
                        questionari = json.load(f)

            # Aggiungiamo la nuova risposta
            questionari.append(new_response)

            # Salviamo
            with open('questionari.json', 'w', encoding='utf-8') as f:
                json.dump(questionari, f, ensure_ascii=False, indent=4)

            st.success("✅ Questionario inviato con successo! Grazie per il tuo tempo.")

    st.markdown('</div>', unsafe_allow_html=True)
