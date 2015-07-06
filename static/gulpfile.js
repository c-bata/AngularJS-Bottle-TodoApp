var gulp       = require('gulp');
var browserify = require('browserify');
var source     = require('vinyl-source-stream');

var paths = {
    test: "./test/*.js",
    src: "./js/",
    dist_src: "./build/js/"
};


gulp.task('browserify', function() {
    browserify({entries: ["./js/app.js"]})
        .bundle()
        .on('error', function(err) {
            console.log(err.message);
            this.emit('end');
        })
        .pipe(source("bundle.js"))
        .pipe(gulp.dest(paths.dist_src));
});

gulp.task('watch', function() {
    gulp.watch('./js/**/*', ['browserify'])
});

gulp.task('default', ['watch']);