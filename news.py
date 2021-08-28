
def read_weekly_news(date, busking, war):
  # print("Coming soon...")
  print("-- ZAHEVIAN TIMES --")
  content(date)
  
  if busking == 0 and war == 0:
    print("Coming soon...")
  if war > 0:
    print(" -- WAR NEWS -- ")
    # 1-15
    if 1 <= war <= 15:
      print("Our brave troops are giving the enemy what for! The Virimals must be quaking in their boots right now!") 
    # 16-30
    elif 16 <= war <= 30:
       print("The noble Zehevian army seems to have the advantage! They are pushing our enemies back as we speak.")  
    # 31-45
    elif 31 <= war <= 45:
       print("Neither side seems to be gaining any ground and the fighting is still warring on. How much longer can this last?")    
    # 46-60
    elif 46 <= war <= 60:
       print("Neither side has an advantage but the battles are still as bloody as ever. Remember to write letters of encouragement to your loved ones, we can use all of the strength we can get...")  
    # 61-75
    elif 46 <= war <= 60:
       print("The Virimals are putting their military might to use and pushing our front lines back by the day. Things are not looking good...") 
    # 76-90
    elif 76 <= war <= 90:
       print("Big trouble! Our forces are taking a serious beating and cannot compete with the onslaught. Remember to pay for our soldiers every day.") 

    print()
    print("War:", war)

  if busking > 0:
    print(" -- BUSKING NEWS -- ")
    # 1-15
    if 1 <= busking <= 15:
      print("The city is very lively and the streets are packed! Street performers are in for a prosperous week.") 
    # 16-30
    elif 16 <= busking <= 30:
      print("The streets appear to be rather busy this week. It's a good time to be hustling out there.")     
    # 31-45
    elif 31 <= busking <= 45:
      print("Average traffic coming it to the city this week, the performers have their work cut out for them.")     
    # 46-60
    elif 46 <= busking <= 60:
      print("Zahevia is less busy than usual so street performers will have to work a little harder for their fill this week.")  
    # 61-75
    elif 46 <= busking <= 60:
      print("Travellers aren't interested in our city at the moment, leading to fiercer competition between local buskers.")  
    # 76-90
    elif 76 <= busking <= 90:
      print("Very few visitors are on the streets this week. Street performers are likely better off waiting for a better time...")    

    print()
    print("Busking:", busking)

  wait = input("Press anything to continue.\n")


def content(date):
  pass
  # # PHASE 1: [5, 1, 0] - [5, 1, 4]
  # if date[0] == 5 and date[2] == 0:
  #   print("Phase 1")
  # # PHASE 2: [5, 1, 0] - [5, 1, 4]
  # elif date[2] == 0 and date[0] >= 6:
  #   print("Phase 2")
  # # PHASE 0: 
  # else:
  #   print("Oblivion")


# Phases:
  # Beginning
  # Busking unlocked
  # Stuff opens up (Gambling, )
  # 
  #
