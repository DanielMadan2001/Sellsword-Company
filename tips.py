
def read_tip(prompt, playerName):
  if prompt == "The Basics":
    basics_prompt()
  if prompt == "Job start":
    job_start_prompt()
  elif prompt == "Classes":
    classes_prompt()
  elif prompt == "Doctor":
    doctor_prompt()
  elif prompt == "Stats":
    stats_prompt()
  elif prompt == "Skills":
    skills_prompt()
  elif prompt == "Free job":
    free_job_prompt()
  elif prompt == "Training":
    training_prompt()
  print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
  wait = input("\nPress anything to continue.\n")


def basics_prompt():
  print("\n* * * * * * * * * * * * * * * * * * * * * THE BASICS  * * * * * * * * * * * * * * * * * * * *\n")
  print(" Welcome to Sellsword Company! This is a strategy game where you run a mercenary agency and earn money through missions, all while unlocking the potential in your employees.\n")
  print(" Every week you have several options of what to do.\n")
  print(" \tJob board: Look at all of the jobs you could do during the week to earn money.\n")
  print(" \tHire: Add a new employee to your ranks.\n")
  print(" \tRoster: See your employeesâ€™ profiles and statistics.\n")
  print(" \tNews: Read the news for the scoop about what is going on in the world.\n")
  print(" \tCurrent jobs being done: Check what jobs are being done and which employees are working in them.\n")
  print(" \tMailbox: Read any mail you have received during the previous weeks.\n")
  print(" At the end of every month, you are required to pay the combined monthly wages of all your employees. The total will be displayed on the third and fourth weeks of every month.\n")
  print(" The game will end if any of the following conditions are met:\n")
  print(" \t1. The commander unit (you) dies during a job.\n")
  print(" \t2. You enter a state of bankruptcy and are incapable of paying the outstanding debt.\n")
  print("More tips will be available for your review.")


def job_start_prompt():
  print("\n* * * * * * * * * * * * * * * * * * * * * JOB START * * * * * * * * * * * * * * * * * * * * *\n")
  print(" By going to the Job board, you can choose a job that units from your roster can partake in.\n")
  print(" There is a minimum number of participants that must be chosen before accepting. There is also a maximum number of participants allowed to join the job at any given time, so think about how you want to spread your units among several jobs.\n")
  print(" Before a unit is added to the participants list, it will display their odds of success, as well as their natural affinity towards that type of work. Having multiple units can increase the odds of success, which is displayed before the ultimate choice to deploy them.\n")
  print(" Once the participants have started the job, you will recieve weekly updates as to their conditionn in the Weekly Update. Once their job is done, you will see the result there too.\n")
  print(" If your party succeeds, they will recieve the promised gold and return with their earnings. They are also able to score bonus perks, such as level-ups, stat-ups and other job opportunities.")


