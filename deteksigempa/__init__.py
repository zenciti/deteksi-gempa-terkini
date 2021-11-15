import requests
from bs4 import BeautifulSoup


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
    try:
        content=requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span',{'class': 'waktu'})
        result = result.text.split(', ')
        waktu = result[1]
        tanggal = result[0]
        
        result = soup.find('div',{'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text

            i = i+1


        hasil = dict()
        hasil['tanggal'] = tanggal #'02 November 2021'
        hasil['waktu'] = waktu #'23:43:53 WIB'
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None



def tampilkan_data(result):
    if result is None:
        print('\ntidak bisa menemukan data gempa terkini')
        return
    print('\ngempa terakhir berdasarkan BMKG')
    print(f"\nTanggal  : {result['tanggal']}")
    print(f"Waktu    : {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"koordinat: LS {result['koordinat']['ls']}, BT {result['koordinat']['bt']}")
    print(f"lokasi   : {result['lokasi']}")
    print(f"Dirasakan: {result['dirasakan']}")

# if __name__ == '__main__':
#     print ('ini adalah package gempa terkini')