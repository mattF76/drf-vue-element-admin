#!/bin/bash
# 从第一行到最后一行分别表示：
# 1. 守护进程执行 celery，没有这个需求的小伙伴可以将第一行命令其删除
# 2. 收集静态文件到根目录，
# 3. 生成数据库可执行文件，
# 4. 根据数据库可执行文件来修改数据库
# 5. 用 gunicorn 启动 django 服务
#celery multi start w1 -A celery_tasks.tasks worker -l info&&
python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
gunicorn mattAdmin.wsgi:application -c gunicorn.conf