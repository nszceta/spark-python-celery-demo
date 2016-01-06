# spark-python-celery-demo
Apache Spark Python 3 Async Results with Celery

# Installation

Install Apache Spark 1.6 and ensure the spark-submit binary is in your $PATH
Adjust the RabbitMQ and Redis broker URLs to suit your local configuration

`pip install -U celery redis`

# Running

Start the Celery worker:

```
# in one terminal run this
celery -A spark_tasks worker

# in another terminal run this
python3 spark_test.py
```
