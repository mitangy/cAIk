"""Database Interfacer to connect to PostgreSQL database and perform CRUD operations.
It will use SQLAlchemy ORM to interact with the database. It will store ingredients and API keys."""

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/dbname"

Base = declarative_base()

class Recipe(Base):
    """Model for a recipe."""
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    ingredients = Column(Text)
    instructions = Column(Text)

class Ingredient(Base):
    """Model for an ingredient."""
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class APIKey(Base):
    """Model for an API key."""
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, index=True)
    key = Column(String)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class DatabaseInterfacer:
    """Class to interact with postgres database"""
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = SessionLocal()

    def create_recipe(self, title: str, description: str, ingredients: str, instructions: str):
        """Create a recipe in the database."""
        db_recipe = Recipe(
            title=title,
            description=description,
            ingredients=ingredients,
            instructions=instructions
        )
        self.db.add(db_recipe)
        self.db.commit()
        self.db.refresh(db_recipe)
        return db_recipe

    def get_recipe(self, recipe_id: int):
        """Get a recipe from the database."""
        return self.db.query(Recipe).filter(Recipe.id == recipe_id).first()

    def update_recipe(self, recipe_id: int, title: str = None, description: str = None,
                      ingredients: str = None, instructions: str = None):
        """Update a recipe in the database."""
        db_recipe = self.db.query(Recipe).filter(Recipe.id == recipe_id).first()
        if db_recipe:
            if title:
                db_recipe.title = title
            if description:
                db_recipe.description = description
            if ingredients:
                db_recipe.ingredients = ingredients
            if instructions:
                db_recipe.instructions = instructions
            self.db.commit()
            self.db.refresh(db_recipe)
        return db_recipe

    def delete_recipe(self, recipe_id: int):
        """Delete a recipe from the database."""
        db_recipe = self.db.query(Recipe).filter(Recipe.id == recipe_id).first()
        if db_recipe:
            self.db.delete(db_recipe)
            self.db.commit()
        return db_recipe

    def add_ingredient(self, name: str):
        """Add an ingredient to the database."""
        db_ingredient = Ingredient(name=name)
        self.db.add(db_ingredient)
        self.db.commit()
        self.db.refresh(db_ingredient)
        return db_ingredient

    def get_ingredients(self):
        """Get all ingredients from the database."""
        return self.db.query(Ingredient).all()

    def get_ingredient(self, ingredient_id: int):
        """Get an ingredient from the database."""
        return self.db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()

    def update_ingredients(self, ingredient_id: int, name: str):
        """Update an ingredient in the database."""
        db_ingredient = self.db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
        if db_ingredient:
            db_ingredient.name = name
            self.db.commit()
            self.db.refresh(db_ingredient)
        return db_ingredient

    def delete_ingredient(self, ingredient_id: int):
        """Delete an ingredient from the database."""
        db_ingredient = self.db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
        if db_ingredient:
            self.db.delete(db_ingredient)
            self.db.commit()
        return db_ingredient

    def add_api_key(self, model: str, key: str):
        """Add an API key to the database."""
        db_api_key = APIKey(model=model, key=key)
        self.db.add(db_api_key)
        self.db.commit()
        self.db.refresh(db_api_key)
        return db_api_key

    def get_api_key(self, model: str):
        """Get an API key from the database."""
        return self.db.query(APIKey).filter(APIKey.model == model).first()
