import os
import shutil

def listele_klasor(dizin):
    """
        Belirtilen dizindeki tüm dosyaları ve klasörleri listeler.

        Args:
            dizin (str): Listelenecek dizinin yolu.

        Returns:
            None: Dosyalar konsola yazdırılır.
    """
    try:
        dosyalar = os.listdir(dizin)
        print(f"{dizin} içindeki dosyalar:")
        for dosya in dosyalar:
            print(dosya)
    except FileNotFoundError:
        print("Geçersiz klasör yolu!")

def ayir_dosyalar(dizin):
    """
        Belirtilen dizindeki dosyaları türlerine göre kategorilere ayırır.

        Args:
            dizin (str): Dosyaların kategorilere ayrılacağı dizin.

        Returns:
            dict: Dosya kategorileri ve bunlara ait dosyaların listesi.
    """
    dosya_turleri = {
        "Resimler": [".jpg", ".jpeg", ".png", ".gif"],
        "Belgeler": [".pdf", ".docx", ".txt"],
        "Videolar": [".mp4", ".mkv", ".avi"],
    }
    dosyalar = os.listdir(dizin)
    kategoriler = {kategori: [] for kategori in dosya_turleri}

    for dosya in dosyalar:
        dosya_yolu = os.path.join(dizin, dosya)
        if os.path.isfile(dosya_yolu):
            uzanti = os.path.splitext(dosya)[1]
            for kategori, uzantilar in dosya_turleri.items():
                if uzanti in uzantilar:
                    kategoriler[kategori].append(dosya)
    return kategoriler

def tasima_veya_kopyalama(dizin, kategoriler, hedef_dizin):
    """
        Dosyaları belirtilen hedef dizine türlerine göre taşır veya kopyalar.

        Args:
            dizin (str): Kaynak dizin yolu.
            kategoriler (dict): Dosyaların kategorilere ayrılmış listesi.
            hedef_dizin (str): Dosyaların taşınacağı hedef dizin.

        Returns:
            None: Dosyalar belirtilen hedef dizine taşınır ve konsola işlem bilgisi yazılır.
    """
    for kategori, dosyalar in kategoriler.items():
        kategori_dizin = os.path.join(hedef_dizin, kategori)
        os.makedirs(kategori_dizin, exist_ok=True)

        for dosya in dosyalar:
            kaynak = os.path.join(dizin, dosya)
            hedef = os.path.join(kategori_dizin, dosya)
            shutil.move(kaynak, hedef)  # Taşıma işlemi
            print(f"{dosya}, {kategori_dizin} klasörüne taşındı.")

# Ana program
"""
Bu program, belirtilen bir dizindeki dosyaları türlerine göre ayırır ve 
kullanıcının seçtiği hedef bir klasöre taşır.

Kullanıcıdan:
1. Kaynak klasör yolu,
2. Hedef klasör yolu bilgileri alınır.

Dosyalar, Resimler, Belgeler ve Videolar gibi kategorilere ayrılarak hedef klasöre taşınır.
"""
klasor_yolu = input("Lütfen bir klasör yolu girin: ")
listele_klasor(klasor_yolu)

kategoriler = ayir_dosyalar(klasor_yolu)
print("Dosya Kategorileri:")
for kategori, dosyalar in kategoriler.items():
    print(f"{kategori}: {dosyalar}")

hedef_klasor = input("Dosyaların taşınacağı hedef klasör yolunu girin: ")
tasima_veya_kopyalama(klasor_yolu, kategoriler, hedef_klasor)
