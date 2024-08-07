import os

#membaca file csv
def readCSV(file, split):
 if file in os.listdir():
  with open(file, "r") as d:
   data = d.read()
  spl = data.split("\n")
  text = data.replace(spl[0] + "\n", "")
  arr = {}
  for aa in text.split("\n"):
   a = aa.split(split)
   arr[a[0]] = {"Tugas 1": int(a[1]), "Tugas 2": int(a[2]), "Quiz 1": int(a[3]), "Quiz 2": int(a[4]), "UTS": int(a[5]), "UAS": int(a[6])}
   if len(a) == 8 and a[7] != "":
    if int(a[7])%2 == 0:
     arr[a[0]]["UTS"] = int(a[7])
    else:
     arr[a[0]]["UAS"] = int(a[7])
  return arr

#list isi dari key pada file dictionary untuk mendapatkan nilai dalam kolom NIM
def listDictKey(dict, key):
 return [dict[a][key] for a in dict]

#pengecekan serta mengelompokan nim batas atas,tengah,bawah untuk menentukan Median/Mean
def cekAtasBawah(dict, key, type="mean"):
 array = listDictKey(dict, key)
 if type.lower() == "mean":
  nilai = mean(array)
 elif type.lower() == "median":
  nilai = median(array)
 else:
  raise Exception("None Type Object: "+type)
 rata = nilai
 atas = {}
 bawah = {}
 for x in dict:
  if dict[x][key] >= rata:
   atas[x] = dict[x][key]
  else:
   bawah[x] = dict[x][key]
 return atas, bawah

#save file baru
def writeCSV(dict, split=",", nama="yourdata.csv"):
 if ".csv" not in nama:
  raise Exception("Your file name must be ended with .csv")
 ret = "NIM"+split+"Tugas 1"+split+"Tugas 2"+split+"Quiz 1"+split+"Quiz 2"+split+"UTS"+split+"UAS"+"\n"
 for user in dict:
  ret += user + split
  for kode in range(len(list(dict[user]))):
   if kode != len(list(dict[user]))-1:
    ret += str(dict[user][list(dict[user])[kode]]) + split
   else:
    ret += str(dict[user][list(dict[user])[kode]])
  ret += "\n"
  a = open(nama, "w")
  a.write(ret)
  a.close()
 return ret

#mencari mean dari data
def mean(data):
 nilai = sum(data)
 return nilai/len(data)

#mencari median dari data
def median(data):
 n = len(data)
 data.sort()
 if n%2 == 0:
  m1 = data[n//2]
  m2 = data[n//2-1]
  m = (m1+m2)/2
 else:
  m = data[n//2]
 return m

data = readCSV("dataset11.csv", ",")

#1. NIM mana yang mendapatkan UTS tertinggi?/
atas1 = listDictKey(data, "UTS")
ret = "\nYang mendapatkan nilai Tertinggi adalah \n"
n = max(atas1)
for nn in data:
 if data[nn]["UTS"] == n:
  ret += nn
print(ret)

#2. NIM mana yang mendapatkan nilai UAS terendah?
bawah = listDictKey(data, "UAS")
n1 = min(bawah)
ret2 = "\nYang mendapat nilai Terendah dalam UAS adalah \n"
for nn in data:
 if data[nn]["UAS"] == n1:
  ret2 += nn + ', '
print(ret2)

#3. NIM mana sajakah yang mendapatkan nilai quiz-1 di atas rata-rata?
atas1, bawah1 = cekAtasBawah(data, "Quiz 1", "mean")
total = len(list(atas1))
ret3 = "\nYang mendapat nilai quiz-1 diatas rata2 adalah \n"
for a in range(total):
 if a != total-1:
  ret3 += list(atas1)[a] + ", "
 else:
  ret3 += "dan " + list(atas1)[a] + "."
print(ret3)

#4. NIM mana sajakah yang mendapatkan nilai quiz-2 di bawah median?
atas2, bawah2 = cekAtasBawah(data, "Quiz 2", "median")
total = len(list(bawah2))
ret4 = "\nYang mendapat nilai quiz-2 dibawah median adalah \n"
for a in range(total):
 if a != total-1:
  ret4 += list(bawah2)[a] + ", "
 else:
  ret4 += "dan " + list(bawah2)[a] + "."
print(ret4) 

#5. NIM mana sajakah yang mendapatkan nilai tugas-1 di bawah median?
atas3, bawah3 = cekAtasBawah(data, "Tugas 1", "median")
total = len(list(bawah3))
ret = "\nNim yang mendapat nilai tugas 1 dibawah median adalah \n"
for a in range(total):
 if a != total-1:
  ret += list(bawah3)[a] + ", "
 else:
  ret += "dan " + list(bawah3)[a] + "."
print(ret)

#6. NIM mana sajakah yang mendapatkan nilai tugas-2 di atas rata-rata?
a, b = cekAtasBawah(data, "Tugas 2", "mean")
total = len(list(a))
ret = "\nNIM Yang mendapatkan nilai Tugas 2 diatas rata rata adalah \n"
for aa in range(total):
 if aa != total - 1:
  ret += list(a)[aa] + ", "
 else:
  ret += "dan " + list(a)[aa] + "."
print(ret)

#7. NIM mana yang nilai akhirnya menjadi pencilan bawah / atas?

#8. NiM mana sajakah yang mendapatkan nilai akhir kurang dari mean?
b, a = cekAtasBawah(data, "UAS", "mean")
total = len(list(a))
ret = "\nNIM Yang mendapatkan nilai UAS dibawah mean adalah \n"
for aa in range(total):
 if aa != total - 1:
  ret += list(a)[aa] + ", "
 else:
  ret += "dan " + list(a)[aa] + ".\n"
print(ret)

print("Data berhasil diolah\n" + writeCSV(data, ";",'dataset11_fixed.csv'))