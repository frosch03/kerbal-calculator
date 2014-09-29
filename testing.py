tmp = __import__('kerbin-system')
globals().update(vars(tmp))


Ship = Craft("Ship")
Station = Craft("Station")
Kerbin.addSatelit(Ship, Orbit(Kerbin, 80e3, 80e3))
Kerbin.addSatelit(Station, Orbit(Kerbin, 80e3, 80e3))


lko     = Orbit(Kerbin, 80e3, 80e3)
mun_o   = Orbit(Kerbin, 12e6, 12e6)
hohmann = [Maneuver(lko, lko.delta_vph(mun_o),   0, (0,0,0)),
           Maneuver(lko, lko.delta_vah(mun_o), 180, (0,0,0))]


def eject_angle(_orbit, _anomaly, _trgOrbit, _trgAnomaly):
    t_h = _orbit.t_h(_trgOrbit)
    trgAngDif =  (t_h / _trgOrbit.T) * 360 - _trgAnomaly
    # r = _orbit.a - _orbit.periapsis -
    return (trgAngDif)

kerbin_orb = Orbit(Kerbin, 13599840256, 13599840256)
duna_orb = Orbit(Duna, 21783189163, 19669121365, inclination = 0.06, Omega = 135.5)
