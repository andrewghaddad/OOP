class Toy():
    """
    A class to represent a toy given to a dog
    """
    def __init__(self, sound):
        pass

    def squeeze(self):
        pass # produce a sound

class Dog():
    HYPER_BREEDS = ["Jack Russels", "Chihuahua", "Spaniel"]
    NUM_HYPER_SQUEEZES = 3
    def __init__(self, breed):
        # should init a toy property to be None
        pass

    def give_toy(self, new_toy):
        pass

    def play(self):
        # if a dog doesn't have a toy, it should "woof"
        # if a dog has a toy and is not a hyper breed: it should squeeze the toy once
        # otherwise it should squeeze the toy NUM_HYPER_SQUEEZES times
        pass