# Assessment untuk apply Program Magang Bersertifikat Kampus Merdeka - Studycle

## Sekilas
- Program sorting digunakan algoritma Bubble Sort, dibandingkan dengan penggunaan fungsi sort() secara langsung
- Input dan output dilakukan melalui CLI / CMD / Terminal
- Digunakan argument parser sebagai metode penerimaan input
- Digunakan bahasa pemrograman Python

## Instalasi
```bash
# Clone this repository
$ git clone https://github.com/amirhsn/studycle__assessment.git
```
## Cara Penggunaan
- Pastikan terinstall Python 3.+
- Buka Terminal PC
- Arahkan directory ke root dir dimana file `main.py` berada
- Perintah memulai dan melakukan operasi program seperti berikut
```bash
$ python main.py [argument] [value]
```
- `argument` dan `value` adalah sebagai berikut

| Argumen       |   Description |
| ------------- | ------------- |
| argument      | Argumen untuk melakukan perintah pada program. Hanya tersedia `-i` untuk memasukkan data input                           |
| value     | Deretan angka yang akan diproses dengan separator berupa spasi        |

## Contoh Penggunaan
- Input
```bash
$ python main.py -i 2 5 2 3 11 9 -2 -3  
```
- Output
```bash
##############################
Data asli             = [2, 5, 2, 3, 11, 9, -2, -3]
Jumlah data           = 8
##############################

Data hasil sorting    = [-3, -2, 2, 2, 3, 5, 9, 11]
Nilai rata-rata       = 3.375
Nilai tengah          = 2.5
Nilai hasil perkalian = 35640 
```

## Limitasi
- Ketika error terjadi, sudah menampilkan pesan error sebagaimana mestinya, tetapi belum bisa menjalankan ulang program untuk mulai dari input lagi secara otomatis
- Masih hanya terdapat 1 argumen saja yaitu `-i` untuk melakukan seluruh operasi (sorting, mean, median, dan hasil kali). Baiknya bisa digunakan lebih banyak argumen seperti `-mean` yang nantinya hanya akan menampilkan nilai mean saja.
