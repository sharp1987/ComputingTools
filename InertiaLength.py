########################################################################
# Name:
#	InertiaLength
#-----------------------------------------------------------------------
# Description:
#	Calculate the inertia length for the flow path between two control
# volumes.
########################################################################

### Input ##############################################################
#Control Volume 1
##Dimension along the Flow Path (m)
L1=1.0
##Floor Area (m**2)
A1=1.0

#Control Volume 2
##Dimension along the Flow Path (m)
L2=1.0
##Floor Area (m**2)
A2=1.0

#Flow Path
##Actual Length (m)
L0=1.0
##Hydraulic Diameter (m)
Dh=1.0
##Flow Area (m**2)
AJ=1.0
### End Input ##########################################################

#Inertia Length (m)
LJ=min(L1,L1*AJ/A1+0.45*Dh/(1.0+AJ/A1))		\
	+L0										\
	+min(L2,L2*AJ/A2+0.45*Dh/(1.0+AJ/A2))

### Output #############################################################
print "I.L. =",LJ,"m"