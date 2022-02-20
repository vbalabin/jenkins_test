docker run \
  --name selenoid-d \
  --detach \
  --restart unless-stopped \
  --network jenkins \
  --network-alias selenoid\
  --shm-size="2g" \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 4444:4444 \
  --volume selenoid-data:/root \
  --volume docker-certs:/certs/client:ro \
  --volume $PWD/config:/etc/selenoid \
  --volume $PWD/logs:/etc/logs \
  --env OVERRIDE_HOME=/root \
  aerokube/selenoid:1.10.7 \
  -conf /etc/selenoid/browsers.json \
  -log-output-dir /etc/logs \
  -session-delete-timeout 2m \
  -service-startup-timeout 1m
  
