# Image Text Removal Project

## Deskripsi
Proyek ini adalah aplikasi Python yang dirancang untuk menghapus teks dari gambar menggunakan OpenCV, pytesseract, dan NumPy. Proyek ini menyediakan dua metode untuk menghapus teks: mengganti teks dengan warna putih dan menggunakan inpainting untuk mengisi area teks dengan warna yang sesuai dengan sekitarnya.

## Struktur Folder
|- Material [Folder] # Tempat menyimpan gambar input
|- Result [Folder] # Tempat menyimpan gambar output
|- main.py # Script utama untuk memproses gambar
|- requirements.txt # Daftar library yang diperlukan
|- README.md # Dokumentasi proyek


## Persyaratan
1. Python 3.x
2. Tesseract-OCR (harus diinstal dan ditambahkan ke PATH)

## Instalasi
1. Clone repositori ini atau unduh file-file proyek.
2. Instal library yang diperlukan menggunakan `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. Pastikan Tesseract-OCR telah diinstal dan ditambahkan ke PATH Anda. 


## Penggunaan
1. Tempatkan gambar yang ingin Anda proses di folder `Material`.
2. Jalankan script `main.py`:
```
python main.py
```
3. Gambar hasil proses akan disimpan di folder `Result`.