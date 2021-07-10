import job

def labour_test(System):
  print("LABOUR TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Labour", 1))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance([System.roster[1], System.roster[2], System.roster[3]])
  print("============================================================================================\n")
  going = [System.roster[2], System.roster[3]]
  System.job_start(-1, going)
  return System


def guard_test(System):
  print("GUARD TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Guard", 10))
  # System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance([System.roster[0]])
  print("============================================================================================\n")
  System.job_start(-1, [System.roster[0]])
  # weekly_update()
  # menu_top()
  # System.roster[0].short_description()
  return System


def battle_test(System):
  print("BATTLE TEST:\n")
  System.available_job_types.append("Battle")
  System.locked_job_types.remove("Battle")
  System.weekly_jobs.append(job.Normal_Job("Battle", 30))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance(System.roster)
  print("============================================================================================\n")
  System.job_start(-1, System.roster)
  return System


def tactician_test(System):
  print("TACTICIAN TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Tactician"))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_chance(System.roster[0])
  print("============================================================================================\n")
  System.job_start(-1, [System.roster[0]])
  for i in System.roster:
    i.short_description()
  return System


def theatre_test(System):
  print("THEATRE TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Theatre"))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_chance(System.roster[0])
  print("============================================================================================\n")
  System.job_start(-1, [System.roster[0]])
  for i in System.roster:
    i.short_description()
  return System


def battle_tactician_test(System):
  print("BATTLE TACTICIAN TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Battle Tactician"))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_chance(System.roster[0])
  print("============================================================================================\n")
  System.job_start(-1, [System.roster[0]])
  for i in System.roster:
    i.short_description()
  return System


def infiltration_test(System):
  print("INFILTRATION TEST:\n")
  System.weekly_jobs.append(job.Normal_Job("Infiltration", 10))
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance([System.roster[0]])
  print("============================================================================================\n")
  System.job_start(-1, [System.roster[0]])
  System.roster[0].long_description()
  return System


def random_test(System):
  print("RANDOM TEST:\n")
  System.weekly_jobs.append(job.Normal_Job())
  System.weekly_jobs[-1].short_description()
  System.weekly_jobs[-1].print_group_chance(System.roster)
  print("============================================================================================\n")
  System.job_start(-1, System.roster)
  for i in System.roster:
    i.short_description()
  return System


def busking_test(System):
  print("BUSKING TEST:\n")
  System.available_free_jobs.append("Busking")
  System.locked_free_jobs.remove("Busking")
  System.free_jobs_in_progress.append(job.Free_Job("Busking"))
  System.free_jobs_in_progress[0].print_chance(System.roster[0])
  System.free_job_start(0, System.roster[0])


def gambling_test(System):
  print("GAMBLING TEST:\n")
  System.available_free_jobs.append("Gambling")
  System.locked_free_jobs.remove("Gambling")
  System.free_jobs_in_progress.append(job.Free_Job("Gambling"))
  System.free_jobs_in_progress[-1].print_chance(System.roster[0])
  System.free_jobs_in_progress[-1].print_chance(System.roster[1])
  System.free_job_start(-1, System.roster[0], 500)
  System.free_job_start(-1, System.roster[1], 500)
  return System


def war_test(System):
  print("WAR TEST:\n")
  System.free_jobs_in_progress.append(job.Free_Job("War"))
  System.free_jobs_in_progress[-1].print_chance(System.roster[2])
  System.free_job_start(-1, System.roster[2])
  System.free_jobs_in_progress[-1].print_chance(System.roster[3])
  System.free_job_start(-1, System.roster[3])
  return System


def stat_training_test(System):
  print("STAT TRAINING TEST:\n")
  System.training_jobs.append(job.Training("Strength"))
  System.training_jobs.append(job.Training("", "Adept Student"))
  # System.training_jobs.append(job.Training("Intelligence"))
  # System.training_jobs.append(job.Training("Agility"))
  # System.training_jobs.append(job.Training("Cunning"))
  # for i in System.training_in_progress:
  #   i.short_description()
  System.training_job_start(0, [System.roster[0]])
  # training_System.job_start(1, [System.roster[1]])
  # training_System.job_start(2, [System.roster[2]])
  # training_System.job_start(3, [System.roster[3]])
  System.training_job_start(0, [System.roster[1]])
  return System
