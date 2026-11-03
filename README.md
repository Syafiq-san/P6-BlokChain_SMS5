# P6-BlokChain_SMS5

## Tugas 4 - Implementasi Blockchain Sederhana

## Tujuan

Program ini mempraktikkan struktur blok, fungsi hash SHA-256, proof-of-work, keterhubungan hash antarblok, dan validasi integritas blockchain.

## Isi blok

Setiap objek `Block` menyimpan `index`, `timestamp`, `data`, `previous_hash`, `hash`, dan `nonce`. Isi blok diserialisasi sebagai JSON dengan urutan kunci konsisten sebelum dihitung menggunakan SHA-256.

## Proof-of-work

Miner mencoba nilai `nonce` sampai hash blok memiliki empat karakter `0` di bagian awal. Nilai kesulitan dapat diubah saat membuat objek `Blockchain`.

## Cara menjalankan

Gunakan Python 3.10 atau yang lebih baru, lalu jalankan dari folder tugas:

```powershell
python blockchain.py
```

Program otomatis membuat genesis block dan tiga blok transaksi, lalu menampilkan detail setiap blok.

## Hasil pengujian

- Genesis block terbentuk otomatis.
- Rantai memiliki tiga blok transaksi.
- Validasi sebelum data diubah menghasilkan `True`.
- Validasi setelah data blok pertama diubah menghasilkan `False`.

Perubahan data mengubah hasil `calculate_hash()`, sehingga tidak sama dengan hash yang sebelumnya tersimpan pada blok. Karena itu validasi mendeteksi perubahan dan menolak rantai.

Untuk bukti pengumpulan, jalankan perintah di atas dan ambil screenshot terminal yang menampilkan jumlah blok serta hasil validasi sebelum dan sesudah data diubah.

## Dokumen referensi

- [Panduan Hands-on Pertemuan 6](referensi/Hands-on_Pertemuan_6_Implementasi_Blockchain_Sederhana_ITTS.pdf)
- [Lembar Tugas 4](referensi/Pertemuan_06_Tugas_4_Implementasi_Blockchain_Python.pdf)

## Batasan

Ini adalah simulasi blockchain lokal untuk pembelajaran. Program belum menerapkan jaringan peer-to-peer, tanda tangan digital, dompet, atau mekanisme konsensus untuk lingkungan produksi.
