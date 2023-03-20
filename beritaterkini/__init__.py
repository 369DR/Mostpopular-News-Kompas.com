
import beritaterkini


def ekstrasi_data():
    """
    A
    Istri Pamer Harta, Ini Alasan LHKPN Pejabat Kemensetneg Esha Rahmansah Tak Bisa Ditelusuri
    Dibaca 22.974 kali
    B
    Isak Tangis Iringi Jenazah Syabda Perkasa Belawa dan Ibunya Saat Tiba di Rumah Duka
    Dibaca 15.648 kali
    C
    Viral, Foto Istrinya Pamer Tas Mewah Hermes dan Gucci, Sekda Riau: Itu KW, Belinya di Mangga Dua
    Dibaca 15.375 kali
    D
    Kronologi Syabda Perkasa Belawa Meninggal Kecelakaan, Pahlawan Piala Thomas Berpulang...
    Dibaca 14.137 kali
    E
    Kabar Duka, Tunggal Putra Indonesia Syabda Perkasa Belawa Meninggal Dunia
    Dibaca 13.526 kali
    F
    Luhut ke IMF: Kalian Jangan Macam-macam...
    Dibaca 13.431 kali
    G
    Saat "Netizen" Bantu KPK Bongkar Pejabat yang Pamer Harta...
    Dibaca 8.932 kali
    H
    Sempat Terbengkalai di Bandara YIA, 38 Calon Jemaah Umrah Asal Rembang Pulang,
    Seorang Perantara Dilaporkan sebagai Penipu
    Dibaca 8.370 kali
    I
    Kala Megawati Semprot Ribuan Kades yang Minta Anggaran Jumbo...
    Dibaca 7.712 kali
    J
    Kapolda Jateng Resmi Pecat 5 Polisi yang Jadi Calo Penerimaan Bintara Polri 2022
    Dibaca 7.358 kali
    :return:
    """

    hasil = dict()
    hasil["A"] = "Berita A"
    hasil["B"] = "Berita B"
    hasil["C"] = "Berita C"
    hasil["D"] = "Berita D"
    hasil["E"] = "Berita E"
    hasil["F"] = "Berita F"
    hasil["G"] = "Berita G"
    hasil["H"] = "Berita H"
    hasil["I"] = "Berita I"
    hasil["J"] = "Berita J"

    return hasil


def tampilkan_data(result):
    print("Berita terkini berdasarkan media Kompas.com")
    print(f"1. {result['A']}")
    print(f"2. {result['B']}")
    print(f"3. {result['C']}")
    print(f"4. {result['D']}")
    print(f"5. {result['E']}")
    print(f"6. {result['F']}")
    print(f"7. {result['G']}")
    print(f"8. {result['H']}")
    print(f"9. {result['I']}")
    print(f"10. {result['J']}")


if __name__ == '__main__':
    print("Aplikasi utama")
    result = beritaterkini.ekstrasi_data()
    beritaterkini.tampilkan_data(result)
