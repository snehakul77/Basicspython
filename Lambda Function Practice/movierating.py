movies = [
    {"title": "Inception", "rating": 8.8},
    {"title": "The Matrix", "rating": 8.7},
    {"title": "Interstellar", "rating": 8.6},
    {"title": "The Room", "rating": 3.7},
    {"title": "Parasite", "rating": 8.6}
]

highest_ratedmovie = max(movies, key=lambda movie: movie["rating"])
lowest_ratedmovie = min(movies, key=lambda movie: movie["rating"])

print(f"Movie: {highest_ratedmovie['title']}")
print(f"Movie: {lowest_ratedmovie['title']}")
