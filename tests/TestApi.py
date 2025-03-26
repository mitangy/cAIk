from fastapi.testclient import TestClient

from server.CookbookAI.api import app  # Assuming your FastAPI app is defined in api.py

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_add_api_key():
    response = client.post("/add_api_key", json={"model": "test_model", "api_key": "test_key"})
    assert response.status_code == 200
    assert response.json() == {"message": "API key added successfully"}

def test_add_ingredients():
    response = client.post("/add_ingredients", json={"ingredients": ["tomato", "cheese"]})
    assert response.status_code == 200
    assert response.json() == {"message": "Ingredients added successfully"}

def test_get_recipe():
    recipe_data = {
        "ingredients": ["tomato", "cheese"],
        "food_restrictions": [],
        "cuisine": "Italian",
        "prep_time": 30,
        "difficulty": "beginner"
    }
    response = client.post("/get_recipe", json=recipe_data)
    assert response.status_code == 200
    # assert that response contains the expected recipe data
    assert "title" in response.json()
    assert "recipe_description" in response.json()
    assert "ingredients" in response.json()
    assert "instructions" in response.json()
    # assert that the recipe data is valid
    assert response.json()["title"]
    assert response.json()["recipe_description"]
    assert response.json()["ingredients"]
    assert response.json()["instructions"]

