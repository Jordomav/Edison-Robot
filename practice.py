#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_VERY_FAST

#--------Your code below-----------
# Ed.PlayBeep()
# Ed.TimeWait(1, Ed.TIME_SECONDS)
# Ed.PlayBeep()
# Ed.DriveLeftMotor(Ed.FORWARD, Ed.SPEED_10, 100)
if 1 == 2:
    Ed.Drive(Ed.FORWARD, Ed.SPEED_FULL, 100)
else:
    Ed.PlayBeep()

