import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=81cfa116f347a94ec4d646ed268b3df7&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
       movie_id = movies.iloc[i[0]].movie_id
       recommended_movie.append(movies.iloc[i[0]].title)

       # fetch poster from API
       recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
   movies['title'].values)

if st.button('Recommend'):
    name , poster = recommend(selected_movie_name)

    row1,row2,row3 = st.columns(3)
    row4, row5,row6 = st.columns(3)





    with row1:
        st.subheader(name[0],divider='rainbow')
        st.image(poster[0])

    with row2:
        st.subheader(name[1],divider='rainbow')
        st.image(poster[1])

    with row3:
        st.subheader(name[2],divider='rainbow')
        st.image(poster[2])

    with row4:
        st.subheader(name[3],divider='rainbow')
        st.image(poster[3])

    with row5:
        st.subheader(name[4],divider='rainbow')
        st.image(poster[4])

    with row6:
        st.subheader(name[5],divider='rainbow')
        st.image(poster[5])













    # col1, col2, col3, col4, col5 = st.columns(5)
    #
    # with col1:
    #     st.header(name[0])
    #     st.image(poster[0])
    #
    # with col2:
    #     st.header(name[1])
    #     st.image(poster[1])
    #
    # with col3:
    #     st.header(name[2])
    #     st.image(poster[2])
    #
    # with col4:
    #     st.header(name[3])
    #     st.image(poster[3])
    #
    # with col5:
    #     st.header(name[4])
    #     st.image(poster[4])