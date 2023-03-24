"""
Aplikasi membuat modularisasi Berita terkini dari kompas TV

"""

import mostpopuler_news

if __name__ == '__main__':
    print(f"Aplikasi utama menggunakan package yang memiliki deskripsi{mostpopuler_news.description}")
    result = mostpopuler_news.data_extraction()
    mostpopuler_news.data_show(result)