# Header
print("")
print("="*50)
teks = "Soal 5 : Memodifikasi String"
print(teks.center(50))
print("="*50)
print("")

# String
s = "Hey there! what should this string be?"

# Modifikasi String s
s = s[0:20]
s = s.replace("re","ra",1)
s = s.replace("Hey","Str",1)
s = s.replace("t shou",'ttome!',1)

# String s menjadi :
print("String (s) menjadi :\n",s)

# Panjangnya harusnya 20
print("\nPanjang dari s = %d"%len(s))

# huruf pertama ‘a’ harusnya di index no 8
print("\nKemunculan pertama a = %d" % s.index("a"))

# Huruf a muncul 2 kali
print("\nHuruf a muncul sebanyak %d"%s.count("a"),"kali")

# memotong string berdasarkan index
print("\nLima karakter pertama adalah '%s'" % s[:5]) # Start to 5
print("\nLima karakter berikutnya adalah '%s'" % s[5:10]) # 5 to 10
print("\nKarakter ketiga belas adalah '%s'" % s[12]) # Just number 12
print("\nKarakter dengan indeks ganjil adalah '%s'" %s[1::2]) #(0-based indexing
print("\nLima karakter terakhir adalah '%s'" % s[-5:]) # 5th-from-last to end

# Konversi ke uppercase
print("\nString dalam huruf besar: %s" % s.upper())

# Konversi ke lowercase
print("\nString dalam huruf kecil: %s" % s.lower())

# Cek bagaimana dimulai
if s.startswith("Str"):
    print("\nString dimulai dengan 'Str'. Good!")

# Cek bagaimana diakhiri
if s.endswith("ome!"):
    print("\nString diakhiri dengan 'ome!'. Good!")

# Pisahkan string menjadi 3 string terpisah, masing-masing string 1 kata
print("\nPisahkan kata-kata dari string tersebut: %s" % s.split(" "))

# Footer
print("")
print("="*50)
end = "Selesai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")
