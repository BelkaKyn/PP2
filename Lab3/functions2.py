1.
def is_above_5_5(movie):
    imdb_score = movie.get('imdb_score')
    
    if imdb_score is not None and imdb_score > 5.5:
        return True
    else:
        return False

# Пример
movie = {'title': 'Example Movie', 'imdb_score': 6.2}
result = is_above_5_5(movie)
print("Is the IMDB score above 5.5?", result)

2.
def filter_movies_above_5_5(movies):
    filtered_movies = []
    for movie in movies:
        imdb_score = movie.get('imdb_score')
        if imdb_score is not None and imdb_score > 5.5:
            filtered_movies.append(movie)
    return filtered_movies

# Пример
movies = [
    {'title': 'Movie 1', 'imdb_score': 6.2},
    {'title': 'Movie 2', 'imdb_score': 4.8},
    {'title': 'Movie 3', 'imdb_score': 7.1}
]
filtered_movies = filter_movies_above_5_5(movies)
print("Movies with an IMDB score above 5.5:")
for movie in filtered_movies:
    print(movie['title'], '-', movie['imdb_score'])

3.
def get_movies_by_category(movies, category_name):
    filtered_movies = []
    for movie in movies:
        categories = movie.get('categories', [])
        if category_name in categories:
            filtered_movies.append(movie)
    return filtered_movies

# Пример
movies = [
    {'title': 'Movie 1', 'categories': ['Action', 'Adventure']},
    {'title': 'Movie 2', 'categories': ['Comedy', 'Drama']},
    {'title': 'Movie 3', 'categories': ['Action', 'Thriller']}
]
category_name = 'Action'
filtered_movies = get_movies_by_category(movies, category_name)
print(f"Movies under the category '{category_name}':")
for movie in filtered_movies:
    print(movie['title'])

4.
def average_imdb_score(movies):
    total_score = 0
    num_movies = len(movies)
    
    if num_movies == 0:
        return 0  
    
    for movie in movies:
        imdb_score = movie.get('imdb_score')
        if imdb_score is not None:
            total_score += imdb_score
    
    return total_score / num_movies

# Пример
movies = [
    {'title': 'Movie 1', 'imdb_score': 6.2},
    {'title': 'Movie 2', 'imdb_score': 7.8},
    {'title': 'Movie 3', 'imdb_score': 5.5}
]
average_score = average_imdb_score(movies)
print("Average IMDB score:", average_score)

5.
def average_imdb_score_by_category(movies, category_name):
    total_score = 0
    num_movies = 0
    
    for movie in movies:
        categories = movie.get('categories', [])
        if category_name in categories:
            imdb_score = movie.get('imdb_score')
            if imdb_score is not None:
                total_score += imdb_score
                num_movies += 1
    
    if num_movies == 0:
        return 0  
    
    return total_score / num_movies

# Пример
movies = [
    {'title': 'Movie 1', 'categories': ['Action'], 'imdb_score': 6.2},
    {'title': 'Movie 2', 'categories': ['Comedy'], 'imdb_score': 7.8},
    {'title': 'Movie 3', 'categories': ['Action'], 'imdb_score': 5.5},
    {'title': 'Movie 4', 'categories': ['Comedy'], 'imdb_score': 6.9}
]
category_name = 'Comedy'
average_score = average_imdb_score_by_category(movies, category_name)
print(f"Average IMDB score for movies under the category '{category_name}': {average_score:.2f}")

