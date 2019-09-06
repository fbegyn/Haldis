from app import create_app
from models import db
import add_oceans_garden, add_admins, add_simpizza, add_primadonna, add_fitchen, add_fom

manager = create_app()

entry_sets = {
    "Admins": add_admins.add,
    "Ocean's Garden": add_oceans_garden.add,
    "SimPizza": add_simpizza.add,
    "Primadonna": add_primadonna.add,
    "Fitchen": add_fitchen.add,
    "Frag-o-matic": add_fom.add
}

yes = ["yes", "y", "Y"]
no = ["no", "n", "N"]


# Commit all the things
def commit():
    db.session.commit()
    print("Committing successful")


def check_if_overwrite():
    answer = input("Do you want to overwrite the previous database? (y/N) ")
    return answer in yes


def add_all():
    for entry_set in entry_sets.keys():
        print("Adding {}.".format(entry_set))
        entry_sets[entry_set]()


def recreate_from_scratch():
    confirmation = "Are you very very sure? (Will delete previous entries!) (y/N) "
    check = "I acknowledge any repercussions!"
    if input(confirmation) in yes and input("Type: '{}' ".format(check)) == check:
        print("Resetting the database!")
        db.drop_all()
        db.create_all()
        add_to_current()


def add_to_current():
    available = [entry_set for entry_set in entry_sets]

    def add_numbers():
        return "  ".join(
            ["{}({}), ".format(loc, i) for i, loc in enumerate(available)]
        ).rstrip(", ")

    while input("Do you still want to add something? (Y/n) ") not in no:
        print(
            "What do you want to add? (Use numbers, or A for all, or C for cancel)   "
        )
        answer = input("Available: {}  : ".format(add_numbers()))
        if answer == "A":
            add_all()
            available = []
        elif answer == "C":
            pass
        elif answer in [str(x) for x in range(len(available))]:
            answer = int(answer)
            print("Adding {}.".format(available[answer]))
            entry_sets[str(available[answer])]()
            del available[answer]
        else:
            print("Not a valid answer.")
    print("Thank you for adding, come again!")


def init():
    print("Database modification script!")
    print("=============================\n\n")
    if check_if_overwrite():
        recreate_from_scratch()
    else:
        add_to_current()
    commit()


init()
