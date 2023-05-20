/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
    "./src/**/*.{ js, jsx, ts, tsx, html }",
    "./src/*.{ js, jsx, ts, tsx }",
    "./public/*.{ html }",
    "./*.{ js, jsx, ts, tsx, html }",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
