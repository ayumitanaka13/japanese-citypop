module.exports = {
  purge: [
    'flaskr/templates/*.html',
    'flaskr/templates/**/*.html',
    'flaskr/static/js/*.js',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        lightpink: '#ff93cd',
        lightblue: '#3dbaf4'
      },
      fontFamily: {
        codystar: ['Codystar', 'cursive'],
        poppins: ['Poppins', 'sans-serif']
      },
      zIndex: {
        '-1': '-1'
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}