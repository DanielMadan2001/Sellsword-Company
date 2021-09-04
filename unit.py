from random import randint

class Unit:
    def __init__(self, name="", level=0, birthday=[0, 0], age=0, job="", personality="", skills=[], commander=False):
        self.name = name
        if len(name) == 0:
            self.give_name()

        self.level = level
        if level == 0:
            self.level = randint(1, 5)

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

            # matchups
            "Fighter": False,  # Eliminates weakness to Fighters
            "Wizard": False,  # Eliminates weakness to Wizards
            "Thief": False,  # Eliminates weakness to Thieves
            "Knight": False,  # Eliminates weakness to Knights
            "Magician": False,  # Eliminates weakness to Magicians
            "Archer": False,  # Eliminates weakness to Archers
            "Monk": False,  # Eliminates weakness to Monk
        }
        self.assign_skills(skills)

        self.matchups = {
        "Fighter": 1, 
        "Wizard": 1, 
        "Thief": 1, 
        "Knight": 1, 
        "Magician": 1, 
        "Archer": 1, 
        "Monk": 1
        }
        self.update_matchups()

        self.work = {
            "Labour": 0,
            "Busking": 0,
            "Guard": 0,
            "Gambling": 0,
            "Battle": 0,
            "Tactician": 0,
            "Theatre": 0,
            "Infiltration": 0,
            "Battle Tactician": 0,
            "War": 0
        } # job preferences
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
            self.strength, self.allure = 2, 1
        elif self.job == "Wizard":
            self.intelligence, self.cunning = 2, 1
        elif self.job == "Thief":
            self.agility, self.allure = 2, 1
        elif self.job == "Knight":
            self.strength, self.intelligence = 2, 1
        elif self.job == "Magician":
            self.cunning, self.intelligence, self.allure = 1, 1, 1 * (
                    self.level // 5)
        elif self.job == "Archer":
            self.agility, self.cunning, self.strength = 1, 1, 1 * (
                    self.level // 5)
        else:
            self.strength, self.intelligence, self.allure = 1, 1, 1
        
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
        return round(total, 2)

    def calculate_wage(self):
        total = self.level * 5
        total += self.strength * 0.75
        total += self.intelligence * 0.75
        total += self.agility * 0.75
        total += self.cunning * 0.75
        total += self.allure * 1.5
        return total

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
            possible_jobs.append("Thief")
        elif self.job == "Wizard":
            possible_jobs.append("History")
            possible_jobs.append("Commanding Voice")
            possible_jobs.append("Passion for Art")
            possible_jobs.append("Fighter")
        elif self.job == "Thief":
            possible_jobs.append("Gymnastics")
            possible_jobs.append("Hawk Eyes")
            possible_jobs.append("Quick Hands")
            possible_jobs.append("Wizard")
        elif self.job == "Knight":
            possible_jobs.append("Awareness")
            possible_jobs.append("Manners")
            possible_jobs.append("Soldier Training")
            possible_jobs.append("Archer")
        elif self.job == "Magician":
            possible_jobs.append("Flair")
            possible_jobs.append("Quick Hands")
            possible_jobs.append("Gymnastics")
            possible_jobs.append("Knight")
        elif self.job == "Archer":
            possible_jobs.append("Hawk Eyes")
            possible_jobs.append("Awareness")
            possible_jobs.append("History")
            possible_jobs.append("Magician")
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
            self.work["Gambling"], self.work["Tactician"], self.work["Labour"], self.work["Busking"], self.work["Theatre"] = 1, 1, -1, -1, 1
        elif self.personality == "Thinker":
            self.work["Battle"], self.work["Tactician"], self.work["Busking"], self.work["Theatre"], self.work["Guard"] = 1, 1, 1, -1, -1
        elif self.personality == "Commander":
            self.work["Battle"], self.work["Tactician"], self.work["Gambling"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Debater":
            self.work["Busking"], self.work["Theatre"], self.work["Gambling"], self.work["Labour"], self.work["Guard"] = 1, 1, 1, -1, -1
        elif self.personality == "Advocate":
            self.work["Busking"], self.work["Theatre"], self.work["Guard"], self.work["Battle"], self.work["Infiltration"] = 1, 1, 1, -1, -1
        elif self.personality == "Mediator":
            self.work["Busking"], self.work["Theatre"], self.work["Guard"], self.work["Battle"], self.work["Tactician"] = 1, 1, 1, -1, -1
        elif self.personality == "Giver":
            self.work["Labour"], self.work["Battle"], self.work["Tactician"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Champion":
            self.work["Busking"], self.work["Theatre"], self.work["Gambling"], self.work["Guard"], self.work[
                "Infiltration"] = 1, 1, 1, -1, -1
        elif self.personality == "Inspector":
            self.work["Tactician"], self.work["Infiltration"], self.work["Labour"], self.work["Battle"] = 1, 1, -1, -1
        elif self.personality == "Protector":
            self.work["Labour"], self.work["Guard"], self.work["Gambling"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Director":
            self.work["Labour"], self.work["Tactician"], self.work["Guard"], self.work["Battle"] = 1, 1, -1, -1
        elif self.personality == "Caregiver":
            self.work["Labour"], self.work["Guard"], self.work["Gambling"], self.work["Infiltration"] = 1, 1, -1, -1
        elif self.personality == "Crafter":
            self.work["Busking"], self.work["Theatre"], self.work["Gambling"], self.work["Battle"], self.work["Tactician"] = 1, 1, 1, -1, -1
        elif self.personality == "Artist":
            self.work["Busking"], self.work["Theatre"], self.work["Battle"], self.work["Labour"], self.work["Guard"] = 1, 1, 1, -1, -1
        elif self.personality == "Persuader":
            self.work["Busking"], self.work["Theatre"], self.work["Infiltration"], self.work["Labour"], self.work["Battle"] = 1, 1, 1, -1, -1
        else:
            self.work["Busking"], self.work["Theatre"], self.work["Battle"], self.work["Guard"], self.work["Tactician"] = 1, 1, 1, -1, -1

        if self.job == "Fighter":
            self.work["Battle"] += 1
        elif self.job == "Wizard":
            self.work["Tactician"] += 1
        elif self.job == "Thief":
            self.work["Infiltration"] += 1
        elif self.job == "Knight":
            self.work["Guard"] += 1
        elif self.job == "Magician":
            self.work["Busking"] += 1
            self.work["Theatre"] += 1
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
        print("--------------------------------------------------------------------------------------------")

    def long_description(self, System):
        all_jobs = System.available_job_types + System.available_free_jobs
        # for i in System.free_jobs_in_progress:
        #   all_jobs.append(i.type)
        # print("System jobs:", all_jobs)
        print("============================================================================================")
        if self.commander:
            print("Name:\t\t\t", self.name, "(Commander)")
        else:
            print("Name:\t\t\t", self.name)
        print("Level:\t\t\t", self.level)
        print("Age:\t\t\t", self.age)
        print("Birthday:\t\t", "M" + str(self.birthday[0]) + ", W" + str(self.birthday[1]))
        print("Job:\t\t\t", self.job)
        print("Personality:\t", self.personality)
        # print("Attitude:\t\t", str(self.attitude) + "/10")
        if self.current_job != None:
            print("Current job:\t", self.current_job.type, "(weeks left:", str(self.current_job.length) + ")")
        else:
            print("Current job:\t Awaiting work")
        print("Condition:\t\t", self.condition)
        print("Worth:\t\t\t", str(self.calculate_worth()) + "$")
        print("Monthly wage:\t", str(self.calculate_wage()) + "$")
        print(
            "--------------------------------------------------------------------------------------------")
        print("Strength:\t\t", self.strength)
        print("Intelligence:\t", self.intelligence)
        print("Agility:\t\t", self.agility)
        print("Cunning:\t\t", self.cunning)
        print("Allure:\t\t\t", self.allure)
        print(
            "--------------------------------------------------------------------------------------------")
        temp = 0
        for j in self.skills:
            if self.skills[j] == True:
                print(j)
                temp += 1
        if temp == 0:
            print("No skills...")
        print(
            "--------------------------------------------------------------------------------------------")
        print("Favourite jobs:")
        for j in self.work:
            if self.work[j] > 0:
                # print("", j + ":", self.work[j])
              if j in all_jobs:
                print("", j)
              else:
                print(" ???")
        print("Least favourite jobs:")
        for j in self.work:
            if self.work[j] < 0:
              # print("", j + ":", self.work[j])
              if j in all_jobs:
                print("", j)
              else:
                print(" ???")
        print("============================================================================================")

    def update_matchups(self):
      skills = ["Fighter", "Wizard", "Thief", "Knight", "Magician", "Archer", "Monk"]
      upgraded_stats = {
        1.5: 1.75,
        1.25: 1.35,
        1: 1.1,
        0.75: 0.95,
        0.5: 0.85
      }
      if self.job == "Fighter":
        self.matchups = {
          "Fighter": 1, 
          "Wizard": 0.5, 
          "Thief": 1.5, 
          "Knight": 1, 
          "Magician": 0.75, 
          "Archer": 1, 
          "Monk": 1
        }
      elif self.job == "Wizard":
        self.matchups = {
          "Fighter": 1.5, 
          "Wizard": 1, 
          "Thief": 0.5, 
          "Knight": 1, 
          "Magician": 1, 
          "Archer": 0.75, 
          "Monk": 1
        }
      elif self.job == "Thief":
        self.matchups = {
          "Fighter": 0.5, 
          "Wizard": 1.5, 
          "Thief": 1, 
          "Knight": 0.75, 
          "Magician": 1, 
          "Archer": 1, 
          "Monk": 1
        }
      elif self.job == "Knight":
        self.matchups = {
          "Fighter": 1, 
          "Wizard": 1, 
          "Thief": 1.25, 
          "Knight": 1, 
          "Magician": 0.75, 
          "Archer": 1.25, 
          "Monk": 1
        }
      elif self.job == "Magician":
        self.matchups = {
          "Fighter": 1.25, 
          "Wizard": 1, 
          "Thief": 1, 
          "Knight": 1.25, 
          "Magician": 1, 
          "Archer": 0.75, 
          "Monk": 1
        }
      elif self.job == "Archer":
        self.matchups = {
          "Fighter": 1, 
          "Wizard": 1.25, 
          "Thief": 1, 
          "Knight": 0.75, 
          "Magician": 1.25, 
          "Archer": 1, 
          "Monk": 1
        }
      
      for i in skills:
        if self.skills[i] == True:
          self.matchups[i] = upgraded_stats[self.matchups[i]]

    def matchup_description(self):
        print("============================================================================================")
        self.update_matchups()
        print(self.name, "the", self.job)
        print("VS. Fighters:\t", str(self.matchups["Fighter"]) + "x")
        print("VS. Wizards:\t", str(self.matchups["Wizard"]) + "x")
        print("VS. Thieves:\t", str(self.matchups["Thief"]) + "x")
        print("VS. Knights:\t", str(self.matchups["Knight"]) + "x")
        print("VS. Magicians:\t", str(self.matchups["Magician"]) + "x")
        print("VS. Archers:\t", str(self.matchups["Archer"]) + "x")
        print("VS. Monks:\t\t", str(self.matchups["Monk"]) + "x")

        # if self.job == "Fighter":
        #     self.strength, self.allure = 2, 1
        # elif self.job == "Wizard":
        #     self.intelligence, self.cunning = 2, 1
        # elif self.job == "Thief":
        #     self.agility, self.allure = 2, 1
        # elif self.job == "Knight":
        #     self.strength, self.intelligence = 2, 1
        # elif self.job == "Magician":
        #     self.cunning, self.intelligence, self.allure = 1, 1, 1 * (
        #             self.level // 5)
        # elif self.job == "Archer":
        #     self.agility, self.cunning, self.strength = 1, 1, 1 * (
        #             self.level // 5)
        # else:
