# Movie Recommendation System 🎥🍿

A **Movie Recommendation System** built using **cosine similarity** and the **TMDB API** to provide personalized movie recommendations. This Streamlit app fetches movie posters and suggests movies similar to a user's selection based on the movie content.

### Demo
Check out the live demo of the project [here](https://movie-recommendation-project-nzcfhbmgcsr82wuekhwccz.streamlit.app/)

### Features
- **Movie Recommendations**: Provides a list of movies similar to the one selected by the user.
- **Poster Fetching**: Fetches movie posters from the TMDB database using the movie's ID.
- **Cosine Similarity**: The recommendation system uses content-based filtering with cosine similarity to find similar movies.
- **Interactive UI**: Developed with **Streamlit** for a smooth, interactive user experience.

### How It Works
1. **Content-based Filtering**: 
   - Features like movie title, genres, keywords, overview, cast, and crew are extracted.
   - These features are processed into a single `tags` column which is preprocessed (lowercasing, removing stop words, stemming).
   - Using **TF-IDF Vectorizer**, these `tags` are converted into vectors.
   - **Cosine Similarity** is calculated between the vectors to find similarities between movies.

2. **Movie Poster Fetching**:
   - The movie poster is fetched from the **TMDB API** using the movie ID. 
   - A `poster_path` is retrieved from TMDB, which is then used to display the movie's poster in the app.

### Data
- **Data Source**: The dataset used in this project consists of features such as movie title, genres, keywords, cast, crew, and more. It is merged to create a single column, `tags`, for the recommendation engine.
- **API**: Movie posters are fetched using the **TMDB API**.

### Technologies
- **Languages**: Python
- **Libraries**: 
  - Data Preprocessing: Pandas, NLTK
  - Machine Learning: Scikit-Learn (for vectorization and similarity computation)
  - Web Framework: Streamlit
  - API: TMDB API for fetching movie posters
- **Tools**: GitHub for version control, Streamlit for deployment, and Python virtual environment for package management.

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/ayushach007/Movie-Recommendation-Project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Movie-Recommendation-Project
   ```
3. Create a virtual environment:
   - Using `python -m venv`:
     ```bash
     python -m venv venv
     ```
   - Or using `conda`:
     ```bash
     conda create --name movie-rec python=3.8
     ```
4. Activate the environment:
   - For `venv`:
     ```bash
     source venv/bin/activate  # On macOS/Linux
     venv\Scripts\activate  # On Windows
     ```
   - For `conda`:
     ```bash
     conda activate movie-rec
     ```
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### API Details
The project uses the **TMDB API** to fetch movie posters:
- A `movie_id` is used to query the TMDB API, retrieve the `poster_path`, and construct the full poster URL.

Example code snippet for fetching a poster:
```python
url = "https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY&language=en-US".format(movie_id)
data = requests.get(url).json()
poster_path = data['poster_path']
full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
```


### License
This project is licensed under the **GNU General Public License**.

### Author
- **Ayush Acharya**

You can check the project repository [here](https://github.com/ayushach007/Movie-Recommendation-Project).