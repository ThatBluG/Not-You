# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image blacky = "bg_blacky.jpg"
image outside = "bg_out_house.jpg"
image house = "bg_house.jpg"
image inside = "bg_inside.jpg"
image kitchen = "bg_kitchen.jpg"
image bed = "bg_bedroom.jpg"
image hud = "hud.png"
image ccf = "chie.png"
image girl = "gril.png"
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

    show ccf

    Cf "Oh, you finally got here, Detective...{w} Anyway, to keep it short, the report came 20 minutes ago, and the body well.."

    Cf "I guess you could just take a look at it. It wouldn't be pretty, though."

    Cf "But before i go, {w} since this is your last case, I thank, you Detective, no, Mr. Ro-"

    "Officer" "CHIEF! THE DEPARTMENT IS CALLING!"

    Cf "Well, i need to go now. See you later, then."
    hide ccf

    scene blacky

    "Thud"
    "Thud"

    scene house
    "As he approach the house, he saw a garden and the door leading inside. Not knowing where the body is, he chose to go through.."

    menu house_or:
        "Enter the House":
            jump in_House
        "Go through the Garden":
            scene blacky
            "As he went to the garden he saw bits and pieces of a window."
            "Looking up he saw a broken window"
            "He then went inside"
            jump in_House
            #second playthrought then go to the garden
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
                    renpy.file(config.basedir + "/fLOWer.jpg")
                except:
                    open(config.basedir + "/fLOWer.jpg", "wb").write(renpy.file("fLOWer.jpg").read())
            "a fLO?"
            jump sevenAM
        "Left":
            "Checking the left pocket he found.."
            python:
                try:
                    renpy.file(config.basedir + "/leTter.jpg")
                except:
                    open(config.basedir + "/leTter.jpg", "wb").write(renpy.file("leTter.jpg").read())
            "A note of som-"
            with vpunch

            jump sevenAM
    return

label Garden:

    return

label sevenAM:
    "..."
    "..."
    "you should look at your files."
    "..."
    vc "Wake up.."
    vc "Waaakeee up..."
    vc "WAKE UP!"
    with hpunch
    #PUT SCENE BEDROOOM HERE

    scene bed

    vc "He woke up, due to the sound of the loud birds outside."

    vc "Confused at just what happened, with his little dream.{w} He decided t- annnd he went to the kitchen."
    
    scene kitchen
    show girl
    vc "The walk to the kitchen was short, after all its just in front of his bedroom."

    vc "In there he met his-"

    m "alright.. i get it."

    vc "Daughter..."

    vc "They were talking about, the people using the weird hoods."

    m "No.. everything.. is fine."

    vc "They, both then sat down onto their seats and continues eating."
    
    "..."
    hide girl
    scene bed

    "After eating he goes to the shower and then changes his clothes"

    scene blacky

    vc "After that he goes to work."

    "..."

    scene outside
    show ccf

    Cf "Oh, you finally got here, Detective...{w} Anyway, to keep it short, the report came 20 minutes ago, and the body well.."

    Cf "I guess you could just take a look at it. It wouldn't be pretty, though."

    Cf "We've also identified 4 suspects, and two have been interrogated."

    Cf "Hmm? Where's the file? I thought for sure i put it here"

    Cf "Well, sorry but i think i left the files at Station before.. but i do remember, those two."

    Cf "First one is Janet Smith, gender is male, and well he was gone from his home during the incident, spotted using a hood."

    Cf "Second Maria, a girl and we just kinda find her near the scene."

    "Officer" "CHIEF! THE DEPARTMENT IS CALLING!"

    Cf "Well, i need to go now. See you later, then."
    hide ccf
    scene blacky

    "Thud"
    "Thud"

    scene house
    "As he approach the house, he saw a garden and the door leading inside. Not knowing where the body is, he chose to go through.."

    menu house_or1:
        "Enter the House":
            jump in_House1

    return

label in_House1:

    return