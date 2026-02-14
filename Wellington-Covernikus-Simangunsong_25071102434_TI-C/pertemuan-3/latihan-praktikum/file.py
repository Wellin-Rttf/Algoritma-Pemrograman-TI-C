class Vehicle:
    def __init__ (self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis

    def sound(self):
        return print("Suara")
    
    def teks(self):
        return print(f"{self.merk} adalah salah satu merk {self.jenis}")

class Mobil(Vehicle):
    def __init__ (self, jenis, merk, tahun_rilis):
        Vehicle.__init__(self, jenis, merk, tahun_rilis)
        self.__merk = merk

    def get_merk(self):
        return self.__merk

class SepedaMotor(Vehicle):
    def __init__ (self, jenis, merk, tahun_rilis):
        Vehicle.__init__(self, jenis, merk, tahun_rilis)
        self.__jenis = jenis

    def get_merk(self):
        return self.__merk
    
    def set_merk(self, merk):
        self.__merk = merk


x = Vehicle("mobil", "Toyota", 2020)
x.teks()

y = Mobil("mobil", "Honda", 2016)
print(y.get_merk())

z = SepedaMotor("motor", "Honda", 2019)
z.set_merk(1991)
print(z.get_merk())

