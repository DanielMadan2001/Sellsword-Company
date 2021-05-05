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
        if len(name) == 0:
            self.give_name()

        self.level = level
        if level == 0:
            self.level = randint(1, 60)

        self.age = age
        if age == 0:
            self.age = randint(14, 49)

        self.birthday = birthday
        if birthday == [0, 0]:
            self.birthday = [randint(1, 12), randint(1, 4)]

        self.job = job
        jobs = ["Fighter", "Wizard", "Thief", "Knight", "Magician", "Archer", "Monk"]
        if self.job == "" or self.job not in jobs:
            self.job = jobs[randint(0, len(jobs) - 1)]

        self.personality = personality
        personalities = ["Architect", "Thinker", "Commander", "Debater",
                         "Advocate", "Mediator", "Giver", "Champion",
                         "Inspector", "Protector", "Director", "Caregiver",
                         "Crafter", "Artist", "Persuader", "Performer"]
        if self.personality == "" or self.personality not in personalities:
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
        if self.condition != "Fine":
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
                if roll == 3:
                    self.get_random_skill()
        # 40-49: 50% chance for a skill, 3 times
        elif 40 <= self.level < 50:
            for i in range(3):
                roll = randint(1, 2)
                if roll == 1:
                    self.get_random_skill()
        # 50-59: 1 skill, 50% chance for a skill, 2 times
        elif 50 <= self.level < 60:
            self.get_random_skill()
            for i in range(2):
                roll = randint(1, 2)
                if roll == 1:
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
            if self.skills[possible_jobs[randNum]] != True:
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
        if self.condition != "Fine":
            print(self.condition)
        elif self.current_job != None:
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
        if self.current_job != None:
            print("Current job:\t", self.current_job.type, "(weeks left:", str(self.current_job.length) + ")")
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
            if self.skills[j] == True:
                print(j)
                temp += 1
        if temp == 0:
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
            if current.current_job == None and current.condition == "Fine":
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
        if self.reward_strength == True:
            print(" Increase strength stat")
        if self.reward_intelligence == True:
            print(" Increase intelligence stat")
        if self.reward_agility == True:
            print(" Increase agility stat")
        if self.recommended_cunning == True:
            print(" Increase cunning stat")
        if self.reward_allure == True:
            print(" Increase allure stat")
        if self.reward_extra_money == True:
            print(" Extra money if done exceptionally")
        print("===================================================================================================\n")

    def calculate_chance(self, unit):
        success_chance = 75
        excel_chance = 15
        injury_chance = 0
        if self.type == "Labour" and unit.skills["Heavy Lifting"] == False:
            injury_chance = 15
        elif self.type == "Battle" or self.type == "Battle Tactician" or self.type == "War":
            injury_chance = 20
            if unit.skills["Soldier Training"] == True:
                injury_chance -= 10
            if unit.skills["Advanced Training"] == True:
                injury_chance -= 10
            if unit.skills["Glory Seeker"] == True:
                injury_chance += 5
        success_chance += 5 * (unit.strength - self.recommended_strength)
        success_chance += 5 * (unit.intelligence - self.recommended_intelligence)
        success_chance += 5 * (unit.agility - self.recommended_agility)
        success_chance += 5 * (unit.cunning - self.recommended_cunning)
        success_chance += 5 * (unit.allure - self.recommended_allure)
        for i in self.success_skills:
            if unit.skills[i] == True:
                success_chance += 30
        for i in self.excel_skills:
            if unit.skills[i] == True:
                excel_chance += 30
        while success_chance > 100:
            success_chance -= 100
            excel_chance += 15
            if success_chance < 100:
                success_chance = 100
                break
        if excel_chance > 100:
            excel_chance = 100
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
            if self.type == "Labour" and i.skills["Heavy Lifting"] == True:
                injury_free = True
        if injury_free == True:
            injury_chance = 0
        return success_chance // len(units), excel_chance, injury_chance // len(units)

    def print_group_chance(self, units):
        chances = self.calculate_group_chance(units)
        print("Group Success chance:", str(chances[0]) + "%")
        print("Group Excel chance:", str(chances[1]) + "%")
        if chances[2] != 0:
            print("Group Injury chance:", str(chances[2]) + "%")


