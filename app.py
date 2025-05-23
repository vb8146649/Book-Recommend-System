import streamlit as st
import pickle
import pandas as pd
import gdown
import os

output = 'similarity.pkl'
file_id = st.secrets['similarity']
if not os.path.exists(output):
    print("Downloading similarity.pkl from Google Drive...")
    gdown.download(id=file_id, output=output, quiet=False)

# Now load the file
with open(output, 'rb') as f:
    similarity = pickle.load(f)

output2 = 'books.pkl'
file_id = st.secrets['books']
if not os.path.exists(output2):
    print("Downloading books.pkl from Google Drive...")
    gdown.download(id=file_id, output=output2, quiet=False)

# Now load the file
with open(output2, 'rb') as f:
    books = pd.DataFrame(pickle.load(f))

# books= pd.DataFrame(pickle.load(open('books.pkl', 'rb')))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(book):
    book_index = books[books['title'] == book].index[0]
    distances = similarity[book_index]
    books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:20]
    
    recommended_books = []
    recommended_books_posters = []
    for i in books_list:
        recommended_books.append(books.iloc[i[0]].title)
        recommended_books_posters.append(books.iloc[i[0]].thumbnail)
    return recommended_books,recommended_books_posters


st.title('Book Recommendation System')


option = st.selectbox(
    "Search Similar Books",
    books['title'].values,
    index=None,
    placeholder="Select Books....",
)

if st.button("Recommend"):
    names, posters = recommend(option)
    
    num_books = len(names)
    num_cols = 4
    rows = (num_books + num_cols - 1) // num_cols

    for row in range(rows):
        cols = st.columns(num_cols)
        for col_idx in range(num_cols):
            idx = row * num_cols + col_idx
            if idx < num_books:
                with cols[col_idx]:
                    st.markdown(
                        f"""
                        <div style="height: 250px; text-align: center;">
                            <img src="{posters[idx]}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px;" />
                            <p style="
                                margin-top: 10px;
                                font-weight: bold;
                                overflow: hidden;
                                white-space: nowrap;
                                text-overflow: ellipsis;
                            " title="{names[idx]}">
                                {names[idx]}
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
