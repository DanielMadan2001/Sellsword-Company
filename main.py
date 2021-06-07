import unit
import hiring
import job
import message
from random import randint
from time import sleep


class System:
  date = [5, 1, 0]  # month, week, year
  money = 1000
  max_level = 30
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

  locked_skill_training_types = ["Adept Student", "Heavy Lifting", "Awareness", "Manners", "Hawk Eyes", "Quick Hands", "Soldier Training", "Advanced Training", "Glory Seeker", "Passion for Art", "Flair", "History", "Commanding Voice", "Shinobi Training", "Gymnastics", "Fighter", "Wizard", "Thief", "Knight", "Magician", "Archer", "Monk"]

  mailbox = []


def menu_top():
    print("\n========================")
    print("Date: M" + str(System.date[0]) + ", W" + str(System.date[1]) + ", Y" + str(System.date[2]))
    print("Funds:", str(System.money) + "$")
    print("Available units:", availability_checker(), "/", len(System.roster))
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
    for i in range(len(System.roster)):
        if System.roster[i].level > System.max_level:
            System.max_level = System.roster[i].level
            

def weekly_update():  # important ######################################################
    # # weekly job checker
    # for i in System.jobs_in_progress:
    #     i.length -= 1
    #     success_chance = i.calculate_group_chance(i.participants)
    #     # chance for injury
    #     for j in i.participants:
    #         random_roll = randint(0, 100)
    #         # print(random_roll, success_chance[2])
    #         if random_roll < success_chance[2]:
    #             print(j.name, "injured themselves and was discharged from the job.")
    #             j.condition = "Injured"
    #             j.current_job = None
    #             i.participants.remove(j)
    #     # end job
    #     if len(i.participants) == 0:
    #         print("All of the workers at the", i.type, "job failed.")
    #         System.jobs_in_progress.remove(i)
    #     elif i.length == 0 and len(i.participants) > 0:
    #         job_rewards(i)
    #         System.jobs_in_progress.remove(i)
    # add weekly jobs
    # System.weekly_jobs = [job.Normal_Job("Labour", 1, 1, 3)]
    # # for i in range(len(System.roster) // 2):
    # #     job_type = System.available_job_types[randint(0, len(System.available_job_types) - 1)]
    # #     System.weekly_jobs.append(job.Normal_Job(job_type, randint(1, System.max_level)))
    # # birthday checker
    # birthday_checker()
     
  # while System.jobs_in_progress[0].length > 0:
  print("======================================= WEEKLY UPDATE ======================================")
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

      i.difficulty = randint(0, 90)
      i.relevant_stats_update()
      print("--------------------------------------------------------------------------------------------")
  
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


def print_job_history():
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
      string += ", Count: " + str(System.job_history[i]["Count"])

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


def job_rewards(job):
    chance = 100 - randint(0, 100)

    success_chances = job.calculate_group_chance(job.participants)

    pass_chance = chance <= success_chances[0]
    pass_plus_chance = chance < success_chances[1]
    excel_chance = chance * 3 < success_chances[1]

    print()

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


def activity_board():
    while System.roster[0].current_job == None:
        menu_top()
        choice = int(input(
            "What do you want to do?\n 1: Job board\n 2: Hire\n 3: Roster\n 4: News\n 5: Current jobs being done\n 6: Wait\n"))
        if choice == 1:  # Jobs
            option_1()
        elif choice == 2:  # Hire
            new = hiring.hiring_board()
            if new != None:
                System.roster.append(new)
                System.money -= new.calculate_worth()
        elif choice == 3:  # Roster
            option_3()
        elif choice == 4:  # News
            print("No news today. Come back next week.")
            sleep(1)
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
            for i in range(len(System.roster)):
                if System.roster[i] not in units and System.roster[i].level >= job.recommended_level and System.roster[i].current_job == None:
                    print(str(i + 1) + ":")
                    System.roster[i].short_description()

        if len(units) == 0:
            unit_choice = int(input("Which unit do you want to assign to this job? Press 0 to quit.\n"))
            if unit_choice == 0:
                break
            elif System.roster[unit_choice - 1].current_job != None:
                pass
            else:
                unit = System.roster[unit_choice - 1]
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
            if unit_choice == 0 or System.roster[unit_choice - 1].current_job != None:
                pass
            elif unit_choice > 0 and System.roster[unit_choice - 1] not in units:
                unit = System.roster[unit_choice - 1]
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
    i.attitude += i.work[job.type]
  System.weekly_jobs.remove(job)
  print("Good to go!")


