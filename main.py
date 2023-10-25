def beautiful_progress_bar(value, goal, length=30):
  progress = min(value, goal)
  gap = goal - progress
  fill_length = int(length * (progress / goal))
  gap_length = length - fill_length
  bar = "█" * fill_length + " " * gap_length
  return f"Progress: [{bar}] ${gap:.2f} away from your next milestone 🏁"

def get_float_input(prompt):
  while True:
      try:
          return float(input(prompt))
      except ValueError:
          print("Please enter a valid numerical value.")

def calculate_remaining_to_next_milestone(current_net_worth, milestones):
  next_milestone = next((milestone for milestone in milestones if milestone > current_net_worth), None)
  if next_milestone is not None:
      return next_milestone - current_net_worth
  else:
      return 0.0

def print_milestone_map(milestones, current_net_worth):
  print("\n🗺️ Financial Milestone Map 🗺️")
  next_milestone = next((milestone for milestone in milestones if milestone > current_net_worth), None)
  for i, milestone in enumerate(milestones, 1):
      progress_marker = "🚀" if milestone == next_milestone else "  "
      print(f"{progress_marker} Level {i}: ${milestone:.2f}")

def set_and_review_morning_routine():
  make_more_money = input("\nYour morning mission: What is one thing you can do today to INCREASE your income? 🤑 ")
  save_more_money = input("Your morning strategy: What's one thing you can do today to cut costs and SAVE money? 💰 ")

  with open("morning_intentions.txt", "w") as file:
      file.write(f"Morning Mission: {make_more_money}\nMorning Strategy: {save_more_money}")

  print("Morning intentions saved. Start your day with purpose!")

def set_and_review_nightly_routine():
  daily_income = get_float_input("\n💰 Nightly reflection: How much gold did you find today? 🤑 $")
  daily_expenses = get_float_input("💸 Nightly reflection: How much treasure did you spend today? 💎 $")

  with open("morning_intentions.txt", "r") as file:
      intentions = file.read()

  print("Morning Intentions:")
  print(intentions)

  print(f"\n💰 Your Wealth Status: You now have ${daily_income - daily_expenses:.2f} in your treasure chest. 💰")
  print("Nightly reflections completed. Prepare for a restful night!")

def check_daily_goals(daily_income, daily_expenses, make_more_money, save_more_money):
  print("\n🎯 Daily Goals Summary 🎯")
  print(f"Morning Mission: {make_more_money}")
  print(f"Morning Strategy: {save_more_money}")
  print(f"💰 Earned: ${daily_income:.2f} | 💸 Spent: ${daily_expenses:.2f}")

  if daily_income >= float(make_more_money) and daily_expenses <= float(save_more_money):
      print("Congratulations! You met your daily goals. Keep it up!")
  else:
      print("You didn't meet your daily goals. Don't worry, there's always tomorrow!")

def display_milestones(milestones, current_net_worth):
  print_milestone_map(milestones, current_net_worth)

def main():
  Name = input("Hello, I'm MoneyBot, your finance co-pilot. What's your name? ")
  print(f"Welcome to the MoneyVerse, {Name}! 🚀")
  print("Let's get this money! 💰")

  routine_choice = input("\nDo you want to set morning intentions, do nightly reflections, or show goals? (morning/night/goals): ").lower()

  if routine_choice == "morning":
      set_and_review_morning_routine()
  elif routine_choice == "night":
      set_and_review_nightly_routine()
      # Continue with gamified features, personal goals, and milestones here...
      # Define your financial milestones (in dollars)
      milestones = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]  # Added an extra milestone for multi-trillionaire goal

      # Collect daily income and expenses from the user
      daily_income = get_float_input("💰 How much did you earn today? 🤑 $")
      daily_expenses = get_float_input("💸 How much did you spend today? 💎 $")

      make_more_money, save_more_money = 0.0, 0.0  # Initialize for the nightly routine

      # Update current net worth based on daily income and expenses
      current_net_worth = daily_income - daily_expenses

      # Calculate the next upcoming milestone
      next_milestone = next((milestone for milestone in milestones if milestone > current_net_worth), None)

      print_milestone_map(milestones, current_net_worth)  # Moved milestone display here

      remaining_to_next_milestone = calculate_remaining_to_next_milestone(current_net_worth, milestones)

      if next_milestone is not None:
          print("\n🌟 Your Current Progress 🟢")
          print(beautiful_progress_bar(current_net_worth, current_net_worth + remaining_to_next_milestone))
          print(f"🚀 Your next milestone: Level {milestones.index(current_net_worth + remaining_to_next_milestone) + 1} 🚀")
      else:
          print("\n🏆 Congratulations! You've reached your ultimate financial goal. Keep it up! 🏆")
  elif routine_choice == "goals":
      # Display financial milestones at the beginning
      milestones = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]  # Added an extra milestone for multi-trillionaire goal
      display_milestones(milestones, 0)  # Start with a net worth of 0

if __name__ == "__main__":
  main()
