# Represent a building with rooms

# a room can be either clean or dirty
# a room should be able to be made clean or dirty
# a room starts off clean
class Room():
    def __init__(self):
        self.is_clean = True

    def clean(self):
        self.is_clean = True

    def dirty(self):
        self.is_clean = False

    def __str__(self):
        state = ""
        if self.is_clean:
            state = "clean"
        else:
            state = "dirty"
        return state


# a building should have an address and a number of rooms
# a room should start clean and can become dirty
# it should be possible to "use" a room, if it is used it becomes dirty
# a room should also be able to be cleaned
class Building():
    def __init__(self, address, num_rooms):
        self.address = address
        self.rooms = []
        for i in range(num_rooms):
            new_room = Room()
            self.rooms.append(new_room) 
        # len(self.rooms) == num_rooms

    def use_room(self, room_num):
        room = self.rooms[room_num]
        room.dirty()

    def clean_room(self, room_num):
        room = self.rooms[room_num]
        room.clean()

    def __str__(self):
        result = ""
        result += self.address + "\n"
        for i in range(len(self.rooms)):
            room = self.rooms[i]
            result += "\tRoom " + str(i) + " is " + str(room) + "\n"
        return result

house = Building("123 Main St.", 8)
print(house)
house.use_room(1)
house.use_room(4)
house.use_room(6)
print(house)
house.clean_room(4)
house.clean_room(6)
print(house)