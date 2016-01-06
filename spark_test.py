import spark_tasks
import time
import json

my_task = spark_tasks.sparktask.delay('test.txt')

ready = False
while not ready:
    ready = my_task.ready()
    print('task ready? ' + str(ready))
    time.sleep(1)

result = json.loads(my_task.get().decode())
print(result)
