import unit
import hiring
import job
import message
import tests
import tips
from int_checker import int_checker
from news import read_weekly_news
from random import randint
from time import sleep

#ctrl+k ctrl+1
# To do list:
  # All letters
  # News
    # Busking difficulty
    # News reports on the war
      # The previous day's difficulty
      # Foreshadowing the dire turn it will take
  # War letter (# war letter)
  # Adjust all inputs to be normal instead of int
  # Info sheets (tutorial)
  # Make personalized victory messages
  # Make better descriptions
  # When in hardcore war phase, increase minimum difficulty for war
  # Balance economy
  # Make attitude effect stuff


class System:
  date = [5, 1, 0]  # month, week, year
  money = 1000
  roster = []

  job_history = {
    "Labour": {1: 0, 0: 0, -1: 0, "Count": 0},
    "Guard": {1: 0, 0: 0, "Count": 0},
    "Battle": {2: 0, 1: 0, 0: 0, -1: 0, "Count": 0}, 
    "Tactician": {1: 0, 0: 0, -1: 0, "Count": 0}, 
    "Theatre": {1: 0, 0: 0, -1: 0, "Count": 0}, 
    "Infiltration": {1: 0, 0: 0, -1: 0, "Count": 0}, 
    "Battle Tactician": {1: 0, 0: 0, -1: 0, "Count": 0},
    "Busking": {1: 0, 0: 0, -1: 0, "Count": 0},
    "Gambling": {2: 0, 1: 0, 0: 0, -1: 0, -2: 0, "Count": 0},
    "War": {2: 0, 1: 0, 0: 0, -1: 0, "Count": 0}
  }
  weekly_jobs = []
  jobs_in_progress = []
  free_jobs_in_progress = []
  training_in_progress = []

  available_job_types = ["Labour"]
  # available_job_types = ["Labour", "Guard", "Battle", "Tactician", "Theatre", "Infiltration", "Battle Tactician"]
  locked_job_types = ["Guard", "Battle", "Tactician", "Theatre", "Infiltration", "Battle Tactician"]

  available_free_jobs = []
  # available_free_jobs = ["Busking"]
  locked_free_jobs = ["Busking", "Gambling", "War"]

  training_jobs = []
  locked_stat_training_types = ["Strength", "Intelligence", "Agility", "Cunning", "Allure"]
  locked_stat_training_types = sorted(locked_stat_training_types)

  locked_skill_training_types = ["Adept Student", "Heavy Lifting", "Awareness", "Manners", "Hawk Eyes", "Quick Hands", "Soldier Training", "Advanced Training", "Glory Seeker", "Passion for Art", "Flair", "History", "Commanding Voice", "Shinobi Training", "Gymnastics", "Fighter", "Wizard", "Thief", "Knight", "Magician", "Archer", "Monk"]
  locked_skill_training_types = sorted(locked_skill_training_types)

  mailbox = []

  wartime_phase_minimum_soldiers = 0
  wartime_phase_current_soldiers = 0

  tips = {
    "Job start": True, # explains how to sign up for a job and how commanding units work
    "Classes": True,   # class roles & preferences
    "Stats": True,
    "Skills": True,
    "Free job": False,
    "Training": False,
    "Doctor": False,   # doctor
  }

  history_open = False

  doctor_open = False
  doctor_heals = 0

  weekly_busking_difficulty = 0
  weekly_war_difficulty = 0
  
  weekly_letter_count = 0

  max_level = 5
  max_strength = 0
  max_intelligence = 0
  max_agility = 0
  max_cunning = 0
  max_allure = 0


def wait():
  input("Press anything to continue.\n")


def menu_top():
  print("\n========================")
  print("Date: M" + str(System.date[0]) + ", W" + str(System.date[1]) + ", Y" + str(System.date[2]))
  print("Funds:", str(System.money) + "$")
  print("Available units:", availability_checker(), "/", len(System.roster))
  if System.wartime_phase_minimum_soldiers > System.wartime_phase_current_soldiers:
    print("Remaining soldiers:", System.wartime_phase_minimum_soldiers - System.wartime_phase_current_soldiers)
  if len(System.mailbox) > 0:
    print("Mailbox:", len(System.mailbox), "message")
  print("========================\n")


def availability_checker():
  count = 0
  for current in System.roster:
    if current.current_job == None and current.condition == "Fine":
      count += 1
  return count


def date_update():
    date = System.date
    date[1] += 1
    if date[1] > 4:  # new month
        wages_for_employees = 0
        for i in range(len(System.roster)):
            wages_for_employees += System.roster[i].calculate_wage()
        System.money -= wages_for_employees
        date[1] = 1
        date[0] += 1
    if date[0] > 12:  # new year
        date[0], date[1] = 1, 1
        date[2] += 1
        check_wartime_phase_soldiers()
    for i in range(len(System.roster)):
        if System.roster[i].level > System.max_level:
            System.max_level = System.roster[i].level


def check_wartime_phase_soldiers():
  if System.wartime_phase_minimum_soldiers > System.wartime_phase_current_soldiers:
    print("You did not enlist enough soldiers into the army and were fined $10,000.")
    System.money -= 10000
            

