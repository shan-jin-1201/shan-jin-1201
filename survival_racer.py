# -*- coding: utf-8 -*-
"""A simple text-based survival racing game with items."""

import random

LANES = ["left", "middle", "right"]
ITEMS = [
    "repair",      # recovers health
    "shield",      # blocks next obstacle
    "nitro",       # skip obstacles for 2 turns
    "coin",        # adds score
    "mystery",     # random effect
]


def random_event():
    """Return a random track event for a lane."""
    choices = ["obstacle"] + ITEMS + [None]  # None represents an empty lane
    return random.choice(choices)


def apply_item(state, item):
    if item == "repair":
        state["health"] = min(100, state["health"] + 20)
        print("You found a repair kit! Health restored by 20.")
    elif item == "shield":
        state["shield"] = True
        print("You picked up a shield! It will block the next obstacle.")
    elif item == "nitro":
        state["nitro"] += 2
        print("Nitro acquired! Skip obstacles for the next 2 turns.")
    elif item == "coin":
        state["score"] += 10
        print("You grabbed a coin! Score +10.")
    elif item == "mystery":
        mystery = random.choice(["repair", "shield", "nitro", "coin", "nothing"])
        if mystery == "nothing":
            print("Mystery box was empty!")
        else:
            apply_item(state, mystery)
    else:
        pass


def display_status(state):
    print(f"Health: {state['health']} | Score: {state['score']} | Nitro: {state['nitro']} | Shield: {state['shield']}")


def main():
    state = {"health": 100, "score": 0, "nitro": 0, "shield": False}
    turn = 0
    print("Welcome to Survival Racer! Dodge obstacles and collect items to survive.")

    while state["health"] > 0:
        turn += 1
        print(f"\n-- Turn {turn} --")
        events = {lane: random_event() for lane in LANES}
        # Show lanes without revealing events
        print("Choose a lane: left (l), middle (m), right (r)")
        choice = input("Your lane [l/m/r]: ").strip().lower()
        lane = {
            "l": "left",
            "m": "middle",
            "r": "right"
        }.get(choice, "middle")

        event = events[lane]
        if event == "obstacle":
            if state["shield"]:
                state["shield"] = False
                print("Your shield absorbed an obstacle!")
            elif state["nitro"] > 0:
                state["nitro"] -= 1
                print("Nitro activated! You zoom past an obstacle unharmed.")
            else:
                state["health"] -= 20
                print("Crash! You hit an obstacle and lost 20 health.")
        elif event:
            apply_item(state, event)
        else:
            print("Nothing here. You race forward unhindered.")

        display_status(state)

    print("\nGame Over! Your final score is", state["score"])


if __name__ == "__main__":
    main()
