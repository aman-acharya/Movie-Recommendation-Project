import streamlit as st
import pandas as pd
import pickle
import requests

# creeat a title in the center
st.markdown("<h1 style='text-align: center; color: red;'>RecFlix</h1>", unsafe_allow_html=True)

def recommend(movie, num_recommendations):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:num_recommendations+1]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2a44a8e55f6471cc065c7c32db1d5256&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# read the data
@st.cache_data
def load_data():
    movies = pd.read_csv('movie_data.csv')
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

# get the movie title
movie_title = st.selectbox(':blue[**Select a movie you like** :]', movies['title'].values)

# get the number of recommendations
num_recommendations = st.number_input(':blue[**Number of recommendations** :]', min_value=1, max_value=100)

if st.button('Recommend', type='primary'):
    recommended_movies, recommended_movies_posters = recommend(movie_title, num_recommendations)
    
    # Display the recommended movies and posters
    for i in range(0, len(recommended_movies), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(recommended_movies):
                with cols[j]:
                    st.image(recommended_movies_posters[i + j])
                    st.write(recommended_movies[i + j])
                    for _ in range(2):  # Use a different variable name here
                        st.write(" ")



