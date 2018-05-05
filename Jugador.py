from Mazo import Mazo
from Carta import Carta
from Operador import calcularPuntosMano


class Jugador:
    __mano = []

    __puntos = {
        "Palos": 0,
        "Espadas": 0,
        "Oro": 0,
        "Copa": 0
    }

    def __init__(self, mazo):
        for _ in range(0, 2):
            self.agarrarCarta(mazo)

    def agarrarCarta(self, mazo):
        nuevaCarta = mazo.agarrarCarta()
        self.__mano.append(nuevaCarta)
        self.__puntos = calcularPuntosMano(
            nuevaCarta,
            True,
            self.__puntos
        )

    def cambiarCartas(self, cambioCartas, mazo):
        self.__mano = [x for x in self.__mano if x not in cambioCartas]
        for viejaCarta in cambioCartas:
            self.__puntos = calcularPuntosMano(
                viejaCarta,
                False,
                self.__puntos
            )
            self.agarrarCarta(mazo)

    def getMaxPuntos(self):
        max = 0
        for pinta in self.__puntos:
            if(self.__puntos[pinta] > max):
                max = self.__puntos[pinta]
        return max

    # def imprimirCartas(self):
    #     for carta in self.__mano:
    #         print(str(carta.getValor()) + " de " + carta.getPinta())

    def getPuntos(self):
        return self.__puntos

    def getMano(self):
        return self.__mano
