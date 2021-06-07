playerName = ""
from random import randint

class Message:

  def __init__(self, sender, type, heading, contents, formality=0, worker=None, normal_job=None, free_job=None, training=None):
    self.sender = sender
    self.type = type.lower()  # mail, job, offer
    self.heading = heading
    self.contents = contents
    self.formality = 0
    self.greeting = ""
    self.closing = ""
    self.determine_formality(formality)
    self.worker = worker
    self.worker_cost = 0
    if self.worker != None:
      self.worker_cost = round(worker.calculate_worth() * 1.15) + randint(0, 150)
    self.normal_job = normal_job
    self.free_job = free_job
    self.training = training


  def determine_formality(self, formality):
    if formality == 0:
      self.greeting = "Dear"
      self.closing = "From:"
    elif formality == 3:
      self.greeting = "Good day to you,"
      self.closing = "Pleasure doing business with you,"
    elif formality == 4:
      self.greeting = "Mr./Ms."
      self.closing = "Don't keep me waiting."
    elif formality == 5:
      self.greeting = "How are you doing,"
      self.closing = "Can't wait to hear back from you!"

      
  def short_description(self):
    print('"'+self.heading+'"')
    print("From:", self.sender)

  def read_letter(self):
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(self.heading, "\n")
    print(self.greeting, playerName + ",")
    print("\t" + self.contents, "\n")
    if self.worker_cost > 0:
      print("\tI am willing to pay $" + str(self.worker_cost), "for " + self.worker.name + ".\n")
    print(self.closing)
    print("\t" + self.sender)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


def create_letter(prompt, unit, job_type):
  sender = ""
  type = ""
  heading = ""
  contents = ""
  formality = 0
  worker = None
  normal_job = None
  free_job = None
  training = None

  if prompt == "offer":
    type = "offer"
    worker = unit
    if job_type == "Labour":
      sender = "Marshal"
      heading = "I'm looking for new workers"
      contents = "I was working with " + unit.name + " and I was impressed with their headstrong attitude. Those types of people are hard to come by these days and I could use someone like that full-time. If you could let me hire " + unit.name + " into my company, it would help a lot!"
      formality = 5
    elif job_type == "Guard":
      sender = "Captain Eduard"
      heading = ""
      contents = ""
      formality = 0
    elif job_type == "Battle":
      sender = "General Wilfred"
      heading = ""
      contents = ""
      formality = 0
    elif job_type == "Tactician":
      sender = "Sir Alvis"
      heading = ""
      contents = ""
      formality = 0 
    elif job_type == "Theatre":
      sender = "Mrs. Nimue"
      heading = ""
      contents = ""
      formality = 0
    elif job_type == "Infiltration":  
      sender = "Ms. Senka"
      heading = ""
      contents = ""
      formality = 0
    elif job_type == "Battle Tactician":
      sender = "Sir Alvis"
      heading = ""
      contents = ""
      formality = 0
    elif job_type == "Busking": 
      sender = "Richard"
      heading = ""
      contents = ""
      formality = 0
    elif job_type == "Gambling":
      sender = "Renard"
      heading = "Let's cut a deal"
      contents = "I would like to buy " + unit.name + "'s services so I can polish them into a true diamond. With my help, they will grow from a mere novice to a true master of the games!"
      formality = 3
    elif job_type == "War": 
      sender = "General Wilfred"
      heading = ""
      contents = ""
      formality = 0
  elif prompt == "Strength":
    sender = "Hugo"
    type = "job"
    heading = "Strength Training TODO"
    contents = "Send your units to me and I can increase their strength."
    formality = 0
    worker = None
    training = prompt
  # elif prompt == "Intelligence":
  #   print(2)
  # elif prompt == "Agility":
  #   print(3)
  # elif prompt == "Cunning":
  #   print(4)
  # elif prompt == "Allure":
  #   print(5)
  else:
    sender = "Mr. Placeholder"
    type = ""
    print("Prompt: ", prompt)
    print("Name: ", unit.name)
    heading = "TODO: " + prompt + " Unit: " + unit.name
    # heading = "TODO: " + prompt + " Unit: " + unit.name + " Type: " + unit.current_job.type

  return Message(sender, type, heading, contents, formality, worker, normal_job, free_job, training)
