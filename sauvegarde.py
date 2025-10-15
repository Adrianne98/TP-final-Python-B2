import json

def save_loop(loop_states, filename="loop.json"):
    with open(filename, "w") as f:
        json.dump(loop_states, f)
    print(f"Boucle sauvegardée dans {filename}")
