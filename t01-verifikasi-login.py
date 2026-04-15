from locust import HttpUser, task, between


class TestPostLogin(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:9999"

    @task
    def login(self):
        data_form = {
            "email": "admin@if.local",
            "password": "rahasia123",
        }
        response = self.client.post("/verifikasi-login", data=data_form)
        print("Status Code:", response.status_code)
