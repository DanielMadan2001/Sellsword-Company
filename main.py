import unit
import hiring
import job
from random import randint
from time import sleep


class System:
  date = [5, 1, 0]  # month, week, year
  money = 1000
  max_level = 5
  roster = []
  weekly_jobs = []
  jobs_in_progress = []
  # available_job_types = ["Labour"]
  available_job_types = ["Labour", "Guard", "Battle", "Tactician", "Theatre", "Infiltration", "Battle Tactician"]
  locked_job_types = ["Guard", "Battle", "Tactician", "Theatre", "Infiltration", "Battle Tactician"]
  available_free_jobs = [""]
  locked_free_jobs = ["Busking", "Gambling", "War"]



def menu_top():
    print("\n========================")
    print("Date: M" + str(System.date[0]) + ", W" + str(System.date[1]) + ", Y" + str(System.date[2]))
    print("Funds:", str(System.money) + "$")
    print("Available units:", availability_checker(), "/", len(System.roster))
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
    System.weekly_jobs = [job.Normal_Job("Labour", 1, 1, 3)]
    # for i in range(len(System.roster) // 2):
    #     job_type = System.available_job_types[randint(0, len(System.available_job_types) - 1)]
    #     System.weekly_jobs.append(job.Normal_Job(job_type, randint(1, System.max_level)))
    # birthday checker
    birthday_checker()


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
    System.weekly_jobs.remove(job)
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


if __name__ == '__main__':
  playerName = "Daniel"
  System.roster.append(unit.Unit(playerName, 5, [3, 4], 20, "Fighter", "Commander", ["Adept Student"], True))
  
  for i in range(3):
    new_unit = unit.Unit()
    System.roster.append(new_unit)

  System.weekly_jobs.append(job.Normal_Job("Labour", 1, 1, 3))
  # for i in range(5):
  #   System.weekly_jobs.append(job.Normal_Job())
  # for i in System.weekly_jobs:
  #   i.short_description()

  # add jobs

  while System.roster[0].commander == True:
    weekly_update()
    if System.roster[0].current_job == None:
      activity_board()
    date_update()

