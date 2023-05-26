# Adventure Game

import random as rdm
import time as tme
from pymodalbox import *


def verified(sel, selction):
    try:
        if sel in selction:
            return True
        else:
            return False
    except Exception:
        return False


def shuffleWithoutRepating(objArray):
    rdm.shuffle(objArray)
    if "gloves" in objArray:
        return objArray
    if len(objArray):
        return [objArray.pop(0), objArray]


def userDetails(info):
    tme.sleep(0.5)
    playerInfo = input("Enter your " + info + "?: ")

    if str(playerInfo) == "":
        print("exit successful.")
        exit()

    print(f"{info} is {playerInfo}\n")


def huntForWeapons(place, weapon, inventory):
    tme.sleep(0.5)
    confirmed = False

    while not confirmed:
        askToCollect = input(
            "You reached a " + place + ", pick up a weapon? (Y)es or (N)o: "
        )
        if verified(askToCollect.upper(), ["Y", "N"]):
            confirmed = True

            if askToCollect.lower() == "y":
                print(f"You picked up {weapon}.")
                inventory.insert(0, weapon)
            else:
                print(f"You back away from the {place} too scared to continue.")
        else:
            print("Not made your mind yet. Please enter 'Y' or 'N' to continue")
        tme.sleep(0.1)

    print(f"Your inventory collections is:\n{inventory}\n")


def fillYourInventory(i, inventory):
    questArray = [
        "home",
        "gloves",
        "cave",
        "sword",
        "hill",
        "axe",
        "snow",
        "rake",
        "park",
        "crowbar",
        "shop",
        "Iron-rod",
    ]

    tme.sleep(0.1)
    print(f"You reached a {questArray[0]}. You picked up {questArray[1]}.")
    inventory.append(questArray[1])
    print(f"Your inventory collections is:\n{inventory}\n")
    tme.sleep(1)

    while i < 12:
        huntForWeapons(questArray[i], questArray[i + 1], inventory)
        tme.sleep(1)
        i += 2

    print("You reach the end of your journey feeling tired.")
    tme.sleep(0.7)
    itemsText = "item" if len(inventory) == 1 else "items"
    print(
        f"Unpacking your inventory you find. You collected {str(len(inventory))} {itemsText}.\n"
    )

    print(f"Your inventory collections is:\n{inventory}\n")


def fightingMonsters(inventory):
    # Monster collections array
    googlis = ["Skeleton", "Zombie", "Wolf", "dragon", "Werewolf"]
    rewards = ["hammer", "pistol", "hacksaw", "chisel", "hand-drill"]
    loss = ["Vampire", "Ogre", "Hydra", "Griffin", "Siren"]

    try:
        while True:
            # Attack monster
            monster = rdm.choice(googlis)
            print(f"You've been attacked by a {monster}\n")
            pickAFight = False

            while not pickAFight:
                first_letter = []
                for w in inventory:
                    first_letter.append(w[0].title())

                tme.sleep(1)
                weapon = input(
                    "choice a weapon from your inventory to fight "
                    + monster
                    + "\n"
                    + "List of wapons in your inventory are:"
                    + "\n"
                    + str(first_letter)
                    + "\n:"
                )

                # choice a weapon from your inventory to fight monster
                if verified(weapon.upper(), first_letter):
                    pickAFight = True

                    for w in inventory:
                        if weapon.lower() == w[0]:
                            print(f"You've selected {w}")

                    if weapon.lower() != "g":
                        print(f"\nYou killed {monster}.\n")
                        googlis.remove(monster)

                        if len(rewards) != 0:
                            questRandom = shuffleWithoutRepating(rewards)
                            inventory.insert(0, questRandom[0])
                    else:
                        del inventory[0]
                        print(f"You killed by {monster}.\n")

                        if len(loss) != 0:
                            questRandom = shuffleWithoutRepating(loss)
                            googlis.append(questRandom[0])
                else:
                    print(
                        "You didn't select weapon in your inventory. Choice the right weapon to fight the monster.\n"
                    )
                tme.sleep(1)

            print(
                f"Your new inventory collections is:\n{inventory}\n"
                if len(googlis) != 0
                else f"Your new inventory collections is empty\n"
            )
            print(
                f"Googlies still around is: {googlis}\n"
                if len(googlis) != 0
                else f"Googlies still around is empty\n"
            )

            if len(googlis) == 0:
                print(
                    "You killed all monsters. Congratulation you win the game!"
                    + "\n"
                    + "\n"
                    + "Starting a new game."
                )
                raise Exception
                # return
            elif len(inventory) == 0:
                print(
                    "You ran out of weapons. You lost the game!"
                    + "\n"
                    + "\n"
                    + "Starting a new game."
                )
                raise Exception
                # return

    except Exception:
        tme.sleep(2)
        main_func()


def start_game(inventory=[]):
    userDetails("username")
    tme.sleep(0.5)
    userDetails("passcode")
    print("Username and passcode correct! Continue to play the game.\n")
    tme.sleep(1)

    fillYourInventory(2, inventory)
    tme.sleep(1)

    fightingMonsters(inventory)


def main_func():
    confirmed = False
    while not confirmed:
        print(
            "\n"
            + "Monster's Game"
            + "\n"
            + "You are been attcked by monsters. Build your weapon inventory and select from it to kill each monster"
            + "\n"
            + "\n"
            + "MAIN MENU:"
            + "\n"
            + "Choose (1) to play the game."
            + "\n"
            + "Choose (2) to exit."
            + "\n"
            + "\n"
            + "PLAY GAME    (Enter 1)"
            + "\n"
            + "EXIT GAME    (Enter 2)"
            + "\n"
        )

        tme.sleep(1)
        try:
            input_option = int(input(">>>>> Please enter a number: "))

            if verified(input_option, [1, 2]):
                confirmed = True
                tme.sleep(1)

                if input_option == 1:
                    start_game()
                elif input_option == 2:
                    print("You cancelled the game.")
            else:
                print("Ooops! Please enter only number: (1 - 2): ")

        except ValueError:
            print("Oi! You can only enter number: (1 - 2) ")
        finally:
            tme.sleep(1)


if __name__ == "__main__":
    main_func()
