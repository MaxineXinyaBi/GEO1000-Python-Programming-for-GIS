# GEO1000 - Assignment 0
# Authors: Xinya Bi
# Studentnumbers: 6195350

def temp_windchill(temp_in_c, windspeed_in_kmh):
    temp_wc = 13.12 + 0.6125 * temp_in_c - 11.37 * windspeed_in_kmh ** 0.16 + 0.3965 * temp_in_c * windspeed_in_kmh ** 0.16
    return temp_wc

print(round(temp_windchill(temp_in_c=5.0, windspeed_in_kmh=10.0),2))
print(round(temp_windchill(temp_in_c=-1.0, windspeed_in_kmh=35.0),2))