📖 Overview
This project is a Movie Recommendation System built using collaborative filtering techniques. The system suggests movies to users based on their past interactions and the preferences of similar users.

🚀 Features
Recommends movies using user-based and item-based collaborative filtering.
Handles sparse data efficiently.
Includes exploratory data analysis (EDA) on user ratings.
Interactive interface for users to get personalized recommendations.

🛠️ Tech Stack
Programming Language: Python
Libraries:
pandas - for data manipulation.
numpy - for numerical operations.
scikit-learn - for similarity computations.
matplotlib/seaborn - for data visualization.

📁 Dataset
The system uses the MovieLens dataset, which contains user ratings for movies.

Dataset Details:
User IDs, Movie IDs, and Ratings.
Additional metadata (e.g., genres, titles).

🧠 Methodology
1. Data Preprocessing
Handled missing data and duplicate entries.
Transformed data into a user-item interaction matrix.
2. Collaborative Filtering
User-based Filtering: Finds similar users and recommends movies they liked.
Item-based Filtering: Recommends movies similar to those a user has already rated highly.
3. Similarity Metrics
Cosine Similarity

