class CarsCollection:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print("Cars {} {} drive fast".format(self.make, self.model))

    def color(self):
        print("This car is red")

    def type(self):
        print("This is normal car")

    def __del__(self):
        print("Car {} {} was destroyed".format(self.make, self.model))
        self.make = ""
        self.model = ""


toyota = CarsCollection("Toyota", "Avensis")
toyota.type()


class SuperCar(CarsCollection):
    def __init__(self, make, model, top_speed):
        super(SuperCar, self).__init__(make, model)
        self.top_speed = top_speed
        print("This is {} {}. This car top speed is {}".format(self.make, self.model, self.top_speed))

    def type(self):
        print("This car is Awesome")


pagani = SuperCar("Pagani", "Zonda", "217mp/h")
pagani.color()
pagani.type()
