import os
#定义镜像名称
imagename = 'registry.cn-beijing.aliyuncs.com/djm/appdemo1:latest'
cmd_pull = 'docker pull {}'.format(imagename)
cmd_down = 'docker-compose down'
cmd_up = 'docker-compose up'

os.system(cmd_pull)
os.system(cmd_down)
os.system(cmd_up)

