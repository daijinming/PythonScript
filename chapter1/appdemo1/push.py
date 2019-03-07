import os
#定义镜像名称
imagename = 'djm/appdemo1'
registry_username = input("输入镜像库帐号：")
registry_password = input("输入镜像库密码: ")
#构建镜像

cmd_build = 'docker build -t {} .'.format(imagename)
os.system(cmd_build)

#开始推送镜像
cmd_login = 'docker login --username={} --password={} registry.cn-beijing.aliyuncs.com'.format(registry_username,registry_password)
cmd_tag = 'docker tag {}:latest registry.cn-beijing.aliyuncs.com/{}:latest'.format(imagename,imagename)
cmd_push = 'docker push registry.cn-beijing.aliyuncs.com/{}:latest'.format(imagename)

os.system(cmd_login)
os.system(cmd_tag)
os.system(cmd_push)
