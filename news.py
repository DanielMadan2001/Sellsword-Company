
def read_weekly_news(date, busking, war):
  # print("Coming soon...")
  print("-- ZAHEVIAN TIMES --")
  content(date)
  if busking > 0:
    # 1-15
    # 16-30
    # 31-45
    # 46-60
    # 61-75
    # 76-90
    print(busking)
  if war > 0:
    # 1-15
    # 16-30
    # 31-45
    # 46-60
    # 61-75
    # 76-90
    print(war)

  wait = input("Press anything to continue.\n")


def content(date):
  if date[0] == 5 and date[2] == 0:
    print("Phase 1")
