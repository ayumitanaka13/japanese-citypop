module.exports = {
    plugins: [
        require('tailwindcss'),
        require('autoprefixer'),
        // require('@fullhuman/postcss-purgecss')({
        //     content:[
        //         'flaskr/templates/*.html',
        //         'flaskr/templates/**/*.html',
        //         'flaskr/static/js/index.js',
        //     ],
        //     defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
        // })
    ] 
}