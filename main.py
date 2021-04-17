from random import randint


class Unit:
    def __init__(self, name="", level=0, age=0, job="", personality="", skills=[]):
        self.name = name
        if name is "":
            self.give_name()

        self.level = level
        if level is 0:
            self.level = randint(1, 60)

        self.age = age
        if age is 0:
            self.age = randint(14, 49)

        self.job = job
        jobs = ["Fighter", "Wizard", "Thief", "Knight", "Magician", "Archer", "Monk"]
        if self.job is "" or self.job not in jobs:
            self.job = jobs[randint(0, len(jobs) - 1)]

        self.personality = personality
        personalities = ["Architect", "Thinker", "Commander", "Debater",
                         "Advocate", "Mediator", "Giver", "Champion",
                         "Inspector", "Protector", "Director", "Caregiver",
                         "Crafter", "Artist", "Persuader", "Performer"]
        if self.personality is "" or self.personality not in personalities:
            self.personality = personalities[randint(0, len(personalities) - 1)]

        self.attitude = 5

        self.condition = "Fine"

        self.strength = 0
        self.intelligence = 0
        self.agility = 0
        self.cunning = 0
        self.allure = 0
        self.get_stats()

        self.worth = self.calculate_worth()

        self.skills = {
            "Adept Student": False,     # Training - increases chance of success
            "Heavy Lifting": False,     # Labour - increases chance of success and lowers chance of injury
            "Awareness": False,         # Guard - increases chance of success
            "Manners": False,           # Guard - increases chance to excel
            "Hawk Eyes": False,         # Gambling - won't get tricked
            "Quick Hands": False,       # Gambling - can trick (lower level) opponents
            "Soldier Training": False,  # Battle - increases chance of success
            "Advanced Training": False, # Battle - increases chance of success (stacks with Soldier Training)
            "Glory Seeker": False,      # Battle - increases chance to excel
            "Passion for Art": False,   # Performance - increases chance of success
            "Flair": False,             # Performance - increases chance to excel
            "History": False,           # Tactician - increases chance of success
            "Commanding Voice": False,  # Tactician - increases chance to excel
            "Shinobi Training": False,  # Infiltration - increases chance of success
            "Gymnastics": False,        # Infiltration - increases chance of gaining agility points

            "Anti-Fighter": False,      # Eliminates weakness to Fighters
            "Anti-Wizard": False,       # Eliminates weakness to Wizards
            "Anti-Thief": False,        # Eliminates weakness to Thieves
            "Anti-Knight": False,       # Eliminates weakness to Knights
            "Anti-Magician": False,     # Eliminates weakness to Magicians
            "Anti-Archer": False,       # Eliminates weakness to Archers
            "Anti-Monk": False,         # Eliminates weakness to Monk
        }
        self.assign_skills(skills)

        self.work = {
            "Labour": 0,
            "Performance": 0,
            "Guard": 0,
            "Gambling": 0,
            "Battle": 0,
            "Tactician": 0,
            "Infiltration": 0
        }
        self.job_preferences()

    def give_name(self):
        names = ["Bob", "Steve", "Adam", "James", "Larry", "Grey"]
        self.name = names[randint(0, len(names) - 1)]

    def get_stats(self):
        # CLASS ############################
        if self.job == "Fighter":
            self.strength, self.allure = 2 * (self.level // 5), 1 * (self.level // 5)
        elif self.job == "Wizard":
            self.intelligence, self.cunning = 2 * (self.level // 5), 1 * (self.level // 5)
        elif self.job == "Thief":
            self.agility, self.allure = 2 * (self.level // 5), 1 * (self.level // 5)
        elif self.job == "Knight":
            self.strength, self.intelligence = 2 * (self.level // 5), 1 * (self.level // 5)
        elif self.job == "Magician":
            self.cunning, self.intelligence, self.allure = 1 * (self.level // 5), 1 * (self.level // 5), 1 * (
                        self.level // 5)
        elif self.job == "Archer":
            self.agility, self.cunning, self.strength = 1 * (self.level // 5), 1 * (self.level // 5), 1 * (
                        self.level // 5)
        else:
            self.strength, self.intelligence, self.allure = 1 * (self.level // 5), 1 * (self.level // 5), 1 * (
                        self.level // 5)
        # PERSONALITY ######################
        if self.personality == "Architect" or self.personality == "Thinker" or self.personality == "Commander" or self.personality == "Debater":
            self.intelligence += 2 * (self.level // 10)
        elif self.personality == "Advocate" or self.personality == "Mediator" or self.personality == "Giver" or self.personality == "Champion":
            self.strength += 2 * (self.level // 10)
        elif self.personality == "Inspector" or self.personality == "Protector" or self.personality == "Director" or self.personality == "Caregiver":
            self.agility += 2 * (self.level // 10)
        elif self.personality == "Crafter" or self.personality == "Artist" or self.personality == "Persuader" or self.personality == "Performer":
            self.cunning += 2 * (self.level // 10)
        # RANDOM ###########################
        skillPts = 7
        lst = []
        for i in range(4):
            if skillPts >= 2:
                randomNum = randint(1, 2)
                skillPts -= randomNum
                lst.append(randomNum)
            elif skillPts == 1:
                randomNum = randint(0, 1)
                skillPts -= randomNum
                lst.append(randomNum)
        lst.append(skillPts)
        self.strength += lst[0] * (self.level // 5)
        self.intelligence += lst[1] * (self.level // 5)
        self.agility += lst[2] * (self.level // 5)
        self.cunning += lst[3] * (self.level // 5)
        self.allure += lst[4] * (self.level // 10)

    def calculate_worth(self):
        total = self.level * 100
        total += self.strength * 2.5
        total += self.intelligence * 2.5
        total += self.agility * 2.5
        total += self.cunning * 2.5
        total += self.allure * 5
        if 25 > self.age > 50:
            total -= 10 * (self.age - 50)
        if self.condition is not "Fine":
            total *= 0.25
        return round(total, 2)

    def assign_skills(self, skills):
        for i in skills:
            if i in self.skills:
                self.skills[i] = True
        # 30-39: 33% chance for a skill, 3 times
        if 30 <= self.level < 40:
            for i in range(3):
                roll = randint(1, 3)
                if roll is 3:
                    self.get_random_skill()
        # 40-49: 50% chance for a skill, 3 times
        elif 40 <= self.level < 50:
            for i in range(3):
                roll = randint(1, 2)
                if roll is 1:
                    self.get_random_skill()
        # 50-59: 1 skill, 50% chance for a skill, 2 times
        elif 50 <= self.level < 60:
            self.get_random_skill()
            for i in range(2):
                roll = randint(1, 2)
                if roll is 1:
                    self.get_random_skill()
        # 60-70: 3 random skills
        elif self.level >= 60:
            for i in range(3):
                self.get_random_skill()

    def get_random_skill(self):
        possible_jobs = ["Adept Student"]
        if self.job == "Fighter":
            possible_jobs.append("Heavy Lifting")
            possible_jobs.append("Glory Seeker")
            possible_jobs.append("Soldier Training")
            possible_jobs.append("Anti-Thief")
        elif self.job == "Wizard":
            possible_jobs.append("History")
            possible_jobs.append("Commanding Voice")
            possible_jobs.append("Passion for Art")
            possible_jobs.append("Anti-Fighter")
        elif self.job == "Thief":
            possible_jobs.append("Gymnastics")
            possible_jobs.append("Hawk Eyes")
            possible_jobs.append("Quick Hands")
            possible_jobs.append("Anti-Wizard")
        elif self.job == "Knight":
            possible_jobs.append("Awareness")
            possible_jobs.append("Manners")
            possible_jobs.append("Soldier Training")
            possible_jobs.append("Anti-Archer")
        elif self.job == "Magician":
            possible_jobs.append("Flair")
            possible_jobs.append("Quick Hands")
            possible_jobs.append("Gymnastics")
            possible_jobs.append("Anti-Knight")
        elif self.job == "Archer":
            possible_jobs.append("Hawk Eyes")
            possible_jobs.append("Awareness")
            possible_jobs.append("History")
            possible_jobs.append("Anti-Magician")
        else:
            possible_jobs.append("Heavy Lifting")
            possible_jobs.append("Manners")
            possible_jobs.append("Shinobi Training")
        while True:
            randNum = randint(0, len(possible_jobs) - 1)
            if self.skills[possible_jobs[randNum]] is not True:
                self.add_skill(possible_jobs[randNum])
                break

    def add_skill(self, skill):
        self.skills[skill] = True

    def job_preferences(self):
        if self.personality == "Architect":
            self.work["Gambling"], self.work["Tactician"], self.work["Labour"], self.work["Performance"] = 1, 1, -1, -1
        elif self.personality == "Thinker":
            self.work["Battle"], self.work["Tactician"], self.work["Performance"], self.work["Guard"] = 1, 1, -1, -1
        elif self.personality == "Commander":
            self.work["Battle"], self.work["Tactician"], self.work["Gambling"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Debater":
            self.work["Performance"], self.work["Gambling"], self.work["Labour"], self.work["Guard"] = 1, 1, -1, -1
        elif self.personality == "Advocate":
            self.work["Performance"], self.work["Guard"], self.work["Battle"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Mediator":
            self.work["Performance"], self.work["Guard"], self.work["Battle"], self.work["Tactician"] = 1, 1, -1, -1
        elif self.personality == "Giver":
            self.work["Labour"], self.work["Battle"], self.work["Tactician"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Champion":
            self.work["Performance"], self.work["Gambling"], self.work["Guard"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Inspector":
            self.work["Tactician"], self.work["Infiltration"], self.work["Labour"], self.work["Battle"] = 1, 1, -1, -1
        elif self.personality == "Protector":
            self.work["Labour"], self.work["Guard"], self.work["Gambling"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Director":
            self.work["Labour"], self.work["Tactician"], self.work["Guard"], self.work["Battle"] = 1, 1, -1, -1
        elif self.personality == "Caregiver":
            self.work["Labour"], self.work["Guard"], self.work["Gambling"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Crafter":
            self.work["Performance"], self.work["Gambling"], self.work["Battle"], self.work["Tactician"] = 1, 1, -1, -1
        elif self.personality == "Artist":
            self.work["Performance"], self.work["Battle"], self.work["Labour"], self.work["Guard"] = 1, 1, -1, -1
        elif self.personality == "Persuader":
            self.work["Performance"], self.work["Infiltration"], self.work["Labour"], self.work["Battle"] = 1, 1, -1, -1
        else:
            self.work["Performance"], self.work["Battle"], self.work["Guard"], self.work["Tactician"] = 1, 1, -1, -1

        if self.job == "Fighter":
            self.work["Battle"] += 1
        elif self.job == "Wizard":
            self.work["Tactician"] += 1
        elif self.job == "Thief":
            self.work["Infiltration"] += 1
        elif self.job == "Knight":
            self.work["Guard"] += 1
        elif self.job == "Magician":
            self.work["Performance"] += 1
        elif self.job == "Archer":
            self.work["Gambling"] += 1
        else:
            self.work["Labour"] += 1


class Roster:
    def __init__(self, playerName):
        self.units = {0: Unit(playerName, 5, 20, "Fighter", "Commander", ["Adept Student"])}
        for i in range(9):
            self.units[len(self.units)] = Unit()
        self.print_all()

    def print_all(self):
        for i in self.units:
            current = self.units[i]
            print("\nUnit", i + 1, "/", len(self.units),
                  "\n=====================================================================================================")
            print("Name:\t\t\t", current.name)
            print("Level:\t\t\t", current.level)
            print("Age:\t\t\t", current.age)
            print("Job:\t\t\t", current.job)
            print("Personality:\t", current.personality)
            print("Attitude:\t\t", str(current.attitude) + "/10")
            print("Condition:\t\t", current.condition)
            if i == 0:
                print("Worth:\t\t\t", str(current.worth) + "$ (can't sell)")
            else:
                print("Worth:\t\t\t", str(current.worth) + "$")
            print(
                "-----------------------------------------------------------------------------------------------------")
            print("Strength:\t\t", current.strength)
            print("Intelligence:\t", current.intelligence)
            print("Agility:\t\t", current.agility)
            print("Cunning:\t\t", current.cunning)
            print("Allure:\t\t\t", current.allure)
            print("-----------------------------------------------------------------------------------------------------")
            temp = 0
            for j in current.skills:
                if current.skills[j] is True:
                    print(j)
                    temp += 1
            if temp is 0:
                print("No skills...")
            print("-----------------------------------------------------------------------------------------------------")
            print("Favourite jobs:")
            for j in current.work:
                if current.work[j] > 0:
                    print("", j+":", current.work[j])
            print("Least favourite jobs:")
            for j in current.work:
                if current.work[j] < 0:
                    print("", j+":", current.work[j])
            print(
                "=====================================================================================================")


if __name__ == '__main__':
    # playerName = input("So you are starting a mercenary agency, kid? I guess that means you're a real pro now. What do I need to address you by from now on?\n")
    # print(playerName+"'s Mercenaries? Sounds kinda generic if you ask me.")
    playerName = "Daniel"
    roster = Roster(playerName)
