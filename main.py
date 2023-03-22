"""
Aplikasi membuat modularisasi Berita terkini dari kompas TV

"""

import  beritaterpopuler

if __name__ == '__main__':
    print(f"Aplikasi utama menggunakan package yang memiliki deskripsi{beritaterpopuler.description}")
    result = beritaterpopuler.ekstrasi_data()
    beritaterpopuler.tampilkan_data(result)