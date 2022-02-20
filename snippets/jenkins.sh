  docker run --name jenkins-blueocean \
  --detach \
  --network jenkins \
  --network-alias jenkins \
  --privileged \
  --shm-size="2g" \
  --restart unless-stopped \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 9090:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume docker-certs:/certs/client:ro \
  --volume "$HOME":/home \
  myjenkins-blueocean:2.319.3-1