def classes_prompt():
  print("\n* * * * * * * * * * * * * * * * * * * * * * CLASS * * * * * * * * * * * * * * * * * * * * * *\n")
  print(" Every unit has an assigned class, which influences their stats and what types of work they are inclined to enjoy.\n")
  print(" In combat scenarios, a unit's class can impact their performance and certain classes are profficient against others.")
  
  print("\n FIGHTERS:")
  print(" Defining traits: Strength, Allure")
  print(" They prefer physically oriented combat jobs where they can put their power to use.")
  print(" Strong against: Thieves")
  print(" Weak against: Wizards")

  print("\n WIZARDS:")
  print(" Defining traits: Intelligence, Cunning")
  print(" They excel at problem solving and guiding others with their strategies.")
  print(" Strong against: Fighters")
  print(" Weak against: Thieves")

  print("\n THIEVES:")
  print(" Defining traits: Agility, Allure")
  print(" Their ability to sneak around and fool an enemy is second to none.")
  print(" Strong against: Wizards")
  print(" Weak against: Fighters")

  print("\n KNIGHTS:")
  print(" Defining traits: Strength, Intelligence")
  print(" They are trained to act as a shield for their lords and protect them by any means.")
  print(" Strong against: Thieves, Archers")
  print(" Weak against: Magicians")

  print("\n MAGICIANS:")
  print(" Defining traits: Cunning, Intelligence, Allure")
  print(" They are energetic spirits who live for the thrill of the spotlight.")
  print(" Strong against: Fighters, Knights")
  print(" Weak against: Archers")

  print("\n ARCHERS:")
  print(" Defining traits: Strength, Agility, Cunning")
  print(" They are talented shooters whose expertise extends to other contests of skill.")
  print(" Strong against: Wizard, Magicians")
  print(" Weak against: Knights")

  print("\n MONKS:")
  print(" Defining traits: Strength, Intelligence, Allure")
  print(" They are disciplined warriors who live to improve through hard work.")
  print(" Strong against: None")
  print(" Weak against: None")
  
  print("\n If you imagine class fights as rock-paper-scissors, imagine that:\n")
  print("\tFighters are rock,")
  print("\tWizards are paper,")
  print("\tThieves are scissor.")
  print("\tKnights, Magicians and Archers don't have as drastic matchups.")
  print("\tKnights are rock and paper,")
  print("\tMagicians are paper and scissors,")
  print("\tArchers are rock and scissors,")


def doctor_prompt():
  print("\n* * * * * * * * * * * * * * * * * * * * * *  DOCTOR * * * * * * * * * * * * * * * * * * * * * ")
  print("When you have a unit who has been injured, take them to the doctor and have him fix them, for a fee of course.")


def stats_prompt():
  print("\n* * * * * * * * * * * * * * * * * * * * * * STATS * * * * * * * * * * * * * * * * * * * * * \n")
  print(" A unit's stats will signify how strong they are in a particular category. Determining factors include:\n")
  print("\tClass: Each class has certain areas in which they excel, so a unit is likely to reflect that.")
  print("\tPersonality: People are more than their jobs, so each person has certain gifts that set them apart.")
  print(" Each job has a description that outlines what attributes are recommended in a worker, so use the stats to find your best candidate.\n")
  print(" A unit's level doesn't often enter the equation when it comes to a unit's performance capabilities. It is a metric used to measure what jobs the unit can accept and tends to imply stats.")
  print(" Age does not really come into effect until the unit is considered 'old' at age 50. From there, the unit is liable to start losing points off of their stats, with the process only getting worse the older they get. Talk about the worst birthday present ever...")


def skills_prompt():
  print("\n* * * * * * * * * * * * * * * * * * * * * * SKILLS * * * * * * * * * * * * * * * * * * * * * \n")
  print(" Each unit can learn skills to increase their odds of success while performing jobs, increase chances of earning extra rewards or minimizing chances of failure, injury or death. Each job describes what skills can be used to augment the chances of success.")
  print("\n Class-based skills ('Fighter', 'Wizard', 'Thief', etc.) can be used to bolster a unit's odds of success against enemies of the specified class. Check the 'Classes' option to learn more.")


def free_job_prompt():
  print("\n* * * * * * * * * * * * * * * * * * * * * FREE JOB * * * * * * * * * * * * * * * * * * * * *\n")
  print(" Jobs classified as 'free jobs' work different than other jobs and training. It can be attempted by an unlimited number of workers and they all work independantly from each other. Once they have completed all of their weeks, they will return while anyone who hasn't will keep working.")
  print("\n These types of jobs typically carry little risk and can grant great rewards, but only extremely skilled (or lucky) workers will be able to make the most out of their time. Keeping up to date with the news will inform you what the expected forecast of work during the week will be.")


def training_prompt():
  print("\n* * * * * * * * * * * * * * * * * * * * * TRAINING * * * * * * * * * * * * * * * * * * * * * \n")
  print(" Send 1-4 of your units to boost their abilities at a training job. These jobs require an upfront fee to participate in and will typically last 4 weeks. The training will either improve a unit's stats or teach them a new skill. Be warned, sometimes your units will fail to learn anything...")