def weekly_update():
  print("======================================= WEEKLY UPDATE ======================================")

  date_update()
  weekly_update_jobs()

  no_jobs = True
  for i in System.jobs_in_progress:
    no_jobs = False
    print("Job #" + str(System.jobs_in_progress.index(i) + 1), "(" + i.type + ")")
    i = i.weekly_update()
  
    # for i in System.roster:
    #   i.short_description()
  # print("Roster size:", len(System.roster))

    if i.length == 0:
      i.job_finish(System)
      for i in range(len(System.roster)):
        if System.roster[0].condition != "Dead":
          System.roster.append(System.roster[0])
        else:
          print(System.roster[0].name, "is dead at", System.roster[0].age, "years old.")
        System.roster.remove(System.roster[0])
      print("\nLiving employees:")
      for j in System.roster:
        print("- ", j.name)
      # System.jobs_in_progress.remove(i)
    print("--------------------------------------------------------------------------------------------")
  
  free_job_total = False
  for i in System.free_jobs_in_progress:
    # print(i.type + ":", len(i.participants))
    if len(i.participants) > 0:
      free_job_total = True
      print(i.type + ":", len(i.participants), "worker")
      for j in i.participants:
        i = i.weekly_update(j)

      for k in list(i.participants):
        if i.participants[k]["Length"] == 0 or i.participants[k]["Gold"] == 0:
          i.job_finish(System, k)

      print("--------------------------------------------------------------------------------------------")

    i.difficulty = randint(1, 90)
    if i.type == "War":
      System.weekly_war_difficulty = i.difficulty
    elif i.type == "Busking":
      System.weekly_busking_difficulty = i.difficulty
    i.relevant_stats_update()
  
  for i in System.training_in_progress:
    i.short_description()
    print(i.instructor_name + "'s", i.type)
    i = i.weekly_update()
    if i.length == 0:
      i.job_finish(System)
      System.training_jobs.append(job.Training(i.stat, i.skill)) # TODO
    print("--------------------------------------------------------------------------------------------")

  for i in System.jobs_in_progress:
    if i.length == 0:
      System.jobs_in_progress.remove(i)
  
  if no_jobs == True and free_job_total == False and len(System.training_in_progress) == 0:
    print("No jobs were done this week...")

  System.weekly_jobs = [job.Normal_Job(System.max_level, "Labour", 1)]
  for i in range(len(System.roster) // 2):
    chosen_type = System.available_job_types[randint(0, len(System.available_job_types)-1)]
    System.weekly_jobs.append(job.Normal_Job(System.max_level, chosen_type))

  if len(sick_list()) > 0 and System.doctor_open == False:
    System.mailbox.append(message.Message("Dr. Lior", "mail", "Doctor office now open", "TODO", 0, None, None, None, None, False, 1))
    print("You got a letter...")

  for i in System.roster:
    if i.level > System.max_level:
      System.max_level = i.level
    if i.strength > System.max_strength:
      System.max_strength = i.strength
    if i.intelligence > System.max_intelligence:
      System.max_intelligence = i.intelligence
    if i.agility > System.max_agility:
      System.max_agility = i.agility
    if i.cunning > System.max_cunning:
      System.max_cunning = i.cunning
    if i.allure > System.max_allure:
      System.max_allure = i.allure

  # print("Max level:", System.max_level)
  # print("Max strength:", System.max_strength)
  # print("Max intelligence:", System.max_intelligence)
  # print("Max agility:", System.max_agility)
  # print("Max cunning:", System.max_cunning)
  # print("Max allure:", System.max_allure)

  # war letter
  if System.date == [5, 1, 3]:
    System.mailbox.append(message.Message("Mr. Placeholder", "mail", "War start placeholder", "", 0, None, None, None, None, False, 2))

  if System.weekly_letter_count == 1:
    print("\nYou got a letter!")
  elif System.weekly_letter_count > 1:
    print("\nYou got " + str(System.weekly_letter_count) + " letters!")
  System.weekly_letter_count = 0

  wait()

  birthday_checker()


def weekly_update_jobs():
  count = 0
  # Busking
  if System.date == [6, 1, 0]:
    System.mailbox.append(message.Message("Mr. Placeholder", "job", "Busking Placeholder", "Busking Placeholder", 0, None, None, "Busking"))
    System.weekly_letter_count += 1
  # Guard
  if System.max_level == 10 and "Guard" in System.locked_job_types:
    System.mailbox.append(message.Message("Mr. Placeholder", "job", "Guard Placeholder", "Guard Placeholder", 0, None, "Guard"))
    System.weekly_letter_count += 1
  # Gambling
  if System.date == [1, 1, 1]:
    System.mailbox.append(message.Message("Mr. Placeholder", "job", "Gambling Placeholder", "Gambling Placeholder", 0, None, None, "Gambling"))
    System.weekly_letter_count += 1
  # Battle
  if len(System.roster) >= 10 and "Battle" in System.locked_job_types:
    System.mailbox.append(message.Message("Mr. Placeholder", "job", "Battle Placeholder", "Battle Placeholder", 0, None, "Battle"))
    System.weekly_letter_count += 1
  # Tactician
  if System.max_intelligence >= 15 and "Tactician" in System.locked_job_types:
    System.mailbox.append(message.Message("Mr. Placeholder", "job", "Tactician Placeholder", "Tactician Placeholder", 0, None, "Tactician"))
    System.weekly_letter_count += 1
  # Theatre    Max. stat    Allure 15, Agility 10
  if System.max_allure >= 15 and System.max_agility >= 15 and "Theatre" in System.locked_job_types:
    System.mailbox.append(message.Message("Mr. Placeholder", "job", "Theatre Placeholder", "Theatre Placeholder", 0, None, "Theatre"))
    System.weekly_letter_count += 1
  # Infiltration    Max. stat    Level 15, Agility 15
  if System.max_level >= 15 and System.max_agility >= 15 and "Infiltration" in System.locked_job_types:
    System.mailbox.append(message.Message("Mr. Placeholder", "job", "Guard Placeholder", "Guard Placeholder", 0, None, "Guard"))
    System.weekly_letter_count += 1
  # Battle Tactician    Job completion    Tactician jobs
  rand = (System.job_history["Tactician"][1] * 10) + (System.job_history["Tactician"][0] * 5)
  if rand >= randint(10, 100) and "Infiltration" in System.locked_job_types:
    System.mailbox.append(message.Message("Mr. Placeholder", "job", "Battle Tactician Placeholder", "Battle Tactician Placeholder", 0, None, "Battle Tactician"))
    System.weekly_letter_count += 1
  # War
  if System.date == [2, 1, 5]:
    System.mailbox.append(message.Message("Mr. Placeholder", "job", "War Placeholder", "War Placeholder", 0, None, None, "War"))
    System.weekly_letter_count += 1
  
  # Adept Student
  if len(System.roster) >= 5 and "Adept Student" in System.locked_skill_training_types:
    System.mailbox.append(message.Message("Jon", "job", "Adept Student Placeholder", "Adept Student Placeholder", 0, None, None, None, "Adept Student"))
    System.weekly_letter_count += 1


def print_job_history():
  print("------------------------------------------ HISTORY ------------------------------------------")
  a = len(System.available_job_types) + len(System.available_free_jobs)
  print("Jobs available:", str(a) + "/10\n---------------------")
  for i in System.job_history:
    if i in System.available_job_types or i in System.available_free_jobs:
      string = ""
      if 2 in System.job_history[i]:
        string += "Perfect: " + str(System.job_history[i][2])
        string += ", Excel: " + str(System.job_history[i][1])
      else:
        string += "Perfect: " + str(System.job_history[i][1])
      string += ", Pass: " + str(System.job_history[i][0])
      if -1 in System.job_history[i]:
        string += ", Fail: " + str(System.job_history[i][-1])
      if -2 in System.job_history[i]:
        string += ", Disaster: " + str(System.job_history[i][-2])
      string += ", Count: " + str(System.job_history[i]["Count"]) # delete later

      if i == "Battle Tactician":
        print(i + ":\t", string)
      elif i == "Infiltration":
        print(i + ":\t\t", string)
      elif i == "Tactician" or i == "Theatre" or i == "Busking" or i == "Gambling":
        print(i + ":\t\t\t", string)
      else:
        print(i + ":\t\t\t\t", string)
    else:
      print("???")
  if System.doctor_open == True:
    print("\nDoctor Heals (Working Title):", System.doctor_heals)


def activity_board():
    while System.roster[0].current_job == None:
        menu_top()
        print_activity_board_items()
        choice = input()
        choice = int_checker(choice)
        # choice = 1
        print()
        if choice == 1:  # Jobs
            option_1()
        elif choice == 2:  # Hire
          if len(System.roster) < 99:
            new = hiring.hiring_board(System)
            if new != None:
                System.roster.append(new)
                System.money -= new.calculate_worth()
          else:
            print("Your roster is full...")
            sleep(2)
        elif choice == 3:  # Roster
            option_3()
        elif choice == 4:  # News
            read_weekly_news(System.date, System.weekly_busking_difficulty, System.weekly_war_difficulty)
            sleep(1)
        elif choice == 5:
            option_5()
        elif choice == 6:
            mailbox()
        elif choice == 7:
            option_7()
        elif choice == 8 and System.history_open == True:
            option_8()
        elif choice == 9 and System.doctor_open == True: # need to implement System.doctor_open
            doctor()
        elif choice == 0:  # Wait
            break
        else:
            print("Error")
    print("See you next week")
    sleep(1)


def print_activity_board_items():
  print("What do you want to do?\n 1: Job board\n 2: Hire\n 3: Roster\n 4: News\n 5: Current jobs being done\n 6: Mailbox\n 7: Tips")
  if System.history_open == True:
    print(" 8: History")
  if System.doctor_open == True:
      print(" 9: Doctor")
  print(" 0: Wait")


def option_1():
  while System.roster[0].current_job == None:
    a = len(System.weekly_jobs) > 0
    b = len(System.free_jobs_in_progress) > 0
    c = len(System.training_jobs) > 0
    d = a == True or b == True or c == True
   
    if a == True and (b == False and c == False):
      normal_job_board()
      break
    elif d == True:
      print("Choose what type of job you want:")
      if a == True:
        print(" 1: Normal Jobs")
      else:
        print(" (No normal jobs remaining...)")
      if b == True:
        print(" 2: Free Jobs")
      if c == True:
        print(" 3: Training")
      elif len(System.locked_skill_training_types) < 22 or len(System.locked_stat_training_types) < 5:
        print(" (All training opportunities are taken...)")
      choice = input("Pick a type (0 to go back)\n")
      choice = int_checker(choice)
      # choice = 3
      if choice == 0:
        break
      elif choice == 1 and a == True:
        normal_job_board()
        pass
      elif choice == 2 and b == True:
        free_job_board()
      elif choice == 3 and c == True:
        training_board()
      else:
        print("\nError")
    else:
      print("Nothing to do now, pal...")
      break

  wait()


def normal_job_board():
  print()
  while True:
    if len(System.weekly_jobs) > 0:
      for i in range(len(System.weekly_jobs)):
        print(str(i + 1) + ":")
        System.weekly_jobs[i].short_description()
      job_choice = input("\nWhat job interests you? Press 0 to quit.\n")
      job_choice = int_checker(job_choice)
      if job_choice == 0:
        break
      elif job_choice == "":
        print("\nError\n")
      elif job_choice > len(System.weekly_jobs) or job_choice < 0:
        print("Error\n\n")
      else:
        job_choice -= 1
        FAU = find_appropriate_units(job_choice)
        if len(FAU) < System.weekly_jobs[job_choice].min_workers:
          print("\nYou don't have enough workers who are qualified to do this job...\n")
          sleep(1)
        else:
          choose_units(job_choice)
          sleep(2)
          break
    else:
      print("Every job is taken, buddy.")
      sleep(2)
      break


def find_appropriate_units(job_choice):
  units = []
  min_lvl = System.weekly_jobs[job_choice].min_level
  for i in System.roster:
    if i.level >= min_lvl and i.current_job == None:
      units.append(i)
  return units


def choose_units(job_choice):
    job = System.weekly_jobs[job_choice]
    print("\n\nThis job requires a minimum of", job.min_workers, "participants.\n")
    units = []
    while True:
      available_count = 0
      if len(units) < job.max_workers:
        for i in range(len(System.roster)):
          if System.roster[i] not in units and System.roster[i].level >= job.min_level and System.roster[i].current_job == None:
            print(str(i + 1) + ":")
            System.roster[i].short_description()
            available_count += 1

      if available_count == 0:
        print("No more available units...\n")
      elif len(units) == 0:
        unit_choice = input("Which unit do you want to assign to this job? Press 0 to quit.\n")
        unit_choice = int_checker(unit_choice)
        if unit_choice == 0:
          break
        elif unit_choice == "":
          print("???\n")
          pass
        elif unit_choice > len(System.roster):
          pass
        elif System.roster[unit_choice - 1].current_job != None or System.roster[unit_choice - 1].level < job.min_level:
          print("\n?\n")
        else:
          unit = System.roster[unit_choice - 1]
          print()
          print(unit.name + "'s chances:")
          job.print_chance(unit)
          print("Assign", unit.name, "to this task? (1 for yes, 0 for no)")
          confirm = input()
          confirm = int_checker(confirm)
          if confirm == 1:
            if unit.commander == True:
              commander_confirm = input("This is your commander unit. If you send them to a job, all of your unemployed mercs will not have a job to do.\nAre you sure? (1 for yes, 0 for no)\n")
              commander_confirm = int_checker(commander_confirm)
              if commander_confirm == 1:
                  units.append(unit)
            else:
                units.append(unit)
      elif 0 < len(units) < job.max_workers:
        unit_choice = input("Are there any other units you want to assign? Press 0 if not.\n")
        unit_choice = int_checker(unit_choice)
        if unit_choice == "":
          pass
        elif unit_choice > len(System.roster):
          pass
        elif unit_choice == 0 or System.roster[unit_choice - 1].current_job != None or System.roster[unit_choice - 1].level < job.min_level:
          pass
        elif unit_choice > 0 and System.roster[unit_choice - 1] not in units:
          unit = System.roster[unit_choice - 1]
          print()
          print(unit.name + "'s chances:")
          job.print_chance(unit)
          print("Assign", unit.name, "to this task? (1 for yes, 0 for no)")
          confirm = input("")
          confirm = int_checker(confirm)
          if confirm == 1:
            if unit.commander == True:
              commander_confirm = input("This is your commander unit. If you send them to a job, all of your unemployed mercs will not have a job to do.\nAre you sure? (1 for yes, 0 for no)\n")
              commander_confirm = int_checker(commander_confirm)
              if commander_confirm == 1:
                units.append(unit)
            else:
              units.append(unit)
          else:
            print("Error")

      if len(units) >= job.min_workers:
        unit_names = ""
        for i in units:
          unit_names += i.name + ", "
        if len(units) > 1:
          job.print_group_chance(units)

        if len(units) < job.max_workers:
          print("Send:", unit_names[0:-2] + "? (Press 1 to confirm, press 2 to add more, press 0 to return to the job list)")
          confirm = input("")
          confirm = int_checker(confirm)
          if confirm == 1:
            job_start(job_choice, units)
            break
          elif confirm == 2:
            print()
            pass
          elif confirm == 0:
            break
        else:
          print("Send:", unit_names[0:-2] + "? (Press 1 to confirm, press 0 to return to the job list)")
          confirm = input("")
          confirm = int_checker(confirm)
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
    i.attitude += i.work[job.type]
  System.weekly_jobs.remove(job)
  print("Good to go!\n")


def free_job_board():
  print()
  while True:
    if len(System.free_jobs_in_progress) > 0:
      for i in range(len(System.free_jobs_in_progress)):
        print(str(i + 1) + ":")
        System.free_jobs_in_progress[i].short_description()
      job_choice = input("\nWhat job interests you? Press 0 to quit.\n")
      job_choice = int_checker(job_choice)
      if job_choice == 0:
        return
      elif job_choice == "":
        pass
      elif job_choice > len(System.free_jobs_in_progress) or job_choice < 0:
        print("Error\n\n")
      elif System.free_jobs_in_progress[job_choice-1].type == "Gambling" and System.money < 100:
        print("\nNot enough money to go gambling with...\n")
      else:
        choose_units_free(job_choice-1)
        sleep(2)
        break


def choose_units_free(job_choice):
  job = System.free_jobs_in_progress[job_choice]
  # while System.roster[0].current_job == None:
  while True:
    available_units = []
    for i in range(len(System.roster)):
      if System.roster[i].current_job == None:
        available_units.append(System.roster[i])
    
    for j in range(len(available_units)):
      print(str(j + 1) + ":")
      System.roster[j].short_description()
    
    unit_choice = input("Which unit do you want to assign to this job? Press 0 to quit.\n")
    unit_choice = int_checker(unit_choice)
    if unit_choice == 0:
      return
    elif unit_choice == "":
      pass
    elif unit_choice > len(available_units) or unit_choice == "":
      print("\nError\n")
    else:
      unit = System.roster[unit_choice - 1]
      # print(unit.name + "'s chances:")
      job.print_chance(unit)
      print("Assign", unit.name, "to this task? (1 for yes, 0 for no)")
      confirm = input("")
      confirm = int_checker(confirm)
      if confirm == 1:
        if unit.commander == True:
          commander_confirm = input("This is your commander unit. If you send them to a job, all of your unemployed mercs will not have a job to do.\nAre you sure? (1 for yes)\n")
          commander_confirm = int_checker(commander_confirm)
          if commander_confirm != 1:
            pass
        money2 = 0
        if job.type == "Gambling":
          while money2 == 0:
            money = input("How much money will you give " + unit.name + "?\n(Minimum: 100, maximum: " + str(System.money) + ")\n")
            money = int_checker(money)
            if money == "":
              pass
            elif 100 <= money <= System.money:
              money2 = money
            else:
              print("Illegal amount.")
        free_job_start(job_choice, System.roster[unit_choice-1], money2)
        print(System.roster[unit_choice-1].name + " is ready to go!")
        if System.roster[unit_choice-1].commander == True:
          return
        else:
          another = input("Do you want to assign any other workers to this task? (1 for yes)\n")
          another = int_checker(another)
          if another != 1:
            return
          else:
            print()
            pass


def free_job_start(index, unit, starting_money=0):
  job = System.free_jobs_in_progress[index]
  unit.current_job = job
  System.money -= starting_money
  job.participants[unit] = {"Length": job.length, "Gold": starting_money, "Original money": starting_money, "Results": []}
  # job.print_all_participants()


def training_board():
  print()
  while True:
    all_training_types = ["Strength", "Intelligence", "Agility", "Cunning", "Allure", "Adept Student", "Heavy Lifting", "Awareness", "Manners", "Hawk Eyes", "Quick Hands", "Soldier Training", "Advanced Training", "Glory Seeker", "Passion for Art", "Flair", "History", "Commanding Voice", "Shinobi Training", "Gymnastics", "Fighter", "Wizard", "Thief", "Knight", "Magician", "Archer", "Monk"]

    new_dict = []
    for i in all_training_types:
      for j in System.training_jobs:
        if j.stat == i or j.skill == i:
          new_dict.append(j)

    System.training_jobs = new_dict

    for i in range(len(System.training_jobs)):
      print(str(i+1) + ":")
      System.training_jobs[i].short_description()
    
    while True:

      choice = input("Which one? (0 to go back)\n")
      choice = int_checker(choice)
      if choice == 0:
        return
      elif choice == "":
        pass
      elif choice < 0 or choice > len(System.training_jobs):
        print("\nError\n") 
      else:
        choose_units_training(choice-1)
        sleep(2)
        break


def choose_units_training(job_choice):
    job = System.training_jobs[job_choice]
    print("\n\nThis job requires a minimum of", job.min_workers, "participants.\n")
    units = []
    while True:
      if len(units) < job.max_workers:
        for i in range(len(System.roster)):
          if System.roster[i] not in units and System.roster[i].current_job == None:
            print(str(i + 1) + ":")
            System.roster[i].short_description()

      if len(units) == 0:
        unit_choice = input("Which unit do you want to assign to this job? Press 0 to quit.\n")
        unit_choice = int_checker(unit_choice)
        if unit_choice == 0:
          break
        elif unit_choice == "":
          pass
        elif unit_choice > len(System.roster) or unit_choice == "":
          pass
        elif System.roster[unit_choice - 1].current_job != None:
          pass
        else:
          unit = System.roster[unit_choice - 1]
          print("\nAssign", unit.name, "to this task? (1 for yes, 0 for no)")
          confirm = input("")
          confirm = int_checker(confirm)
          if confirm == 1:
            if unit.commander == True:
              commander_confirm = input("This is your commander unit. If you send them to a job, all of your unemployed mercs will not have a job to do.\nAre you sure? (1 for yes, 0 for no)\n")
              commander_confirm = int_checker(commander_confirm)
              if commander_confirm == 1:
                  units.append(unit)
            else:
                units.append(unit)
      elif 0 < len(units) < job.max_workers:
        unit_choice = input("Are there any other units you want to assign? Press 0 if not.\n")
        unit_choice = int_checker(unit_choice)
        if unit_choice == "":
          pass
        elif unit_choice > len(System.roster):
          pass
        elif unit_choice == 0 or System.roster[unit_choice - 1].current_job != None:
          pass
        elif unit_choice > 0 and System.roster[unit_choice - 1] not in units:
          unit = System.roster[unit_choice - 1]
          print()
          print("Assign", unit.name, "to this task? (1 for yes, 0 for no)")
          confirm = input("")
          confirm = int_checker(confirm)
          if confirm == 1:
            if unit.commander == True:
              commander_confirm = input("This is your commander unit. If you send them to a job, all of your unemployed mercs will not have a job to do.\nAre you sure? (1 for yes, 0 for no)\n")
              commander_confirm = int_checker(commander_confirm)
              if commander_confirm == 1:
                units.append(unit)
            else:
              units.append(unit)
          else:
            print("Error")

      if len(units) >= job.min_workers:
        unit_names = ""
        for i in units:
          unit_names += i.name + ", "

        if len(units) < job.max_workers:
          print("Send:", unit_names[0:-2] + "? (Press 1 to confirm, press 2 to add more, press 0 to return to the job list)")
          confirm = input("")
          confirm = int_checker(confirm)
          if confirm == 1:
            training_job_start(job_choice, units)
            break
          elif confirm == 2:
            pass
          elif confirm == 0:
            break
        else:
          print("Send:", unit_names[0:-2] + "? (Press 1 to confirm, press 0 to return to the job list)")
          confirm = input("")
          confirm = int_checker(confirm)
          if confirm == 1:
            training_job_start(job_choice, units)
            break
          elif confirm == 0:
            break


def training_job_start(index, units):
  job = System.training_jobs[index]
  job.participants = units
  System.training_in_progress.append(job)
  for i in units:
    i.current_job = job
  System.training_jobs.remove(job)
  print("Good to go!\n")


def option_3():
    while True:
        print_all()
        choice = input("\nChoose a unit to inspect (unit #) or 0 to go back\n")
        choice = int_checker(choice)
        if choice == 0:
            break
        elif choice == "":
            print("\nError")
        elif choice > len(System.roster):
            print("\nWho?")
        else:
            System.roster[choice - 1].long_description(System)
            choice = input("Press anything to go back")


def option_5():
  total_count = len(System.jobs_in_progress) + len(System.training_in_progress)
  for i in System.free_jobs_in_progress:
    total_count += len(i.participants)
  if total_count > 0:
    for i in range(len(System.jobs_in_progress)):
        job = System.jobs_in_progress[i]
        print("Job", str(i + 1) + "/" + str(len(System.jobs_in_progress)),
              "\n-------------------------------------------------")
        print(job.type)
        print("Workers:")
        for j in job.participants:
            print(" -", j.name)
        print("Weeks left:", job.length)
        print()
    for j in System.free_jobs_in_progress:
      if len(j.participants) > 0:
        print(j.type, "\n-------------------------------------------------")
        print("Workers:")
        for k in j.participants:
          if j.participants[k]["Length"] == 1:
            print(" -", k.name + ":", j.participants[k]["Length"], "week left.")
          else:
            print(" -", k.name + ":", j.participants[k]["Length"], "weeks left.")
        print()
    for m in range(len(System.training_in_progress)):
      job = System.training_in_progress[m]
      print("Training", str(m + 1) + "/" + str(len(System.training_in_progress)),
            "\n-------------------------------------------------")
      print(job.type)
      print("Workers:")
      for j in job.participants:
        print(" -", j.name)
      print("Weeks left:", job.length)
      print()
    wait()
  else:
    print("No jobs being done...")
    sleep(2)


def option_7(): # important ############################################################
  while True:
    print()
    choices = {}
    current = 1
    for i in System.tips:
      if System.tips[i] == True:
        choices[current] = i
        print(str(current) + ":", i)
        current += 1
    while True:
      choice = input("Which one do you want? (0 to go back)\n")
      choice = int_checker(choice)
      if choice == 0:
        return
      elif choice == "":
        print("\n???\n")
      elif 0 < choice < current:
        tips.read_tip(choices[choice], System.roster[0].name)
        break
      else:
        print("\n?\n")  


def option_8():
  print()
  print_job_history()
  wait()


def mailbox():
  first_switch = True
  if len(System.mailbox) == 0:
    print("No mail...")
    sleep(1)
  while len(System.mailbox) > 0 and first_switch == True:
    for i in range(len(System.mailbox)):
      print(str(i+1) + ":")
      System.mailbox[i].short_description()
      print("-------------------------------------------------")
    read_all_option = False
    if len(System.mailbox) > 1:
      read_all_option = True
      print(str(len(System.mailbox) + 1) + ": Read all mail")
      print()
    second_switch = True
    while second_switch == True:
      choice = input("Choose a letter to read by selecting its corresponding number. Press 0 to go back.\n")
      choice = int_checker(choice)
      print()
      if choice == 0:
        second_switch = False
        first_switch = False
      elif choice == "":
        pass
      elif choice == (len(System.mailbox) + 1) and read_all_option == True:
        for x in range(len(System.mailbox)):
          read_mail(0)
      elif choice > len(System.mailbox) or choice < 0:
        pass
      else:
        read_mail(choice-1)
        second_switch = False
    if len(System.mailbox) == 0:
      print("\nOut of letters to read...")
      wait()


def read_mail(index):
  letter = System.mailbox[index]
  letter.read_letter()
  destroy = True
  if letter.type == "mail":
    if letter.special_event == 1 and System.doctor_open == False:
      System.doctor_open = True
      System.tips["Doctor"] = True
    if letter.special_event == 2: # war letter
      pass
    wait()
  elif letter.type == "job":
    wait()
    normal_check = letter.normal_job in System.locked_job_types
    free_check = letter.free_job in System.locked_free_jobs
    stat_check = letter.training in System.locked_stat_training_types
    skill_check = letter.training in System.locked_skill_training_types
    all_check = normal_check == False and free_check == False and stat_check == False and skill_check == False
    if all_check == True:
      print("This letter is obsolete...")
    elif letter.normal_job != None:
      System.available_job_types.append(letter.normal_job)
      System.locked_job_types.remove(letter.normal_job)
      print      ("********************************************************************************************", "You can now do " + letter.normal_job + " jobs!", "\n********************************************************************************************")
    elif letter.free_job != None:
      print(letter.free_job in System.locked_free_jobs)
      print(System.locked_free_jobs)
      System.available_free_jobs.append(letter.free_job)
      System.locked_free_jobs.remove(letter.free_job)
      System.free_jobs_in_progress.append(job.Free_Job(letter.free_job))
      print("********************************************************************************************", "You can now do " + letter.free_job + "!", "\n********************************************************************************************")
      if System.tips["Free job"] == False:
        System.tips["Free job"] = True
    elif letter.training != None:
      if letter.training in System.locked_stat_training_types:
        System.training_jobs.append(job.Training(letter.training, ""))
        System.locked_stat_training_types.remove(letter.training)
      elif letter.training in System.locked_skill_training_types:
        System.training_jobs.append(job.Training("", letter.training))
        System.locked_skill_training_types.remove(letter.training)
      print("********************************************************************************************", "You can now do " + letter.training + " training!", "\n********************************************************************************************")
      if System.tips["Training"] == False:
        System.tips["Training"] = True
    for i in System.training_jobs:
      print(i.type)
    print("Normal job types:", System.available_job_types)
    print("Locked normal job types:", System.locked_job_types)
    print("Free job types:", System.available_free_jobs)
    print("Locked free job types:", System.locked_free_jobs)
    print("Training types:", System.training_jobs)
    print("Locked training types:", System.locked_stat_training_types, System.locked_skill_training_types)

    wait()
    print()
  elif letter.type == "offer":
    while True:
      choice = input("\nSell " + letter.worker.name + " for $" + str(letter.worker_cost) + "?(1 for yes, 0 for no)\n")
      choice = int_checker(choice)
      if choice == 1:
        print("Worker is in party:", letter.worker in System.roster)
        if letter.worker not in System.roster:
          print("This letter is obsolete...\n")
          destroy = False
          break
        elif letter.worker.current_job != None:
          print("The subject is busy...\n")
          break
        else:
          System.money += letter.worker_cost
          System.roster.remove(letter.worker)
          break
      elif choice == 0:
        break
      else:
        pass
  if destroy == True:
    System.mailbox.remove(letter)


def doctor():
  print("************************************* DOCTOR'S OFFICE *************************************")

  patients1 = sick_list()
  if len(patients1) == 0:
    print("Don't come in here unless you got some patients that I can help. This place is busy, you know.\n")
    wait()
    return
  
  if System.doctor_heals == 0:
    print("This is your first time so I'll treat you for free once. Afterwards, it'll be 500$ per patient...")
    wait()
  elif System.money < 500 and System.doctor_heals > 0:
    print("Sorry to say, but you can't afford the treatment fee. Come back when you can pay.\n")
    wait()
    return

  while True:
    normal_cost = 500
    if System.doctor_heals == 0:
      cost = 0
    else:
      cost = normal_cost

    patients2 = sick_list()

    if len(patients2) == 0:
      print("\nEveryone is ready to go. Come back anytime...")
      wait()
      return

    print("\nPossible patients:")
    for i in range(len(patients2)):
      print(str(i+1) + ":", patients2[i].name)
    if len(patients2) > 1:
      print(str(len(patients2) + 1) + ": Heal everyone")
    # elif choice > len(patients2)
    choice = input("Choose a patient to heal. (0 to go back)\n")
    choice = int_checker(choice)
    if choice == 0:
      return
    elif choice == "":
      pass
    elif choice == len(patients2) + 1:
      total_cost = len(patients2) * normal_cost
      if cost == 0:
        total_cost -= normal_cost
      choice2 = input("\nPay " + str(total_cost) + "$ to heal everyone? (1 for yes, 0 for no)\n")
      choice2 = int_checker(choice2)
      if choice2 == 0:
        pass
      elif choice2 == 1:
        for i in patients2:
          i.condition = "Fine"
          System.doctor_heals += 1
        print("Everyone is all better now!")
    elif choice > len(patients2) + 2 or choice < 0:
      print("\nError")
    else:
      choice2 = input("\nPay " + str(cost) + "$ to heal " + patients2[choice-1].name + "? (1 for yes, 0 for no)")
      choice2 = int_checker(choice2)
      if choice2 == 0:
        pass
      elif choice2 == 1:
        if System.doctor_heals > 0:
          System.money -= cost
        patients2[choice2-1].condition = "Fine"
        patients2[choice2-1].short_description()
        System.doctor_heals += 1
        print(patients2[choice2-1].name + " is all better now!")
  
  return


def sick_list():
  patients = []
  for i in System.roster:
    if i.condition == "Injured":
      patients.append(i)
  return patients


def birthday_checker():
  for current in System.roster:
    # print(current.name, current.birthday)
    if current.birthday == [System.date[0], System.date[1]]:
      end_num = str(current.age)[-1]
      if end_num == "1":
        print("It's", current.name + "'s", str(current.age) + "st" ,"birthday!")
      elif end_num == "2":
        print("It's", current.name + "'s", str(current.age) + "nd" ,"birthday!")
      elif end_num == "3":
        print("It's", current.name + "'s", str(current.age) + "rd" ,"birthday!")
      else:
        print("It's", current.name + "'s", str(current.age) + "th" ,"birthday!")
      current.age += 1
      if current.age > 50:
        count = (current.age // 10) - 4
        while count > 0:
          roll = randint(1, 10)
          print(roll)
          if current.strength == 0 and current.intelligence == 0 and current.agility == 0 and current.cunning == 0 and current.allure == 0:
            count == 1
          elif (roll == 1 or roll == 2) and current.strength > 0:
            current.strength -= 1
            print(current.name, "got a bit weaker...")
          elif roll == 3 and current.intelligence > 0:
            current.intelligence -= 1
            print(current.name, "got a bit duller...")
          elif (roll == 4 or roll == 5 or roll == 6) and current.agility > 0:
            current.agility -= 1
            print(current.name, "got a bit slower...")
          elif roll == 6 and current.cunning > 0:
            current.cunning -= 1
            print(current.name, "got a bit less cunning...")
          elif roll == 7 and current.allure > 0:
            current.allure -= 1
            print(current.name, "got a bit less charming...")
          elif roll == 8 or roll == 9 or roll == 10:
            print("Got lucky this time...")
          else:
            count += 1
          count -= 1


def bankrupcy():
  print("You are", str((System.money) * (-1)) + "$ in debt, " + System.roster[0].name + ". Please sell some units to make back your money.\n")
  while System.money < 0:
    if len(System.roster) == 1:
      print("You have nothing else to give and your company has been disbanded...")
      System.roster[0].commander = False
      return
    for i in range(len(System.roster)):
      if i > 0:
        print(str(i) + ":")
        System.roster[i].short_description()
    choice = input("\nWho will you sell?\n")
    choice = int_checker(choice)
    if choice == "":
      pass
    elif 1 <= choice <= len(System.roster) - 1:
      amount = System.roster[choice].calculate_worth()
      print("You sold " + System.roster[choice].name + " and recieved " + str(amount) + "$.")
      System.money += amount
      System.roster.remove(System.roster[choice])
      if System.money < 0:
        print("You are still " + str((System.money) * (-1)) + " in debt.")
      else:
        print("Thank you.")
    else:
      print()


def print_all():
  print()
  for i in range(len(System.roster)):
    current = System.roster[i]
    print("Unit", i + 1, "/", len(System.roster))
    current.short_description()


def test():  # important ###############################################################
  # labour_test()
  # guard_test()
  # battle_test()
  # tactician_test()
  # theatre_test()
  # infiltration_test()
  # battle_tactician_test()
  # random_test()

  # busking_test()  
  # tests.gambling_test(System)
  # war_test()
  
  # unlock_all_jobs()

  # stat_training_test()

  # while True:
  #   weekly_update()
  #   menu_top()
  #   wait()
  #   date_update()

  menu_top()
  
  for i in range(2):
    weekly_update()
  menu_top()
  # for i in System.roster:
  #   i.long_description()
  # for i in System.training_jobs:
  #   i.short_description()
  mailbox()
  # for i in System.mailbox:
  #   i.read_letter()
  #   print()
  # print_job_history()


def unlock_all_jobs():
  System.available_job_types.append("Guard")
  System.locked_job_types.remove("Guard")
  System.available_job_types.append("Battle")
  System.locked_job_types.remove("Battle")
  System.available_job_types.append("Tactician")
  System.locked_job_types.remove("Tactician")
  System.available_job_types.append("Theatre")
  System.locked_job_types.remove("Theatre")
  System.available_job_types.append("Infiltration")
  System.locked_job_types.remove("Infiltration")
  System.available_job_types.append("Battle Tactician")
  System.locked_job_types.remove("Battle Tactician")
  System.available_free_jobs.append("Busking")
  System.locked_free_jobs.remove("Busking")
  System.available_free_jobs.append("Gambling")
  System.locked_free_jobs.remove("Gambling")
  System.available_free_jobs.append("War")
  System.locked_free_jobs.remove("War")
  System.free_jobs_in_progress.append(job.Free_Job("Busking"))
  System.free_jobs_in_progress.append(job.Free_Job("Gambling"))
  System.free_jobs_in_progress.append(job.Free_Job("War"))

  for i in System.locked_stat_training_types:
    # print(i)
    System.training_jobs.append(job.Training(i))
  for i in System.locked_skill_training_types:
    # print(i)
    System.training_jobs.append(job.Training("", i))


def unlock_all_options():
  System.history_open = True
  System.doctor_open = True


def letter_test():
  for i in System.available_job_types:
    System.mailbox.append(message.create_letter("offer", System.roster[1], i))
  for i in System.available_free_jobs:
    System.mailbox.append(message.create_letter("offer", System.roster[1], i))
  for i in System.training_jobs:
    System.mailbox.append(message.create_letter(i.type, System.roster[1], i))

  tally = 0
  for i in System.mailbox:
    if i.contents == "TODO":
      tally += 1
  print(tally, "letters left...")

  while True:
    menu_top()
    mailbox()


if __name__ == '__main__':
  # playerName = "Daniel"
  # System.roster.append(unit.Unit(playerName, 15, [3, 4], 20, "Fighter", "Commander", ["Adept Student"], True))
  # System.roster.append(unit.Unit())
  # System.roster.append(unit.Unit("", 30))
  # System.roster.append(unit.Unit("", 60))
  # message.playerName = playerName
  # System.mailbox.append(message.Message("Eggman", "mail", "I've come to make announcement", "Shadow the Hedgehog's a bitch-ass motherfucker. He pissed on my fucking wife. That's right. He took his hedgehog fuckin' quilly dick out and he pissed on my FUCKING wife, and he said his dick was THIS BIG, and I said that's disgusting. So I'm making a callout post on my Twitter.com. Shadow the Hedgehog, you got a small dick. It's the size of this walnut except WAY smaller. And guess what? Here's what my dong looks like. That's right, baby. Tall points, no quills, no pillows, look at that, it looks like two balls and a bong. He fucked my wife, so guess what, I'm gonna fuck the earth. That's right, this is what you get! My SUPER LASER PISS! Except I'm not gonna piss on the earth. I'm gonna go higher. I'm pissing on the MOOOON! How do you like that, OBAMA? I PISSED ON THE MOON, YOU IDIOT! You have twenty-three hours before the piss DROPLETS hit the fucking earth, now get out of my fucking sight before I piss on you too!"))
  # System.mailbox.append(message.Message("Mr. McLemon", "Offer", "You got a good lad", "I'll buy " + System.roster[1].name + ".", 0, System.roster[1]))
  # System.mailbox.append(message.Message("Mr. Iyazak", "job", "Hawk Eyes training", "Do u wanna learn some hawk eyes?", 0, None, None, None, "Hawk Eyes"))
  # System.mailbox.append(message.Message("Mr. Grayson", "job", "Strength training", "Get swole.", 0, None, None, None, "Strength"))
  # System.mailbox.append(message.Message("Mr. Stone", "job", "Theatre opportunity", "Let's dance. Put on your red shoes and dance the blues.", 0, None, "Theatre"))
  # System.mailbox.append(message.Message("Mr. Dylan", "job", "Busking is now a thing", "Let's get this bread.", 0, None, None, "Busking"))
 
  # for i in range(3):
  #   new_unit = unit.Unit()
  #   System.roster.append(new_unit)

  # System.weekly_jobs.append(job.Normal_Job("Labour", 1, 1, 3))
  # # for i in range(5):
  # #   System.weekly_jobs.append(job.Normal_Job())
  # # for i in System.weekly_jobs:
  # #   i.short_description()
  
  # while System.roster[0].commander == True:
  #   weekly_update()
  #   if System.roster[0].current_job == None:
  #     activity_board()
  #   date_update()

  # test()


####################################################################################
####################################### GAME #######################################
####################################################################################
  
  playerName = "Daniel"
  # while True:
  #   playerName = input("What's your name?\n(Character limit: 10 or input nothing for default name)\n")
  #   playerName = playerName[0:10]
  #   if playerName == "":
  #     playerName = "Harold"
  #   confirm = int(input("\nAre you OK with " + playerName + "? (1 for yes, anything else for no)\n"))
  #   if confirm == 1:
  #     break
  
  unlock_all_jobs()
  unlock_all_options()

  System.roster.append(unit.Unit(playerName, 5, [3, 4], 20, "Fighter", "Commander", ["Adept Student"], True))
  message.playerName = playerName
  System.weekly_jobs.append(job.Normal_Job(System.max_level, "Labour", 1))

  System.roster.append(unit.Unit("", 5))
  # System.roster.append(unit.Unit("", 15))
  # System.roster.append(unit.Unit("", 25))
  # free_job_start(0, System.roster[1])
  # System.roster.append(unit.Unit("", 5))
  # training_job_start(0, [System.roster[2]])
  
  letter_test()
  
  while System.roster[0].commander == True:
    # System.roster[0].condition = "Injured"
    if System.roster[0].current_job == None:
      activity_board()
      if System.money < 0:
        bankrupcy()
    weekly_update()
  print("GAME OVER")
