#convert liters per 100km to miles per gallon
def liters_100km_to_miles_gallon(liters):  
    m = (100 *1000)/1609.344   #convert 100 km to miles
    g = liters/3.785411784   #comvert liters to gallons
    return m/g             #calculate miles per gallon used
    

#convert miles per gallon to liters per 100km
def miles_gallon_to_liters_100km(miles):  
    g = miles/25     #calculate gallons used to cover the miles in question
    lpkm = g * 3.785411784   #convert gallons (g) to liters per 100 km
    return lpkm

#test solutions
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))