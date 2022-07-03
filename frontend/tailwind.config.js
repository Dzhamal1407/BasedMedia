module.exports = {
  purge: [
      "./src/pages/**/*.{js,ts,jsx,tsx}",
      "./src/components/**/*.{js,ts,jsx,tsx}",
  ],
  content: [],
  theme: {
    screens: {
      'modal': '400px'
    },
    extend: {},
  },
  plugins: [],
}
