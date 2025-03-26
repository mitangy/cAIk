import { useState } from "react";

export default function LoginModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-8 rounded shadow-lg w-96">
        <h2 className="text-2xl font-semibold mb-4">Login</h2>
        <form>
          <div className="mb-4">
            <label className="block text-gray-700">Email</label>
            <input
              type="email"
              className="border p-2 w-full"
              placeholder="Enter your email"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Password</label>
            <input
              type="password"
              className="border p-2 w-full"
              placeholder="Enter your password"
            />
          </div>
          <div className="flex justify-end">
            <button
              type="button"
              className="bg-blue-500 text-white px-4 py-2 rounded"
              onClick={onClose}
            >
              Close
            </button>
            <button
              type="submit"
              className="bg-green-500 text-white px-4 py-2 rounded ml-2"
            >
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
