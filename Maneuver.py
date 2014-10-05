from kerbal import *
from kerbinsystem import *

class From(object):
    def __init__(self, _starsystem, _body):
        self.starsystem = _starsystem
        self.sBody  = _body
        self.sOrbit = _starsystem.getOrbitOf(_body)

    def to(self, _body):
        self.tBody  = _body
        self.tOrbit = self.starsystem.getOrbitOf(_body)
        return(self)

    def d_incl(self):
        s_incl = self.sOrbit.i if self.sOrbit.i else 0
        t_incl = self.tOrbit.i if self.tOrbit.i else 0
        return(t_incl - s_incl)

    def d_Omega(self):
        s_Omega = self.sOrbit.O if self.sOrbit.O else 0
        t_Omega = self.tOrbit.O if self.tOrbit.O else 0
        return(t_Omega - s_Omega)

    def d_omega(self):
        s_omega = self.sOrbit.o if self.sOrbit.o else 0
        t_omega = self.tOrbit.o if self.tOrbit.o else 0
        return(t_omega - s_omega)

    def dPlane(self):
        maneuver  = "* Change Inclination difference of %6.2f\n"%self.d_incl()
        maneuver += self.toRefPlane() + "\n"
        maneuver += self.toTgtPlane()
        return (maneuver)

    def toRefPlane(self):
        s_omega = self.sOrbit.o if self.sOrbit.o else 0 
        if self.sOrbit.i:
            maneuver = "** At: %6.2f ChgIncl: %6.2f"%((360 - s_omega),
                                               -self.sOrbit.i)
            return (maneuver)
        else:
            return("** In Reference Plane")

    def toTgtPlane(self):
        if self.tOrbit.O:
            maneuver = "** At: %6.2f ChgIncl: %6.2f"%((self.tOrbit.O),
                                               self.tOrbit.i)
            return (maneuver)

        
        

class kFrom(From):
    def __init__(self, _body):
        super(kFrom, self).__init__(Kerbol, _body)
        

class Maneuver(object):
    def __init__(self, _orbit, _delta_v, _anomaly, _direction):
        self.orbit     = _orbit,
        self.delta_v   = _delta_v
        self.anomaly   = _anomaly
        self.direction = _direction


def inclManeuver(_main, _sBody,  _tBody):
    sHeight = 80e3
    d_i = kFrom(_sBody).to(_tBody).d_incl()
    d_o = kFrom(_sBody).to(_tBody).d_omega()
    d_O = kFrom(_sBody).to(_tBody).d_Omega()
    Maneuver(Orbit(_main, sHeight, sHeight), 0, )
    
