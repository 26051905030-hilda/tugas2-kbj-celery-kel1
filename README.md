# Tugas 2 Jaringan Komputer - Distributed Systems (Celery & RabbitMQ)

Repositori ini berisi kode implementasi tugas sistem terdistribusi menggunakan Celery dan RabbitMQ CloudAMQP untuk pencarian bilangan Armstrong secara paralel.

## Anggota Kelompok 1
* Achmad Zakariyah — NIM 26051905010
* Hilda Bernika (26051905030)

## Daftar File
* `celery_app.py`: Konfigurasi koneksi broker (CloudAMQP).
* `tasks.py`: Logika fungsi task `cek_armstrong`.
* `producer.py`: Skrip pengirim tugas dan penampil rekapitulasi hasil.