def free_job_start(index, unit, starting_money=0):
  job = System.free_jobs_in_progress[index]
  unit.current_job = job
  System.money -= starting_money
  job.participants[unit] = {"Length": job.length, "Gold": starting_money, "Original money": starting_money, "Results": []}
  # job.print_all_participants()


def training_job_start(index, units):
  job = System.training_jobs[index]
  job.participants = units
  System.training_in_progress.append(job)
  for i in units:
    i.current_job = job
  System.training_jobs.remove(job)
  print("Good to go!")


def option_3():
    while True:
        print_all()
        choice = int(input("\nChoose a unit to inspect (unit #) or 0 to go back\n"))
        if choice == 0:
            break
        else:
            System.roster[choice - 1].long_description()
            choice = input("Press anything to go back")


def option_5():
  if len(System.jobs_in_progress) > 0:
    for i in range(len(System.jobs_in_progress)):
        job = System.jobs_in_progress[i]
        print(str(i + 1) + "/" + str(len(System.jobs_in_progress)),
              "\n-------------------------------------------------")
        print(job.type)
        print("Workers:")
        for j in job.participants:
            print(" -", j.name)
        print("Weeks left:", job.length)
  else:
    print("No jobs being done...")
  sleep(1)


def mailbox():
  first_switch = True
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
      choice = int(input("Choose a letter to read by selecting its corresponding number. Press 0 to go back.\n"))
      print()
      if choice == 0:
        second_switch = False
        first_switch = False
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
      wait = input("\nPress anything to continue.\n")


def read_mail(index): # important #######################################################
  letter = System.mailbox[index]
  letter.read_letter()
  if letter.type == "mail":
    wait = input("\nPress anything to continue.\n")
  elif letter.type == "job":
    wait = input("\nPress anything to continue.\n")
    if letter.normal_job != None:
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
    elif letter.training != None:
      if letter.training in System.locked_stat_training_types:
        System.training_jobs.append(job.Training(letter.training, ""))
        System.locked_stat_training_types.remove(letter.training)
      elif letter.training in System.locked_skill_training_types:
        System.training_jobs.append(job.Training("", letter.training))
        System.locked_skill_training_types.remove(letter.training)
      print("********************************************************************************************", "You can now do " + letter.training + " training!", "\n********************************************************************************************")
    for i in System.training_jobs:
      print(i.type)
    print("Normal job types:", System.available_job_types)
    print("Locked normal job types:", System.locked_job_types)
    print("Free job types:", System.available_free_jobs)
    print("Locked free job types:", System.locked_free_jobs)
    print("Training types:", System.training_jobs)
    print("Locked training types:", System.locked_stat_training_types, System.locked_skill_training_types)

    wait = input("\nPress anything to continue.\n")
    print()
  elif letter.type == "offer":
    while True:
      choice = int(input("\nSell " + letter.worker.name + " for $" + str(letter.worker_cost) + "?(1 for yes, 0 for no)\n"))
      if choice == 1:
        System.money += letter.worker_cost
        System.roster.remove(letter.worker)
        break
      elif choice == 0:
        break
      else:
        pass
  System.mailbox.remove(letter)


def birthday_checker():
  for current in System.roster:
    if current.birthday == [System.date[0], System.date[1]]:
        print("It's", current.name + "'s birthday!")
        current.age += 1


def print_all():
  print()
  for i in range(len(System.roster)):
    current = System.roster[i]
    print("Unit", i + 1, "/", len(System.roster))
    current.short_description()


def test():  # important #################################################################
  # labour_test()
  # guard_test()
  battle_test()
  # tactician_test()
  # theatre_test()
  # infiltration_test()
  # battle_tactician_test()
  # random_test()
  
  # busking_test()  
  # gambling_test()
  # war_test()

  # System.available_job_types.append("Guard")
  # System.locked_job_types.remove("Guard")
  # System.available_job_types.append("Battle")
  # System.locked_job_types.remove("Battle")
  # System.available_job_types.append("Tactician")
  # System.locked_job_types.remove("Tactician")
  # System.available_job_types.append("Theatre")
  # System.locked_job_types.remove("Theatre")
  # System.available_job_types.append("Infiltration")
  # System.locked_job_types.remove("Infiltration")
  # System.available_job_types.append("Battle Tactician")
  # System.locked_job_types.remove("Battle Tactician")
  # System.available_free_jobs.append("Busking")
  # System.locked_free_jobs.remove("Busking")
  # System.available_free_jobs.append("War")
  # System.locked_free_jobs.remove("War")

  # stat_training_test()

  for i in range(6):
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
  print_job_history()


