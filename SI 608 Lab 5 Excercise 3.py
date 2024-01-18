# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:56:56 2023

@author: raamc
"""
import pandas as pd
from pathlib import Path
import networkx as nx
from collections import defaultdict
from random import choice
from tqdm import tqdm

# Step 1
data_dir = Path('C:/Users/raamc/OneDrive/Desktop/Projects')

# Load the data
user_movie_df = pd.read_csv(data_dir / 'ratings.csv')
movie_df = pd.read_csv(data_dir / 'movies.csv')

# Display the data types and the first few rows to inspect the structure
print(user_movie_df.dtypes)
print(user_movie_df.head())
print(movie_df.dtypes)
print(movie_df.head())

# Extract and display the unique identifiers
userIds = user_movie_df['userId'].unique()
movieIds = user_movie_df['movieId'].unique()
print(f'We have {len(userIds)} users, {len(movieIds)} movies, and {len(user_movie_df)} connections in this dataset.')

#Step 2
# Initialize the bipartite graph
user_movie_graph = nx.Graph()

# Add user nodes with a 'type' attribute set to 'user'
for user_id in user_movie_df['userId'].unique():
    user_movie_graph.add_node(user_id, type='user')

# Add movie nodes with a 'type' attribute set to 'movie'
for movie_id in user_movie_df['movieId'].unique():
    user_movie_graph.add_node(movie_id, type='movie')

# Add edges between users and movies
for _, row in user_movie_df.iterrows():
    user_movie_graph.add_edge(row['userId'], row['movieId'], rating=row['rating'])

# Output the graph to check it has been created correctly
print(user_movie_graph)

#Step 3
def naive_random_walk(user_id, graph, steps, num_runs):
    user_id = int(user_id)  
    recommended_movies = defaultdict(int)

    for _ in tqdm(range(num_runs)):
        cur_user = user_id
        for _ in range(steps):
            # Randomly select a movie favored by the current user
            movies = [n for n in graph.neighbors(cur_user) if graph.nodes[n]['type'] == 'movie']
            if not movies:  # if no movies found, break the current run
                break
            movie_id = choice(movies)
            recommended_movies[movie_id] += 1

            # Randomly select a user who favors this movie
            users = [n for n in graph.neighbors(movie_id) if graph.nodes[n]['type'] == 'user']
            if not users:  # if no users found, break the current run
                break
            cur_user = choice(users)

    # Sort the recommended movies based on count
    results = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
    return results

# Example use of the function
# This assumes 'user_movie_graph' is already defined and is the bipartite graph
top_movies = naive_random_walk('1', user_movie_graph, 50, 1000)[:5]
print(top_movies)

#Step 4
class NaiveRecommendationSystem:
    def __init__(self, user_movie_graph, movie_df):
        self.user_movie_graph = user_movie_graph
        self.movie_df = movie_df

    def movie_id2movie_name(self, movie_id):
        # Adjust the movie_id to integer if necessary
        movie_id = int(movie_id)
        movie_name = self.movie_df[self.movie_df['movieId'] == movie_id]['title'].values[0]
        return movie_name

    def naive_random_walk(self, user_id, steps, num_runs, top_k):
        recommended_movies = defaultdict(int)

        for _ in tqdm(range(num_runs)):
            cur_user = user_id
            for _ in range(steps):
                movies = [n for n in self.user_movie_graph.neighbors(cur_user) if self.user_movie_graph.nodes[n]['type'] == 'movie']
                if not movies:
                    break
                movie_id = choice(movies)
                recommended_movies[movie_id] += 1

                users = [n for n in self.user_movie_graph.neighbors(movie_id) if self.user_movie_graph.nodes[n]['type'] == 'user']
                if not users:
                    break
                cur_user = choice(users)

        results = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
        return results[:top_k]

    def recommend(self, user_id, steps=50, num_runs=1000, top_k=5):
        # Convert user_id to the correct format if needed, e.g., to int
        user_id = int(user_id)  # Adjust this based on your graph's user ID format

        recommended_ids = self.naive_random_walk(user_id, steps, num_runs, top_k)
        print(f'Top-{top_k} recommended movies for user {user_id} are:')
        for idx, (recommended_id, _) in enumerate(recommended_ids):
            movie_name = self.movie_id2movie_name(recommended_id)
            print(f'{idx+1}: {movie_name}')

# Create an instance of the recommendation system
naive_recommendation_system = NaiveRecommendationSystem(user_movie_graph, movie_df)

# Make a recommendation for a user
naive_recommendation_system.recommend(1)  # Assuming user IDs are integers