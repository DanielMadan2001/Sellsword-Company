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
    elif formality == 8:  # friendly business
      self.greeting = "Good morning"
      self.closing = "We hope to see you there!"
    elif formality == 9:  # friendly business
      self.greeting = "To:"
      self.closing = "Please and thank you!"

      
  def short_description(self):
    print('"'+self.heading+'"')
    print("From:", self.sender)


  def read_letter(self):
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(self.heading, "\n")
    print(self.greeting, playerName + ",")
    print("\t" + self.contents, "\n")
    if self.worker_cost > 0 and self.type == "offer":
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
      heading = "Happy to see another busker around here!"
      contents = "I run a small band of buskers, nothing fancy but plenty spirited. One of the members told me about " + unit.name + " and I think they would be a perfect fit for the group."
      formality = 1
    elif job_type == "Gambling":
      sender = "Renard"
      heading = "Let's cut a deal"
      contents = "During a routine visit to the casino I could not help but notice one of your employees named " + unit.name + ". They were playing the games as best they could but they were obviously a cut below a master player such as myself. They reminded me of a diamond in the rough, capable of great potential, but rough nonetheless. I would like to buy " + unit.name + "'s services so I can polish them into a true diamond. With my help, they will grow from a mere novice to a true master of the games!"
      formality = 3
    elif job_type == "War": 
      sender = "General Wilfred"
      heading = "I'd like to recruit " + unit.name
      contents = "I was able to witness " + unit.name + "'s ability in the battlefield firsthand and I was very impressed. I could really use a soldier like them in the army fulltime so I'd like to buy his contract from you."
      formality = 2
  # elif prompt in all_training:
  #   print("Got", prompt)
  #   type = "job"
  #   training = prompt
  elif prompt == "Strength training":
    sender = "Hugo"
    type = "job"
    heading = "My gym is opening soon"
    contents = "I was working with " + unit.name + " on my most recent job and we got to know each other a little. I just so happen to be opening my own gym soon and I want to give you, " + unit.name + " and the rest of your crew an early bird special! Let me know anytime you want me to beef you up."
    formality = 5
    worker = unit
    training = "Strength"
  elif prompt == "Intelligence training":
    sender = "Wyatt"
    type = "job"
    heading = "Sign up for classes today!"
    contents = "I became aquainted with " + unit.name + " recently and they expressed a desire to learn more from a qualified teacher. I just so happen to be a teacher in my spare time so I will begin giving classes to anyone who wants to learn today!"
    formality = 3
    worker = unit
    training = "Intelligence"
  elif prompt == "Agility training":
    sender = "Soma"
    type = "job"
    heading = "Come train at my studio"
    contents = unit.name + " and I hit it off on one of my recent missions and I like his stuff. I promised to train with him sometime and I'm extending the invitation to your whole company. Drop by anytime and increase your agility."
    formality = 1
    worker = unit
    training = "Agility"
  elif prompt == "Cunning training":
    sender = "Flint"
    type = "job"
    heading = "Learn from an expert"
    contents = "Manipulating others into my own little game is one of my greatest talents, and I can help you and your hired mercenaries learn the art of the deal. It won't be cheap, but by the time they're done they will be swindling and sweet talking all day."
    formality = 7
    worker = unit
    training = "Cunning"
  elif prompt == "Allure training":
    sender = "Isa"
    type = "job"
    heading = "Become beautiful with my help!"
    contents = "I am already a veteran of the stage, but I am aware that the true responsibility of the talented is to pass that gift on to new generations. I am willing to teach budding performers how to flourish and increase their appeal to the masses."
    formality = 6
    worker = unit
    training = "Allure"
  else:
    training = str(prompt[0:-9])
    worker = unit
    type = "job"
    if training == "Adept Student":
      sender = "Jon"
      heading = "I'll help you out"
      contents = "You've already got yourself a little crew of helpers, huh? That's good, but soon you gotta expand your options beyond manual labour. They need to be adaptable and I can teach them a little bit of the training we got as soldiers. It'll cost a little, but with my help they will be able to pick up on new skills much easier."
      formality = 1
    elif training == "Heavy Lifting":
      sender = "Marshal"
      heading = "Learn to lift properly"
      contents = "Doing manual labour all day is not as easy as people might think. Proper technique is paramount to avoiding injury and I can help you learn it. With my help, you and your friends will never experience injuries while lifting heavy objects again!"
      formality = 1
    elif training == "Awareness":
      sender = "Sir Teddy"
      heading = "Staying vigilant on the job"
      contents = "When another's life is in your hands, you must remember to keep your eyes out at all times. Never let an assassin escape your vision or fail to thwart a heinous trap. Inexperienced bodyguards will lose their lives for such petty mistakes, which is why I'm offering classes to solve this issue. Come to me if you are interested."
      formality = 2
    elif training == "Manners":
      sender = "Sir Ward"
      heading = "Learning chivalry"
      contents = "When working as a royal guard, it is of the utmost importance that you are able to cater to the client's every need. Even when they are not in danger, they should feel respected and comfortable. If you would like, I could teach you and your company how to make a client feel welcome."
      formality = 2
    elif training == "Hawk Eyes":
      sender = "Mr. Hawk"
      heading = "No place for fair play"
      contents = "Gambling is a sport that only the wiliest of players dare to play. Knowing how to notice misdirection and foul play is paramount and I can teach you to avoid being cheated. Come to me if you want to learn how to even the playing field."
      formality = 4
    elif training == "Quick Hands":
      sender = "Mr. Vulture"
      heading = "Don't let yourself be a chump"
      contents = "I was playing against your friend " + unit.name + " at the parlor and I couldn't help but notice their novice handwork. I could cheat of them all day if I weren't so nice. That won't do in a den of professionals like that and I'm willing to fix this. Send me some of your rooky gamblers and I'll help them play like pros in no time."
      formality = 7
    elif training == "Soldier Training":
      sender = "Captain Eduard"
      heading = "Fight with courage and wisdom"
      contents = "The battlefield is a place for glory and honor, but Death is always watching to find his next victim. Don't enter the fray without sufficient training, and I am willing to provide that to newer soldiers. Come to me and I will instruct you in basic training for new recruits in the Zehevian army."
      formality = 2
    elif training == "Advanced Training":
      sender = "General Wilfred"
      heading = "Fight like a true Zehevian"
      contents = "The war is raging on and we are taking measures to ensure that every soldier who enters the battlefield is equipped with a wealth of experience. I, along with other members of the Royal Army will begin training for any who choose to fight with increased courage. It will be tough, but it is necessary for victory."
      formality = 2
    elif training == "Glory Seeker":
      sender = "Buster"
      heading = "Learn to yearn for the fight!"
      contents = "The people I hate most in the world are people who treat safety as the golden rule of life. You need to listen to your heart and much as your brain. You need to imprint your mark on the world, and if there's anywhere to do it, it's on the battlefield. Come to me if you want to stare death in the face with a smile!"
      formality = 6
    elif training == "Passion for Art":
      sender = "Lana"
      heading = "School of art"
      contents = "The way I see it, your generation isn't taught how to truly express yourselves. Art is NOT a side activity after you do your homework, it IS what we should be learning. Come to my school, and I'll teach you to harness your passion for the arts!"
      formality = 8
    elif training == "Flair":
      sender = "Arthur"
      heading = "Be the star of the stage!"
      contents = "In order to be known, you need to make sure your audience will never forget you. To do that, you must make the spotlight your own. If you want to take your theatrical ability to the next level, I can help instruct you to the top of the world!"
      formality = 3
    elif training == "History":
      sender = "Prof. Aldegund"
      heading = "Historic advantage"
      contents = "Many younger folks are disregarding our proud heritage and think that the old ways of fighting are behind us. They could not be more wrong. The old ways are used so we can push them into the future. If you want to help the future too, enroll in my classes for understanding historical battle tactics."
      formality = 7
    elif training == "Commanding Voice":
      sender = "Meyer"
      heading = "Learn to project your presence"
      contents = "Tactical ability is useless unless you can convey it in a sophisticated and strong manner, which is why projecting your voice while you speak is crucial to public speaking. I am accepting students who have a hard time expressing their ideas and you can join too."
      formality = 1
    elif training == "Shinobi Training":
      sender = "Ace"
      heading = "The path to understanding oneself..."
      contents = "The path to inner peace is ironically quite difficult, at least when you are alone. Asking for help is a sign of strength and when you have achieved complete understanding can you fight like a shinobi. Come to me and I will help you."
      formality = 2
    elif training == "Gymnastics":
      sender = "Jez"
      heading = "Fly above the rest"
      contents = "Among all the different attributes a fighter can have, agility is the most versatile and can be used from theatrics to melee combat. If you really want to keep your head fastened to your neck, come to me and I'll teach you all about dodging swords and arrows."
      formality = 3
    elif training == "Fighter":
      sender = "Zeru"
      heading = "Dealing with Fighters"
      contents = "I am a reknown Wizard in my region and have plenty of combat experience, especially against the stubborn types. As gratitude for your help in this bandit attack, I will help you use your brain to defeat an enemy's brawn. For a fee, of course."
      formality = 6
    elif training == "Wizard":
      sender = "Aria the Wind"
      heading = "I can help you outwit Wizards"
      contents = "As a thief by trade, I happen to know all the secrets to making Wizards lose their hair. As a thank you gift for your aid in my hometown's battle, I'll show you and your crew my moves to better help you fight those dorks."
      formality = 3
    elif training == "Thief":
      sender = "Sir Demir"
      heading = "Stopping tricksters in their tracks"
      contents = "I fight in the Zehevian army and have seen many ruffians and tricksters in my time. Thieves are at their best when fighting an inexperienced opponent, so I want to help you avoid such a scenario. Let me know if you are interested in learning how to fight back against Thieves."
      formality = 5
    elif training == "Knight":
      sender = "Jove"
      heading = "Helping you fight the Knights"
      contents = "I am a magician who uses his magic tricks to fight on the front lines but I can't let my trade secrets get out to just anyone. I have deemed you and your employees to be trustworthy as I fought alongside them, so I will teach you how to fight against Knights using a little spectacle."
      formality = 2
    elif training == "Magician":
      sender = "Fletcher"
      heading = "Seeing through magic tricks"
      contents = "It annoy when I have to deal with flashy showmen on the battlefield, so I learned how to nail them with an arrow everytime I see them. I am willing to pass my technique on to you and your men, for a price of course."
      formality = 4
    elif training == "Archer":
      sender = "Captain Wallace"
      heading = "How to bring a sword to an arrow fight"
      contents = "Fighting on the front lines is never easy, which is why adaptabiity is so important. You and your company have much to learn when it comes to fighting in unpredictable conditions and I can help with that. Specifically, I can teach you how to deal with long range fighters like Archers."
      formality = 5
    elif training == "Monk":
      sender = "Girisha"
      heading = "Martial arts training"
      contents = "I am a monk who has been living in the village that your company helped save from a recent bandit attack. I wish to show my gratitude by teaching the martial arts to you and your workers and in doing so will help them fight against other Monks. Contact me if you are interested."
      formality = 7
    else:
      sender = "Mr. Placeholder"
      heading = prompt
      contents = "Error"
      formality = 0

    # sender = "Mr. Placeholder"
    # type = "job"
    # heading = prompt
    # contents = "TODO"
    # formality = 0
    # worker = unit

    # training = prompt[0:-10]
    # print(training)
    # sender = "Mr. Placeholder"
    # type = "job"
    # # print("Prompt: ", prompt)
    # # print("Name: ", unit.name)
    # heading = "TODO: " + prompt + " Unit: " + unit.name
    # contents = "TODO"
    
    # heading = "TODO: " + prompt + " Unit: " + unit.name + " Type: " + unit.current_job.type

  if contents == "TODO":
    print(training)

  return Message(sender, type, heading, contents, formality, worker, normal_job, free_job, training, commander)


# possibly unlock Advanced Training when War is unlocked
