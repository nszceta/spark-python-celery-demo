import subprocess
from celery import Celery
import json
app = Celery('tasks', backend='redis://127.0.0.1/0', broker='amqp://api:api@localhost//')

@app.task
def sparktask(logfile):
    proc = subprocess.Popen('spark-submit spark_work.py test.txt --master spark://abc123.local:7077/'.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    my_stdout, my_stderr = proc.communicate()
    print('stdout ' + '~' * 60)
    print(my_stdout)
    #print('stderr ' + '~' * 200)
    #print(my_stderr)
    return my_stdout if my_stdout else None
