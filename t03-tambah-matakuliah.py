from time import time

from locust import HttpUser, SequentialTaskSet, between, task


class TestTambahMatakuliah(SequentialTaskSet):
    wait_time = between(1, 3)
    host = "http://localhost:9999"

    def on_start(self):
        credentials = {
            "email": "admin@if.local",
            "password": "rahasia123",
        }
        self.client.post(
            "/verifikasi-login",
            data=credentials,
            name="/verifikasi-login",
            allow_redirects=False,
        )

    @task
    def add_course(self):
        suffix = str(int(time() * 1000))
        payload = {
            "course_name": f"Load Test {suffix}",
            "sks": "3",
            "description": "Data uji load testing otomatis",
        }
        # Flask route me-redirect setelah insert; 302 dianggap sukses untuk operasi create.
        self.client.post("/courses/add", data=payload, name="/courses/add", allow_redirects=False)


class UserWebFlask(HttpUser):
    tasks = [TestTambahMatakuliah]
    host = "http://localhost:9999"
    wait_time = between(1, 3)
