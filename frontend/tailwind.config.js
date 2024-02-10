/*eslint no-undef: "error"*/
/*eslint-env node*/
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [require("daisyui")],
  daisyui:{
    themes: [
      "dim",
      "light"
    ]
  }
}
