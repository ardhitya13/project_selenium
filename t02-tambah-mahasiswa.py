from locust import HttpUser, SequentialTaskSet, task, between


class TestTambahMahasiswa(SequentialTaskSet):
    wait_time = between(1, 3)
    host = "http://localhost:9999"

    def on_start(self):
        self.login()

    def login(self):
        credentials = {
            "email": "admin@if.local",
            "password": "rahasia123",
        }

        response = self.client.post("/verifikasi-login", data=credentials)
        if response.status_code == 200:
            print("Login berhasil!")
        else:
            print("Login gagal!")

    @task
    def add_student(self):
        student_data = {
            "nim": "123456789",
            "nama_lengkap": "Fulaninho",
            "alamat": "Batu Aji Ujung",
        }
        response = self.client.post("/mahasiswa/tambah", data=student_data)
        if response.status_code == 200:
            print("Data mahasiswa SUKSES diinput!")
        else:
            print("Data mahasiswa GAGAL diinput!")


class UserWebFlask(HttpUser):
    tasks = [TestTambahMahasiswa]
    host = "http://localhost:9999"
    wait_time = between(1, 3)
