"""
Aplikasi membuat modularisasi Berita terkini dari kompas TV

"""

import  beritaterpopuler

if __name__ == '__main__':
    print("Aplikasi utama")
    result = beritaterpopuler.ekstrasi_data()
    beritaterpopuler.tampilkan_data(result)