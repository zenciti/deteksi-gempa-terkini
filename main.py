"""
aplikasi deteksi gempa terkini

MODULARISASI DENGAN FUNCTION
"""
import deteksigempa

if __name__ == '__main__':
    print('\nAplikasi Utama')
    result = deteksigempa.ekstraksi_data()
    deteksigempa.tampilkan_data(result)
    

