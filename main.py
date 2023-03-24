"""
Aplikasi membuat modularisasi Berita terkini dari kompas TV

"""

import mostpopuler_news

if __name__ == '__main__':
        print("main application")
        result = mostpopuler_news.data_extraction()
        mostpopuler_news.data_show(result)
