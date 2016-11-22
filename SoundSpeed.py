########################################################################
# Name:
#	SoundSpeed
#-----------------------------------------------------------------------
# Description:
#	Calculate the Sound Speed in the Air.
########################################################################

import math

### Input ##############################################################
#Temperature (C)
T=120.0
### End Input ##########################################################

#Sound Speed (m/s)
SoundSpeed=331.45*math.sqrt(1.0+T/273.15)

### Output #############################################################
print "w = ",SoundSpeed,"m/s"