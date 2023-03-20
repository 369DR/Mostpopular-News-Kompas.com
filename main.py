"""
Aplikasi membuat modularisasi Berita terkini dari kompas TV

"""

import  beritaterkini

if __name__ == '__main__':
    print("Aplikasi utama")
    result = beritaterkini.ekstrasi_data()
    beritaterkini.tampilkan_data(result)