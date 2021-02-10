# test_docker_slim
DockerSlim testing app

## Build docker image

```shell script
docker build -t ts .
```

## Test original image
```shell script
docker run -v /data:/data --rm --network host -e MODEL='ssd_mobilenet_v1_coco_2018_01_28' ts
```

## Slimify

```shell script
docker-slim build --http-probe=false --mount /data:/data --include-path /usr/local/lib/python3.7/site-packages/certifi --show-clogs ts
```

## Test to see what happens with the slim result image

```shell script
docker run -v /data:/data --rm --network host -e MODEL='ssd_mobilenet_v1_coco_2018_01_28' ts.slim
```
