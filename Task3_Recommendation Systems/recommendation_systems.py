# RECOMMENDATION SYSTEM – SINGLE FILE VERSION
# CodSoft Internship Task 4

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ---------------------------------------------------------
# SAMPLE DATA (you can replace this with your CSV files)
# ---------------------------------------------------------

items = pd.DataFrame({
    "item_id": [1, 2, 3, 4],
    "title": ["Inception", "Interstellar", "The Dark Knight", "Memento"],
    "combined_features": [
        "sci-fi thriller dreams mind bending",
        "sci-fi space time travel emotional",
        "action superhero crime thriller",
        "thriller mystery memory loss"
    ]
})

ratings = pd.DataFrame({
    "user_id": [1, 1, 2, 2, 3],
    "item_id": [1, 2, 1, 3, 2],
    "rating": [5, 4, 4, 5, 5]
})


# ---------------------------------------------------------
# CONTENT-BASED RECOMMENDATION
# ---------------------------------------------------------

def content_based_recommend(item_title, top_n=3):

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(items["combined_features"])

    similarity = cosine_similarity(tfidf)

    # Find index of the movie
    index = items[items["title"] == item_title].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Skip the first one (same movie)
    scores = scores[1: top_n + 1]

    result = [items.iloc[i]["title"] for i, _ in scores]
    return result


# ---------------------------------------------------------
# COLLABORATIVE FILTERING (ITEM-BASED)
# ---------------------------------------------------------

def collaborative_recommend(user_id, top_n=3):

    user_item_matrix = ratings.pivot_table(index="user_id",
                                           columns="item_id",
                                           values="rating")

    item_matrix = user_item_matrix.T.fillna(0)
    similarity = cosine_similarity(item_matrix)
    similarity_df = pd.DataFrame(similarity,
                                 index=item_matrix.index,
                                 columns=item_matrix.index)

    user_ratings = user_item_matrix.loc[user_id].dropna()

    scores = {}

    for item in item_matrix.index:
        if item in user_ratings.index:
            continue

        sim_items = similarity_df.loc[item, user_ratings.index]
        rating_values = user_ratings.values

        if sim_items.sum() == 0:
            continue

        predicted = np.dot(sim_items, rating_values) / sim_items.sum()
        scores[item] = predicted

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[:top_n]

    recommended_items = [items[items["item_id"] == item]["title"].values[0]
                         for item, score in sorted_scores]

    return recommended_items


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

print("=== SIMPLE RECOMMENDATION SYSTEM ===")
print("1. Content-Based Recommendation")
print("2. Collaborative Filtering Recommendation")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter movie title (Inception, Interstellar, etc): ")
    print("\nTop Recommendations:")
    print(content_based_recommend(name))

elif choice == "2":
    uid = int(input("Enter user ID (1, 2, or 3): "))
    print("\nTop Recommendations:")
    print(collaborative_recommend(uid))

else:
    print("Invalid choice.")
