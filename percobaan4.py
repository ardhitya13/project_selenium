from locust import HttpUser, between, task


class TestHalamanLogin(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:9999"

    @task
    def visit_login_form(self):
        self.client.get("/")
