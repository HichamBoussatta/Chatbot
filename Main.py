import streamlit as st
import openai

# Interface Streamlit
st.title("Chatbot Gemini")

# Récupérer la clé API de Gemini, soit saisie par l'utilisateur, soit par défaut dans secrets.toml
api_key = st.text_input("Entrez votre clé API Gemini", type="password")

# Si la clé API n'est pas fournie par l'utilisateur, récupérer celle du fichier secrets.toml
if not api_key:
    api_key = st.secrets["gemini_api_key"]

# Si la clé API est valide
if api_key:
    # Configurer l'API d'OpenAI (ou Gemini si disponible)
    openai.api_key = api_key

    # Zone pour entrer un message utilisateur
    user_input = st.text_input("Entrez votre message ici:")

    if user_input:
        try:
            # Utilisation du modèle Gemini ou OpenAI
            response = openai.Completion.create(
                model="text-davinci-003",  # Remplacer par le modèle exact de Gemini si disponible
                prompt=user_input,
                max_tokens=150
            )
            st.write("Réponse du Chatbot:")
            st.write(response.choices[0].text.strip())
        except Exception as e:
            st.error(f"Erreur dans la communication avec l'API : {e}")
            st.write("Désolé, je n'ai pas pu traiter votre demande.")
    
    # Option pour réinitialiser la session
    if st.button("Réinitialiser"):
        st.rerun()

else:
    st.warning("Veuillez entrer votre clé API Gemini pour continuer.")
