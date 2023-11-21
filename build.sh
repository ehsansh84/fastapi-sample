docker stop  || true
docker rm hulo || true
docker rmi hulo || true
docker build -t hulo .
docker run --name hulo -p 8000:8000 -d --restart always hulo
