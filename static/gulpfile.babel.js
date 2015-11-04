import gulp       from 'gulp';
import browserify from 'browserify';
import babelify   from 'babelify';
import source     from 'vinyl-source-stream';
import buffer     from 'vinyl-buffer';
import sourcemaps from 'gulp-sourcemaps';

var paths = {
    test: "./test/*.js",
    src: "./js/",
    dist_src: "./build/js/"
};


gulp.task('browserify', () => {
    browserify({entries: [ paths.src + "app.js"]})
        .transform(babelify)
        .bundle()
        .on('error', function(err) {
            console.log(err.message);
            this.emit('end');
        })
        .pipe(source("bundle.js"))
        .pipe(buffer())
        .pipe(sourcemaps.init({loadMaps: true}))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(paths.dist_src));
});

gulp.task('watch', () => {
    gulp.watch( paths.src + '**/*', ['browserify'])
});

gulp.task('default', ['watch']);
