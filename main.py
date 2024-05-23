import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from src.graphql.schemas.query_schema import Query
from src.graphql.schemas.mutation_schema import Mutation
from config import settings
import strawberry

# Crie o aplicativo FastAPI
app = FastAPI()

# Defina e construa o esquema GraphQL completo
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

# Adicione a rota GraphQL ao servidor FastAPI
app.include_router(graphql_app, prefix="/graphql")

# Defina outras rotas do aplicativo
@app.get("/")
async def root():
    return {"message": "Bem-vindo"}

@app.get("/home")
async def home():
    return {"message": "Recomendação de Filmes!"}

def main():
    uvicorn.run(
        'main:app',
        host=settings.HOST_URL,
        port=settings.HOST_PORT,
        reload=bool(settings.RELOAD)
    )

if __name__ == '__main__':
    main()