# main #################################################################################################################
class System:
    date = [5, 1, 0]  # month, week, year
    money = 1000
    max_level = 1
    playerName = "Daniel"
    roster = Roster(playerName)
    available_job_types = [
        "Labour"]  # can unlock "Guard", "Battle", "Tactician", "Theatre", "Infiltration", "Battle Tactician"
    endless_job_types = ["Busking"]  # can unlock "Gambling", "War"
    training_types = {"Bauer's Strength Training": False,
                      "Wyatt's Intelligence Training": False,
                      "Cody's Agility Training": False,
                      "Enzo's Cunning Training": False,
                      "Anthony's Allure Training": False
                      }
    skill_training_types = {"Adept Student Training": False,  # Training - increases chance of success
                            "Heavy Lifting Training": False,  # Labour - increases chance of success and lowers chance of injury
                            "Awareness Training": False,  # Guard - increases chance of success
                            "Manners Training": False,  # Guard - increases chance to excel
                            "Hawk Eyes Training": False,  # Gambling - won't get tricked
                            "Quick Hands Training": False,  # Gambling - can trick (lower level) opponents
                            "Soldier Training Training": False,  # Battle - increases chance of success
                            "Advanced Training Training": False, # Battle - increases chance of success (stacks with Soldier Training)
                            "Glory Seeker Training": False,  # Battle - increases chance to excel
                            "Passion for Art Training": False,  # Performance - increases chance of success
                            "Flair Training": False,  # Performance - increases chance to excel
                            "History Training": False,  # Tactician - increases chance of success
                            "Commanding Voice Training": False,  # Tactician - increases chance to excel
                            "Shinobi Training Training": False,  # Infiltration - increases chance of success
                            "Gymnastics Training": False,  # Infiltration - increases chance of gaining agility points

                            "Anti-Fighter Training": False,  # Eliminates weakness to Fighters
                            "Anti-Wizard Training": False,  # Eliminates weakness to Wizards
                            "Anti-Thief Training": False,  # Eliminates weakness to Thieves
                            "Anti-Knight Training": False,  # Eliminates weakness to Knights
                            "Anti-Magician Training": False,  # Eliminates weakness to Magicians
                            "Anti-Archer Training": False,  # Eliminates weakness to Archers
                            "Anti-Monk Training": False,  # Eliminates weakness to Monk
                            }
    weekly_jobs = []
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
    for i in range(len(System.roster.units)):
        if System.roster.units[i].level > System.max_level:
            System.max_level = System.roster.units[i].level


