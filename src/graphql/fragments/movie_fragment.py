import strawberry

from src.graphql.models.movie import Movie, MovieAdded, MovieNotFound


# GetMovieResponse = strawberry.union("GetMovieResponse", (Movie, MovieNotFound))
# AddMovieResponse = strawberry.union("AddMovieResponse", (Movie, MovieAdded))
