#阶段二：脚本简化Docker镜像部署

 1、编写代码
 
 2、构建镜像，推送镜像到镜像库 'python3 push.py'
 
 3、服务器上拉去镜像库最新镜像，重启Docker容器 'python3 pull.py'

-----------------------------------

- appdemo1 目录下是程序源码和脚本文件(push.py、Dockerfile)

- server 目录下是部署在服务器上的脚本文件(pull.py,docker-compose.yml)

