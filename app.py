import streamlit as st
import pandas as pd
import pickle
import requests

# creeat a title in the center
st.markdown("<h1 style='text-align: center; color: red;'>RecFlix</h1>", unsafe_allow_html=True)

def recommend(movies, selected_movie, num_recommendations, similarity):
    '''
    Function to recommend movies

    Args: 
        - movie: str: name of the movie
        - num_recommendations: int: number of recommendations to return

    Returns:
        - recommended_movie_names: list: list of recommended movie names
        - recommended_movie_posters: list: list of recommended movie posters
    '''
    try:
        index = movies[movies['title'] == selected_movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:num_recommendations+1]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names,recommended_movie_posters

    except Exception as e:
        st.info(':warning: Error recommending movies. Please try again.')
        return None, None

def fetch_poster(movie_id):
    '''
    Function to fetch the movie poster
    
    Args:
        - movie_id: int: id of the movie
    
    Returns:
        - full_path: str: full path of the movie poster
    '''
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=2a44a8e55f6471cc065c7c32db1d5256&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path

    except Exception as e:
        st.info(':warning: Error fetching the movie poster for selected movie. Please try another movie.')
        return None

# read the data
@st.cache_data
def load_data():
    '''
    Function to load the data and similarity matrix

    Returns:
        - movies: pd.DataFrame: dataframe containing the movie data
        - similarity: np.array: similarity matrix
    '''
    try:
        movies = pd.read_csv('movie_data.csv')
        similarity = pickle.load(open('similarity.pkl', 'rb'))
        return movies, similarity   
    
    except Exception as e:
        st.info(':warning: Error loading the data. Please try again.')
        return None, None
    
def main():
    try:
        movies, similarity = load_data()

        # create 2 columns
        col1, col2 = st.columns(2)

        # get the movie title
        with col1:
            movie_title = st.selectbox(':blue[**Select a movie you like** :]', movies['title'].values)

        # get the number of recommendations
        with col2:
            num_recommendations = st.number_input(':blue[**Number of recommendations** :]', min_value=1, max_value=100)

        if st.button('Recommend', type='primary'):
            recommended_movies, recommended_movies_posters = recommend(movies=movies, selected_movie=movie_title, num_recommendations=num_recommendations, similarity=similarity)
            
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

    except Exception as e:
        st.info(':warning: Error recommending movies. Please try again.')

if __name__ == "__main__":
    main()



