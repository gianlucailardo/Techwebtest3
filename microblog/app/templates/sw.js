let cacheName = 'B&BIlSoleCache';
let filesToCache = [
    '/',
    './static/bootstrap-5.1.3-dist/css/bootstrap.min.css',
     './static/styles/StyleP.css',
     './static/styles/style.scss',
     './static/styles/style.css',
     './static/styles/form_sign.css',
     './static/styles/Desc.css',
    './static/images/bannernapoli.jpg',
    './static/images/banner-bg.jpg',
    './static/images/blog-1.jpg',
     './static/images/blog-2.jpg',
    './static/images/blog-3.jpg',
    './static/images/des-1.jpg',
    './static/images/des-2.jpg',
    './static/images/des-3.jpg',
    './static/images/des-4.jpg',
    './static/images/des-5.jpg',
    './static/images/des-6.jpg',
    './static/images/des-7.jpg',
    './static/images/des-8.jpg',
    './static/images/gallery-img-1.jpg',
    './static/images/gallery-img-2.jpg',
    './static/images/gallery-img-3.jpg',
    './static/images/gallery-img-4.jpg',
    './static/images/gallery-img-5.jpg',
    './static/images/gallery-img-6.jpg',
    './static/images/gallery-img-7.jpg',
    './static/images/gallery-img-8.jpg',
    './static/images/home-bg.jpg',
    './static/images/logo.png',
    './static/images/logosole.png',
    './static/images/pic-1.png',
    './static/images/pic-2.png',
    './static/images/pic-3.png',
    './static/images/pic-4.png',
    './static/images/stanzanapoli.png',
    './static/images/stanzanapoli1.png',
    './static/images/stanzanapoli2.png',
    './static/images/stanzanapoli3.png',
    './static/images/stanzanapoli4.png',
    './static/images/video1.mp4',
    './script.js',
    './templates/Describe1.html',
    './templates/index.html',
    './templates/login.html',
    './templates/Prenot.html',
    './templates/register.html',
    './templates/Success.html'
];
/* Start the service worker and cache all of the app's content */
self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open(cacheName).then(function(cache) {
            return cache.addAll(filesToCache);
        })
    );
});
/* Serve cached content when offline */
self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});
