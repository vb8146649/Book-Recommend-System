# 📚 Book Recommendation System

This is a **Book Recommendation System** built with [Streamlit](https://streamlit.io/). The app suggests similar books based on your selected favorite using a precomputed similarity matrix and book metadata. Covers are fetched using the Open Library API.

👉 **[Click here to use the app](https://book-recommend-system-abkn8473oa6numahr2sqks.streamlit.app/)**  

---
## 📸 Screenshots

### 🔍 Book Search 
<img src="https://github.com/vb8146649/Book-Recommend-System/blob/main/demo.gif" alt="book-recommender-demo" width=100%>

---

## 🔗 Links

- 📓 **Google Colab Notebook (Model Training)**: 
    - [Open in Colab](https://colab.research.google.com/drive/1lRsR3rXrBgW9-akx6Hn_kkmGl4hH8KNW?usp=sharing)
- 🏷️ **Model Files on Kaggle**: 
    - [Books Dataset](https://www.kaggle.com/datasets/abdallahwagih/books-dataset)

---

## 🚀 Features

- Search and select a book title
- Get up to 20 similar book recommendations
- View covers fetched dynamically using Open Library API
- Fast loading through optimized `.pkl` model files hosted on Google Drive

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [gdown](https://pypi.org/project/gdown/)
- Google Drive for model file storage
- Open Library API for book cover retrieval

---

## 🔐 Secrets Configuration

Create a `.streamlit/secrets.toml` file for sensitive keys:

```toml
similarity = "your_google_drive_file_id_for_similarity.pkl"
movies_dict = "your_google_drive_file_id_for_movies_dict.pkl"
