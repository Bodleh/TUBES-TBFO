<h1 align="center">Tugas Besar Teori Bahasa Formal dan Otomata</h1>
<h1 align="center">K02 gilaNubes</h3>
<h3 align="center">HTML Checker with Push Down Automata</p>

## Table of Contents

- [Abstraction](#abstraction)
- [Built With](#built-with)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [File Structures ](#File-Structure)
- [Links](#links)



Our Team members :
- 13522073 - Juan Alfred Wijaya
- 13522081 - Albert
- 13522111 - Ivan Hendrawan Tan


## Abstraction

Proyek ini mengembangkan sebuah alat validasi HTML berbasis Pushdown Automata (PDA) yang dirancang untuk menganalisis dan memvalidasi struktur dokumen HTML. Program ini efektif dalam mengidentifikasi kesalahan sintaks dan struktural yang umum dalam HTML, termasuk penanganan tag yang tidak ditutup, penggunaan void elements, dan kesalahan dalam struktur bersarang. Dengan memanfaatkan prinsip Last In, First Out (LIFO) dari stack, alat ini secara akurat menelusuri pembukaan dan penutupan tag, memberikan feedback yang sesuai mengenai kesesuaian dokumen HTML dengan standar yang ditetapkan. 


## Built With

- [Python](https://www.python.org/)

## Prerequisites

Untuk menjalankan proyek ini, Anda perlu melakukan beberapa instalasi, termasuk:
- `HTML5` : Ini adalah bahasa markup yang digunakan untuk mengatur struktur konten halaman web. Ini adalah bagian fundamental dari pengembangan web.
- `Python version 3` : Ini diperlukan dalam proyek ini sebagai debugger dan parser untuk tag HTML.

## Installation

Jika Anda ingin menjalankan program ini, Anda perlu melakukan langkah-langkah berikut:

1. Kloning repositori ini :
```shell
git clone https://github.com/Bodleh/TUBES-TBFO.git
```

2. Open directory :
```shell
cd  TUBES-TBFO
```

3. Jalankan program utama :
```shell
python main.py "pda.txt" "<file.html>"
```

Pastikan Anda mendefinisikan file PDA dan file HTML untuk menjalankan program ini.


## Features
- `Error Line`: Fitur ini menunjukkan di baris mana terjadi kesalahan dalam "file.html"
- `Error input`: Fitur ini menampilkan input yang salah dari "file.html"

### File-Structure

- `htmlparser.py` : File ini berisi kode untuk mengurai (parse) dokumen HTML. Fungsi utamanya adalah untuk memproses  struktur HTML menjadi token token yang akan dibaca oleh PDA.
- `main.py` :  Ini merupakan file eksekusi utama program. File ini mengkoordinasikan operasi program, termasuk memanggil parser HTML dan PDA, serta menampilkan hasilnya.
- `pdaparser.py` : File ini mengimplementasikan logika Pushdown Automata (PDA). Fungsi utamanya adalah untuk validasi struktur dokumen HTML berdasarkan aturan dan struktur yang didefinisikan dalam file PDA.
- `pda.txt` : Berisi definisi dan aturan PDA yang digunakan untuk analisis dan validasi HTML. File ini menjadi acuan bagi pdaparser.py dalam mengevaluasi dokumen HTML.
- `test1.html`, `test2.html`,`test3.html` : File-file ini adalah contoh dokumen HTML yang digunakan untuk menguji dan mendemonstrasikan fungsionalitas program. Masing-masing file berisi variasi struktur HTML yang berbeda untuk mengevaluasi kemampuan program dalam mendeteksi berbagai jenis kesalahan.

## Links
- Repository : https://github.com/Bodleh/TUBES-TBFO


### Kontributor Utama

1. Juan Alfred Widjaya / 13522073 (https://github.com/juanaw6)
2. Albert Choe / 13522081 (https://github.com/AlbertChoe)
3. Ivan Hendrawan Tan / 13522111 (https://github.com/Bodleh)
