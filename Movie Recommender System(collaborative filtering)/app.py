import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies_df = pd.read_csv(os.path.join(BASE_DIR, 'movies.csv'))
ratings_df = pd.read_csv(os.path.join(BASE_DIR, 'ratings.csv'))


merged_df = pd.merge(movies_df, ratings_df, on='movieId')


rating_matrix = merged_df.pivot_table(index='movieId', columns='userId', values='rating')


rating_matrix = rating_matrix.fillna(0)


def get_movie_id(movie_title):
    movie = movies_df.loc[movies_df['title'] == movie_title, 'movieId']
    if movie.empty:
        return None
    return movie.iloc[0]


def recommend_movies(movie_title, num_recommendations=5):
    movie_id = get_movie_id(movie_title)
    
    if movie_id is None:
        return []

    # Ratings vector of selected movie
    movie_ratings = rating_matrix.loc[movie_id].values.reshape(1, -1)

    # Cosine similarity with all movies
    similarity = cosine_similarity(movie_ratings, rating_matrix.values).flatten()

    # Get top similar movies (excluding itself)
    top_indices = np.argsort(similarity)[::-1][1:num_recommendations+1]

    # Map indices to movie titles
    recommended_movies = movies_df[
        movies_df['movieId'].isin(rating_matrix.index[top_indices])
    ]['title'].tolist()

    return recommended_movies


st.title("Movie Recommendation System")


movie_title = st.selectbox("Select a movie", movies_df['title'])


if st.button("Recommend movies"):
    recommended_movies = recommend_movies(movie_title, 5)
    st.write("Recommended movies:")
    for movie in recommended_movies:

        st.write(movie)

