# encoding=UTF-8
import csv
import datetime as dt
# menünün ve menü dosyasının oluşturulması
menufile = open("Menu.txt", "w", encoding="utf-8")
menufile.write("Lütfen Bir Pizza Tabanı Seçiniz: \n")
menufile.write("1: Klasik\n")
menufile.write("2: Margarita\n")
menufile.write("3: Sucuklu Pizza")
menufile.write("\nve seçeceğiniz sos:\n")
menufile.write("11: Zeytin\n")
menufile.write("12: Mantar\n")
menufile.write("13: Mısır\n")
menufile.write("işlem seçiniz(ürün seçmek için pizza numarasını, ardından seçtiğiniz sosu giriniz / bilgi almak için b, ardından bilgi almak istediğiniz ürünün numarasını giriniz)")
menufile.write("\nTeşekkür Ederiz!\n")
menufile.close()
menufile = open("Menu.txt", "r", encoding="utf-8")
print(menufile.read())
menufile.close()
# Pizza ana sınıfının oluşturulması
class Pizza:
    def __init__(self, isim, fiyat, aciklama):
        self.fiyat = fiyat
        self.aciklama = aciklama
        self.isim = isim

    def get_cost(self):
        return self.fiyat

    def get_desc(self):
        return f"Bu pizza, {self.aciklama} ve fiyatı {self.fiyat} TL'dir."

# pizza türleri için alt sınıflar
class Margarita(Pizza):
    def __init__(self, isim, fiyat, aciklama):
        super().__init__(isim, fiyat, aciklama)


class Klasik(Pizza):
    def __init__(self, isim, fiyat, aciklama):
        super().__init__(isim, fiyat, aciklama)


class Sucuklu(Pizza):
    def __init__(self, isim, fiyat, aciklama):
        super().__init__(isim, fiyat, aciklama)


normal_pizza = Margarita("margarita", 46, "diğer pizzalarımıza nazaran daha sade bir pizzadır")

klasik_pizza = Klasik("klasik", 50, "değişmez bir lezzete sahip, tadına doyamayacağınız bir pizzadır")

sucuklu_pizza = Sucuklu("sucuklu", 52, "sucuk severlerin bayılacağı, bol sucuklu bir pizzadır")

# soslar için ana sınıf oluşturulması
class SosveSus:
    def __init__(self, isim, fiyat, aciklama):
        self.fiyat = fiyat
        self.aciklama = aciklama
        self.isim = isim

    def get_cost(self):
        return self.fiyat

    def get_desc(self):
        return f"{self.aciklama}, fiyatı {self.fiyat} TL'dir."

# sos türleri için alt sınıflar
class Zeytin(SosveSus):
    def __init__(self, isim, fiyat, aciklama):
        super().__init__(isim, fiyat, aciklama)


class Mantar(SosveSus):
    def __init__(self, isim, fiyat, aciklama):
        super().__init__(isim, fiyat, aciklama)


class Misir(SosveSus):
    def __init__(self, isim, fiyat, aciklama):
        super().__init__(isim, fiyat, aciklama)


zeytin_ekleme = Zeytin("zeytin eklemeli", 3, "seçtiğiniz pizzaya isteğe bağlı zeytin eklenir")

mantar_ekleme = Mantar("mantar eklemeli", 6, "seçtiğiniz pizzaya isteğe bağlı mantar eklenir")

misir_ekleme = Misir("mısır eklemeli", 5, "seçtiğiniz pizzaya isteğe bağlı mısır eklenir")

sos_yok = SosveSus("sossuz", 0, "sos seçilmemiştir")
# sosların açıklamasını görüntülemeyi sağlayan menü
def aciklama_secimi():
    secim_iki = input("hakkında bilgi almak istediğiniz ürünü belirtin\
    (1/2/3/11/12/13/c(çıkış)):")
    if secim_iki == "1":
      print(normal_pizza.get_desc())
      secim()
    elif secim_iki == "2":
        print(klasik_pizza.get_desc())
        secim()
    elif secim_iki == "3":
        print(sucuklu_pizza.get_desc())
        secim()
    elif secim_iki == "11":
        print(zeytin_ekleme.get_desc())
        secim()
    elif secim_iki == "12":
        print(mantar_ekleme.get_desc())
        secim()
    elif secim_iki == "13":
        print(misir_ekleme.get_desc())
        secim()
    elif secim_iki == "c":
      print("çıkılıyor")
      secim()
    else:
      print("geçerli bir seçenek girilmedi")
      aciklama_secimi()
# taban seçim menüsü
def secim():
    taban_secim = input("işlem belirtiniz(ürünler içinden 1/2/3 veya bilgi almak için b)")
    if taban_secim == "b":
      aciklama_secimi()
    elif taban_secim == "1":
      return klasik_pizza
    elif taban_secim == "2":
      return normal_pizza
    elif taban_secim == "3":
      return sucuklu_pizza
    else:
      print("geçerli bir seçenek girilmedi")
      secim()
# sos seçim menüsü
def sos_secimi():
  sos_secim = input("istediğiniz sosu seçiniz (1(zeytin)/2(mantar)/3(mısır), sos seçmeyi geçmek için y)")
  if sos_secim == "1":
    return zeytin_ekleme
  elif sos_secim == "2":
    return mantar_ekleme
  elif sos_secim == "3":
    return misir_ekleme
  elif sos_secim == "y":
    return sos_yok
  else:
    print("geçerli bir seçenek değil")
    sos_secimi()

secilen_taban = secim()
secilen_sos = sos_secimi()
toplam_fiyat = secilen_taban.get_cost() + secilen_sos.get_cost()
# fiyatın gösterilmesi, ardından csv dosyasının oluşturulup ödeme bilgilerinin alınması ile bu verilerin dosyaya yazılması
def odeme():
  print(f"ödenecek ücret {toplam_fiyat} TL'dir")
  print("siparişinizi tamamlamak için istenen bilgileri giriniz: \n")
odeme()
suan = dt.datetime.now()
header = ["sipariş detayı", "sipariş zamanı", "TC kimlik numarası", "isim", "kart numarası", "kart şifresi"]
data = [str(secilen_taban.isim) + " " + str(secilen_sos.isim), suan.strftime("%Y-%m-%d %H:%M:%S")]
for i in header:
    if i == "sipariş detayı" or i == "sipariş zamanı":
        continue
    else:
        data.append(str(input(i + " giriniz ")))

with open("Orders_Database.csv", 'w', newline="", encoding="utf-8") as datafile:
  csvwriter = csv.writer(datafile)
  csvwriter.writerow(header)
  csvwriter.writerow(data)

def __main__():
  pass
__main__()
