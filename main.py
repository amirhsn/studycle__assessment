import argparse
import sys

#Argument parser untuk dapat parse nilai langsung di CLI
parser = argparse.ArgumentParser(description='Mencari hasil sorting, mean, median dan hasil kali')
parser.add_argument('-i', '--input', action='store', type=int, dest='alist', nargs='*', help='Masukkan angka yang mau diproses, cukup pisahkan dengan 1 spasi')

try:
  args = parser.parse_args()
except:
  print('\n!!!!\n\nHarap masukkan input data dengan benar dan silahkan coba lagi.\n\n!!!!\n\n--help untuk bantuan')
  sys.exit()

input = args.alist

#Fungsi untuk sorting data input 
def sorting(data):
  #Sorting menggunakan bubble sort (metode yg sama dengan fungsi .sort())
  global sortedNum
  sortedNum = data
  #Perulangan awal untuk bubble sort
  for p in range(len(data)):
    #Perulangan kedua untuk membandingkan nilai saat ini dan sesudah
    for i in range(len(data)):
      if i == len(data)-1:  #Bila indeks sudah sampai ke terakhir
        break #Keluar loop kedua
      else: 
        if sortedNum[i] > sortedNum[i+1]: #Bila nilai saat ini > sesudah
          bowl = sortedNum[i]             #Variabel menyimpan nilai saat ini
          sortedNum[i] = sortedNum[i+1]   #Tukar
          sortedNum[i+1] = bowl           #Tukar
        else:
          continue                        #Lanjut loop
  return sortedNum          

#fungsi untuk mencari mean / rata2
def findMean(data):
  global mean
  mean = 0
  for i in data:
    mean = mean+i                         #Jumlahkan seluruh nilai
  mean = mean / (len(data))               #Bagi dengan frekuensi data
  return mean
     
#Fungsi untuk mencari nilai tengah
def findMedian(data):
  global median
  #Gunakan fungsi sorting terlebih dahulu
  sortedNum = sorting(data)
  dataLength = len(sortedNum)
  
  if (dataLength % 2) == 0:               #Jika modulus 2 == 0 (genap)
    median = (sortedNum[int(dataLength/2)] + sortedNum[int(dataLength/2)-1]) / 2
  else:                                   #Jika modulus 2 != 0 (ganjil)
    median = sortedNum[int((dataLength/2)-0.5)]
  return median

#Fungsi mencari hasil perkalian semua bilangan
def findMultiplied(data):
  global multiplied
  multiplied = 1                          #Nilai awal variabel adalah 1
  for i in data:
    multiplied = multiplied * i           #Kali dengan setiap elemen di data
  return multiplied

print('\n##############################')
print(f'Data asli             = {input}')
print(f'Jumlah data           = {len(input)}')
print('##############################\n')
print(f'Data hasil sorting    = {sorting(input)}')
print(f'Nilai rata-rata       = {findMean(input)}')
print(f'Nilai tengah          = {findMedian(input)}')
print(f'Nilai hasil perkalian = {findMultiplied(input)}')