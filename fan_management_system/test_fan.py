from fan import Fan

class TestFan:
    def __init__(self):
        self.fan1 = Fan()
        self.fan1.set_speed(Fan.FAST)
        self.fan1.set_radius(10)
        self.fan1.set_color("yellow")
        self.fan1.set_on(True)