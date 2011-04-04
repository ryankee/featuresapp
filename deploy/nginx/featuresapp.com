proxy_cache_path /var/www/featuresapp-cache levels=1:2 keys_zone=featuresapp-cache:8m max_size=1000m inactive=600m;

server {
    server_name featuresapp.com;
    access_log /var/log/nginx/featuresapp.log;

    location /demo/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_pass_header Set-Cookie;

        proxy_cache_key $cookie_sessionid:$request_uri;
        proxy_cache featuresapp-cache;
        proxy_cache_valid 200 302 5m;
        proxy_cache_valid 400 1m;
    }

    location / {
        rewrite ^ http://github.com/bytecollective/featuresapp permanent;
    }
}
