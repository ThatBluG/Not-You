# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image blacky = "bg_blacky.jpg"
image outside = "bg_out_house.jpg"
image house = "bg_house.jpg"
image inside = "bg_inside.jpg"
image kitchen = "bg_kitchen.jpg"
define Cf = Character("Chief")
define vc = Character(None, what_italic = True)
define m = Character("Miyori")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene blacky

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    "..."
    "..."
    "..."

    scene outside

    Cf "Oh, you finally got here, Detective...{w} Anyway, to keep it short, the report came 20 minutes ago, and the body well.."

    Cf "I guess you could just take a look at it. It wouldn't be pretty, though."

    Cf "But before i go, {w} since this is your last case, I thank, you Detective, no, Mr. Ro-"

    "Officer" "CHIEF! THE DEPARTMENT IS CALLING!"

    Cf "Well, i need to go now. See you later, then."

    scene blacky

    "Thud"
    "Thud"

    scene house
    "As he approach the house, he saw a garden and the door leading inside. Not knowing where the body is, he chose to go through.."

    menu house_or:
        "Enter the House":
            jump in_House
        "Go through the Garden":
            jump Garden
    # This ends the game.

    return

label in_House:
    scene inside
    "Going inside, he decides to look around, nothing seems out of the ordinary in the kitchen or in the master bedroom."

    "He then decides to go into the living room, inside it was broken furnitre, bits of vases, and glasses, it was obvious there are signs of the victim struggle struggle."

    "Looking around a bit more he found a stairway leading to the second floor.."

    scene blacky
    "Thud"
    "Thud"

    "In there he found a body lying in the ground, with warning signs all over the room."

    "He decided to oame closer to the body, looking closer at it, somenthing sticks out of the pocket of the victim."

    menu which_pocket:
        "Right":
            "Checking the left pocket he found.."
            python:
                try:
                    open(config.basedir + "/game/catnip/sayori.jpg")
                except:
                    open(config.basedir + "/game/catnip/sayori.jpg", "wb").write(renpy.file("cLue1.jpg").read())

            jump sevenAM
        "Left":
            "Checking the left pocket he found.."
            python:
                try:
                    open(config.basedir + "/game/catnip/first_letter.txt")
                except:
                    open(config.basedir + "/game/catnip/first_letter.txt", "wb").write(renpy.file("cLue11.jpg").read())
            "A note of som-"
            with vpunch

            jump sevenAM
    return

label Garden:

    return

label sevenAM:
    vc "Wake up.."
    vc "Waaakeee up..."
    vc "WAKE UP!"
    with hpunch
    #PUT SCENE BEDROOOM HERE
    vc "He woke up, due to the sound of the loud birds outside."

    vc "Confused at just what happened, with his little dream.{w} He decided t- annnd he went to the kitchen."
    
    scene kitchen

    vc "The walk to the kitchen was short, after all its just in front of his bedroom."

    vc "In there he met his-"

    m "alright.. i get it."

    return