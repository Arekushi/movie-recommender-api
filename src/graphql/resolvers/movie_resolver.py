import strawberry

from src.db import prisma
from src.graphql.models.movie import Movie, MovieCreateInput, MovieNotFound, MovieAdded
from typing import List
from dataclasses import asdict


async def get_movie(
    id: str
) -> Movie:
    movie = await prisma.movie.find_first(
        where={
            'id': {
                'equals': id
            }
        }
    )

    if movie is None:
        pass

    return Movie(**movie.__dict__)


async def get_movies() -> List[Movie]:
    movies = await prisma.movie.find_many()
    return [Movie(**movie.__dict__) for movie in movies]


async def add_movie(
    movie: MovieCreateInput
) -> Movie:
    added_movie = await prisma.movie.create(
        data=asdict(movie)
    )

    return Movie(**added_movie.__dict__)


