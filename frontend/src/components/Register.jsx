import React from 'react';
import '../assets/styles/style.css';

function Register() {
  return (
    <body className={styles.cont}>
      <div class="flex flex-col items-center justify-center h-screen bg-gray-100">
        <div class="absolute top-4 left-4 rounded-full bg-yellow-500 w-8 h-8 flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-4 h-4 text-white">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </div>
        <h1 class="text-3xl font-bold text-yellow-500 mt-8 mb-4">Войдите или зарегистрируйтесь</h1>
        <p class="text-lg text-gray-500 mb-8">Чтобы пользоваться сервисом</p>
        <div class="relative w-full max-w-xs">
            <input type="text" placeholder="Email или номер телефона" class="w-full px-4 py-2 border border-gray-400 rounded-md text-gray-700 focus:outline-none focus:border-yellow-500"/>
            <span class="absolute top-2 left-4 text-gray-400 pointer-events-none">Email или номер телефона</span>
        </div>
         <button class="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded-md mt-4">Вход</button>
      </div>
    </body>
  );
}

export default Register;
