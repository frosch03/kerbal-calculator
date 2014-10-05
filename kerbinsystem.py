from kerbal import *

Kerbol = Star('Kerbol', 261.6e6, float('Inf'), 1.7565670e28)

Moho   = Planet('Moho', 250e3, 9646663, 2.5263617e21)

Eve    = Planet('Eve',  700e3, 85109365, 1.2244127e23)
Gilly  =   Moon('Gilly', 13e3, 126123.27, 1.2420512e17)
Eve.addSatelit(Gilly, Orbit(Eve, 48.825e6 -700e3, 14.175e6 -700e3, inclination = 12, Omega = 80, omega = 10))

Kerbin = Planet('Kerbin',  600e3, 84159286,   5.2915793e22)
Mun    =   Moon('Mün',     200e3,  2429559.1, 9.7600236e20)
Minmus =   Moon('Minmus',   60e3,  2247428.4, 2.6457897e19)
Kerbin.addSatelit(Mun,    Orbit(Kerbin, 12e6 -600e3, 12e6 -600e3))
Kerbin.addSatelit(Minmus, Orbit(Kerbin, 47e6 -600e3, 47e6 -600e3, inclination = 6, Omega = 78, omega = 38))

Duna   = Planet('Duna', 320e3, 47921949,   4.5154812e21)
Ike    =   Moon('Ike',  130e3,  1049598.9, 2.7821949e20)
Duna.addSatelit(Ike, Orbit(Duna, 3.296e6 -320e3, 3.104e6 -320e3, inclination = 0.03))

Dres   = Planet('Dres', 138e3, 32832840, 3.2191322e20)

Jool   = Planet('Jool',     6e6, 2.4559852e9, 4.2332635e24)
Laythe =   Moon('Laythe', 500e3,  3723645.8,  2.9397663e22)
Vall   =   Moon('Vall',   300e3,  2406401.4,  3.1088028e21)
Tylo   =   Moon('Tylo',   600e3, 10856518,    4.2332635e22)
Bop    =   Moon('Bop',     65e3,  1221060.9,  3.7261536e19)
Pol    =   Moon('Pol',     44e3,  1042138.9,  1.0813636e19)
Jool.addSatelit(Laythe, Orbit(Jool,  27.184e6    -6e6,  27.184e6    -6e6))
Jool.addSatelit(Vall,   Orbit(Jool,  43.152e6    -6e6,  43.152e6    -6e6))
Jool.addSatelit(Tylo,   Orbit(Jool,  68.5e6      -6e6,  68.5e6      -6e6, inclination =  0.025))
Jool.addSatelit(Bop,    Orbit(Jool, 158.6975e6   -6e6,  98.3025e6   -6e6, inclination = 15,    Omega = 10, omega = 25))
Jool.addSatelit(Pol,    Orbit(Jool, 210.624206e6 -6e6, 149.155794e6 -6e6, inclination =  4.25, Omega =  2, omega = 15))

Eeloo  = Planet('Eeloo', 210e3, 1.1908294e8, 1.1149358e21)

Kerbol.addSatelit(Moho,   Orbit(Kerbol,  6315765980-261.6e6,   4210510628-261.6e6, inclination = 7, Omega = 70, omega = 15))
Kerbol.addSatelit(Eve,    Orbit(Kerbol,  9931011387-261.6e6,   9734357701-261.6e6, inclination = 2.1, Omega = 15))
Kerbol.addSatelit(Kerbin, Orbit(Kerbol,  13599840256-261.6e6,  13599840256-261.6e6))
Kerbol.addSatelit(Duna,   Orbit(Kerbol,  21783189163-261.6e6,  19669121365-261.6e6, inclination = 0.06,  Omega = 135.5))
Kerbol.addSatelit(Dres,   Orbit(Kerbol,  46761053522-261.6e6,  34917642884-261.6e6, inclination = 5,     Omega = 280, omega = 90))
Kerbol.addSatelit(Jool,   Orbit(Kerbol,  72212238387-261.6e6,  65334882253-261.6e6, inclination = 1.302, Omega = 52))
Kerbol.addSatelit(Eeloo,  Orbit(Kerbol,  113549713200-261.6e6, 66687926800-261.6e6, inclination = 6.15,  Omega = 50, omega = 260))




LKO = Orbit(Kerbin, 80e3, 80e3)
KSO = Orbit(Kerbin, 2.868e6, 2.868e6)
