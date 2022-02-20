docker run \
  --name selenoid-d-ui \
  --detach \
  --restart unless-stopped \
  --network jenkins \
  --network-alias selenoid-ui\
  --publish 8088:8080 \
  aerokube/selenoid-ui \
  --selenoid-uri http://selenoid:4444
  
