def euro_to_dollars(euro:float, taux_change:float = 1.1) -> float:
   euro = euro * taux_change
   return euro

def degre_to_farenheit(degre:float) -> float:
   degre = (degre*9/5) + 32
   return degre

def km_to_miles(km:float) -> float:
   km = km*0.621371
   return km
