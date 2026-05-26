var CACHE_NAME='sinfon-v1';
var URLS=[
  './',
  './index.html',
  './before.jpg',
  './after.jpg',
  './u2netp.onnx'
];
self.addEventListener('install',function(e){
  e.waitUntil(caches.open(CACHE_NAME).then(function(c){return c.addAll(URLS)}));
});
self.addEventListener('fetch',function(e){
  e.respondWith(
    caches.match(e.request).then(function(r){
      return r || fetch(e.request).then(function(resp){
        if(resp.ok && e.request.url.indexOf('huggingface')>-1){
          var clone=resp.clone();
          caches.open(CACHE_NAME).then(function(c){c.put(e.request,clone)});
        }
        return resp;
      });
    })
  );
});