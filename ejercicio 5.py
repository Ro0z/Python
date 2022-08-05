import math


print("Ingrese GB: ") 
GB = float( input())
MG = GB*1024 
MD = MG/1.44
print("\nel resultado es: ") 
print(MD)
print ("numero de discos necesarios", math.ceil (MD))