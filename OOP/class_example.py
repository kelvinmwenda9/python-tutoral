class House:

    num_rooms = 5
    bathrooms = 4

    def cost_evaluation(self, rate):
        cost = rate * self.num_rooms
        return cost


house = House()
print(house.num_rooms)
house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)


'''Hello World'''

