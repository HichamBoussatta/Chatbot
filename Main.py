import streamlit as st
import openai
import os

# Charger la clé API depuis les secrets
api_key = st.secrets.get("gemini_api_key", None)

# Configurer OpenAI ou Gemini API avec la clé
if api_key:
    openai.api_key = api_key
else:
    st.warning("Veuillez configurer votre API Gemini dans les secrets de l'application Streamlit.")

# Fonction pour obtenir une réponse du modèle
def get_response_from_gemini(user_input):
    try:
        # Remplacer par l'API spécifique de Gemini si disponible
        response = openai.Completion.create(
            model="text-davinci-003",  # Utiliser ici le modèle Gemini si disponible
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Erreur dans la communication avec l'API : {e}")
        return "Désolé, je n'ai pas pu traiter votre demande."

# Interface Streamlit
st.title("Chatbot Gemini")

# Zone pour entrer un message utilisateur
user_input = st.text_input("Entrez votre message ici:")

if user_input:
    if api_key:  # Assurez-vous que l'API est correctement configurée
        # Obtenez la réponse du modèle
        response = get_response_from_gemini(user_input)
        st.write("Réponse du Chatbot:")
        st.write(response)
    else:
        st.warning("API non configurée, veuillez entrer votre clé API dans les secrets.")

# Option pour réinitialiser la session
if st.button("Réinitialiser"):
    st.experimental_rerun()
