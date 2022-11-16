

def checkStability(points, z, steps):
    stabilityList = []
    for p in points:
        cnum = complex(p[0], p[1])
        cnum_tracker = complex(p[0], p[1])
        i = 0
        boundsTracker = False
        while(i < steps and not boundsTracker):
            cnum_tracker = (cnum_tracker**z) + cnum
            if cnum_tracker.real > 5 or cnum_tracker.imag > 5 or cnum_tracker.real < -5 or cnum_tracker.imag < -5:
                boundsTracker = True
            i = i + 1
        stabilityList.append(i)
    
    return stabilityList