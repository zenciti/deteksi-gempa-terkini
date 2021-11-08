def ekstraksi_data():
    """
    tanggal: 02 November 2021
    waktu: 23:43:53 WIB
    magnitudo: 6.1
    kedalaman: 123 km
    lokasi : LS= 6.93 BT=130.63
    Pusat gempa: berada di laut 123 km barat Larat,Kab. Kepulauan Tanimbar
    Dirasakan: (Skala MMI): III Saumlaki, II-III Tual
    :RETURN:
    """
    hasil = dict()
    hasil['tanggal'] = '02 November 2021'
    hasil['waktu'] = '23:43:53 WIB'
    hasil['magnitudo'] = 6.1
    hasil['kedalaman'] = '123 km'
    hasil['lokasi'] = {'ls': 6.93, 'bt': 130.63}
    hasil['pusat gempa'] ='berada di laut 123 km barat Larat,Kab. Kepulauan Tanimbar'
    hasil['dirasakan'] ='(Skala MMI): III Saumlaki, II-III Tual'

    return hasil


def tampilkan_data(result):
    print('gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS {result['lokasi']['ls']}, BT {result['lokasi']['bt']}")
    print(f"Pusat gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")

# if __name__ == '__main__':
#     print ('ini adalah package gempa terkini')