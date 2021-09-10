\* Pr1_2 *\
Maximize
OBJ: 20 Astro + 30 Cosmo
Subject To
Astro_Line_Capacity: Astro <= 60
Cosmo_Line_Capacity: Cosmo <= 50
Labor_Capacity: Astro + 2 Cosmo <= 158
_C1: Cosmo - 2 imsi = 0
Bounds
Cosmo free
imsi free
Generals
Cosmo
imsi
End
