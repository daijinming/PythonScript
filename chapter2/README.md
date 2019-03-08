在命令行输入 `crontab -e` 开始编辑自动执行脚本


输入如下内容，每15分钟执行一次更新
~~~
15,30,45,59 * * * * sh /root/codebase/appdemo1/autopull.sh >> /root/codebase/appdemo1/cron.log 2>&1
~~~
