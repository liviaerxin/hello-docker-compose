# Docker Compose for Development and Production

If you want to deploy your **Docker Compose** application (locally in development) on a single server (remotely) for production, you can work with the multiple Compose fils to achieve.

A common **workflow** for deploying an container-orchestrated application from development to production is like:

1. Build the Docker production-ready images for each service.
    - Like `Dockerfile.dev` for **development**, `Dockerfile` for **production**
    - On a CI/CD server, or a local server  
2. Upload these images to the remote server.
    - Use a registry
        - push the images to the registry
        - pull the images on the server
    - Copy/Paste
        - save the images in a file
        - zip the file
        - upload the file to the remote server
        - on the server, unzip and load
3. Use an **Orchestrator** to run for **production**. If you use **Docker Compose** as the **Orchestrator**, changing the configuration as:
    - Running services on `image` not `build`, as:
        - `image` option for `production` environment
        - `build` option for `development` or `testing` environment
    - Removing any volume bindings for application code
    - Binding to different ports on the host
    - Setting environment variables differently, such as:
        - Reducing the verbosity of logging
        - To specify settings for external services such as an email server
    - Specifying a restart policy like restart: always to avoid downtime
    - Adding extra services such as:
        - Log aggregator
        - Performance Monitor

## Local Development

```sh
docker compose up
```

This equals the following:

```sh
docker compose --env-file .env -f compose.yml -f compose.override.yml up
```

## Deploy For Production

1. Build production-release images in local or CI/CD

```sh
docker compose --env-file .env.prod -f compose.yml build
```

2. Run on your remote production server

```sh
docker compose --env-file .env.prod -f compose.yml -f compose.prod.yml up
```

## Other Useful Commands

Dry up running the configuration, (Parse, resolve and render compose file in canonical format)

```sh
docker compose config
docker compose -f compose.yml -f compose.prod.yml config
```

## Resources

https://docs.docker.com/compose/multiple-compose-files/merge/#example

https://stackoverflow.com/questions/64629559/how-to-deploy-a-docker-app-to-production-without-using-docker-compose

https://stackoverflow.com/questions/42170124/docker-compose-when-to-use-image-over-build

https://docs.docker.com/compose/compose-file/13-merge/#reset-value