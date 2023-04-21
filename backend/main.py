import json
import os
import graphene
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class Query(graphene.ObjectType):
    testing = graphene.String()

    def resolve_hello(self, info):
        return 'World'


schema = graphene.Schema(query=Query)

# this is to allow CORS so that you can connect backend and frontend locally
load_dotenv()
origins = os.environ.get("ALLOW_CORS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
  return {"message": "Hello World"}

@app.get('/boba_list')
async def get_boba_list():
  with open('./database/bobalist.json') as f:
      # Load the JSON data into a Python object
    bobaList = json.load(f)
  return bobaList["data"]

@app.get('/milk_list')
async def get_milk_list():
  with open('./database/milkoption.json') as f:
    milkOption = json.load(f)
  return milkOption["data"]

@app.get('/toppings_list')
async def get_toppings_list():
  with open('./database/toppingsoption.json') as f:
    toppingsOption = json.load(f)
  return toppingsOption["data"]
