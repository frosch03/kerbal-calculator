from math import pi, sqrt
# from pygraph.classes.graph import graph

# Gravitation Constant: [N*(m/kg)^2]
G = 6.673*(10**-11)

class Body(object):
    def __init__(self, _name):
        self.name = _name

    def __str__(self):
        return (self.name)

class Craft(Body):
    def __init__(self, _name, delta_v = None):
        super(Craft, self).__init__(_name)
        if delta_v:
            self.delta_v = delta_v

class CelestialBody(Body):
    def __init__(self, _name, _r, _soi, _mass, system = None):
        super(CelestialBody, self).__init__(_name)
        self.radius = _r
        self.system = {}
        self.mass = _mass
        # Std. Grav. Parameter: [m^3 / s^2]
        self.mue = G * self.mass 
        self.soi = _soi

        if system:
            self.system = system
            
    def __str__(self):
        sysStr = ""
        sysStr = self.name + "\n" +\
                 "+ r:" + str(self.radius) + "m\n" +\
                 "+ m:" + str(self.mass) + "kg\n" +\
                 "+ System:" + "\n"
        for orb in self.system:
            sysStr += "  - " + str(orb) + "\n"
            anoStr  = ""
            for anomaly in self.system[orb]:
                anoStr += "    * Anomaly: " + str(anomaly) + "°\n      - "
                for i,body in enumerate(self.system[orb][anomaly]):
                    anoStr += body.name + "\n      - " 
                anoStr = anoStr[:-8]
            sysStr += anoStr
        return (sysStr[:-1])

    def __setattr__(self, name, value):
        if name == 'mass':
            self.__dict__['mass'] = value
            self.__dict__['mue']  = G * self.mass
        else:
            try: 
                self.__dict__[name] = value
            except:
                raise (AttributeError, ("no such attribute: %s"%name))
        
    def addSatelit(self, _body, _orbit, anomaly = 0):
        try: 
            self.system[str(_orbit)][anomaly].append(_body)
        except:
            try:
                self.system[str(_orbit)][anomaly] = [_body]
            except:
                self.system[str(_orbit)] = {}
                self.system[str(_orbit)][anomaly] = [_body]

    def delSatelit(self, _orbit, body = None):
        if not body and len(self.system[str(_orbit)]) > 1:
            raise ValueError ("multiple body's on orbit: %s"%str(_orbit))
        if body:
            ano_to_del = list(self.system[str(_orbit)].keys())[list(self.system[str(_orbit)].values()).index(body)]
            del(self.system[str(_orbit)][ano_to_del])
        else:
            del(self.system[str(_orbit)])

class Moon(CelestialBody):
    def __init__(self, _name, _r, _soi, _mass):
        super(Moon, self).__init__(_name, _r, _soi, _mass)
    
class Planet(CelestialBody):
    def __init__(self, _name, _r, _soi, _mass, system = None):
        if system:
            super(Planet, self).__init__(_name, _r, _soi, _mass, system = system)
        else:
            super(Planet, self).__init__(_name, _r, _soi, _mass)

class Star(CelestialBody):
    def __init__(self, _name, _r, _soi, _mass, system = None):
        if system:
            super(Star, self).__init__(_name, _r, _soi, _mass, system)
        else:
            super(Star, self).__init__(_name, _r, _soi, _mass)
    

class Orbit(object):
    # a = length of semi major axis
    # e = eccentricity
    # i = inclination
    # Omega = longitude of the ascending node
    # omega = argument of periapsis
    # tp = time of periapsis passage

    def __init__(self, _planet, _r1, _r2, inclination = None, Omega = None, omega = None):
        self.planet    = _planet
        self.periapsis = (_r1 if _r1 < _r2 else _r2)
        self.apoapsis  = (_r1 if _r1 > _r2 else _r2)
        self.a = self.periapsis + self.apoapsis + (2 * self.planet.radius)
        self.T = 2 * pi * sqrt((self.a ** 3)/self.planet.mue)
        self.e = abs(1 - (2 / \
                          (((self.planet.radius + self.apoapsis) / \
                            (self.planet.radius + self.periapsis)) + 1) ))
        self.i = inclination
        self.O = Omega
        self.o = omega

    def __str__(self):
        orbStr = ""
        orbStr = "Apo: " + str(self.apoapsis) + ", Peri " + str(self.periapsis)+ \
                 ((", Inclination: " + str(self.i) + "°") if self.i else "") +\
                 ((", Long of Asc: " + str(self.O) + "°") if self.O else "") +\
                 ((", Arg of Peri: " + str(self.o) + "°") if self.o else "")

        
        return (orbStr)

    def T(self):
        return (2 * pi * sqrt(self.a**3 / self.planet.mue))

    def t_h(self, _target):
        return ( pi * sqrt((_target.periapsis + self.apoapsis + (2 * self.planet.radius))**3 / (8 * self.planet.mue)) )

    def a_h(self, _target):
        return ( 0.5 * (2 * self.planet.radius + self.periapsis + _target.periapsis) )
        
    def E_h(self, _target):
        return ( -1 * ((self.planet.mue) / (2 * self.a_h(_target))) )

    def v_p_h(self, _target):
        # r_1: inner circle radi / r_2: outer circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        r_2 = self.planet.radius + (_target.periapsis if _target.periapsis > self.periapsis else self.periapsis)
        return ( sqrt(self.planet.mue * ((2 / r_1) - (2 / (r_1 + r_2)))) )

    def v_c_1(self, _target):
        # r_1: inner circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        return ( sqrt(self.planet.mue / r_1) )

    def delta_vph(self, _target):
        return ( self.v_p_h(_target) - self.v_c_1(_target) )
        
    def v_a_h(self, _target):
        # r_1: inner circle radi / r_2: outer circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        r_2 = self.planet.radius + (_target.periapsis if _target.periapsis > self.periapsis else self.periapsis)
        return ( sqrt(self.planet.mue * ((2 / r_2) - (2 / (r_1 + r_2)))) )
        
    def v_c_2(self, _target):
        # r_2: outer circle radi
        r_2 = self.planet.radius + (_target.periapsis if _target.periapsis > self.periapsis else self.periapsis)
        return ( sqrt(self.planet.mue / r_2) )
        
    def delta_vah(self, _target):
        return ( self.v_c_2(_target) - self.v_a_h(_target) )
        
    def delta_vth(self, _target):
        return ( self.delta_vph(_target) + self.delta_vah(_target) )

    def h_h(self, _target):
        # r_1: inner circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        return ( r_1 * self.v_p_h(_target) )

    def ecc_h(self, _target):
        return ( sqrt(1 + ((2 * self.E_h(_target) * (self.h_h(_target) ** 2)) / (self.planet.mue ** 2))) )

class Maneuver(object):
    def __init__(self, _orbit, _delta_v, _anomaly, _direction):
        self.orbit     = _orbit,
        self.delta_v   = _delta_v
        self.anomaly   = _anomaly
        self.direction = _direction

