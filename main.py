import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from strawberry.asgi import GraphQL
from src.graphql.schemas.query_schema import Query
from src.app import create_app
from config import settings

app = Starlette()

# Defina o esquema GraphQL
schema = Query

# Crie a função de visualização para a rota GraphQL
async def graphql(request):
    data = await request.json()
    response = schema.execute_sync(data.get("query"))
    return JSONResponse(response)

# Adicione a rota GraphQL ao servidor
app.add_route("/graphql", GraphQL(schema=schema))

# Defina outras rotas do aplicativo
@app.route("/")
async def root(request):
    return JSONResponse({"message": "Hello World"})

@app.route("/home")
async def home(request):
    return JSONResponse({"message": "Bem-Vindo a página inicial"})

def main():
    uvicorn.run(
        app,
        host=settings.HOST_URL,
        port=settings.HOST_PORT,
        reload=bool(settings.RELOAD)
    )

if __name__ == '__main__':
    main()
