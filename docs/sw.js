var CACHE='sinfon-v2';
var MODEL='https://huggingface.co/neural-architect-dev/sinfon-model/resolve/main/u2net.onnx';

self.addEventListener('install',function(e){self.skipWaiting()});
self.addEventListener('activate',function(e){
  e.waitUntil(caches.keys().then(function(n){return Promise.all(n.filter(function(k){return k!==CACHE}).map(function(k){return caches.delete(k)}))}).then(function(){return self.clients.claim()}));
});
self.addEventListener('fetch',function(e){
  if(e.request.url.indexOf('huggingface')>-1||e.request.url.indexOf('u2net')>-1){
    e.respondWith(caches.open(CACHE).then(function(c){
      return c.match(e.request).then(function(r){
        if(r)return r;
        return fetch(e.request).then(function(resp){
          if(resp.ok)c.put(e.request,resp.clone());
          return resp;
        });
      });
    }));
  }
});