# Traefik HTTP Routing Example in Docker

1. Redirection from `http://xxx.com` to `http://xxx.com/foo`
2. Routing different path to different services, with a middleware **strip-prefix**
3. Specifying more than one router and service per container