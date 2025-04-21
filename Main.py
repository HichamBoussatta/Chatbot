import streamlit as st
import openai
import os

# Charger la clé API depuis les secrets
api_key = st.secrets["gemini_api_key"]

# Configurer OpenAI ou Gemini API avec la clé
openai.api_key = api_key

# Fonction pour obtenir une réponse du modèle Gemini
def get_response_from_gemini(user_input):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Remplacer par le modèle exact de Gemini si disponible
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Erreur dans la communication avec Gemini : {e}")
        return "Désolé, je n'ai pas pu traiter votre demande."

# Interface Streamlit
st.title("Chatbot Gemini")

# Demander à l'utilisateur de saisir sa clé API s'il ne l'a pas fait
if not api_key:
    st.warning("Veuillez configurer votre API Gemini dans le fichier secrets.toml.")

# Zone pour entrer un message utilisateur
user_input = st.text_input("Entrez votre message ici:")

if user_input:
    # Obtenez la réponse du modèle Gemini
    response = get_response_from_gemini(user_input)
    st.write("Réponse du Chatbot:")
    st.write(response)

# Option pour réinitialiser la session
if st.button("Réinitialiser"):
    st.experimental_rerun()
