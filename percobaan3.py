from locust import HttpUser, SequentialTaskSet, task, between


class MyTaskSet(SequentialTaskSet):
    @task
    def method1(self):
        print("Fitur method 1")

    @task
    def method2(self):
        print("Fitur method 2")

    @task
    def method3(self):
        print("Fitur method 3")


class UserWebflask(HttpUser):
    tasks = [MyTaskSet]
    host = "http://localhost:9999"
    wait_time = between(1, 3)
