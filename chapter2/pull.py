import os
#定义镜像名称
imagename = 'registry.cn-beijing.aliyuncs.com/djm/appdemo1:latest'
cmd_pull = 'docker pull {}'.format(imagename)

cmd_up = '/usr/local/bin/docker-compose up -d'

os.system(cmd_pull)
os.system(cmd_up)
