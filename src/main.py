"""
Martingale roulette strategy simulation.

50/50 chance of red/black on each round, no house edge.
"""

import matplotlib.pyplot as plt
import random
import json

__CONFIG__ = json.loads((f := open("./config.json")).read()); f.close()

player = {
    "cash": __CONFIG__["cash"],
    "betAmount": __CONFIG__["betAmount"]
}

rounds = []

def getColor() -> str:
    return random.choice(["Red", "Black"])


plt.title(f"Martingale roulette simulation ({__CONFIG__['color']} - ${__CONFIG__['betAmount']})")
plt.xlabel("Rounds")
plt.ylabel("Cash ($)")

while len(rounds) < __CONFIG__["rounds"]:
    randomColor = getColor()

    if randomColor.lower() == __CONFIG__["color"].lower():
        player["cash"] += player["betAmount"] * 2
        player["betAmount"] = 1
    else:
        player["cash"] -= player["betAmount"]
        player["betAmount"] *= 2
    
    rounds.append({"EndingAmount": player["cash"], "Win": randomColor.lower() == __CONFIG__["color"].lower(), "BetAmount": player["betAmount"]})

    plt.plot([i for i in range(len(rounds))], [int(round["EndingAmount"]) for round in rounds], color=__CONFIG__["color"].lower())
    plt.pause(0.01)

(f := open("./results.txt", "w")).write(str(rounds)); f.close()
