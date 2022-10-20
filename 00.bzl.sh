regurl=ghcr.io/ivanaxu/dalpine
ver=v1

# export CR_PAT=
echo $CR_PAT | docker login ghcr.io -u IvanaXu --password-stdin

docker rmi $regurl:$ver
docker build -t $regurl:$ver .

docker run --name testi $regurl:$ver sh 01.run.sh
docker rm testi

docker push $regurl:$ver

