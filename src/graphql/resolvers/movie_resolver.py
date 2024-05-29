import strawberry
from typing import List
from dataclasses import asdict
import asyncio
import logging

from src.db import prisma
from src.graphql.models.movie import Movie, MovieCreateInput

# Configurar o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para verificar e conectar o Prisma
async def ensure_prisma_connected():
    if not prisma.is_connected():
        logger.info("Connecting to Prisma...")
        await prisma.connect()

# Função para executar uma operação Prisma com timeout
async def run_with_timeout(coro, timeout: int = 60):  # Aumentar o timeout para 60 segundos
    try:
        return await asyncio.wait_for(coro, timeout)
    except asyncio.TimeoutError:
        logger.error("The request to the database timed out")
        raise TimeoutError("The request to the database timed out")

async def get_movie(
    id: str
) -> Movie:
    await ensure_prisma_connected()  # Verifica e conecta o Prisma se necessário

    try:
        movie = await run_with_timeout(
            prisma.movie.find_first(
                where={
                    'id': {
                        'equals': id
                    }
                }
            )
        )
    except asyncio.TimeoutError:
        raise TimeoutError("The request to the database timed out")

    if movie is None:
        raise ValueError("Movie not found")

    return Movie(**movie.__dict__)

async def get_movies() -> List[Movie]:
    await ensure_prisma_connected()  # Verifica e conecta o Prisma se necessário

    try:
        movies = await run_with_timeout(
            prisma.movie.find_many()
        )
    except asyncio.TimeoutError:
        raise TimeoutError("The request to the database timed out")

    return [Movie(**movie.__dict__) for movie in movies]

async def add_movie(
    movie: MovieCreateInput
) -> Movie:
    await ensure_prisma_connected()  # Verifica e conecta o Prisma se necessário

    try:
        added_movie = await run_with_timeout(
            prisma.movie.create(
                data=asdict(movie)
            )
        )
    except asyncio.TimeoutError:
        raise TimeoutError("The request to the database timed out")

    return Movie(**added_movie.__dict__)
