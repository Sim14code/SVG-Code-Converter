from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql_schema import schema

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql_schema import schema

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
