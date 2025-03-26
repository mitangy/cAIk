"use client";
import { useState } from "react";
import LoginModal from "../components/LoginModal";

export default function Home() {
  const [ingredients, setIngredients] = useState([
    { name: "Tomato", quantity: 2, expiration: "2025-03-28" },
    { name: "Cheese", quantity: 1, expiration: "2025-03-30" },
  ]);
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);

  const handleRemoveIngredient = (index) => {
    const newIngredients = [...ingredients];
    newIngredients.splice(index, 1);
    setIngredients(newIngredients);
  };

  const handleQuantityChange = (index, quantity) => {
    const newIngredients = [...ingredients];
    newIngredients[index].quantity = quantity;
    setIngredients(newIngredients);
  };

  const toggleLoginModal = () => {
    setIsLoginModalOpen(!isLoginModalOpen);
  };

  return (
    <div className="container mx-auto p-4">
      <header className="flex justify-between items-center py-4">
        <h1 className="text-4xl font-bold">cAIk</h1>
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded"
          onClick={toggleLoginModal}
        >
          Login
        </button>
      </header>

      <main>
        <section className="my-8">
          <h2 className="text-2xl font-semibold">What would you like to make today?</h2>
          <input
            type="text"
            placeholder="Type a dish..."
            className="border p-2 w-full my-2"
          />
          <div className="flex space-x-4 my-4">
            <div>
              <label>Prep-time:</label>
              <select className="border p-2">
                <option>15 minutes</option>
                <option>30 minutes</option>
                <option>45 minutes</option>
                <option>1 hour+</option>
              </select>
            </div>
            <div>
              <label>Skill level:</label>
              <select className="border p-2">
                <option>Beginner</option>
                <option>Intermediate</option>
                <option>Advanced</option>
              </select>
            </div>
            <div>
              <label>Dietary Restrictions:</label>
              <div>
                <label>
                  <input type="radio" name="diet" value="none" /> None
                </label>
                <label>
                  <input type="radio" name="diet" value="vegetarian" /> Vegetarian
                </label>
                <label>
                  <input type="radio" name="diet" value="vegan" /> Vegan
                </label>
                <label>
                  <input type="radio" name="diet" value="gluten-free" /> Gluten-Free
                </label>
              </div>
            </div>
          </div>
          <div>
            <label>Ingredients to use:</label>
            <input
              type="text"
              placeholder="Type ingredients..."
              className="border p-2 w-full my-2"
            />
          </div>
        </section>

        <section className="my-8">
          <h2 className="text-2xl font-semibold">Trending Recipes</h2>
          <div className="flex space-x-4 overflow-x-auto">
            {/* Example recipe tiles */}
            <div className="border p-4 w-64">
              <h3 className="font-semibold">Recipe 1</h3>
              <p>Summary of recipe 1...</p>
            </div>
            <div className="border p-4 w-64">
              <h3 className="font-semibold">Recipe 2</h3>
              <p>Summary of recipe 2...</p>
            </div>
            {/* Add more recipe tiles as needed */}
          </div>
        </section>

        <section className="my-8">
          <h2 className="text-2xl font-semibold">Your Ingredients</h2>
          <ul>
            {ingredients.map((ingredient, index) => (
              <li key={index} className="flex justify-between items-center my-2">
                <div>
                  <span>{ingredient.name}</span>
                  <span> (Expires: {ingredient.expiration})</span>
                </div>
                <div>
                  <input
                    type="number"
                    value={ingredient.quantity}
                    onChange={(e) =>
                      handleQuantityChange(index, parseInt(e.target.value))
                    }
                    className="border p-1 w-16"
                  />
                  <button
                    onClick={() => handleRemoveIngredient(index)}
                    className="bg-red-500 text-white px-2 py-1 ml-2 rounded"
                  >
                    Remove
                  </button>
                </div>
              </li>
            ))}
          </ul>
        </section>
      </main>

      <LoginModal isOpen={isLoginModalOpen} onClose={toggleLoginModal} />
    </div>
  );
}
