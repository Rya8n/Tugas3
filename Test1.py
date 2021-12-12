year = int(input())
tahun_kabisat = bool()

if year % 400 == 0 :
    tahun_kabisat = True
elif year % 400 != 0 and year % 100 == 0:
    tahun_kabisat = False
elif year % 400 != 0 and year % 100 != 0 and year % 4 == 0 :
    tahun_kabisat = True
elif year % 400 != 0 and year % 100 != 0 and year % 4 != 0 :
    tahun_kabisat = False

print(tahun_kabisat)