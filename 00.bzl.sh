docker rmi dalpine:v1
docker build -t dalpine:v1 .

docker run --name testi dalpine:v1 sh 01.run.sh
docker rm testi