def weekly_update():
    # weekly job checker
    for i in System.jobs_in_progress:
        i.length -= 1
        success_chance = i.calculate_group_chance(i.participants)
        # chance for injury
        for j in i.participants:
            random_roll = randint(0, 100)
            # print(random_roll, success_chance[2])
            if random_roll < success_chance[2]:
                print(j.name, "injured themselves and was discharged from the job.")
                j.condition = "Injured"
                j.current_job = None
                i.participants.remove(j)
        # end job
        if len(i.participants) == 0:
            print("All of the workers at the", i.type, "job failed.")
            System.jobs_in_progress.remove(i)
        elif i.length == 0 and len(i.participants) > 0:
            job_rewards(i)
            System.jobs_in_progress.remove(i)
    # add weekly jobs
    System.weekly_jobs = [Job("Labour", 1, 1, 3)]
    for i in range(len(System.roster.units) // 2):
        job_type = System.available_job_types[randint(0, len(System.available_job_types) - 1)]
        System.weekly_jobs.append(Job(job_type, randint(1, System.max_level)))
    # birthday checker
    System.roster.birthday_checker()


def job_rewards(job):
    chance = 100 - randint(0, 100)

    success_chances = job.calculate_group_chance(job.participants)

    pass_chance = chance <= success_chances[0]
    pass_plus_chance = chance < success_chances[1]
    excel_chance = chance * 3 < success_chances[1]

    print()
    # print(chance)
    # print(success_chances[0], pass_chance)
    # print(success_chances[1], pass_plus_chance)
    # print(success_chances[1] // 3, excel_chance)

    unit_names = ""
    for i in job.participants:
        unit_names += i.name + ", "
    unit_names = unit_names[0:-2]

    if pass_chance:
        if excel_chance:
            result = 2
            print(unit_names, "did amazing!!!")
        elif pass_plus_chance:
            result = 1
            print(unit_names, "did great!")
        else:
            result = 0
            print(unit_names, "succeeded!")
    else:
        if randint(1, 3) == 3:
            result = -2
            print(unit_names, "messed up.")
        else:
            result = -1
            print(unit_names, "failed.")
    # print(result)

    for j in job.participants:
        unit_rewards(job, j, result)
        j.current_job = None

    System.money += job.reward_gold


def unit_rewards(job, unit, result):
    if job.type == "Labour":
        if result >= 1:
            unit.level += 1
            unit.strength += 1
            print(unit.name, "is stronger and more experienced.")
        elif result <= 0:
            unit.level += 1
            print(unit.name, "is more experienced.")
    # elif self.type == "Busking":
    # elif self.type == "Guard":
    # elif self.type == "Gambling":
    # elif self.type == "Battle":
    # elif self.type == "Tactician":
    # elif self.type == "Theatre":
    # elif self.type == "Infiltration":
    # elif self.type == "Battle Tactician":
    # elif self.type == "War":


def activity_board():
    # if len(System.weekly_jobs) > 0:
    #     job_start(0, [System.roster.units[0]])
    while System.roster.units[0].current_job == None:
        menu_top()
        choice = int(input(
            "What do you want to do?\n 1: Job board\n 2: Hire\n 3: Roster\n 4: News\n 5: Current jobs being done\n 6: Wait\n"))
        if choice == 1:  # Jobs
            option_1()
        elif choice == 2:  # Hire
            new = hiring_board()
            if new != None:
                System.roster.add_unit(new)
        elif choice == 3:  # Roster
            option_3()
        elif choice == 4:  # News
            print("No news today. Come back next week.")
        elif choice == 5:
            option_5()
        elif choice == 6:  # Wait
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
                if System.roster.units[i] not in units and System.roster.units[i].level >= job.recommended_level and System.roster.units[i].current_job == None:
                    print(str(i + 1) + ":")
                    System.roster.units[i].short_description()

        if len(units) == 0:
            unit_choice = int(input("Which unit do you want to assign to this job? Press 0 to quit.\n"))
            if unit_choice == 0:
                break
            elif System.roster.units[unit_choice - 1].current_job != None:
                pass
            else:
                unit = System.roster.units[unit_choice - 1]
                print(unit.name + "'s chances:")
                job.print_chance(unit)
                print("Assign", unit.name, "to this task? (1 for yes, 0 for no)")
                confirm = int(input(""))
                if confirm == 1:
                    if unit.commander == True:
                        commander_confirm = int(input(
                            "This is your commander unit. If you send them to a job, all of your unemployed mercs will not have a job to do.\nAre you sure? (1 for yes, 0 for no)\n"))
                        if commander_confirm == 1:
                            units.append(unit)
                    else:
                        units.append(unit)
        elif 0 < len(units) < job.maximum_workers:
            unit_choice = int(input("Are there any other units you want to assign? Press 0 if not.\n"))
            if unit_choice == 0 or System.roster.units[unit_choice - 1].current_job != None:
                pass
            elif unit_choice > 0 and System.roster.units[unit_choice - 1] not in units:
                unit = System.roster.units[unit_choice - 1]
                print(unit.name + "'s chances:")
                job.print_chance(unit)
                print("Assign", unit.name, "to this task? (1 for yes, 0 for no)")
                confirm = int(input(""))
                if confirm == 1:
                    if unit.commander == True:
                        commander_confirm = int(input(
                            "This is your commander unit. If you send them to a job, all of your unemployed mercs will not have a job to do.\nAre you sure? (1 for yes, 0 for no)\n"))
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
                print("Send:", unit_names[
                               0:-2] + "? (Press 1 to confirm, press 2 to add more, press 0 to return to the job list)")
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
    System.jobs_in_progress.append(job)
    for i in units:
        i.current_job = job
    System.weekly_jobs.remove(job)
    print("Good to go!")


def option_3():
    while True:
        System.roster.print_all()
        choice = int(input("\nChoose a unit to inspect (unit #) or 0 to go back\n"))
        if choice == 0:
            break
        else:
            System.roster.units[choice - 1].long_description()
            sleep(1)


def option_5():
    for i in range(len(System.jobs_in_progress)):
        job = System.jobs_in_progress[i]
        print(str(i + 1) + "/" + str(len(System.jobs_in_progress)),
              "\n-------------------------------------------------")
        print(job.type)
        print("Workers:")
        for j in job.participants:
            print(" -", j.name)
        print("Weeks left:", job.length)
    sleep(1)


if __name__ == '__main__':
    # playerName = input("So you are starting a mercenary agency, kid? I guess that means you're a real pro now. What do I need to address you by from now on?\n")
    # print(playerName+"'s Mercenaries? Sounds kinda generic if you ask me.")

    for i in range(3):
        new_unit = Unit()
        System.roster.add_unit(new_unit)

    while System.roster.units[0].commander == True:
        weekly_update()
        if System.roster.units[0].current_job == None:
            activity_board()
        date_update()
