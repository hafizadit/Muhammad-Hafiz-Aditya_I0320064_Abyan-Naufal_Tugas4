# Header
print("")
print("="*50)
end = "Soal 4 : Program Seleksi Kursus"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")

# Input
x = int(input("Berapakah Usiamu :"))
y = input("Apakah anda sudah lulus ujian (y/t)?")

print("")

# Kode
if x >= 21 and y == "y":
    print("Anda dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")

# Footer
print("")
print("="*50)
end = "Selesai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")
