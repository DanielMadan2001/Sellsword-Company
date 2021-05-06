from random import randint
import main


class Normal_Job:
    def __init__(self, type="", recommended_level=0, minimum_workers=1, maximum_workers=20):
        if type == "":
            # infinite number of Busking, Gambling and War gigs
            possible_job_types = main.System.available_job_types
            type = possible_job_types[randint(0, len(possible_job_types) - 1)]
        self.type = type

        if recommended_level == 0:
            recommended_level = randint(3, main.System.max_level)
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
        print("---------------------------------------------------------------------------------------------")

    def long_description(self):
        print(self.type)
        print("Recommended level:", self.recommended_level)
        print("# of workers", self.minimum_workers, "-", self.maximum_workers)
        print("---------------------------------------------------------------------------------------------")
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
        print("---------------------------------------------------------------------------------------------")
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
