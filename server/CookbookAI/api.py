"""API for CookbookAI"""
from typing import List
import json
import uvicorn

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from server.CookbookAI.recipe_generator import Recipe, Difficulty, RecipeGenerator
from server.CookbookAI.database_interfacer import DatabaseInterfacer

app = FastAPI()

origins = ["http://localhost", "http://localhost:8000",
           "http://localhost:3000", "http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_keys = {}
ingredients = []
recipes = []

API_KEY = (
    "sk-proj-zM7tkkLTVfqOovs9PpFTh9Gz8-G87H1Fqfe5sXMXSuabx1PqecWF9Nmnd4QnK_UyTgMp"
    "PvpYFMT3BlbkFJrAfHvjh9UAiviFaEn_j9FF47KLBdc_7vCPAbpwqYlPkgUuZQ-VAGeQuRMlVSeKb"
    "PfDT73sujoA"
)

class APIKey(BaseModel):
    """Model for an API key."""
    model: str
    api_key: str

class Ingredients(BaseModel):
    """Model for a list of ingredients."""
    ingredients: List[str]

class RecipeData(BaseModel):
    """Model for recipe data """
    ingredients: List[str]
    food_restrictions: List[str]
    cuisine: str
    prep_time: int
    difficulty: str

@app.get("/")
async def root(request: Request):
    """Root endpoint. Generates a template saying hello world."""
    return {"message": "Hello World"}

@app.post("/add_api_key")
async def add_api_key(api_key: APIKey):
    """Add an API key to the database."""
    api_keys[api_key.model] = api_key.api_key
    return {"message": "API key added successfully"}

@app.post("/add_ingredients")
async def add_ingredients(ingredients_data: Ingredients):
    """Add a list of ingredients to the database."""
    ingredients.extend(ingredients_data.ingredients)
    return {"message": "Ingredients added successfully"}

@app.get("/get_ingredients")
async def get_ingredients():
    """Get a list of ingredients."""
    return {"ingredients": ingredients}

@app.post("/get_recipe", response_model=Recipe)
async def get_recipe(recipe_data: RecipeData):
    """Get a recipe based on the given parameters."""
    print(recipe_data)
    recipes.append(recipe_data)
    recipe = RecipeGenerator(API_KEY).get_recipe(
        ingredients=recipe_data.ingredients, cuisine=recipe_data.cuisine,
        prep_time=recipe_data.prep_time, difficulty=Difficulty(recipe_data.difficulty)
    )
    return recipe

def start_server():
    """Start the server."""
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == '__main__':
    start_server()
