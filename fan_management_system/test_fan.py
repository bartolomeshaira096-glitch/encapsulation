from fan import Fan

class TestFan:
    def __init__(self):
        self.fan1 = Fan()
        self.fan1.set_speed(Fan.FAST)
        self.fan1.set_radius(10)
        self.fan1.set_color("yellow")
        self.fan1.set_on(True)

        self.fan2 = Fan()
        self.fan2.set_speed(Fan.MEDIUM)
        self.fan2.set_radius(5)
        self.fan2.set_color("blue")
        self.fan2.set_on(False)

    def get_fans(self):
        return self.fan1, self.fan2