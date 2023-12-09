FROM python:3.11

# 创建 app 文件夹
RUN mkdir /opt/app
WORKDIR /opt/app
COPY . .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

#EXPOSE 8080
#设置环境变量
#ENV SPIDER=/my_blog