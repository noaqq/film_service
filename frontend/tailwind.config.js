/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        "main-bg":
          "background-image: linear-gradient(to bottom, rgb(31, 31, 31),rgb(13, 13, 13)",
      },
    },
  },
  plugins: [],
};
