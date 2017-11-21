import pygame

pygame.mixer.init()

# Maybe you can subclass the pygame.mixer.Sound and
# add the methods below to it..
class Fader(object):
    instances = []
    def __init__(self, fname):
        super(Fader, self).__init__()
        self.sound = pygame.mixer.Sound(fname)
        self.increment = 0.01 # tweak for speed of effect!!
        self.next_vol = 0.1 # fade to 100 on start
        Fader.instances.append(self)

    def fade_to(self, new_vol):
        # you could change the increment here based on something..
        self.next_vol = new_vol

    @classmethod
    def update(cls):
        for inst in cls.instances:
            curr_volume = inst.sound.get_volume()
            # print inst, curr_volume, inst.next_vol
            if inst.next_vol > curr_volume:
                inst.sound.set_volume(curr_volume + inst.increment)
            elif inst.next_vol < curr_volume:
                inst.sound.set_volume(curr_volume - inst.increment)