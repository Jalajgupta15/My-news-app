import streamlit as st
import requests

# Language options supported by Newsdata API
languages = {
    "Tamil": "ta",
    "Kannada": "kn",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Hindi": "hi",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Telugu": "te",
    "Malayalam": "ml",
    "Urdu": "ur"
}

# Apply custom CSS for the background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://t3.ftcdn.net/jpg/02/18/89/20/360_F_218892058_wzVOgz5ZMgWUojZPgJPCpuTkX1h1juLV.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("My News App")

# Description below the title
st.write("An app that provides news updates in your local language.")
st.write("Stay informed with the latest news headlines in your preferred languages from across India.")
st.write("Select from a range of Indian languages, and explore top stories tailored to your region.")

# Multi-select dropdown for language selection
selected_languages = st.multiselect("Select Languages", list(languages.keys()))

# Function to fetch news articles for each selected language
def fetch_news(language_code):
    api_key = "pub_58294d7dd9146c79712185714243c955c82c7"
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&language={language_code}&country=in"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        st.error(f"Failed to fetch news for language code {language_code}")
        return []

# Display news articles for each selected language
for lang in selected_languages:
    st.subheader(f"Top News in {lang}")
    articles = fetch_news(languages[lang])
    if articles:
        for article in articles:
            st.write(f"**{article['title']}**")
            st.write(f"{article['description']}")
            st.write(f"[Read more]({article['link']})")
            st.write("---")
    else:
        st.write("No news articles available.")

# To run the app, use `streamlit run app.py` in your terminal
