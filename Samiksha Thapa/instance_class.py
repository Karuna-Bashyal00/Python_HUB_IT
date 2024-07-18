class House():
    def __init__(self, owner):
        self.owner = owner

    def set_house_color(self, color):
        self.color = color

    def get_house_color(self):
        return (f'House Owner: {self.owner}'+ ' ' + f'House Color: {self.color}')

mero_ghar = House('Lily')
mero_ghar.set_house_color('blue')
print(mero_ghar.get_house_color())

mero_ghar2 = House('Dipen')
mero_ghar2.set_house_color('purple')
print(mero_ghar2.get_house_color())