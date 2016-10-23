import sys
from sa import sa
from maxwalksat import mws
from osyczka2 import Osyczka2
from kursawe import Kursawe
from schaffer import Schaffer

for model in [Schaffer, Osyczka2, Kursawe]:
    for optimizer in [sa, mws]:
           optimizer(model())
