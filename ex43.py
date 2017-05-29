from sys import exit
from random import randint

class Scene(object):

    def enter(self, cheat=False):
        print("This scene is not yet configured.", end=' ')
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self, cheat=False):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n--------")
            next_scene_name = current_scene.enter(cheat)
            if next_scene_name == "finished":
                break
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    quips = [
            "You died. You kinda suck at this.",
            "Your mon would be proud...if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
            ]

    def enter(self, cheat=False):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self, cheat=False):
        print("The Gothons of Planet Percal #25 have invaded your ship and")
        print("destroyed your entire crew. You are the last surviving member")
        print("and your last mission is to get the neutron destruct bomb from")
        print("the Weapons Armory, put it in the bridge, and blow the ship up")
        print("after getting into an escape pod.")
        print("\n")
        print("You're running down the central corridor to the Weapons Armory")
        print("when a Gothon jumps out, red scaly skin, dark grimy teeth, and")
        print("evil clown costume flowing around his hate filled body. He's")
        print("blocking the door to the Armory and about to pull a weapon to")
        print("blast you.")

        action = input("> ")

        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it at")
            print("the Gothon. His clown costume is flowing and moving around")
            print("his body, which throws off your aim. Your laser hits his")
            print("costume but misses him entirely. This completely ruins his")
            print("brand new costume his mother bought him, which makes him")
            print("fly into a rage and blast you repeatedly in the face until")
            print("you are dead. Then he eats you.")
            return 'death'
        elif action == "dodge!":
            print("Like a world class boxer you dodge, weave, slip and slide")
            print("right as the Gothon's blaster cranks a laser past your")
            print("head. In the middle of your artful dodge your foot slips")
            print("and you bang your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothon stomps")
            print("on your head and eats you.")
            return 'death'
        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the")
            print("academy. You tell the one Gothon joke you know:")
            print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur")
            print("fvgf nebhaq gur ubhfr.")
            print("The Gothon stops, tries not to laugh, then busts out")
            print("laughing and can't move. While he's laughing you run up")
            print("and shoot him square in the head putting him down, then")
            print("jump through the Weapon Armory door.")
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self, cheat=False):
        print("You do a dive roll into the Weapon Armory, crouch and scan the")
        print("room for more Gothons that might be hiding. It's dead quiet,")
        print("too quiet. You stand up and run to the far side of the room")
        print("and find the neutron bomb in its container. There's a keypad")
        print("lock on the box and you need the code to get the bomb out. If")
        print("you get the code wrong 10 times then the lock closes forever")
        print("and you can't get the bomb. The code is 3 digits.")
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        if cheat:
            print(code)
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("The container clicks open and the seal breaks, letting gas")
            print("out. You grab the neutron bomb and run as fast as you can")
            print("to the bridge where you must place it in the right spot.")
            return 'the_bridge'
        else:
            print("The lock buzzes one last time and then you hear a")
            print("sickening melting sound as the mechanism is fused")
            print("together. You decide to sit there, and finally the Gothons")
            print("blow up the ship from their ship and you die.")
            return 'death'

class TheBridge(Scene):

    def enter(self, cheat=False):
        print("You burst onto the Bridge with the neutron destruct bomb under")
        print("your arm and surprise 5 Gothons who are trying to take control")
        print("of the ship. Each of them has an even uglier clown costume")
        print("than the last. They haven't pulled their weapons out yet, as")
        print("they see the active bomb under your arm and don't want to set")
        print("it off.")

        action = input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons and")
            print("make a leap for the door. Right as you drop it a Gothon")
            print("shoots you right in the back killing you. As you die you")
            print("see another Gothon frantically try to disarm the bomb. You")
            print("die knowing they will probably blow up when it goes off.")
            return 'death'
        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under your arm and the")
            print("Gothons put their hands up and start to sweat. You inch")
            print("backward to the door, open it, and then carefully place")
            print("the bomb on the floor, pointing your blaster at it. You")
            print("then jump back through the door, punch the close button")
            print("and blast the lock so the Gothons can't get out.")
            print("Now that the bomb is placed you run to the escape pod to")
            print("get off this tin can.")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self, cheat=False):
        print("You rush through the ship desperately trying to make it to the")
        print("escape pod before the whole ship explodes. It seems like")
        print("hardly any Gothons are on the ship, so your run is clear of")
        print("interference. You get tot he chamber with the escape pods, and")
        print("now need to pick one to take. Some of them could be damaged")
        print("but you don't have time to look. There's 5 pods, which one do")
        print("you take?")

        good_pod = randint(1,5)
        if cheat:
            print(good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then implodes")
            print("as the hull ruptures, crushing your body into jam jelly.")
            return 'death'
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to the planet")
            print("below. As it flies to the planet, you look back and see")
            print("your ship implode then explode like a bright star, taking")
            print("out the Gothon ship at the same time. You won!")
            return 'finished'

class Map(object):

    scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death(),
            }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play(True)
