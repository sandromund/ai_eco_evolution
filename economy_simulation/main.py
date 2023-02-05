from world import World

from god import God


if __name__ == "__main__":

    god = God()

    w = World(humans=god.crate_humans(10))

    w.companies[0].customers = w.humans[5:]
    w.companies[0].employers = w.humans[:5]
    w.companies[1].customers = w.humans[:5]
    w.companies[1].employers = w.humans[5:]
    w.meta_data()
    w.run(100)
    print("\n\n")
    w.meta_data()