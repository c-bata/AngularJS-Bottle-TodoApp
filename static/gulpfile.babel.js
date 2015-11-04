import gulp       from 'gulp';
import browserify from 'browserify';
import source     from 'vinyl-source-stream';

var paths = {
    test: "./test/*.js",
    src: "./js/",
    dist_src: "./build/js/"
};


gulp.task('browserify', () => {
    browserify({entries: ["./js/app.js"]})
        .bundle()
        .on('error', function(err) {
            console.log(err.message);
            this.emit('end');
        })
        .pipe(source("bundle.js"))
        .pipe(gulp.dest(paths.dist_src));
});

gulp.task('watch', () => {
    gulp.watch('./js/**/*', ['browserify'])
});

gulp.task('default', ['watch']);