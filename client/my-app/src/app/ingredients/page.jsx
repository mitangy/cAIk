"use client";
import React, { useEffect, useState } from 'react';

const IngredientsPage = () => {
    const [ingredients, setIngredients] = useState([]);

    useEffect(() => {
        fetch('http://localhost:3000/get_ingredients')
            .then(response => response.json())
            .then(data => setIngredients(data))
            .catch(error => console.error('Error fetching ingredients:', error));
    }, []);

    return (
        <div>
            <h1>Ingredients</h1>
            <ul>
                {ingredients.map((ingredient, index) => (
                    <li key={index}>{ingredient.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default IngredientsPage;
