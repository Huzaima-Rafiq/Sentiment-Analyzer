import streamlit as st
from textblob import TextBlob

# Page config
st.set_page_config(
    page_title="Simple Sentiment Analyzer",
    page_icon="💬",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
    <style>
    .stTextArea textarea {
        font-size: 16px;
        padding: 15px;
        border: 1px solid #ced4da;
        border-radius: 5px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 5px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("💬 Simple Sentiment Analyzer")
st.write("Enter your sentence and get an instant sentiment score using basic natural language processing.")

# User input
text = st.text_area("Type your sentence here:", height=150)

# Analyze button
if st.button("Analyze Sentiment"):
    if not text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Sentiment label
        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        # Display result
        st.success(f"**Sentiment:** {sentiment}")
        st.write(f"**Polarity Score:** {polarity:.2f}")
        st.write(f"**Subjectivity Score:** {subjectivity:.2f}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Built with 💡 TextBlob and Streamlit</p>", unsafe_allow_html=True)
