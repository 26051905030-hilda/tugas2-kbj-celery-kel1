import time
from celery_app import app

def is_armstrong(n):
    digit = str(n)
    pangkat = len(digit)
    return n == sum(int(d) ** pangkat for d in digit)

@app.task(bind=True, name="tasks.cek_armstrong",
          autoretry_for=(Exception,), retry_kwargs={"max_retries": 3, "countdown": 5})
def cek_armstrong(self, awal, akhir):
    worker = self.request.hostname
    print(f"[{worker}] Tugas diterima: cek angka {awal:,} - {akhir:,}")

    mulai = time.time()
    ditemukan = []
    for angka in range(awal, akhir + 1):
        if is_armstrong(angka):
            ditemukan.append(angka)
            print(f"[{worker}]   Ketemu: {angka}")

    durasi = time.time() - mulai
    print(f"[{worker}] Selesai dalam {durasi:.2f} detik, {len(ditemukan)} bilangan")

    return {
        "awal": awal,
        "akhir": akhir,
        "ditemukan": ditemukan,
        "worker": worker,
        "durasi": round(durasi, 2),
    }