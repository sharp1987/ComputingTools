########################################################################
# Name:
#	Humidity
#-----------------------------------------------------------------------
# Description:
#	Calculate the humidity for the wet air.
########################################################################

### Input ##############################################################
#Volume Fraction of Steam
x=0.2
#Pressure (kPa)
e=200.0
#Temperature (K)
T=100.0+273.16
#Saturation Pressure at the Given Temperature (kPa)
psat=101.45
### End Input ##########################################################

#Gas Constant of Water
Rw=461.526		#J/(kg K)

#Absolute Humidity (kg/m**3)
rhow=e*x*1000.0/(Rw*T)

#Relative Humidity (%)
RH=e*x/psat*100.0

### Output #############################################################
print "AH = ",rhow,"kg/m**3"
print "RH = ",RH,"%"