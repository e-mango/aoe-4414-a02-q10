# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Converts LLH to ECEF vector
# Parameters:
#  lat_deg: latitude in deg
#  lon_deg: longitiude in deg
#  hae_km: hieght above elipsoid in km
# Output:
#  Prints r_x_km and r_y_km and r_z_km components of the ECEF vector
#
# Written by Evan Schlein
# Other contributors: None
#

# import Python modules
import math # math module
import sys  # argv

# "constants"
R_E_KM = 6378.1363
E_E    = 0.081819221456

# helper functions

## calculated denominator
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

# initialize script arguments
lat_deg = float('nan') # latitude in deg
lon_deg = float('nan') # longitude in deg
hae_km = float('nan') # hieght above elipsoid in km

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])
else:
  print(\
   'Usage: '\
   'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
  )
  exit()

# write script below this line

# calculate variables
lat_rad = lat_deg * math.pi/180.0
lon_rad = lon_deg * math.pi/180.0

denom = calc_denom(E_E,lat_rad)
c_E = R_E_KM/denom
s_E = R_E_KM*(1-E_E**2)/denom

# calculate components
r_x_km = (c_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (c_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (s_E+hae_km)*math.sin(lat_rad)

r = math.sqrt(r_x_km**2 + r_y_km**2 + r_z_km**2)

# print r_x_km (km), r_y_km (km), and r_z_km (km)
print(r_x_km)
print(r_y_km)
print(r_z_km)