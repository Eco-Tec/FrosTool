import esp


class debug_mode():
    """Clase usada para gestionar el modo debug"""

    def __init__(self, modo=False):
        super(debug_mode, self).__init__()
        self.modo = modo
        self.set_modo(self.modo)

    def active(self):
        """Activa el debug"""
        esp.osdebug(False)
        print("Modo debug activado ...")

    def desactive(self):
        """Desactive debug"""
        print("Modo debug desactivado ....")
        esp.osdebug(0)

    def printDebug(self, msm):
        """Envia mensajes por debug si esta activado"""
        if self.modo:
            print(str(msm))

    def set_modo(self, modo):
        """Cambia el modo de debug"""
        self.modo = modo
        if not modo:
            self.desactive()
        else:
            self.active()
