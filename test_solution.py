from schlange import drucke, eingabe, ganze_zahl

x = ganze_zahl(eingabe("Geben Sie eine Zahl ein: "))

if x > 5:
    drucke("x ist größer 5")
else: 
    drucke("x ist kleiner oder gleich 5")
