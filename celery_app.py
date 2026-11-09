from celery import Celery
from kombu import Exchange, Queue

# Masukkan URL CloudAMQP milikmu di bawah ini:
URL_CLOUDAMQP = "amqps://oyjvpmwz:Q2udjNd7K2YQanoFjq7TWrCPqDb2_pgf@armadillo.rmq.cloudamqp.com/oyjvpmwz"

app = Celery(
    "armstrong",
    broker=URL_CLOUDAMQP,
    backend="rpc://",
    include=["tasks"],
)

app.conf.update(
    task_queues=[
        Queue("armstrong", Exchange("armstrong", type="direct"), routing_key="armstrong"),
    ],
    task_routes={"tasks.cek_armstrong": {"queue": "armstrong"}},
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    worker_prefetch_multiplier=1,
    task_acks_late=True,
    timezone="Asia/Jakarta",
    enable_utc=True,
)