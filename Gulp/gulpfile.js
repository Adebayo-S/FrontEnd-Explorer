/* ---------- SASS ----------------*/

const gulp = require("gulp"); //npm init; npm install --save-dev gulp
const sass = require("gulp-sass")(require('sass')); //npm install gulp-sass; npm install --save-dev sass
const autoprefixer = require("gulp-autoprefixer"); //npm install --save-dev gulp-autoprefixer
const browserSync = require("browser-sync").create(); //npm install browser-sync

gulp.task("styles", async function() {
    gulp.src("sass/**/*.scss")
        .pipe(sass().on("error", sass.logError))
        .pipe(autoprefixer({})) //browsers option removed and used in package.json
        .pipe(gulp.dest("./css"))
        .pipe(browserSync.stream()); //reloads the browser
})

gulp.task("default", gulp.series("styles", async function() {
    gulp.watch("sass/**/*.scss", gulp.series("styles"));
    browserSync.init({
        server: "./"
    });   //starts the server
}));




