"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#


def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """

    a = brevet_start_time
    if (brevet_dist_km < 200):
        a = a.replace(hours =+ (control_dist_km/34))
    elif (brevet_dist_km < 400):
        a = a.replace(hours =+ (brevet_dist_km/32))
    elif (brevet_dist_km < 600):
        a = a.replace(hours =+ (brevet_dist_km/30))
    elif (brevet_dist_km < 800):
        a = a.replace(hours =+ (brevet_dist_km/28))
    elif (brevet_dist_km < 1000):
        a = a.replace(hours =+ (brevet_dist_km/26))
    else:
        a = a.replace(hours =+ (brevet_dist_km/26))
    print (a)
    return a.isoformat()

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    a = brevet_start_time
    if (brevet_dist_km > 600):
        a = a.replace(hours =+ (brevet_dist_km/11.43))
    else:
        a = a.replace(hours =+ (brevet_dist_km/15))

    print (a)
    return a.isoformat()

