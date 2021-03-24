# Header
print("")
print("="*50)
teks = "Soal 6 : Operator Binary"
print(teks.center(50))
print("="*50)
print("")


x = 4
y = 11

print("x =",x,"Dengan Binary :",format(x,"08b"))
print("y =",y,"Dengan Binary :",format(y,"08b"))

print("")
print(x,"|",y,"adalah", x|y, ", Binary :",format(x|y,"08b"))

print("")
print(x,">>",y,"adalah", x>>y, ", Binary :",format(x>>y,"08b"))

print("")
print(x,"^",y,"adalah", x^y, ", Binary :",format(x^y,"08b"))

print("")
print("~",x,"adalah", ~x, ", Binary :",format(~x,"08b"))

print("")
print(y,"&",x,"adalah", y&x, ", Binary :",format(y&x,"08b"),"\n")

# Footer
print("="*50)
end = "Selesai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")
