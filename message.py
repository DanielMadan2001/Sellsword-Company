playerName = ""
from random import randint

all_training = ["Strength", "Intelligence", "Agility", "Cunning", "Allure", "Adept Student", "Heavy Lifting", "Awareness", "Manners", "Hawk Eyes", "Quick Hands", "Soldier Training", "Advanced Training", "Glory Seeker", "Passion for Art", "Flair", "History", "Commanding Voice", "Shinobi Training", "Gymnastics", "Fighter", "Wizard", "Thief", "Knight", "Magician", "Archer", "Monk"]

class Message:

  def __init__(self, sender, type, heading, contents, formality=0, worker=None, normal_job=None, free_job=None, training=None, commander=False, special_event=0):
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
    self.special_event = special_event


  def determine_formality(self, formality):
    if formality == 0:  # default
      self.greeting = "Dear"
      self.closing = "From:"
    elif formality == 1:  # casual
      self.greeting = "Hey"
      self.closing = "Have a good day!"
    elif formality == 2:  # formal
      self.greeting = "Dear"
      self.closing = "From:"
    elif formality == 3:  # sly
      self.greeting = "Good day to you,"
      self.closing = "Pleasure doing business with you,"
    elif formality == 4:  # shady
      self.greeting = "Mr./Ms."
      self.closing = "Don't keep me waiting."
    elif formality == 5:  # hardy
      self.greeting = "How are you doing,"
      self.closing = "Can't wait to hear back from you!"
    elif formality == 6:  # sultry
      self.greeting = "Dearest"
      self.closing = "Take care!"
    elif formality == 7:  # posh
      self.greeting = "Good day,"
      self.closing = "Sincerely,"

      
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


def create_letter(prompt, unit, job_type, commander=False):
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
      heading = "I wish to enlist one of your men..."
      contents = "I was notified that one of your men has recently completed a service as a bodyguard and showed tremendous skill and bravery. These are qualities that I value in my men and would like to offer " + unit.name + " a place in my battalion. Under my watch, they will grow into a seasoned warrior fitting to represent our great nation."
      formality = 2
    elif job_type == "Battle":
      sender = "General Wilfred"
      heading = "I would like to recruit " + unit.name
      contents = "I heard about the daring exploits of " + unit.name + " and I think they would be an excellent inclusion in the Zahevian army. Should you choose to sell their contract to me, they can spend the rest of his life proudly protecting their country."
      formality = 2
    elif job_type == "Tactician":
      sender = "Sir Alvis"
      heading = "I'm very impressed"
      contents = "I have heard some positive reviews about " + unit.name + ", one of your employees. While they are a fine tactician as they are now, they have much yet to learn. If you would let me employ them, I could mold them into a seasoned strategist befitting of the royal council. The choice is yours."
      formality = 7 
    elif job_type == "Theatre":
      sender = "Mrs. Nimue"
      heading = unit.name + " has potential..."
      contents = "I was attending a show for pleasure and took a liking to your little " + unit.name + ". I am looking for new talent to add to my gallery and I think they would fit perfectly! I would love to make them a full time member of my theatre company."
      formality = 0
    elif job_type == "Infiltration":  
      sender = "Ms. Senka"
      heading = "I have an offer for you."
      contents = "I heard through the grapevine that you have some employees who dabble in espianoge and other shady business. As someone familiar with that type of work, I would be happy to have another partner in crime. " + unit.name + " is exactly the type of person I'm talking about and I'd like to buy his freedom."
      formality = 4
    elif job_type == "Battle Tactician":
      sender = "Sir Alvis"
      heading = "I'm very impressed"
      contents = "I have heard fantastic tales about " + unit.name + "'s leadership skills in combat and would like to recruit him into my personal circle of military strategists."
      formality = 0
    elif job_type == "Busking": 
      sender = "Richard"
      heading = "TODO: Busking"
      contents = "TODO"
      formality = 1
    elif job_type == "Gambling":
      sender = "Renard"
      heading = "Let's cut a deal"
      contents = "I would like to buy " + unit.name + "'s services so I can polish them into a true diamond. With my help, they will grow from a mere novice to a true master of the games!"
      formality = 3
    elif job_type == "War": 
      sender = "General Wilfred"
      heading = "I'd like to recruit " + unit.name
      contents = "TODO"
      formality = 0
  # elif prompt in all_training:
  #   print("Got", prompt)
  #   type = "job"
  #   training = prompt
  elif prompt == "Strength":
    sender = "Hugo"
    type = "job"
    heading = "Strength Training TODO"
    contents = "Send your units to me and I can increase their strength."
    contents = "TODO"
    formality = 0
    worker = None
    training = prompt
  elif prompt == "Intelligence":
    sender = "Wyatt"
    type = "job"
    heading = "Intelligence Training TODO"
    contents = "Send your units to me and I can increase their brain size."
    contents = "TODO"
    formality = 0
    worker = None
    training = prompt
  elif prompt == "Agility":
    sender = "Soma"
    type = "job"
    heading = "Agility Training TODO"
    contents = "Send your units to me and I can increase their speed(?)."
    contents = "TODO"
    formality = 0
    worker = None
    training = prompt
  elif prompt == "Cunning":
    sender = "Flint"
    type = "job"
    heading = "Cunning Training TODO"
    contents = "Send your units to me and I can increase their chances of not going to Heaven."
    contents = "TODO"
    formality = 0
    worker = None
    training = prompt
  elif prompt == "Allure":
    sender = "Isa"
    type = "job"
    heading = "Cunning Training TODO"
    contents = "Send your units to me and I can increase their chances of getting laid."
    contents = "TODO"
    formality = 0
    worker = None
    training = prompt
  else:
    sender = "Mr. Placeholder"
    type = ""
    # print("Prompt: ", prompt)
    # print("Name: ", unit.name)
    heading = "TODO: " + prompt + " Unit: " + unit.name
    contents = "TODO"
    

    # heading = "TODO: " + prompt + " Unit: " + unit.name + " Type: " + unit.current_job.type

  return Message(sender, type, heading, contents, formality, worker, normal_job, free_job, training, commander)
