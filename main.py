from random import randint
from time import sleep


# from roster import Roster
# from roster import Unit
# from hiring_menu import hiring_board


# hiring_menu ##########################################################################################################
def hire_list():
    menu = []
    while len(menu) < 5:
        new_unit = Unit("", randint(1, 15))
        if new_unit.worth < System.money * 0.85:
            menu.append(new_unit)
    for i in range(len(menu)):
        print(str(i + 1) + ":")
        menu[i].short_description()
    return menu


def hiring_board():
    lst = hire_list()
    while True:
        choice = int(input("\nWhich one do you want to hire? Press 0 to exit.\n"))
        if 0 < choice < len(lst) + 1 and lst[choice - 1].calculate_worth() <= System.money:
            choice2 = int(input("You want " + lst[choice - 1].name + "? (1 for yes, 0 for no)\n"))
            if choice2 == 1:
                break
        elif choice == 0:
            return
        elif lst[choice - 1].calculate_worth() > System.money:
            print("Sorry,",
                  System.playerName + ". I can't give credit! Come back when you're a little... MMMMMMM... Richer!")
        else:
            print("Error, try again.")
    System.money = System.money - lst[choice - 1].calculate_worth()
    return lst[choice - 1]


# roster ###############################################################################################################
class Unit:
    def __init__(self, name="", level=0, birthday=[0, 0], age=0, job="", personality="", skills=[], commander=False):
        self.name = name
        if name is "":
            self.give_name()

        self.level = level
        if level is 0:
            self.level = randint(1, 60)

        self.age = age
        if age is 0:
            self.age = randint(14, 49)

        self.birthday = birthday
        if birthday == [0, 0]:
            self.birthday = [randint(1, 12), randint(1, 4)]

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

        self.current_job = None
        self.condition = "Fine"

        self.strength = 0
        self.intelligence = 0
        self.agility = 0
        self.cunning = 0
        self.allure = 0
        self.get_stats()

        self.worth = 0

        self.skills = {
            "Adept Student": False,  # Training - increases chance of success
            "Heavy Lifting": False,  # Labour - increases chance of success and lowers chance of injury
            "Awareness": False,  # Guard - increases chance of success
            "Manners": False,  # Guard - increases chance to excel
            "Hawk Eyes": False,  # Gambling - won't get tricked
            "Quick Hands": False,  # Gambling - can trick (lower level) opponents
            "Soldier Training": False,  # Battle - increases chance of success
            "Advanced Training": False,  # Battle - increases chance of success (stacks with Soldier Training)
            "Glory Seeker": False,  # Battle - increases chance to excel
            "Passion for Art": False,  # Performance - increases chance of success
            "Flair": False,  # Performance - increases chance to excel
            "History": False,  # Tactician - increases chance of success
            "Commanding Voice": False,  # Tactician - increases chance to excel
            "Shinobi Training": False,  # Infiltration - increases chance of success
            "Gymnastics": False,  # Infiltration - increases chance of gaining agility points

            "Anti-Fighter": False,  # Eliminates weakness to Fighters
            "Anti-Wizard": False,  # Eliminates weakness to Wizards
            "Anti-Thief": False,  # Eliminates weakness to Thieves
            "Anti-Knight": False,  # Eliminates weakness to Knights
            "Anti-Magician": False,  # Eliminates weakness to Magicians
            "Anti-Archer": False,  # Eliminates weakness to Archers
            "Anti-Monk": False,  # Eliminates weakness to Monk
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

        self.commander = commander

    def give_name(self):
        names = [
            "Adam", "Avery", "Allen", "Aaron", "Alexander", "Anthony",
            "Bob", "Brendon", "Bryce", "Benji", "Boris", "Baker",
            "Clement", "Chandler", "Collin", "Cody", "Chucky", "Curtis",
            "Derrick", "Darell", "Dune", "Dwain", "Doug", "David",
            "Ed", "Elijah", "Emile", "Earl", "Elliott", "Elroy", "Elwood",
            "Frank", "Fabian", "Foster", "Florence", "Finn", "Frederick",
            "Grey", "Graham", "George", "Gill",
            "Harold", "Harvey", "Hugh", "Hector", "Holden",
            "Ivan", "Irving", "Isaac", "Ignatius", "Inigo",
            "James", "Jeffrey", "John", "Justin", "Jimmy", "JoJo",
            "Kade", "Koby", "Ken", "Kurt", "Keith", "Karl",
            "Larry", "Leon", "Lance", "Lincoln", "Louis", "Lucius",
            "Michael", "Melvin", "Marvin", "Matthew", "Murray", "Morgan",
            "Nick", "Nigel", "Normand", "Nathan", "Noah", "Ned",
            "Oswin", "Oliver", "Owen", "Otis", "Orville",
            "Patrick", "Palmer", "Pierce", "Peter", "Porter", "Philip", "Paul",
            "Quincy",
            "Rufus", "Ryder", "Rolland", "Rhett", "Raymond", "Roy", "Richard",
            "Steven", "Sam", "Stanley", "Sylvain", "Simon", "Scott",
            "Tatum", "Tristen", "Thomas", "Tim", "Tyler", "Theodore",
            "Ulysses", "Ulric",
            "Vance", "Vernon", "Victor", "Vincent", "Val",
            "William", "Wayne", "Wallace", "Wesley", "Wright",
            "Xavier",
            "Zach", "Zeke", "Zeph", "Zayne",

            "Amy", "Alicia", "Athena", "Alice",
            "Beverly", "Bridget", "Briana",
            "Camellia", "Cecilia", "Charlie",
            "Danica", "Deborah", "Donna",
            "Elizabeth", "Edith", "Emily",
            "Ferne", "Fiona", "Francine",
            "Gabrielle", "Gilda", "Gloria",
            "Hayley", "Harlow", "Hortense",
            "Isabelle", "Ilene", "Iris",
            "Jodene", "Jacqueline", "June", "Jill",
            "Kori", "Katherine", "Kelly",
            "Lora", "Lacy", "Leslie",
            "Mackenzie", "Madonna", "Marie",
            "Nancy", "Natalie", "Noelle",
            "Olivia", "Oakley", "Odilia",
            "Pamella", "Paige", "Peggy", "Phoebe",
            "Queen",
            "Rebecca", "Rosalie", "Ruby",
            "Shayna", "Sinclair", "Sabrina", "Stephanie",
            "Talia", "Theresa", "Tana",
            "Ursula", "Ulyssa", "Unice",
            "Valerie", "Veronica", "Vivian",
            "Winter", "Wilma", "Wendy",
            "Xanthia",
            "Yolanda", "Yasmin", "Yona",
            "Zoey", "Zaria", "Zella"
        ]
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
        total = self.level * 50
        total += self.strength * 2.5
        total += self.intelligence * 2.5
        total += self.agility * 2.5
        total += self.cunning * 2.5
        total += self.allure * 5
        if self.age < 25:
            total *= 0.9
        elif self.age > 50:
            total -= 10 * (self.age - 50)
        if self.condition is not "Fine":
            total *= 0.25
        return round(total, 3)

    def calculate_wage(self):
        return self.level * 5

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
            self.work["Performance"], self.work["Gambling"], self.work["Guard"], self.work[
                "Infiltration"] = 1, 1, -1, -1
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

    def short_description(self):
        if self.commander:
            print(self.name, "(Commander)")
        else:
            print(self.name)
        print("Lvl.", self.level, self.job, "\t", self.age, "years old\tWorth:",
              str(self.calculate_worth()) + "$\tMonthly wage:", str(self.calculate_wage()) + "$")
        if self.condition is not "Fine":
            print(self.condition)
        elif self.current_job is not None:
            print("Currently working")
        print("-----------------------------------------------------------------------------------------------------")

    def long_description(self):
        print("=====================================================================================================")
        if self.commander:
            print("Name:\t\t\t", self.name, "(Commander)")
        else:
            print("Name:\t\t\t", self.name)
        print("Level:\t\t\t", self.level)
        print("Age:\t\t\t", self.age)
        print("Birthday:\t\t", "M" + str(self.birthday[0]) + ",W" + str(self.birthday[1]))
        print("Job:\t\t\t", self.job)
        print("Personality:\t", self.personality)
        print("Attitude:\t\t", str(self.attitude) + "/10")
        if self.current_job is not None:
            print("Current job:\t\t\t", self.current_job)
        else:
            print("Current job:\t Awaiting work")
        print("Condition:\t\t", self.condition)
        print("Worth:\t\t\t", str(self.calculate_worth()) + "$")
        print("Yearly wage:\t", str(self.calculate_wage()) + "$")
        print(
            "-----------------------------------------------------------------------------------------------------")
        print("Strength:\t\t", self.strength)
        print("Intelligence:\t", self.intelligence)
        print("Agility:\t\t", self.agility)
        print("Cunning:\t\t", self.cunning)
        print("Allure:\t\t\t", self.allure)
        print(
            "-----------------------------------------------------------------------------------------------------")
        temp = 0
        for j in self.skills:
            if self.skills[j] is True:
                print(j)
                temp += 1
        if temp is 0:
            print("No skills...")
        print(
            "-----------------------------------------------------------------------------------------------------")
        print("Favourite jobs:")
        for j in self.work:
            if self.work[j] > 0:
                print("", j + ":", self.work[j])
        print("Least favourite jobs:")
        for j in self.work:
            if self.work[j] < 0:
                print("", j + ":", self.work[j])
        print("=====================================================================================================")


class Roster:
    def __init__(self, playerName):
        self.units = {0: Unit(playerName, 5, [3, 4], 20, "Fighter", "Commander", ["Adept Student"], True)}
        # for i in range(4):
        #     self.units[len(self.units)] = Unit()
        # self.print_all()

    def add_unit(self, new_unit):
        self.units[len(self.units)] = new_unit

    def print_all(self):
        print()
        for i in self.units:
            current = self.units[i]
            print("Unit", i + 1, "/", len(self.units))
            current.short_description()
            # if len(current.name) >= 6:
            #     print("", current.name, "\tAge:", current.age, "\tBirthday:", current.birthday)
            # else:
            #     print("", current.name, "\t\tAge:", current.age, "\tBirthday:", current.birthday)

    def birthday_checker(self):
        for i in self.units:
            current = self.units[i]
            if current.birthday == [System.date[0], System.date[1]]:
                print("It's", current.name + "'s birthday!")
                current.age += 1

    def availability_checker(self):
        count = 0
        for i in self.units:
            current = self.units[i]
            if current.current_job is None and current.condition is "Fine":
                count += 1
        return count


# jobs #################################################################################################################
class Job:
    def __init__(self, type="", recommended_level=0, minimum_workers=1, maximum_workers=20):
        if type == "":
            # infinite number of Busking, Gambling and War gigs
            possible_job_types = ["Labour", "Guard", "Battle", "Tactician", "Theatre", "Infiltration",
                                  "Battle Tactician"]
            type = possible_job_types[randint(0, len(possible_job_types) - 1)]
        self.type = type

        if recommended_level == 0:
            recommended_level = randint(3, 50)
        self.recommended_level = recommended_level

        self.location = "Douver"

        self.minimum_workers = minimum_workers
        self.maximum_workers = maximum_workers

        self.length = 0
        self.determine_length()

        self.success_skills = []
        self.excel_skills = []

        self.recommended_strength = 1
        self.recommended_intelligence = 1
        self.recommended_agility = 1
        self.recommended_cunning = 1
        self.recommended_allure = 1

        self.reward_gold = (100 * self.minimum_workers * (1 + self.recommended_level // 5) + randint(0,
                                                                                                     50)) * self.length
        self.reward_skill = None
        self.reward_strength = False
        self.reward_intelligence = False
        self.reward_agility = False
        self.reward_cunning = False
        self.reward_allure = False
        self.reward_extra_money = False
        self.reward_extra_money2 = False
        self.determine_rewards_and_stats()

        self.participants = []

    def determine_length(self):
        # Type of work
        if self.type == "Labour" or self.type == "Busking" or self.type == "Gambling" or self.type == "Battle" or self.type == "Labour":
            self.length = 1
        elif self.type == "Tactician" or self.type == "Infiltration":
            self.length = 2
        elif self.type == "Battle Tactician":
            self.length = 3
        elif self.type == "Guard" or self.type == "Stat Training" or self.type == "Skill Training" or self.type == "Theatre":
            self.length = 4
        elif self.type == "War":
            self.length = 12

        # Location

        # Number of workers
        self.length += self.minimum_workers // 3

    def determine_rewards_and_stats(self):
        if self.type == "Labour":
            self.recommended_strength = 3 + self.recommended_level // 2
            self.reward_strength = True
            self.success_skills.append("Heavy Lifting")
        elif self.type == "Busking":
            self.recommended_allure = 3 + self.recommended_level // 2
            self.reward_allure = True
            self.success_skills.append("Passion for Art")
            self.excel_skills.append("Flair")
        elif self.type == "Guard":
            self.recommended_strength = 3 + self.recommended_level // 2
            self.recommended_allure = 2 + self.recommended_level // 3
            self.reward_extra_money = True
            self.success_skills.append("Awareness")
            self.excel_skills.append("Manners")
        elif self.type == "Gambling":
            self.recommended_cunning = 15 + self.recommended_level // 2
            self.recommended_allure = 3 + self.recommended_level // 3
            self.reward_cunning = True
            self.reward_extra_money = True
            self.reward_extra_money2 = True
            self.success_skills.append("Hawk Eyes")
            self.excel_skills.append("Quick Hands")
        elif self.type == "Battle":
            self.recommended_strength = 3 + self.recommended_level // 3
            self.recommended_intelligence = 3 + self.recommended_level // 3
            self.recommended_cunning = 3 + self.recommended_level // 3
            self.recommended_agility = 3 + self.recommended_level // 3
            self.reward_strength = True
            self.reward_intelligence = True
            self.reward_agility = True
            self.success_skills.append("Soldier Training")
            self.success_skills.append("Advanced Training")
            self.excel_skills.append("Glory Seeker")
        elif self.type == "Tactician":
            self.recommended_intelligence = 2 + self.recommended_level // 3
            self.recommended_cunning = 2 + self.recommended_level // 3
            self.recommended_allure = 1 + self.recommended_level // 4
            self.reward_intelligence = True
            self.success_skills.append("History")
            self.excel_skills.append("Commanding Voice")
        elif self.type == "Theatre":
            self.recommended_allure = 3 + self.recommended_level // 2
            self.reward_agility = True
            self.reward_allure = True
            self.success_skills.append("Passion for Art")
            self.excel_skills.append("Flair")
        elif self.type == "Infiltration":
            self.recommended_agility = 6 + self.recommended_level // 2
            self.reward_agility = True
            self.reward_extra_money = True
            self.success_skills.append("Shinobi Training")
            self.excel_skills.append("Gymnastics")
        elif self.type == "Battle Tactician":
            self.recommended_strength = 3 + self.recommended_level // 2
            self.recommended_intelligence = 2 + self.recommended_level // 3
            self.recommended_cunning = 2 + self.recommended_level // 3
            self.recommended_allure = 1 + self.recommended_level // 4
            self.reward_intelligence = True
            self.reward_cunning = True
            self.success_skills.append("History")
            self.excel_skills.append("Commanding Voice")
        elif self.type == "War":
            self.recommended_strength = 5 + self.recommended_level // 2
            self.recommended_intelligence = 5 + self.recommended_level // 2
            self.recommended_cunning = 5 + self.recommended_level // 2
            self.recommended_agility = 5 + self.recommended_level // 2
            self.reward_strength = True
            self.reward_intelligence = True
            self.reward_agility = True
            self.reward_extra_money = True
            self.reward_extra_money2 = True
            self.success_skills.append("Soldier Training")
            self.success_skills.append("Advanced Training")
            self.excel_skills.append("Glory Seeker")

    def short_description(self):
        print(self.type)
        print("Recommended level:", self.recommended_level)
        print("# of workers", self.minimum_workers, "-", self.maximum_workers)
        print("Reward:", str(self.reward_gold) + "$")
        print("---------------------------------------------------------------------------------------------------")

    def long_description(self):
        print(self.type)
        print("Recommended level:", self.recommended_level)
        print("# of workers", self.minimum_workers, "-", self.maximum_workers)
        print("---------------------------------------------------------------------------------------------------")
        print("Recommended stats:")
        if self.recommended_strength > 1:
            print(" Strength:\t\t", self.recommended_strength)
        if self.recommended_intelligence > 1:
            print(" Intelligence:\t", self.recommended_intelligence)
        if self.recommended_agility > 1:
            print(" Agility:\t\t", self.recommended_agility)
        if self.recommended_cunning > 1:
            print(" Cunning:\t\t", self.recommended_cunning)
        if self.recommended_allure > 1:
            print(" Allure:\t\t", self.recommended_allure)
        print("Relevant skills:")
        for i in self.success_skills:
            print("", i)
        for i in self.excel_skills:
            print("", i)
        print("---------------------------------------------------------------------------------------------------")
        print("Rewards:")
        print(" Gold:", str(self.reward_gold) + "$")
        if self.reward_strength is True:
            print(" Increase strength stat")
        if self.reward_intelligence is True:
            print(" Increase intelligence stat")
        if self.reward_agility is True:
            print(" Increase agility stat")
        if self.recommended_cunning is True:
            print(" Increase cunning stat")
        if self.reward_allure is True:
            print(" Increase allure stat")
        if self.reward_extra_money is True:
            print(" Extra money if done exceptionally")
        print("===================================================================================================\n")

    def calculate_chance(self, unit):
        success_chance = 75
        excel_chance = 15
        injury_chance = 0
        if self.type == "Labour" and unit.skills["Heavy Lifting"] is False:
            injury_chance = 15
        elif self.type == "Battle" or self.type == "Battle Tactician" or self.type == "War":
            injury_chance = 20
            if unit.skills["Soldier Training"] is True:
                injury_chance -= 10
            if unit.skills["Advanced Training"] is True:
                injury_chance -= 10
            if unit.skills["Glory Seeker"] is True:
                injury_chance += 5
        # print(unit.strength - self.recommended_strength)
        # print(unit.intelligence - self.recommended_intelligence)
        # print(unit.agility - self.recommended_agility)
        # print(unit.cunning - self.recommended_cunning)
        # print(unit.allure - self.recommended_allure)
        success_chance += 5 * (unit.strength - self.recommended_strength)
        success_chance += 5 * (unit.intelligence - self.recommended_intelligence)
        success_chance += 5 * (unit.agility - self.recommended_agility)
        success_chance += 5 * (unit.cunning - self.recommended_cunning)
        success_chance += 5 * (unit.allure - self.recommended_allure)
        for i in self.success_skills:
            if unit.skills[i] is True:
                success_chance += 30
        for i in self.excel_skills:
            if unit.skills[i] is True:
                excel_chance += 30
        return success_chance, excel_chance, injury_chance

    def print_chance(self, unit):
        chances = self.calculate_chance(unit)
        print("Success chance:", str(chances[0]) + "%")
        print("Excel chance:", str(chances[1]) + "%")
        if chances[2] != 0:
            print("Injury chance:", str(chances[2]) + "%")

    def calculate_group_chance(self, units):
        success_chance = 0
        excel_chance = 0
        injury_chance = 0
        injury_free = False
        for i in units:
            result = self.calculate_chance(i)
            success_chance += result[0] + 5
            if excel_chance < result[1]:
                excel_chance = result[1]
            else:
                excel_chance += 1
            injury_chance += result[2]
            if self.type == "Labour" and i.skills["Heavy Lifting"] is True:
                injury_free = True
        if injury_free is True:
            injury_chance = 0
        return success_chance // len(units), excel_chance, injury_chance // len(units)

    def print_group_chance(self, units):
        chances = self.calculate_group_chance(units)
        print("Group Success chance:", str(chances[0]) + "%")
        print("Group Excel chance:", str(chances[1]) + "%")
        if chances[2] != 0:
            print("Group Injury chance:", str(chances[2]) + "%")

    # def end_date(self):
    #     current_date = System.date
    #     for i in range(self.length):
    #         current_date[1] += 1
    #         if current_date[1] > 4:
    #             current_date[1] = 1
    #             current_date[0] += 1
    #         if current_date[0] > 12:  # new year
    #             current_date[0], current_date[1] = 1, 1
    #             current_date[2] += 1
    #     return current_date

    # def weekly_update(self):
    #     for i in self.participants:
    #         # injury check
    #         if len(self.participants == 1):
    #             if randint(0, 100) < i.calculate_chance[2]:
    #                 i.condition = "Injured"
    #         else:
    #             if randint(0, 100) < self.calculate_chance(self.participants)[2]:
    #                 i.condition = "Injured"



# main #################################################################################################################
class System:
    date = [5, 1, 0]  # month, week, year
    money = 1000
    playerName = "Daniel"
    roster = Roster(playerName)
    weekly_jobs = [Job("Labour", 1, 1, 3)]
    jobs_in_progress = []


def refresh():
    for i in range(50):
        print()


def menu_top():
    print("\n========================")
    print("Date: M" + str(System.date[0]) + ", W" + str(System.date[1]) + ", Y" + str(System.date[2]))
    print("Funds:", str(System.money) + "$")
    print("Available units:", System.roster.availability_checker(), "/", len(System.roster.units))
    print("========================\n")


def date_update():
    date = System.date
    date[1] += 1
    if date[1] > 4:  # new month
        wages_for_employees = 0
        for i in range(len(System.roster.units)):
            wages_for_employees += System.roster.units[i].calculate_wage()
        System.money -= wages_for_employees
        date[1] = 1
        date[0] += 1
    if date[0] > 12:  # new year
        date[0], date[1] = 1, 1
        date[2] += 1


def date_checker():
    for i in System.jobs_in_progress:
        i.length -= 1
        print(i.length)
        if i.length == 0:
            for j in i.participants:
                j.current_job = None
            System.jobs_in_progress.remove(i)
    System.roster.birthday_checker()


def activity_board():
    while True:
        menu_top()
        choice = int(input("What do you want to do?\n 1: Jobs\n 2: Hire\n 3: Roster\n 4: News\n 5: Wait\n"))
        if choice is 1:  # Jobs
            option_1()
        elif choice is 2:  # Hire
            new = hiring_board()
            if new is not None:
                System.roster.add_unit(new)
        elif choice is 3:  # Roster
            option_3()
        elif choice is 4:  # News
            print("No news today. Come back next week.")
        elif choice is 5:  # Wait
            break
        else:
            print("\nError")
    print("See you next week")
    sleep(1)


def option_1():
    while True:
        if len(System.weekly_jobs) > 0:
            for i in range(len(System.weekly_jobs)):
                print(str(i + 1) + ":")
                System.weekly_jobs[i].short_description()
            job_choice = int(input("\nWhat job interests you? Press 0 to quit.\n"))
            if job_choice == 0:
                break
            elif job_choice > len(System.weekly_jobs) or job_choice < 0:
                print("Error")
            else:
                choose_units(job_choice - 1)
                sleep(2)
                break
        else:
            print("Every job is taken, buddy.")
            sleep(2)
            break


def choose_units(job_choice):
    job = System.weekly_jobs[job_choice]
    print("This job requires a minimum of", job.minimum_workers, "participants.\n")
    units = []
    while True:
        if len(units) < job.maximum_workers:
            for i in System.roster.units:
                if System.roster.units[i] not in units and System.roster.units[i].level >= job.recommended_level:
                    print(str(i + 1) + ":")
                    System.roster.units[i].short_description()

        if len(units) == 0:
            unit_choice = int(input("Which unit do you want to assign to this job? Press 0 to quit.\n"))
            if unit_choice == 0:
                break
            else:
                unit = System.roster.units[unit_choice - 1]
                print(unit.name + "'s chances:")
                job.print_chance(unit)
                print("Assign", unit.name, "to this task? (1 for yes, 0 for no)")
                confirm = int(input(""))
                if confirm == 1:
                    if unit.commander is True:
                        commander_confirm = int(input("This is your commander unit. If you send them to a job, all of your unemployed mercs will not have a job to do.\nAre you sure? (1 for yes, 0 for no)\n"))
                        if commander_confirm == 1:
                            units.append(unit)
                    else:
                        units.append(unit)
        elif 0 < len(units) < job.maximum_workers:
            unit_choice = int(input("Are there any other units you want to assign? Press 0 if not.\n"))
            if unit_choice == 0:
                pass
            elif unit_choice > 0 and System.roster.units[unit_choice - 1] not in units:
                unit = System.roster.units[unit_choice - 1]
                print(unit.name + "'s chances:")
                job.print_chance(unit)
                print("Assign", unit.name, "to this task? (1 for yes, 0 for no)")
                confirm = int(input(""))
                if confirm == 1:
                    if unit.commander is True:
                        commander_confirm = int(input("This is your commander unit. If you send them to a job, all of your unemployed mercs will not have a job to do.\nAre you sure? (1 for yes, 0 for no)\n"))
                        if commander_confirm == 1:
                            units.append(unit)
                    else:
                        units.append(unit)
            else:
                print("Error")

        if len(units) >= job.minimum_workers:
            unit_names = ""
            for i in units:
                unit_names += i.name + ", "
            if len(units) > 1:
                job.print_group_chance(units)

            if len(units) < job.maximum_workers:
                print("Send:", unit_names[0:-2] + "? (Press 1 to confirm, press 2 to add more, press 0 to return to the job list)")
                confirm = int(input(""))
                if confirm == 1:
                    job_start(job_choice, units)
                    break
                elif confirm == 2:
                    pass
                elif confirm == 0:
                    break
            else:
                print("Send:", unit_names[0:-2] + "? (Press 1 to confirm, press 0 to return to the job list)")
                confirm = int(input(""))
                if confirm == 1:
                    job_start(job_choice, units)
                    break
                elif confirm == 0:
                    break


def job_start(job_choice, units):
    job = System.weekly_jobs[job_choice]
    job.participants = units
    for i in units:
        i.current_job = str(job.type) + " job. Working for: " + str(job.length) + " weeks."
    System.jobs_in_progress.append(job)
    System.weekly_jobs.remove(job)
    print("Good to go!")


def option_3():
    while True:
        System.roster.print_all()
        choice = int(input("\nChoose a unit to inspect (unit #) or 0 to go back\n"))
        if choice == 0:
            break
        else:
            System.roster.units[choice-1].long_description()
            sleep(1)


if __name__ == '__main__':
    # playerName = input("So you are starting a mercenary agency, kid? I guess that means you're a real pro now. What do I need to address you by from now on?\n")
    # print(playerName+"'s Mercenaries? Sounds kinda generic if you ask me.")

    for i in range(3):
        new_unit = Unit()
        System.roster.add_unit(new_unit)

    while System.roster.units[0].commander is True:
        date_checker()
        if System.roster.units[0].current_job is None:
            activity_board()
        date_update()


#
    # # System.roster.print_all()
    # # for i in range(len(System.roster.units) // 3):
    # #     new_job = Job()
    # #     weekly_jobs.append(new_job)
    # for i in range(len(weekly_jobs)):
    #     print(str(i + 1) + ":")
    #     weekly_jobs[i].long_description()
    # while True:
    #     job_choice = int(input("\nWhat job interests you? Press 0 to quit.\n"))
    #     if job_choice == 0:
    #         break
    #     elif job_choice > len(weekly_jobs):
    #         print("Error")
    #     else:
    #         job_choice -= 1
    #         units = []
    #         while True:
    #             for i in System.roster.units:
    #                 if System.roster.units[i] not in units and System.roster.units[i].level >= weekly_jobs[job_choice].recommended_level:
    #                     print(str(i+1)+":")
    #                     System.roster.units[i].short_description()
    #             if len(units) == 0:
    #                 unit_choice = int(input("Which unit do you want to assign to this job? Press 0 to quit.\n"))
    #                 if unit_choice == 0:
    #                     break
    #                 else:
    #                     unit = System.roster.units[unit_choice-1]
    #                     print(unit.name+"'s chances:")
    #                     weekly_jobs[job_choice].print_chance(unit)
    #                     print("Assign", unit.name, "to this task? (1 for yes, 0 for no)")
    #                     confirm = int(input(""))
    #                     if confirm == 1:
    #                         units.append(unit)
    #             # 0: exits if units empty or
    #
    #             if len(units) > 0:
    #                 unit_names = ""
    #                 for i in units:
    #                     unit_names += i.name + ", "
    #                 print("Send:", unit_names[0:-2]+"?")
    #                 confirm = int(input(""))
    #                 if confirm == 1:
    #                     print("Epic")
    #                 else:
    #                     break
    #         break
