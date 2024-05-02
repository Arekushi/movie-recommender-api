import strawberry

from src.graphql.resolvers.movie_resolver import add_movie


@strawberry.type
class Mutation:
    add_movie = strawberry.mutation(resolver=add_movie)
