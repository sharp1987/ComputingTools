########################################################################
# Name:
#	HydraulicDiameter
#-----------------------------------------------------------------------
# Description:
#	Calculate the hydraulic diameter for the control volume.
########################################################################

### Input ##############################################################
#Control Volume Dimensions (m)
width=10.0
depth=0.05
height=0.05

#Correction Term for Volume (m**3)
deltaV=0.0
#Correction Term for Surface Area (m**2)
deltaA=0.0
### End Input ##########################################################

#Control Volume Parameter
V=width*depth*height
A=2.0*(width*depth+width*height+depth*height)

#Hydraulic Diameter (m)
HD=4.0*(V-deltaV)/(A-deltaA)

### Output #############################################################
print "Vol. = ",V,"m**3"
print "H.D. = ",HD,"m"