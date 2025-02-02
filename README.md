📚 Book Categorization Streamlit App
Automatically categorize books based on their descriptions using Machine Learning and K-Means clustering.

🚀 Project Overview
This Streamlit application takes a book description as input and categorizes it into a relevant topic using a K-Means clustering model trained on IT-related books. It also provides related topics and generates a word cloud for visualization.

📂 Features
✅ Categorize books based on their descriptions.
✅ Displays related topics based on similarity.
✅ Generates a Word Cloud for visualizing book descriptions.
✅ Supports bulk categorization via CSV upload.
✅ Modern UI with Streamlit and CSS styling.

🔧 Installation
## **1️⃣ Clone this repository (if applicable)**
```bash
Copy
Edit
git clone https://github.com/kalopez0621/Categorizing_Books.git
cd your-repository
```
## **2️⃣ Create a Virtual Environment (Optional, Recommended)**
```bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # For Mac/Linux
.venv\Scripts\activate     # For Windows
```
## **3️⃣ Install Dependencies**
```bash
Copy
Edit
pip install -r requirements.txt
If you don’t have a requirements.txt, manually install dependencies:

bash
Copy
Edit
pip install streamlit wordcloud pandas numpy scikit-learn nltk joblib matplotlib
```
## **4️⃣ Download NLTK Stopwords**
```python
Copy
Edit
import nltk
nltk.download("stopwords")
nltk.download("punkt")
```
## **▶️ Running the App**
Start the Streamlit app with:

```bash
Copy
Edit
streamlit run mystreamlitapp.py
```
## 📌 How to Use
### 1️⃣ Enter a book description into the text box.
### 2️⃣ Click "Categorize Book" to see its category and related topics.
### 3️⃣ Click "Generate Word Cloud" to visualize key terms.
### 4️⃣ Upload a CSV file (optional) to categorize multiple books at once.

## 📸 Screenshots

### **Book Categorization**
![Book Categorization](https://raw.githubusercontent.com/kalopez0621/Categorizing_Books/images/0.01.png)

### **Word Cloud Generation**
![Word Cloud](https://raw.githubusercontent.com/kalopez0621/Categorizing_Books/images/0.002.png)


## 📜 Project Structure
```bash
Copy
Edit
📂 Project-Folder
│── 📄 mystreamlitapp.py        # Main Streamlit App
│── 📄 mylibraryfile.py         # Categorization Logic & Preprocessing
│── 📄 requirements.txt         # Dependencies (if applicable)
│── 📄 README.md                # Documentation
│── 📂 models                   # Saved models (TF-IDF & K-Means)
│── 📂 data                     # Dataset (if applicable)
```

## 📌 Future Enhancements
🔹 Deploy to Streamlit Cloud or Hugging Face Spaces.
🔹 Improve model accuracy with additional training data.
🔹 Enhance UI with more visuals and animations.

## 💡 Credits
Python, Streamlit, Scikit-Learn, NLTK, Matplotlib for ML & UI.
Inspired by IT books dataset.
## 📜 License
This project is open-source under the MIT License. Feel free to modify and improve it!

## 🎯 Ready to Deploy?
If you want to deploy this on Streamlit Cloud, simply:

Push your code to GitHub.
Go to Streamlit Cloud.
Connect your repository & deploy!
📬 Contact
📧 Email: kalopez0621@gmail.com
🔗 GitHub: 

