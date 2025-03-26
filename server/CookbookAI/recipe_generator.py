"""Recipe Generator module to generate recipes based on user input."""
import json

from enum import Enum
import sys
from typing import List

from mirascope import llm
from pydantic import BaseModel
import os

API_KEY = (
    "sk-proj-zM7tkkLTVfqOovs9PpFTh9Gz8-G87H1Fqfe5sXMXSuabx1PqecWF9Nmnd4QnK_UyTgMp"
    "PvpYFMT3BlbkFJrAfHvjh9UAiviFaEn_j9FF47KLBdc_7vCPAbpwqYlPkgUuZQ-VAGeQuRMlVSeKb"
    "PfDT73sujoA"
)

class Difficulty(str, Enum):
    """Enum for recipe difficulty levels."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"

class Recipe(BaseModel):
    """Model for a recipe."""
    title: str
    # recipe_reference_urls: list
    recipe_description: str
    ingredients: list
    instructions: list

class RecipeGenerator:
    """Class to generate recipes."""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.set_api_env()

    @llm.call(provider="openai", model="gpt-4o-mini", response_model=Recipe)
    def get_recipe(self, cuisine: str, prep_time: int, difficulty: Difficulty,
                   ingredients: List[str]) -> str:
        """Generate a recipe based on the given parameters."""
        print(difficulty.value)
        return (
            f"I am a {difficulty.value} level cook. I want to make something {cuisine} "
            f"that takes no more than {prep_time} minutes. Create a recipe which "
            f"must include these ingredients: {ingredients}. Provide the website sources "
            "used to create this recipe."
        )

    def set_api_env(self):
        """Set the API environment by storing to ENV."""
        os.environ["OPENAI_API_KEY"] = self.api_key

def main(ingredients: List[str], cuisine: str, prep_time: int, difficulty: Difficulty):
    """Main function to generate and print a recipe."""
    recipe_generator = RecipeGenerator(API_KEY)
    ret_recipe: Recipe = recipe_generator.get_recipe(
        ingredients=ingredients, cuisine=cuisine, prep_time=prep_time,
        difficulty=difficulty
    )
    print(json.dumps(ret_recipe.model_dump(), indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python RecipeGenerator.py <cuisine> <prep_time> <difficulty> "
              "<ingredient1> <ingredient2> ...")
        sys.exit(1)

    m_cuisine = sys.argv[1]
    m_prep_time = int(sys.argv[2])
    m_difficulty = Difficulty(sys.argv[3])
    m_ingredients = sys.argv[4:]
    print(f"Cuisine: {m_cuisine}")
    print(f"Prep Time: {m_prep_time}")
    print(f"Difficulty: {m_difficulty}")
    print(f"Ingredients: {m_ingredients}")
    main(m_ingredients, m_cuisine, m_prep_time, m_difficulty)
