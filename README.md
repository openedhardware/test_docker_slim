# test_docker_slim
DockerSlim testing app

## Build docker image

```shell script
docker build -t ts .
```

## Slimify

```shell script
docker-slim build --http-probe=false --include-path /usr/local/lib/python3.7/site-packages/certifi --show-clogs ts
```

## Test to see what happens

```shell script
docker run --privileged -v /data:/data --rm --network host ts.slim
```
