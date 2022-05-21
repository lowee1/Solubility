import random
import click


class Ion:
    def __init__(self, name, symbol, charge):
        self.name = name
        self.symbol = symbol
        self.charge = charge

    def type(self):
        return "cation" if self.charge > 0 else "anion"

    def __str__(self) -> str:
        return (
            click.style(self.symbol, fg="green")
            if self.charge > 0
            else click.style(self.symbol, fg="red")
        )


# cations
sodium = Ion("Sodium", "Na", 1)
potassium = Ion("Potassium", "K", 1)
calcium = Ion("Calcium", "Ca", 2)
magnesium = Ion("Magnesium", "Mg", 2)
barium = Ion("Barium", "Ba", 2)
silver = Ion("Silver", "Ag", 1)
ammonium = Ion("Ammonium", "NH4", 1)
lead = Ion("Lead", "Pb", 2)
cations = (sodium, potassium, calcium, magnesium, barium, silver, ammonium, lead)

# anions
nitrate = Ion("Nitrate", "NO3", -1)
sulfate = Ion("Sulfate", "SO4", -2)
chloride = Ion("Chloride", "Cl", -1)
carbonate = Ion("Carbonate", "CO3", -2)
hydroxide = Ion("Hydroxide", "OH", -1)
anions = (nitrate, sulfate, chloride, carbonate, hydroxide)


def check_solubility(cation: Ion, anion: Ion) -> bool:
    """returns whether the compound is soluble or not

    Args:
        cation (Ion): a cation
        anion (Ion): an anion

    Returns:
        bool: whether the compound is soluble or not
    """
    # sodium potassium and ammonium salts
    if cation == sodium or cation == potassium or cation == ammonium:
        return True

    # all nitrate soluble
    if anion == nitrate:
        return True

    # most chloride are soluble
    if anion == chloride:
        # except silver and lead chloride
        if cation == silver or cation == lead:
            return False
        return True

    # most sulfates are soluble
    if anion == sulfate:
        # except lead, barium and calcium sulfate
        if cation == lead or cation == barium or cation == calcium:
            return False
        return True

    # most carbonates and hydroxides are insoluble
    # except for sodium potassium and ammonium (at the top)
    if anion == carbonate or anion == hydroxide:
        return False

    return True


def solubility_enquiry():
    """asks the user for a cation and anion and click.echos whether the compound is soluble or not"""
    cation_names = [c.name for c in cations]
    anion_names = [a.name for a in anions]

    cation = ""
    while cation not in cation_names:
        cation = input("Enter cation: ")
        if cation not in cation_names:
            click.echo(click.style("Invalid cation", fg="orange"))

    anion = ""
    while anion not in anion_names:
        anion = input("Enter anion: ")
        if anion not in anion_names:
            click.echo(click.style("Invalid anion", fg="orange"))

    cation: Ion = [c for c in cations if c.name == cation][0]
    anion: Ion = [a for a in anions if a.name == anion][0]

    if check_solubility(cation, anion):
        click.echo("The compound is soluble in water.")
    else:
        click.echo("The compound is not soluble in water.")


def solubility_quiz():
    """a continuous quiz to test if the user can determine if a randomly selected compound is soluble or not"""

    score = 0
    question_count = 0
    while True:
        # generate a random anion and cation
        anion = random.choice(anions)
        cation = random.choice(cations)

        # click.echo the question
        click.echo("Is " + str(cation) + " " + str(anion) + " soluble in water?")

        # get the user's answer
        answer = input("Enter yes or no: ")

        # check if the answer is correct
        if (check_solubility(cation, anion) and answer == "yes") or (
            not check_solubility(cation, anion) and answer == "no"
        ):
            click.echo(click.style("Correct!", fg="green"))
            score += 1
        else:
            click.echo(click.style("Incorrect!", fg="red"))

        question_count += 1
        if question_count == 10:
            # ask if the user wants to continue
            answer = input("Continue? (y/n) ")
            if answer == "n":
                click.echo("You scored " + str(score))
                break
        question_count %= 10


while True:
    # ask if the user wants to check individual compounds or do a quiz
    click.echo(
        """
    1. Check individual compounds
    2. Do a quiz
    3. Exit
    """
    )
    choice = input("Enter your choice: ")
    if choice == "1":
        solubility_enquiry()
    elif choice == "2":
        solubility_quiz()
    elif choice == "3":
        break
    else:
        click.echo("Invalid choice.")
