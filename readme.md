
# Info

This is a basic library for calculating orbital changes. Up to now,
there is only information for hohmann transfer maneuver. The are
listed in the following list.

# Orbits

## Time of Hohmann transfer \(t_h\)

The time (in seconds) of the transfer is calculated by 
\[
   t_h = \pi * \sqrt{\frac{(r_1 + r_2 + 2R)^3}{8*\mu}}
   \]
Which is done by:

    def t_h(self, _target):
        return ( pi * sqrt((_target.periapsis + self.apoapsis + (2 * self.planet.radius))**3 / (8 * self.planet.mue)) )

## The semi major axis of Hohmann transer Orbit \(a_{hohmann}\)

The semi major axis of the transfer is calculated via:
\[
   a_{hohmann} = \frac{1}{2} * (2R + r_1 + r_2)
   \]
Which is done by:

    def a_h(self, _target):
        return ( 0.5 * (2 * self.planet.radius + self.periapsis + _target.periapsis) )

## The Energy of Hohmann transer \(E_{hohmann}\)

The Energy of the transfer is calculated by:
\[
   E_{hohmann} = - \frac{\mu}{2*a}
   \]
Which is done by:

    def E_h(self, _target):
        return ( -1 * ((self.planet.mue) / (2 * self.a_h(_target))) )

## The Velocity needed at the Priapsis of the Hohmann transer \(v_{\pi,hohmann}\)

Is calculated by:
\[
   v_{\pi,hohmann} = \sqrt{\mu * (\frac{2}{r_1}) - (\frac{2}{r_1+r_2})}
   \]
Which is done by:

    def v_p_h(self, _target):
        # r_1: inner circle radi / r_2: outer circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        r_2 = self.planet.radius + (_target.periapsis if _target.periapsis > self.periapsis else self.periapsis)
        return ( sqrt(self.planet.mue * ((2 / r_1) - (2 / (r_1 + r_2)))) )

## The Velocity needed at the Apoapsis of the Hohmann transer \(v_{\alpha,hohmann}\)

Is calculated by:
\[
   v_{\alpha,hohmann} = \sqrt{\mu * (\frac{2}{r_2}) - (\frac{2}{r_1+r_2})}
   \]
Which is done by:

    def v_a_h(self, _target):
        # r_1: inner circle radi / r_2: outer circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        r_2 = self.planet.radius + (_target.periapsis if _target.periapsis > self.periapsis else self.periapsis)
        return ( sqrt(self.planet.mue * ((2 / r_2) - (2 / (r_1 + r_2)))) )

## The initial Velocity before the Hohmann transer \(v_{c1}\)

Is calculated by:
\[
   v_{c1} = \sqrt{\frac{\mu}{r_1}}
   \]
Which is done by:

    def v_c_1(self, _target):
        # r_1: inner circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        return ( sqrt(self.planet.mue / r_1) )

## The final Velocity after the Hohmann transer \(v_{c2}\)

Is calculated by:
\[
   v_{c2} = \sqrt{\frac{\mu}{r_2}}
   \]
Which is done by:

    def v_c_2(self, _target):
        # r_2: outer circle radi
        r_2 = self.planet.radius + (_target.periapsis if _target.periapsis > self.periapsis else self.periapsis)
        return ( sqrt(self.planet.mue / r_2) )

## The difference in Velocity at Periapsis of Hohmann transer \(\Delta v_{\pi,hohmann}\)

Is calculated by:
\[
   \Delta v_{\pi,hohmann} = v_{\pi,hohmann} - v_{c1}
   \]
Which is done by:

    def delta_vph(self, _target):
        return ( self.v_p_h(_target) - self.v_c_1(_target) )

## The difference in Velocity at Apoapsis of Hohmann transer \(\Delta v_{\alpha,hohmann}\)

Is calculated by:
\[
   \Delta v_{\alpha,hohmann} = v_{c2} - v_{\alpha,hohmann}
   \]
Which is done by:

    def delta_vah(self, _target):
        return ( self.v_c_2(_target) - self.v_a_h(_target) )

## The total difference in Velocity of the Hohmann transer \(\Delta v_{T,hohmann}\)

Is calculated by:
\[
   \Delta v_{T,hohmann} = \Delta v_{\pi,hohmann} + \Delta v_{\alpha,hohmann}
   \]
Which is done by:

    def delta_vth(self, _target):
        return ( self.delta_vph(_target) + self.delta_vah(_target) )

## The specific angular Momentum of Hohmann transer \(h_{hohmann}\)

Is calculated by:
\[
   h_{hohmann} = r_1 * v_{\pi,hohmann}
   \]
Which is done by:

    def h_h(self, _target):
        # r_1: inner circle radi
        r_1 = self.planet.radius + (self.periapsis if self.periapsis < _target.periapsis else _target.periapsis)
        return ( r_1 * self.v_p_h(_target) )

## The Eccentricity of the Hohmann transer Elipsis \\(e\_)hohmann}\\]

Is calculated by:
\[
   e_{hohmann} = \sqrt{1 + \frac{2 * E_{hohmann} * h_{hohmann}^2}{\mu^2}}
   \]
Which is done by:

    def ecc_h(self, _target):
        return ( sqrt(1 + ((2 * self.E_h(_target) * (self.h_h(_target) ** 2)) / (self.planet.mue ** 2))) )

# \[\my\] Formula

\[
  6.673*10^{-11} [N* (\frac{m}{kg})^2] * 5.92719*10^{24} [kg]
  \]
