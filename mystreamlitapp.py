from mylibraryfile import categorizeBooks
import streamlit as st

try:
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    wordcloud_available = True
except ImportError:
    wordcloud_available = False

# Apply Custom CSS for Styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    .stAlert {
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Book Categorizer")
st.header("Automatically Categorize Books by Their Description")
st.write("✨ Enter a book description below, and this AI-powered app will classify it into a relevant category!")

# Text area for input
bookdescription = st.text_area("📖 Book Description:", 
             placeholder="Type or Paste the book description here...", 
             height=150)

# Categorization button
if st.button("📌 Categorize Book"):
    if len(bookdescription.strip()) == 0:
        st.error("⚠️ Please enter a valid book description!")
    else:
        category, related_topics = categorizeBooks(bookdescription)
        
        # Display results
        st.success(f"📌 **Book Category:** {category}")
        st.info(f"🔍 **Related Topics:** {', '.join(related_topics)}")

# Function to generate and display a word cloud
if wordcloud_available:
    def generate_wordcloud(text):
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10,5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)

    # Button to generate word cloud for entered description
    if st.button("🌥️ Generate Word Cloud for Description"):
        if len(bookdescription.strip()) == 0:
            st.error("⚠️ Please enter a valid book description!")
        else:
            generate_wordcloud(bookdescription)
else:
    st.warning("⚠️ WordCloud library is not installed. Please install it using `pip install wordcloud`.")

# Footer
st.markdown("---")
st.markdown("💡 *This app uses Machine Learning to categorize books based on their descriptions.*")