def labour_test():
  print("LABOUR TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Labour", 1))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance([System.roster[1], System.roster[2], System.roster[3]])
  print("============================================================================================\n")
  going = [System.roster[2], System.roster[3]]
  job_start(-1, going)


def guard_test():
  print("GUARD TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Guard", 10))
  # System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance([System.roster[0]])
  print("============================================================================================\n")
  job_start(-1, [System.roster[0]])
  # weekly_update()
  # menu_top()
  # System.roster[0].short_description()


def battle_test():
  print("BATTLE TEST:\n")
  # System.available_job_types.append("Battle")
  # System.locked_job_types.remove("Battle")
  System.weekly_jobs.append(job.Normal_Job("Battle", 30))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance(System.roster)
  print("============================================================================================\n")
  job_start(-1, System.roster)


def tactician_test():
  print("TACTICIAN TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Tactician"))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_chance(System.roster[0])
  print("============================================================================================\n")
  job_start(-1, [System.roster[0]])
  weekly_update()
  menu_top()
  for i in System.roster:
    i.short_description()


def theatre_test():
  print("THEATRE TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Theatre"))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_chance(System.roster[0])
  print("============================================================================================\n")
  job_start(-1, [System.roster[0]])
  weekly_update()
  menu_top()
  for i in System.roster:
    i.short_description()


def battle_tactician_test():
  print("BATTLE TACTICIAN TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Battle Tactician"))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_chance(System.roster[0])
  print("============================================================================================\n")
  job_start(-1, [System.roster[0]])
  weekly_update()
  menu_top()
  for i in System.roster:
    i.short_description()


def infiltration_test():
  print("INFILTRATION TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Infiltration", 10))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance([System.roster[0]])
  print("============================================================================================\n")
  job_start(-1, [System.roster[0]])
  weekly_update()
  menu_top()
  System.roster[0].long_description()


def random_test():
  print("RANDOM TEST:\n")
  System.weekly_jobs.append(job.Normal_Job())
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance(System.roster)
  print("============================================================================================\n")
  job_start(-1, System.roster)
  weekly_update()
  menu_top()
  for i in System.roster:
    i.short_description()


def busking_test():
  print("BUSKING TEST:\n")
  System.available_free_jobs.append("Busking")
  System.locked_free_jobs.remove("Busking")
  System.free_jobs_in_progress.append(job.Free_Job("Busking"))
  System.free_jobs_in_progress[0].print_chance(System.roster[0])
  free_job_start(0, System.roster[0])


def gambling_test():
  print("GAMBLING TEST:\n")
  System.available_free_jobs.append("Gambling")
  System.locked_free_jobs.remove("Gambling")
  System.free_jobs_in_progress.append(job.Free_Job("Gambling"))
  System.free_jobs_in_progress[-1].print_chance(System.roster[0])
  System.free_jobs_in_progress[-1].print_chance(System.roster[1])
  free_job_start(-1, System.roster[0], 500)
  free_job_start(-1, System.roster[1], 500)


def war_test():
  print("WAR TEST:\n")
  System.free_jobs_in_progress.append(job.Free_Job("War"))
  System.free_jobs_in_progress[-1].print_chance(System.roster[2])
  free_job_start(-1, System.roster[2])
  System.free_jobs_in_progress[-1].print_chance(System.roster[3])
  free_job_start(-1, System.roster[3])


def stat_training_test():
  print("STAT TRAINING TEST:\n")
  System.training_jobs.append(job.Training("Strength"))
  System.training_jobs.append(job.Training("", "Adept Student"))
  # System.training_jobs.append(job.Training("Intelligence"))
  # System.training_jobs.append(job.Training("Agility"))
  # System.training_jobs.append(job.Training("Cunning"))
  # for i in System.training_in_progress:
  #   i.short_description()
  training_job_start(0, [System.roster[0]])
  # training_job_start(1, [System.roster[1]])
  # training_job_start(2, [System.roster[2]])
  # training_job_start(3, [System.roster[3]])
  training_job_start(0, [System.roster[1]])


if __name__ == '__main__':
  playerName = "Daniel"
  System.roster.append(unit.Unit(playerName, 15, [3, 4], 20, "Fighter", "Commander", ["Adept Student"], True))
  System.roster.append(unit.Unit())
  System.roster.append(unit.Unit("", 30))
  System.roster.append(unit.Unit("", 60))
  message.playerName = playerName
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
  test()


  # To do list:

    # Job finish will check System.job_history and maybe give them them a training type
    # Make attitude effect stuff
    # Make personalized victory messages
    # Make better descriptions
    # When in hardcore war phase, increase minimum difficulty for war
    # Balance economy
