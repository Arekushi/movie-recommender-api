import strawberry

from config import settings
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.db import prisma

from src.graphql.schemas.mutation_schema import Mutation
from src.graphql.schemas.query_schema import Query


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=True)
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    yield
    await prisma.disconnect()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    graphql_app = GraphQLRouter(schema)
    app.include_router(
        graphql_app,
        prefix=settings.graphql.prefix
    )
    
    return app
