print ( "Ingrese numero de partidos ganados: ") 
PG = int( input())
print( "Ingrese numero de partidos empatados: ") 
PE = int( input())
print( "Ingrese numero de partidos perdidos: ") 
PP = int( input())
PPG = PG*3 
PPE = PE*1 
PPP = PP*0
PF = PPG + PPE + PPP 
print( "Puntaje Final: ", PF)