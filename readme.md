
# Info

This is a basic library for calculating orbital changes. Up to now,
there is only information for hohmann transfer maneuver. The are
listed in the following list.

# Orbits

## Time of Hohmann transfer ![equation](http://latex.codecogs.com/gif.latex?%5C%28t_h%5C%29)

The time (in seconds) of the transfer is calculated by 

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20t_h%20%3D%20%5Cpi%20%2A%20%5Csqrt%7B%5Cfrac%7B%28r_1%20%2B%20r_2%20%2B%202R%29%5E3%7D%7B8%2A%5Cmu%7D%7D%0A%20%20%20%5C%5D)

Which is done by:

    def t_h(self, _target):
        return ( pi * sqrt((_target.periapsis + self.apoapsis + (2 * self.planet.radius))**3 / (8 * self.planet.mue)) )

## The semi major axis of Hohmann transer Orbit ![equation](http://latex.codecogs.com/gif.latex?%5C%28a_%7Bhohmann%7D%5C%29)

The semi major axis of the transfer is calculated via:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20a_%7Bhohmann%7D%20%3D%20%5Cfrac%7B1%7D%7B2%7D%20%2A%20%282R%20%2B%20r_1%20%2B%20r_2%29%0A%20%20%20%5C%5D)

Which is done by:

    def a_h(self, _target):
        return ( 0.5 * (2 * self.planet.radius + self.periapsis + _target.periapsis) )

## The Energy of Hohmann transer ![equation](http://latex.codecogs.com/gif.latex?%5C%28E_%7Bhohmann%7D%5C%29)

The Energy of the transfer is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20E_%7Bhohmann%7D%20%3D%20-%20%5Cfrac%7B%5Cmu%7D%7B2%2Aa%7D%0A%20%20%20%5C%5D)

Which is done by:

    def E_h(self, _target):
        return ( -1 * ((self.planet.mue) / (2 * self.a_h(_target))) )

## The Velocity needed at the Priapsis of the Hohmann transer \(v_{\pi,hohmann}\)

Is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20v_%7B%5Cpi%2Chohmann%7D%20%3D%20%5Csqrt%7B%5Cmu%20%2A%20%28%5Cfrac%7B2%7D%7Br_1%7D%29%20-%20%28%5Cfrac%7B2%7D%7Br_1%2Br_2%7D%29%7D%0A%20%20%20%5C%5D)

Which is done by:

    def v_p_h(self, _target):
        # r_1: inner circle radi / r_2: outer circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        r_2 = self.planet.radius + (_target.periapsis if _target.periapsis > self.periapsis else self.periapsis)
        return ( sqrt(self.planet.mue * ((2 / r_1) - (2 / (r_1 + r_2)))) )

## The Velocity needed at the Apoapsis of the Hohmann transer ![equation](http://latex.codecogs.com/gif.latex?%5C%28v_%7B%5Calpha%2Chohmann%7D%5C%29)

Is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20v_%7B%5Calpha%2Chohmann%7D%20%3D%20%5Csqrt%7B%5Cmu%20%2A%20%28%5Cfrac%7B2%7D%7Br_2%7D%29%20-%20%28%5Cfrac%7B2%7D%7Br_1%2Br_2%7D%29%7D%0A%20%20%20%5C%5D)

Which is done by:

    def v_a_h(self, _target):
        # r_1: inner circle radi / r_2: outer circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        r_2 = self.planet.radius + (_target.periapsis if _target.periapsis > self.periapsis else self.periapsis)
        return ( sqrt(self.planet.mue * ((2 / r_2) - (2 / (r_1 + r_2)))) )

## The initial Velocity before the Hohmann transer ![equation](http://latex.codecogs.com/gif.latex?%5C%28v_%7Bc1%7D%5C%29)

Is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20v_%7Bc1%7D%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Cmu%7D%7Br_1%7D%7D%0A%20%20%20%5C%5D)

Which is done by:

    def v_c_1(self, _target):
        # r_1: inner circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        return ( sqrt(self.planet.mue / r_1) )

