import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from src.graphql.schemas.query_schema import Query
from src.graphql.schemas.mutation_schema import Mutation
from config import settings
from prisma import Prisma
import strawberry

# Inicialize o cliente Prisma
prisma = Prisma()

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

# Conectar o cliente Prisma na inicialização do aplicativo
@app.on_event("startup")
async def startup():
    await prisma.connect()

# Desconectar o cliente Prisma na finalização do aplicativo
@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

def main():
    uvicorn.run(
        'main:app',
        host=settings.HOST_URL,
        port=settings.HOST_PORT,
        reload=bool(settings.RELOAD)
    )

if __name__ == '__main__':
    main()
