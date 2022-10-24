# Base Images
## 从天池基础镜像构建
FROM alpine:3.16

## 把当前文件夹里的文件构建到镜像的根目录下
ADD . /

## 指定默认工作目录为根目录（需要把run.sh和生成的结果文件都放在该文件夹下，提交后才能运行）
WORKDIR /

## 在构建镜像时安装依赖包
RUN apk add --no-cache python3 python3-dev py-pip build-base gfortran cmake openblas-dev && pip3 install --no-cache-dir -i https://pypi.org/simple -r requirements.txt && apk del build-base gfortran cmake 

## 镜像启动后统一执行 sh run.sh
CMD ["sh", "run.sh"]

