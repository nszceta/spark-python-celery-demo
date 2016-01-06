import subprocess
from celery import Celery
import json
import os

app = Celery('tasks', backend='redis://127.0.0.1/0', broker='amqp://api:api@localhost//')

@app.task
def sparktask(logfile):
    env = os.environ.copy()
    env['PYSPARK_PYTHON'] = '/Users/adam/semanticmd/api/venv/bin/python'
    proc = subprocess.Popen('spark-submit spark_work.py test.txt --master spark://abc123.local:7077/'.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    my_stdout, my_stderr = proc.communicate()

    # eagerly detect a json-like response and return it
    for line in my_stdout.split(b'\n'):
        print(line)
        if line.startswith(b'{'):
            return line