## The final Velocity after the Hohmann transer ![equation](http://latex.codecogs.com/gif.latex?%5C%28v_%7Bc2%7D%5C%29)

Is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20v_%7Bc2%7D%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Cmu%7D%7Br_2%7D%7D%0A%20%20%20%5C%5D)

Which is done by:

    def v_c_2(self, _target):
        # r_2: outer circle radi
        r_2 = self.planet.radius + (_target.periapsis if _target.periapsis > self.periapsis else self.periapsis)
        return ( sqrt(self.planet.mue / r_2) )

## The difference in Velocity at Periapsis of Hohmann transer ![equation](http://latex.codecogs.com/gif.latex?%5C%28%5CDelta%20v_%7B%5Cpi%2Chohmann%7D%5C%29)

Is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20%5CDelta%20v_%7B%5Cpi%2Chohmann%7D%20%3D%20v_%7B%5Cpi%2Chohmann%7D%20-%20v_%7Bc1%7D%0A%20%20%20%5C%5D)

Which is done by:

    def delta_vph(self, _target):
        return ( self.v_p_h(_target) - self.v_c_1(_target) )

## The difference in Velocity at Apoapsis of Hohmann transer ![equation](http://latex.codecogs.com/gif.latex?%5C%28%5CDelta%20v_%7B%5Calpha%2Chohmann%7D%5C%29)

Is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20%5CDelta%20v_%7B%5Calpha%2Chohmann%7D%20%3D%20v_%7Bc2%7D%20-%20v_%7B%5Calpha%2Chohmann%7D%0A%20%20%20%5C%5D)

Which is done by:

    def delta_vah(self, _target):
        return ( self.v_c_2(_target) - self.v_a_h(_target) )

## The total difference in Velocity of the Hohmann transer ![equation](http://latex.codecogs.com/gif.latex?%5C%28%5CDelta%20v_%7BT%2Chohmann%7D%5C%29)

Is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20%5CDelta%20v_%7BT%2Chohmann%7D%20%3D%20%5CDelta%20v_%7B%5Cpi%2Chohmann%7D%20%2B%20%5CDelta%20v_%7B%5Calpha%2Chohmann%7D%0A%20%20%20%5C%5D)

Which is done by:

    def delta_vth(self, _target):
        return ( self.delta_vph(_target) + self.delta_vah(_target) )

## The specific angular Momentum of Hohmann transer ![equation](http://latex.codecogs.com/gif.latex?%5C%28h_%7Bhohmann%7D%5C%29)

Is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20h_%7Bhohmann%7D%20%3D%20r_1%20%2A%20v_%7B%5Cpi%2Chohmann%7D%0A%20%20%20%5C%5D)

Which is done by:

    def h_h(self, _target):
        # r_1: inner circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        return ( r_1 * self.v_p_h(_target) )

## The Eccentricity of the Hohmann transer Elipsis ![equation](http://latex.codecogs.com/gif.latex?%5C%28e_%7Bhohmann%7D%5C%29)

Is calculated by:

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%20%20e_%7Bhohmann%7D%20%3D%20%5Csqrt%7B1%20%2B%20%5Cfrac%7B2%20%2A%20E_%7Bhohmann%7D%20%2A%20h_%7Bhohmann%7D%5E2%7D%7B%5Cmu%5E2%7D%7D%0A%20%20%20%5C%5D)

Which is done by:

    def ecc_h(self, _target):
        return ( sqrt(1 + ((2 * self.E_h(_target) * (self.h_h(_target) ** 2)) / (self.planet.mue ** 2))) )

# ![equation](http://latex.codecogs.com/gif.latex?%5C%5B%5Cmy%5C%5D) Formula

![equation](http://latex.codecogs.com/gif.latex?%5C%5B%0A%20%206.673%2A10%5E%7B-11%7D%20%5BN%2A%20%28%5Cfrac%7Bm%7D%7Bkg%7D%29%5E2%5D%20%2A%205.92719%2A10%5E%7B24%7D%20%5Bkg%5D%0A%20%20%5C%5D)
