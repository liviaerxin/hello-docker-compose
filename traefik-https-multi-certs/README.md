# Configure Traefik for HTTPS with multiple certificates in Docker Compose

Create a local **CA**

```sh
./cert.sh ca
```

Sign the certificate for the local server,

```sh
./cert.sh sign a.localhost
```

```sh
./cert.sh sign b.localhost
```

[Optional] create a default certificate:

```sh
./cert.sh sign 127.0.0.1 localhost *.localhost
```