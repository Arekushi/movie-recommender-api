import strawberry

from src.graphql.resolvers.movie_resolver import get_movie, get_movies


@strawberry.type
class Query:
    movie = strawberry.field(resolver=get_movie)
    movies = strawberry.field(resolver=get_movies)


