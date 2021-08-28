from random import randint
import main
import message


class Job:
  def __init__(self):
    self.type = ""            # the type of job (labour, gambling, battle, etc.)
    self.description = ""       # the description of the job

    self.length = 0             # set as work defaults
    self.min_level = 0
    self.min_workers = 0
    self.max_workers = 0
    
    self.relevant_stats = {
      "Strength": 0,
      "Intelligence": 0,
      "Agility": 0,
      "Cunning": 0,
      "Allure": 0,
    }

    self.success_skills = []   # the relevant skills that further increase success rate
    self.excel_skills = []   # the relevant skills that further increase excel rate
    
    self.min_result = 0
    self.max_result = 0
    
    self.gold = 0               # how much money can be earned from the job
    self.unit_rewards = { 
      "Level-Up": False,
      "Strength-Up": False,
      "Intelligence-Up": False,
      "Agility-Up": False,
      "Cunning-Up": False,
      "Allure-Up": False,
      "Skills": {
        "Adept Student": False,
        "Heavy Lifting": False,
        "Awareness": False,
        "Manners": False,
        "Hawk Eyes": False,
        "Quick Hands": False,
        "Soldier Training": False,
        "Advanced Training": False,
        "Glory Seeker": False,
        "Passion for Art": False,
        "Flair": False,
        "History": False,
        "Commanding Voice": False,
        "Shinobi Training": False,
        "Gymnastics": False,
        "Fighter": False,
        "Wizard": False,
        "Thief": False,
        "Knight": False,
        "Magician": False,
        "Archer": False,
        "Monk": False
      },
      "Injury": False
    }   
    self.participants = []
    self.enemy_classes = []

    self.death_trigger = False

    self.offer_dict = {
      "Labour":           ["Strength", "Heavy Lifting"],
      "Guard":            ["Awareness", "Manners"],
      "Battle":           ["Glory Seeker", "Fighter", "Wizard", "Thief", "Knight", "Magician", "Archer", "Monk"], 
      "Tactician":        ["Battle Tactician", "Intelligence", "History", "Commanding Voice"], 
      "Theatre":          ["Allure", "Passion for Art", "Flair"], 
      "Infiltration":     ["Agility", "Shinobi Training", "Gymnastics"], 
      "Battle Tactician": ["Intelligence", "History", "Commanding Voice"],
      "Busking":          ["Allure", "Passion for Art", "Flair"],
      "Gambling":         ["Cunning", "Hawk Eyes", "Quick Hands"],
      "War":              ["Glory Seeker"] 
    }
    self.offer_dict_enemies = []


  def short_description(self):
    print(self.type)
    print(self.description)
    if self.length == 1:
      print("Length: 1 week")
    else:
      print("Length:", int(self.length), "weeks")
    print("Minimum level:", self.min_level)
    if self.min_workers == self.max_workers:
      print("# of workers:", self.min_workers)
    else:
      print("# of workers:", self.min_workers, "-", self.max_workers)
    print("Important stats:")
    if self.relevant_stats["Strength"] != 0:
      print("\tStrength", self.relevant_stats["Strength"])
    if self.relevant_stats["Intelligence"] != 0:
      print("\tIntelligence", self.relevant_stats["Intelligence"])
    if self.relevant_stats["Agility"] != 0:
      print("\tAgility", self.relevant_stats["Agility"])
    if self.relevant_stats["Cunning"] != 0:
      print("\tCunning", self.relevant_stats["Cunning"])
    if self.relevant_stats["Allure"] != 0:
      print("\tAllure", self.relevant_stats["Allure"])
    if len(self.enemy_classes) > 0:
      print("Enemies:")
      for i in self.enemy_classes:
        print("\t"+i)
    print("Reward:", str(self.gold) + "$")
    print("--------------------------------------------------------------------------------------------")
  
  
  def calculate_chance(self, unit):
    success_chance = 75
    excel_chance = 15
    injury_chance = 0

    if self.type == "Labour" and unit.skills["Heavy Lifting"] == False:
      injury_chance = 15

    elif self.type == "Battle" or self.type == "Battle Tactician" or self.type == "War":
      injury_chance = 20
      # for i in self.enemy_classes:
      #   injury_chance *= unit.skills[i]
      if unit.skills["Soldier Training"] == True:
        injury_chance -= 5
      if unit.skills["Advanced Training"] == True:
        injury_chance -= 5
      if unit.skills["Glory Seeker"] == True:
        injury_chance += 5

    elif self.type == "Theatre":
      injury_chance = 15

    if self.relevant_stats["Strength"] != 0:
      success_chance += 5 * (unit.strength - self.relevant_stats["Strength"])
    if self.relevant_stats["Intelligence"] != 0:
      success_chance += 5 * (unit.intelligence - self.relevant_stats["Intelligence"])
    if self.relevant_stats["Agility"] != 0:
      success_chance += 5 * (unit.agility - self.relevant_stats["Agility"])
    if self.relevant_stats["Cunning"] != 0:
      success_chance += 5 * (unit.cunning - self.relevant_stats["Cunning"])
    if self.relevant_stats["Allure"] != 0:
      success_chance += 5 * (unit.allure - self.relevant_stats["Allure"])

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
            success_chance = 95
            break

    if excel_chance > 100:
        excel_chance = 100

    if success_chance < 10:
      success_chance = 10
    elif success_chance > 95 and (self.type == "Battle" or self.type == "War"):
      success_chance = 95

    if injury_chance > 100:
        injury_chance = 100

    return success_chance, excel_chance, injury_chance
  

  def calculate_group_chance(self, units):
    success_chance = 0
    excel_chance = 0
    injury_chance = 0
    injury_free = False
    for i in units:
      result = self.calculate_chance(i)
      success_chance += result[0]
      if excel_chance < result[1]:
          excel_chance = result[1]
      if len(self.participants) > 1:
        excel_chance += 1
        success_chance += 5
      injury_chance += result[2]
      if self.type == "Labour" and i.skills["Heavy Lifting"] is True:
        injury_free = True
    if injury_free is True:
      injury_chance = 0
    return success_chance // len(units), excel_chance, injury_chance // len(units)

  
  def print_chance(self, unit):
    print("Chance for:", unit.name)
    chances = self.calculate_chance(unit)
    print("Success chance:", str(chances[0]) + "%")
    print("Excel chance:", str(chances[1]) + "%")
    if chances[2] != 0:
      print("Injury chance:", str(chances[2]) + "%")
    if unit.work[self.type] > 0:
      print(unit.name, "really likes this type of work.")
    elif unit.work[self.type] < 0:
      print(unit.name, "dislikes this type of work.")


  def print_group_chance(self, units):
    names = ""
    for i in units:
      names += i.name + ", "
    print("Chance for:", names[0:-2])
    chances = self.calculate_group_chance(units)
    print("Group Success chance:", str(chances[0]) + "%")
    print("Group Excel chance:", str(chances[1]) + "%")
    if chances[2] != 0:
        print("Group Injury chance:", str(chances[2]) + "%")
  

  def determine_enemies(self, min=0):
    jobs = ["Fighter", "Wizard", "Thief", "Knight", "Magician", "Archer", "Monk"]
    if min == 0:
      min = self.min_level
    num = (min // 15) + 1
    # print(self.type, "min:", num)
    while len(self.enemy_classes) < num:
      random = jobs[randint(0, len(jobs)-1)]
      if random not in self.enemy_classes:
        self.enemy_classes.append(random)
        self.offer_dict_enemies.append(random)


  def job_finish(self, System):   # important

    if System.history_open == False:  # can view job history after completing first job
      System.history_open = True

    completion_trigger = False
    names = self.participants_check()
    if names != "":
      completion_trigger = True

    if completion_trigger == False:
      print("The job was incomplete")
      result = -1
    elif len(self.participants) == 0:
      result = self.min_result * -1
    elif len(self.participants) > 0:
      success_chance = self.calculate_group_chance(self.participants)
      if self.min_result == 0:
        if success_chance[1] >= randint(0, 100):
          print(names + " did amazing!!! (perfect)")
          result = 1
        else:
          print(names + " did well! (pass)")
          result = 0
      elif success_chance[0] >= randint(0, 100):   # pass 
        if success_chance[1] >= randint(0, 100):  # exceled
          if self.max_result == 1:  # only 1 level of exceling
            print(names + " did amazing!!! (perfect)")
            result = 1
          else: # can either get perfect or excel
            if randint(1, 3) == 3:  # got perfect
              print(names + " did amazing!!! (perfect)")
              result = 2
            else: # got excel
              print(names + " did great!! (excel)")
              result = 1
        else:
          print(names + " did well! (pass)")
          result = 0
      else: # did not pass
        if self.max_result == 1:  # can only fail
          print(names + " failed their task. (fail)")
          result = -1
        else:
          if randint(0, 3) != 1:  # fail
            print(names + " failed their task. (fail)")
            result = -1
          else: # disaster
            print(names + " messed up... (disaster)")
            result = -2
    
    System.job_history[self.type][result] += 1

    System.job_history[self.type]["Count"] = self.find_job_history_tally(System.job_history[self.type])
    roll = randint(0, 100)
    job_offer = False
    if System.job_history[self.type]["Count"] >= roll:
      job_offer = True

    self.determine_rewards(result)
    if job_offer == True:
      self.find_job_offer(System)
    # self.find_job_offer(System)

    System.money += self.gold
    print("\nRecieved", str(self.gold) + "$")
    
    for i in self.participants:
      if i.condition == "Fine":
        unit = self.give_unit_rewards(i)
      unit = System.roster[System.roster.index(i)]
      unit.current_job = None
    
    # for i in System.roster:
    #   if i.condition == "Dead":
    #     print(i.name, "is dead at", i.age, "years old.")
    #     System.roster.remove(i)

    # if len(System.roster) == 1 and System.roster[0].condition == "Dead":
    #   print(System.roster[0].name, "is dead at", System.roster[0].age, "years old.")
    #   System.roster.remove(System.roster[0])

    return System


  def give_unit_rewards(self, unit):
    if self.unit_rewards["Level-Up"] == True:
      unit.level += 1
      print(unit.name + " is now lvl. " + str(unit.level) + "!\t(" + str(unit.level - 1) + " -> " + str(unit.level) + ")")

    if self.unit_rewards["Strength-Up"] == True:
      unit.strength += 1
      print(unit.name + " is stronger! \t(" + str(unit.strength - 1) + " -> " + str(unit.strength) + ")")

    if self.unit_rewards["Intelligence-Up"] == True:
      unit.intelligence += 1
      print(unit.name + " is smarter! \t(" + str(unit.intelligence - 1) + " -> " + str(unit.intelligence) + ")")

    if self.unit_rewards["Agility-Up"] == True:
      unit.agility += 1
      print(unit.name + " is faster! \t(" + str(unit.agility - 1) + " -> " + str(unit.agility) + ")")

    if self.unit_rewards["Cunning-Up"] == True:
      unit.cunning += 1
      print(unit.name + " is more cunning! \t(" + str(unit.cunning - 1) + " -> " + str(unit.cunning) + ")")

    if self.unit_rewards["Allure-Up"] == True:
      unit.allure += 1
      print(unit.name + " is more charming! \t(" + str(unit.allure - 1) + " -> " + str(unit.allure) + ")")

    for i in self.unit_rewards["Skills"]:
      if self.unit_rewards["Skills"][i] == True:
        unit.skills[i] = True
        print(unit.name + " now knows " + i + "!")
      
    if self.unit_rewards["Injury"] == True:
      unit.condition = "Injured"
      print(unit.name + " is now injured.")


  def participants_check(self):
    names = ""
    for i in self.participants:
      if i.condition == "Fine":
        names += i.name + ", "
    names = names [0:-2]
    return names
  
  
  def determine_rewards(self, result):  
    return  # takes result int and changes self.unit_rewards to reflect it


  def weekly_update(self):  # uses a random roll and group chance to figure out what happens for each of them
    # success_chance = i.calculate_group_chance(i.participants)
    self.length -= 1
    return self


  def find_job_history_tally(self, history_entry):
    job_history_tally = 0
    job_history_tally += history_entry[1] * 5
    job_history_tally += history_entry[0] * 5
    if -1 in history_entry:
      job_history_tally += (history_entry[-1] * 7)
    if -2 in history_entry:
      job_history_tally += (history_entry[-2] * 10)
    if 2 in history_entry:
      job_history_tally += (history_entry[2] * 5)
    return job_history_tally

  
  def find_job_offer(self, System, unit=None):
    System.job_history[self.type]["Count"] = 0
    possible_offers = []
    commander = False
    if unit != None:
      if unit.condition != "Dead" and unit.commander == False:
        possible_offers.append("offer")
    else:
      for i in self.participants:
        if i.condition != "Dead" and i.commander == False:
          possible_offers.append("offer")
          unit = i
          break
      if unit == None:
        unit = self.participants[0]
        commander = True

    # if unit == None:
    #   possible_offers.append(self.participants[randint(0, len(self.participants)-1)])
    # else:
    #   possible_offers.append(unit)
    for i in self.offer_dict[self.type]:
      if i in System.locked_job_types or i in System.locked_free_jobs or i in System.locked_stat_training_types or i in System.locked_skill_training_types:
        possible_offers.append(i)
    for j in self.offer_dict_enemies:
      possible_offers.append(j)
    
    # "-Fighter", "-Wizard", "-Thief", "-Knight", "-Magician", "-Archer", "-Monk"
    
    # print(possible_offers)
    if len(possible_offers) > 0:
      chosen_one = possible_offers[randint(0, len(possible_offers)-1)]      
      System.mailbox.append(message.create_letter(chosen_one, unit, self.type))
      
      System.weekly_letter_count += 1

      # if commander == False:
      #   print("\n" + unit.name, "came back with a letter...")
      # else:
      #   print("\nYou got a letter...")

    return System

    
class Normal_Job(Job):
  def __init__(self, max_level, type="", min_level=0):

    super().__init__()
    self.max_level = max_level

    if type == "":
      possible_job_types = main.System.available_job_types
      type = possible_job_types[randint(0, len(possible_job_types) - 1)]
    self.type = type

    self.min_level = min_level
  
    self.make_job(self.type, min_level)

    self.gold = ((50 * self.min_level) + (50 * self.length) + randint(0, 50))


  def make_job(self, type, min_level):
    if type == "Labour":
      self.description = "Complete manual labor for a small amount of money. Low risk, low reward."

      self.min_level_finder(1)

      self.length = 1 + 1 * (self.min_level // 5)
      self.min_workers = 1 + 1 * (self.min_level // 10)
      self.max_workers = self.min_workers * 3 

      self.relevant_stats["Strength"] = 3 + (self.min_level // 2) - 1
      self.success_skills.append("Heavy Lifting")

      self.min_result = 1
      self.max_result = 1
    
    elif type == "Guard":
      self.description = "Act as a guard for a client. Thwart attacks and serve them well. Be prepared to give your life for your service."

      self.min_level_finder(10)

      self.length = 4 + 1 * (self.min_level // 10) - 1   # for every sixth min_level it increases for a week
      self.min_workers = 1
      self.max_workers = 1 

      self.relevant_stats["Strength"] = 3 + (self.min_level // 2) - 1
      self.relevant_stats["Intelligence"] = 2 + (self.min_level // 4) - 1
      self.success_skills.append("Awareness")
      self.excel_skills.append("Manners")

      self.min_result = 0
      self.max_result = 1
    
    elif type == "Tactician":
      self.description = "Work as a tactician during a council meeting."

      self.min_level_finder(10)

      self.length = 2 + 1 * (self.min_level // 20)   # for every sixth min_level it increases for a week
      self.min_workers = 1
      self.max_workers = 1 

      self.relevant_stats["Intelligence"] = 5 + (self.min_level // 2) - 1
      self.relevant_stats["Cunning"] = 2 + (self.min_level // 4) - 1
      self.relevant_stats["Allure"] = 1 + (self.min_level // 5) - 1
      self.success_skills.append("History")
      self.excel_skills.append("Commanding Voice")

      self.min_result = 1
      self.max_result = 1
    
    elif type == "Battle":
      self.description = "Participate in a battle that tests a unit’s combat ability. High chance of death if underleveled."

      self.min_level_finder(7)

      self.length = 2 + 1 * (self.min_level // 7) - 1
      self.min_workers = 1 + self.min_level // 7 - 1 
      self.max_workers = self.min_workers + 5

      self.relevant_stats["Strength"] = 5 + int(self.min_level // 3) - 1
      self.relevant_stats["Intelligence"] = 4 + int(self.min_level // 3) - 1
      self.relevant_stats["Agility"] = 3 + int(self.min_level // 3) - 1
      self.relevant_stats["Cunning"] = 1 + (self.min_level // 4) - 1
      self.success_skills.append("Soldier Training")
      self.success_skills.append("Advanced Training")
      self.excel_skills.append("Glory Seeker")

      self.min_result = 1
      self.max_result = 1

      self.determine_enemies()

    elif type == "Theatre":
      self.description = "Join an theatre company to help them put on a production."

      self.min_level_finder(15)

      self.length = 4 + 1 * (self.min_level // 20)
      self.min_workers = 1
      self.max_workers = 1 + self.min_level // 30 

      self.relevant_stats["Allure"] = 10 + (self.min_level // 3) - 1
      self.relevant_stats["Agility"] = 2 + (self.min_level // 3) - 1
      self.success_skills.append("Passion for Art")
      self.excel_skills.append("Flair")

      self.min_result = 1
      self.max_result = 1
    
    elif type == "Infiltration":
      self.description = "Infiltrate a guarded area. Failure is not an option."

      self.min_level_finder(15)

      self.length = 2 + 1 * (self.min_level // 15) - 1
      self.min_workers = 1 + self.min_level // 15 - 1 
      self.max_workers = 1 + self.min_workers

      self.relevant_stats["Agility"] = 8 + (self.min_level // 3) - 1
      self.relevant_stats["Cunning"] = self.min_level // 2 - 1
      self.success_skills.append("Shinobi Training")
      self.excel_skills.append("Gymnastics")

      self.min_result = 1
      self.max_result = 1 # changed from 2
    
    elif type == "Battle Tactician":
      self.description = "Instruct an army in battle. Carries the risk of death."

      self.min_level_finder(15)

      self.length = 3 + 1 * (self.min_level // 10) - 1
      self.min_workers = 1 + self.min_level // 20 - 1 
      self.max_workers = self.min_workers + 2

      self.relevant_stats["Intelligence"] = 8 + int(self.min_level // 1.5) - 1
      self.relevant_stats["Cunning"] = 4 + (self.min_level // 3) - 1
      self.relevant_stats["Allure"] = 1 + (self.min_level // 5) - 1
      self.success_skills.append("History")
      self.excel_skills.append("Commanding Voice")

      self.min_result = 1
      self.max_result = 1

      self.determine_enemies()

  
  def min_level_finder(self, min):
    # print(self.max_level)
    if 0 < self.min_level < min:
      self.min_level = min
    elif self.min_level == 0 or self.min_level > self.max_level:
      self.min_level = randint(min, self.max_level)


  def weekly_update(self):
    
    success_chance = self.calculate_group_chance(self.participants)

    self.length -= 1
 
    if self.type == "Labour":
      for i in self.participants:
        if success_chance[2] > randint(0,100):
          print(i.name, "injured themselves and were discharged.")
          i.condition = "Injured"
          i.current_job = None
    
    elif self.type == "Guard":
      event = self.min_level > randint(0, 100)
      if event == True:
        print("Event!")
        roll = randint(0,100)
        print("Chance:", success_chance[0], "Roll:", roll)
        if success_chance[0] < roll:
          print(self.participants[0].name, "has been slain...")
          self.participants[0].condition = "Dead"
          self.length = 0
        else:
          print("Averted!")
      else:
        print(self.participants_check(), "is doing fine.")
    
    elif self.type == "Battle":
      self.weekly_update_battle()

    elif self.type == "Tactician":
      unit = self.participants[0]
      success_chance = self.calculate_chance(unit)
      roll = randint(0, 100)
      print("Chance:", success_chance[0], "Roll:", roll)
      if success_chance[0] == 100:
        print(unit.name, "has got nothing to worry about.")
      elif success_chance[0] >= roll:
        print(unit.name, "is doing great so far.")
      elif success_chance[0] < roll:
        print(unit.name, "is having a hard time.")
      elif success_chance[0] < (roll // 2):
        print(unit.name, "is overwhelmed.")
    
    elif self.type == "Infiltration":
      if self.length == 1: 
        for i in self.participants:
          if i.condition != "Dead":
            roll = randint(0,100)
            print("Chance:", success_chance[0], "Roll:", roll)
            if success_chance[0] < roll:
              print(i.name, "has been slain...")
              i.condition = "Dead"
              if len(self.participants) == 1:
                self.length = 0
            else:
              print(i.name, "is still alive!")

    elif self.type == "Theatre":
      roll = randint(0,100)
      for i in self.participants:
        print("For:", i.name + ", Chance:", success_chance[2], "Roll:", roll)
        if success_chance[2] >= roll and i.condition == "Fine":
          print(i.name, "injured themselves and were discharged.")
          i.condition = "Injured"
          i.current_job = None
          names = self.participants_check()
          if names == "":
            self.length = 0
        elif i.condition == "Fine":
          if success_chance[0] == 100:
            print(i.name, "has got nothing to worry about.")
          elif success_chance[0] >= roll:
            print(i.name, "is doing great so far.")
          elif success_chance[0] < roll:
            print(i.name, "is having a hard time.")
          elif success_chance[0] < (roll // 2):
            print(i.name, "is overwhelmed.")

    elif self.type == "Battle Tactician":
      print(self.enemy_classes)
      victory_chance = success_chance[0]
      for i in self.enemy_classes:
        victory_chance = round(victory_chance / self.participants[0].matchups[i], 2)
      roll = randint(0,100)
      print("Chance:", 100 - victory_chance, "Roll:", 100 - roll)
      if (100 - victory_chance) > (100 - roll):
        roll2 = randint(1, 3)
        print(roll2)
        if roll2 == 2:
          print(self.participants[0].name, "has been slain...")
          self.participants[0].condition = "Dead"
          self.length = 0
        else:
          print("Things are getting dire...")
      else:
        print(self.participants[0].name, "is still commanding.")  # work on later
    
    # print()
    if self.length > 1:
      print(self.length, "weeks left.")
    elif  self.length == 1:
      print(self.length, "week left.")
    else:
      print("The job is done.\n")

    return self
  

  def weekly_update_battle(self):    
    group_chance = self.calculate_group_chance(self.participants)
    print(self.enemy_classes)
    for i in self.participants: # injury chances are checked individually
      chance = self.calculate_chance(i)
      for j in self.enemy_classes:
        chance = [chance[0], chance[1], round(chance[2] / i.matchups[j], 2)]
      if i.condition == "Fine":
        roll = randint(0,100)
        print("Chance:", 100 - chance[2], "Roll:", 100 - roll, "\tClass:", i.job)
        if chance[2] > roll:
          roll2 = randint(0,100)
          print("Chance:", 100 - group_chance[0], "Roll:", 100 - roll2)
          if group_chance[0] > roll2:
            print(i.name, "injured themselves and were discharged.")
            i.condition = "Injured"
            i.current_job = None
          else:
            print(i.name, "has been slain...")
            i.condition = "Dead"
            if len(self.participants) == 1:
              self.length = 0
        else:
          print(i.name, "is still in the fight!")
      names = self.participants_check()
      if names == "":
        self.length = 0

  
  def determine_rewards(self, result):
    if self.type == "Labour":
      if result == 1:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Strength-Up"] = True
        self.gold = (self.gold * 1.25) + randint(0,25)
      elif result == 0:
        self.unit_rewards["Level-Up"] = True
        self.gold = (self.gold * 1.25) + randint(0,25)
      elif result == -1:
        self.unit_rewards["Level-Up"] = True
        self.gold = 0
    
    elif self.type == "Guard":
      if result == 1:
        self.gold = (self.gold * 1.25) + randint(0,25)
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Allure-Up"] = True
      elif result == 0:
        self.unit_rewards["Level-Up"] = True
    
    elif self.type == "Battle":
      if result == 1:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Strength-Up"] = True
        self.unit_rewards["Intelligence-Up"] = True
        self.unit_rewards["Agility-Up"] = True
      elif result == 0:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Strength-Up"] = True
      elif result == -1:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Strength-Up"] = True
        self.gold = (self.gold * 0.5) + randint(0,25)
    
    elif self.type == "Tactician":
      if result == 1:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Intelligence-Up"] = True
      elif result == 0:
        self.unit_rewards["Level-Up"] = True
      elif result == -1:
        self.gold = 0

    elif self.type == "Theatre":
      if result == 1:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Agility-Up"] = True
        self.unit_rewards["Allure-Up"] = True
      elif result == 0:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Allure-Up"] = True
      elif result == -1:
        self.gold = 0
    
    elif self.type == "Infiltration":
      alive = False
      for i in self.participants:
        if i.condition == "Fine":
          alive = True
      if alive == False:
        self.gold = 0
      elif result == 1:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Agility-Up"] = True
        self.gold = (self.gold * 1.25) + randint(0,25)
      elif result == 0:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Agility-Up"] = True
      elif result == -1:
        self.unit_rewards["Level-Up"] = True
    
    elif self.type == "Battle Tactician":
      if result == 1:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Intelligence-Up"] = True
        self.unit_rewards["Cunning-Up"] = True
      elif result == 0:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Intelligence-Up"] = True
      elif result == -1:
        self.unit_rewards["Level-Up"] = True
        self.unit_rewards["Intelligence-Up"] = True
        self.gold = (self.gold * 0.5) + randint(0,25)

  
class Free_Job(Job):
  def __init__(self, type=""):
    
    super().__init__()

    self.type = type

    self.difficulty = randint(0, 90)

    if self.type == "Busking":
      self.length = 1
      self.description = "Perform on the streets for any passerbys"

      self.success_skills.append("Passion for Art")
      self.excel_skills.append("Flair")

      self.min_result = 1
      self.max_result = 1

    elif self.type == "Gambling":
      self.length = 2
      self.description = "Go to the local gambling house and wage your earnings"

      self.success_skills.append("Hawk Eyes")
      self.excel_skills.append("Quick Hands")

      self.min_result = 2
      self.max_result = 2

    elif self.type == "War":
      self.description = "Answer the call of duty and fight for your homeland"
      self.length = 12

      self.success_skills.append("Soldier Training")
      self.success_skills.append("Advanced Training")
      self.excel_skills.append("Glory Seeker")

      self.determine_enemies(self.difficulty)

      self.min_result = 1
      self.max_result = 2

    self.relevant_stats_update()

    self.participants = {
    }


  def relevant_stats_update(self):
    if self.type == "Busking":
      self.relevant_stats["Allure"] = 1 + self.difficulty // 6
    elif self.type == "Gambling":
      self.relevant_stats["Cunning"] = 1 + self.difficulty // 5
    elif self.type == "War":
      self.relevant_stats["Strength"] = 3 + int(self.difficulty // 7)
      self.relevant_stats["Intelligence"] = 2 + int(self.difficulty // 7)
      self.relevant_stats["Agility"] = 2 + int(self.difficulty // 8)
      self.relevant_stats["Cunning"] = 1 + int(self.difficulty // 8)


  def print_all_participants(self):
    # print(self.participants)
    for i in self.participants:
      print(i.name, "\tWeeks:", self.participants[i]["Length"])
      print("--------------------------------------------------------------------------------------------")


  def print_difficulty_message(self):
    if self.difficulty <= 15:
      print("Easy", self.difficulty)
    elif 15 < self.difficulty <= 30:
      print("Not bad", self.difficulty)
    elif 30 < self.difficulty <= 45:
      print("OK", self.difficulty)
    elif 45 < self.difficulty <= 60:
      print("Normal", self.difficulty)
    elif 60 < self.difficulty <= 85:
      print("Hard", self.difficulty)
    elif 85 < self.difficulty:
      print("Difficult", self.difficulty)
    else:
      print(self.difficulty)


  def weekly_update(self, unit):
    
    # self.print_difficulty_message()
    self.length -= 1 
    
    chance = self.calculate_chance(unit)
    self.participants[unit]["Length"] -= 1

    if self.type == "Busking":
      weekly_gold = (self.difficulty * 3) + randint(0, 20)
      if weekly_gold < 50:
        weekly_gold = 50 + randint(0, 20)
      if chance[0] > (self.difficulty / 2):
        self.participants[unit]["Gold"] += weekly_gold * 1.25
        self.participants[unit]["Results"].append(1)
        print(unit.name, "got a lot of money this week!")
      elif chance[0] >= self.difficulty:
        self.participants[unit]["Gold"] += weekly_gold
        self.participants[unit]["Results"].append(0)
        print(unit.name, "did OK this week.")
      elif chance[0] < self.difficulty:
        self.participants[unit]["Results"].append(-1)
        print(unit.name, "didn't do well this week.")
      # print(unit.name, "Chance:", chance[0], "Difficulty:", self.difficulty, self.participants[unit])
    elif self.type == "Gambling":
      difference = chance[0] - self.difficulty
      # print("Difference:", difference)
      if self.participants[unit]["Gold"] > 0:
        if -10 <= difference <= 10:
          # print(0)
          print(unit.name, "is having some luck.")
          self.participants[unit]["Gold"] += randint(-50, 50)
          self.participants[unit]["Results"].append(0)
        elif -40 <= difference < -10:
          # print(-1)
          print(unit.name, "is having bad luck.")
          self.participants[unit]["Gold"] = (self.participants[unit]["Gold"] * 0.5) + randint(-50, 50)
          self.participants[unit]["Results"].append(-1)
        elif difference < -40:
          # print(-2)
          print(unit.name, "struck out and is now broke.")
          self.participants[unit]["Gold"] = 0
          self.participants[unit]["Results"].append(-2)
        elif 10 < difference < 40:
          # print(1)
          print(unit.name, "is having good luck.")
          self.participants[unit]["Gold"] = (self.participants[unit]["Gold"] * 1.25) + randint(-50, 50)
          self.participants[unit]["Results"].append(1)
        elif 40 <= difference:
          # print(2)
          print(unit.name, "is having great luck.")
          self.participants[unit]["Gold"] = (self.participants[unit]["Gold"] * 1.5) + randint(-50, 50)
          self.participants[unit]["Results"].append(2)
      
      if self.participants[unit]["Gold"] > 0:
        print("Their current pocket:", str(self.participants[unit]["Gold"]) + "$")
      # print(unit.name, "Chance:", chance[0], "Difficulty:", self.difficulty, self.participants[unit])
    elif self.type == "War":
      self.participants[unit]["Gold"] += 300 + randint(-50, 50)

      roll = randint(0,100)
      # print(unit.name, "Chance:", chance[2], "Roll:", roll)
      if chance[2] > roll:
      # if chance[2] >= 0:
        print(unit.name, "is in a tough spot...")
        roll2 = randint(0,100)
        # print("Chance:", chance[0], "Roll:", roll2)
        # if chance[0] >= roll2:
        if chance[0] >= (roll2 * 1.5):
          print(unit.name, "fought their way through!")
          self.participants[unit]["Results"].append(2)
        # elif roll2 > chance[0] >= (roll2 // 2):
        elif chance[0] >= roll2:
          print(unit.name, "injured themselves and were discharged.")
          unit.condition = "Injured"
          unit.current_job = None
          self.participants[unit]["Length"] = 0
          self.participants[unit]["Results"].append(-1)
        else:
          print(unit.name, "has been slain...")
          unit.condition = "Dead"
          self.participants[unit]["Length"] = 0
          self.participants[unit]["Results"].append(-1)
      else:
        print(unit.name, "is still fighting. Weeks left:", self.participants[unit]["Length"])
        self.participants[unit]["Results"].append(1)

      # print(unit.name, "Injury chance:", chance[2], "Difficulty:", self.difficulty, "Enemies:", self.enemy_classes, self.participants[unit])
    
    
    return self


  def determine_rewards(self, unit, result):
    self.unit_rewards["Level-Up"] = True
    
    if self.type == "Busking":
      if result == 1:
        self.unit_rewards["Allure-Up"] = True

    if self.type == "Gambling":
      if result >= 0:
        self.unit_rewards["Cunning-Up"] = True

    elif self.type == "War": 
      self.unit_rewards["Strength-Up"] = True
      self.unit_rewards["Intelligence-Up"] = True
      self.unit_rewards["Agility-Up"] = True


  def job_finish(self, System, unit):
    print()

    if System.history_open == False:  # can view job history after completing first job
      System.history_open = True

    System.money += self.participants[unit]["Gold"]
    
    money_achieved = self.participants[unit]["Gold"] - self.participants[unit]["Original money"]
    if money_achieved > 0:
      print(unit.name, "earned", str(money_achieved) + "$")
    elif money_achieved < 0:
      print(unit.name, "lost", str(abs(money_achieved)) + "$")
    else:
      print(unit.name, "didn't earn any money...")

    total = 0
    for i in self.participants[unit]["Results"]:
      total += i
    b = total // len(self.participants[unit]["Results"])
    if unit.condition != "Fine":
      pass
    elif b == 0:
      print(unit.name + " did well! (pass)")
    elif b == 1:
      if self.max_result == 1:
        print(unit.name + " did amazing!!! (perfect)")
      else:
        print(unit.name + " did great!! (excel)")
    elif b == 2:
      print(unit.name + " did amazing!!! (perfect)")
    elif b == -1:
      if self.min_result == -1:
        print(unit.name + " did amazing!!! (perfect)")
      else:
        print(unit.name + " messed up... (disaster)")
    elif b == -2:
      print(unit.name + " messed up... (disaster)")

    a = System.roster[System.roster.index(unit)]

    System.job_history[self.type][b] += 1

    System.job_history[self.type]["Count"] = self.find_job_history_tally(System.job_history[self.type])
    roll = randint(0, 100)
    job_offer = False
    print(System.job_history[self.type]["Count"], roll)
    if System.job_history[self.type]["Count"] >= roll:
      job_offer = True

    self.determine_rewards(a, b)
    if job_offer == True:
      self.find_job_offer(System, unit)
    # self.find_job_offer(System, unit)

    if unit.condition == "Fine":
      self.give_unit_rewards(a)
    System.roster[System.roster.index(unit)].current_job = None
    print()
    # System.free_jobs_in_progress[self].partipants.remove(unit)
    # print(self.participants.index(self.participants[unit]))
    # self.participants.pop(unit)

    self.participants.pop(unit)

    for i in System.roster:
      if i.condition == "Dead":
        print(i.name, "is dead at", i.age, "years old.")
        System.roster.remove(i)

    return System


  def short_description(self):
    print(self.type)
    print(self.description)
    if self.length == 1:
      print("Length: 1 week")
    else:
      print("Length:", int(self.length), "weeks")
    print("Current # of workers:", len(self.participants))
    print("Important stats:")
    if self.relevant_stats["Strength"] != 0:
      print("\tStrength", self.relevant_stats["Strength"])
    if self.relevant_stats["Intelligence"] != 0:
      print("\tIntelligence", self.relevant_stats["Intelligence"])
    if self.relevant_stats["Agility"] != 0:
      print("\tAgility", self.relevant_stats["Agility"])
    if self.relevant_stats["Cunning"] != 0:
      print("\tCunning", self.relevant_stats["Cunning"])
    if self.relevant_stats["Allure"] != 0:
      print("\tAllure", self.relevant_stats["Allure"])
    # if len(self.enemy_classes) > 0:
    #   print("Enemies:")
    #   for i in self.enemy_classes:
    #     print("\t"+i)
    print("--------------------------------------------------------------------------------------------")


class Training(Job):
  def __init__(self, stat="", skill=""):

    super().__init__()

    self.stat = stat
    self.skill = skill
    self.instructor_name = ""
    self.determine_instructor_name()

    if stat != "":
      self.cost = 500
      if stat == "Strength":
        self.type = "Strength training"
        # self.type = "strength training"
        self.description = "Send units to Hugo and he will help them build some muscle."
        self.unit_rewards["Strength-Up"] = True

      elif stat == "Intelligence":
        self.type = "Intelligence training"
        # self.type = "intelligence training"
        self.description = "Send units to Wyatt and he will help them expand their horizons."
        self.unit_rewards["Intelligence-Up"] = True

      elif stat == "Agility":
        self.type = "Agility training"
        # self.type = "agility training"
        self.description = "Send units to Soma and he will train their flexibility and acrobatics."
        self.stat = "Agility"
      
      elif stat == "Cunning":
        self.type = "Cunning training"
        # self.type = "cunning training"
        self.description = "Send units to Flint and he will teach them the ways of deceit."
        self.stat = "Cunning"
      
      elif stat == "Allure":
        self.type = "Allure training"
        # self.type = "allure training"
        self.description = "Send units to Isa and she will teach them to perfect their public image."
        self.stat = "Allure"
    
    elif skill != "":
      self.cost = 1000
      self.description = "Send units to " + self.instructor_name + " to learn the skill " + self.skill
      # self.type = skill.lower() + " training"
      self.type = skill + " training"
      self.skill = skill

    self.length = 4
    self.min_workers = 1
    self.max_workers = 4


  def determine_instructor_name(self):
    stat_name = {
      "Strength": "Hugo",
      "Intelligence": "Wyatt",
      "Agility": "Soma",
      "Cunning": "Flint",
      "Allure": "Isa"
    }

    skill_name = {
      "Adept Student": "Jon",
      "Heavy Lifting": "Marshal",
      "Awareness": "Sir Teddy",
      "Manners": "Sir Ward",
      "Hawk Eyes": "Mr. Hawk",
      "Quick Hands": "Mr. Vulture",
      "Soldier Training": "Captain Edward",
      "Advanced Training": "Captain Wilfred",
      "Glory Seeker": "Buster",
      "Passion for Art": "Lana",
      "Flair": "Arthur",
      "History": "Aldegund",
      "Commanding Voice": "Meyer",
      "Shinobi Training": "Ace",
      "Gymnastics": "Jez",
      "Fighter": "Zeru",
      "Wizard": "Aria",
      "Thief": "Sir Demir",
      "Knight": "Jove",
      "Magician": "Fletcher",
      "Archer": "Captain Wallace",
      "Monk": "Girisha"
    }
    if self.stat != "":
      self.instructor_name = stat_name[self.stat]
    elif self.skill != "":
      self.instructor_name = skill_name[self.skill]


  def weekly_update(self):

    self.length -= 1

    if self.length > 0:
      print(self.participants_check(), "are still training. Weeks left:", self.length)
    elif self.length == 0:
      print(self.participants_check(), "are done their training.")

    return self    


  def short_description(self):
    print(self.type)
    print(self.description)
    print("Length:", int(self.length), "weeks")
    print("# of participants:", self.min_workers, "-", self.max_workers)
    print("Cost per participant:", str(self.cost) + "$")
    print("--------------------------------------------------------------------------------------------")


  def job_finish(self, System):

    for i in self.participants:
      min = 0
      if i.skills["Adept Student"] == True:
        min = 20
      roll = randint(min, 100)
      print(roll)

      if self.stat != "":
        if roll >= 90:
          print(i.name, "did amazing!")
        elif 90 > roll >= 60:
          print(i.name, "did great!")
        elif 60 > roll >= 30:
          print(i.name, "did well!")
        else:
          print(i.name, "failed...")
      elif self.skill != "":
        if roll >= 90:
          print(i.name, "did amazing!")
        elif roll >= 50:
          print(i.name, "did well!")
        else:
          print(i.name, "failed...")
      
      self.give_unit_rewards(i, roll)

      i.current_job = None

    return System


  def give_unit_rewards(self, unit, result):
    
    lvl_result = result // 45
    if lvl_result > 0:
      unit.level += lvl_result
      print(unit.name + " is now lvl. " + str(unit.level) + "!\t(" + str(unit.level - lvl_result) + " -> " + str(unit.level) + ")")

    stat_result = result // 30
    if stat_result > 0 and self.stat != "":
      if self.unit_rewards["Strength-Up"] == True:
        unit.strength += stat_result
        print(unit.name + " is stronger! \t(" + str(unit.strength - stat_result) + " -> " + str(unit.strength) + ")")

      if self.unit_rewards["Intelligence-Up"] == True:
        unit.intelligence += stat_result
        print(unit.name + " is smarter! \t(" + str(unit.intelligence - stat_result) + " -> " + str(unit.intelligence) + ")")

      if self.unit_rewards["Agility-Up"] == True:
        unit.agility += stat_result
        print(unit.name + " is faster! \t(" + str(unit.agility - stat_result) + " -> " + str(unit.agility) + ")")

      if self.unit_rewards["Cunning-Up"] == True:
        unit.cunning += stat_result
        print(unit.name + " is more cunning! \t(" + str(unit.cunning - stat_result) + " -> " + str(unit.cunning) + ")")

      if self.unit_rewards["Allure-Up"] == True:
        unit.allure += stat_result
        print(unit.name + " is more charming! \t(" + str(unit.allure - stat_result) + " -> " + str(unit.allure) + ")")

    skill_result = result // 40
    if skill_result > 0 and self.skill != "":
      unit.skills[self.skill] = True
      print(unit.name + " now knows " + self.skill + "!")
