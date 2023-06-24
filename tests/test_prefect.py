import prefect
from prefect import task, flow


@task
def hello_task():
    print("Hello world!")


@flow
def flow():
    hello_task()


flow()
