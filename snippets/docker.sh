docker run \
  --name selenoid-docker \
  --detach \
  --privileged \
  --restart unless-stopped \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --volume lib-docker:/var/lib/docker \
  --publish 3000:3000 \
  --publish 2376:2376 \
  docker:dind \
  --storage-driver overlay2 \
  