# Panduan Cepat P05 (Pytest + Selenium)

## 1) Persiapan awal
1. Jalankan Apache dan MySQL (XAMPP/Laragon).
2. Pastikan database `dbpolibatam` sudah di-import dari `dbpolibatam.sql`.
3. Buka terminal di folder project:
   ```powershell
   cd C:\xampp\htdocs\pengujian_perangkat_lunak\project_selenium
   ```
4. Install dependency:
   ```powershell
   pip install flask pymysql requests selenium pytest
   ```

## 2) Jalankan aplikasi Flask
1. Dari folder project, jalankan:
   ```powershell
   python app.py
   ```
2. Pastikan web bisa diakses di `http://127.0.0.1:9999`.

## 3) Jalankan seluruh pengujian
1. Buka terminal baru.
2. Masuk ke folder testing:
   ```powershell
   cd C:\xampp\htdocs\pengujian_perangkat_lunak\project_selenium\testing
   ```
3. Jalankan:
   ```powershell
   pytest -v
   ```

## 4) File test yang sudah disiapkan
- `test_01_uji_login.py`
- `test_02_tambah_mhs.py`
- `test_03_ubah_mhs.py`
- `test_04_hapus_mhs.py`
- `test_05_uji_tambah_matkul.py`
- `test_06_uji_ubah_matkul.py`
- `test_07_uji_hapus_matkul.py`
- `test_08_joke.py`
- `test_09_tentang.py`

## 5) Bagian screenshot untuk laporan
1. Screenshot terminal saat `python app.py` berhasil jalan (muncul running on `127.0.0.1:9999`).
2. Screenshot terminal hasil `pytest -v` (bagian daftar test dan status `PASSED`/`FAILED`).
3. Screenshot folder `testing/screenshots` (bukti gambar otomatis dari Selenium).
4. Jika dosen minta hasil per fitur, pakai file screenshot otomatis ini:
   - `test_05_tambah_matkul_*.png`
   - `test_06_ubah_matkul_*.png`
   - `test_07_hapus_matkul_*.png`
   - `test_08_joke_*.png`
   - `test_09_tentang_*.png`

## 6) Catatan penting
- Jangan tutup terminal `python app.py` saat menjalankan `pytest`.
- Jika Chrome tidak terbuka, update Chrome dan Selenium:
  ```powershell
  pip install --upgrade selenium
  ```
