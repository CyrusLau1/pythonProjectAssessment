# @author: cyrus
# You will construct a program that presents the quiz to the user, checks the answer and gives
# some kind of feedback. Your program will ask the user for their age, as this productivity tool
# will only be suitable for ages 12-16. Your program will output a suitable advice.

print("Productivity tool! Get better! You are awesome!")

"""What inputs are required from the user? """
# Ask the user for their age and check whether they are suitable for this tool
# The variable age will be an integer data type
age = int(input("Please enter your age. You must be between 12 and 16 to use this tool. Your answer: "))
if 12 > age >= 0:
    print("Sorry, this productivity tool is only suitable for ages 12-16. Come back when you are 12!")
    exit()
elif 16 < age <= 123:
    print("Sorry, this productivity tool is only suitable for ages 12-16.")
    exit()
elif age > 123:
    print("The oldest person in history was 122 years old. Please enter a valid age!")
    exit()
elif age < 0:
    print("Please enter a valid age.")
else:
    print("Please select your routine focus.")

# The variable routines wil be a list of options
routines = ["breakfast", "eat the frog", "reading", "sleep", "tidy up", "time management", "work out"]
print("Your options are: ")
for item in routines:
    print(item)

# The variable routine_focus will be a string data type
routine_focus = str(input("What is your focus? Your answer: ")).strip().lower()

def focus_breakfast():
    # Ask the user how many times they eat breakfast per week and determine whether they are healthy or not.
    weekly_num_bf = int(input("How many times do you eat breakfast every week on average? Your answer: "))
    if weekly_num_bf == 6 or weekly_num_bf == 7:
        print("Great! You are eating healthily.")
        print("Did you know that breakfast is often considered the most important meal "
                "of the day? \nBreakfast provides your body and brain with the necessary fuel and nutrients to start the day "
                "off right, \nso make sure to continue eating breakfast every day to increase your productivity!")
    if 5 >= weekly_num_bf > 0:
        print("That's not too good...")
        print(
            f"As a {age} year old teenager, you should try to eat breakfast every day as it is often considered the most "
            "important meal of the day. \nBreakfast provides your body and brain with the necessary fuel and nutrients to "
            "start the day off right, which increases your productivity. \nIf you really really need to skip breakfast, aim "
            "to make up for the nutritional content you missed at breakfast with your lunch and dinner.")
    if weekly_num_bf == 0:
        print("That's super unhealthy!")
        print(
            f"As a {age} year old teenager, you should try to eat breakfast every day as it is often considered the "
            "most important meal of the day. \nBreakfast provides your body and brain with the necessary fuel and nutrients to "
            "start the day off right. \nMake sure to start eating breakfast tomorrow as skipping breakfast has "
            "many negative effects on your body, which may decrease your productivity.")
    if weekly_num_bf > 7 or weekly_num_bf < 0:
        print("There are 7 days in a week! Enter a number between 0 and 7.")
        focus_breakfast()
    print(
        "Remember: A healthy breakfast may contain some of these: eggs, protein pancakes, oatmeal, cereal & milk, "
        "fruits, \ngreek yoghurt, whole wheat bread, nuts, or anything else that is high in nutrition. \nTry to plan an "
        "exciting breakfast yourself so that you can look forward to it.")
    # Ask whether the user would like to continue using the tool
    next = input("Would you like to choose another focus? Your answer: ").strip().lower()
    if next == "yes":
        print("Please restart the tool to choose another focus.")
    elif next == "no":
        exit()
    else:
        print("Say either yes or no!")
        focus_breakfast()

def focus_eat_frog():
    # Ask whether the user tackles the hardest problems first or easiest ones first and give appropriate advice
    eat_frog = str(input("Do you usually tackle the hardest problems first or the easiest ones first? For example, "
                            "when doing homework or studying. Your answer: ")).strip().lower()
    if eat_frog == "hardest":
        print(
            "That's awesome! \nTackling the hardest problems first can help you maximize your productivity, reduce "
            "stress, improve decision-making, \nand create a sense of momentum and confidence that can help you succeed"
            " in your work. Keep it up!")
    elif eat_frog == "easiest":
        print(
            "That's okay, but it's not the most efficient method. \nTackling the hardest problems first can help you "
            "maximize your productivity, reduce stress, improve decision-making, \nand create a sense of momentum and "
            "confidence that can help you succeed in your work. \nYou might want to start 'eating the frog' tomorrow!")
    else:
        print("Say either hardest or easiest!")
        focus_eat_frog()
    print(
        "Remember: Although tackling the hardest problems first may be more efficient, it isn't the same for everyone. \n"
        "If you think tackling the easiest ones first is more productive, then do what you think is best for you.")
    # Ask whether the user would like to continue using the tool
    next = input("Would you like to choose another focus? Your answer: ").strip().lower()
    if next == "yes":
        print("Please restart the tool to choose another focus.")
    elif next == "no":
        exit()
    else:
        print("Say either yes or no!")
        focus_eat_frog()

def focus_reading():
    # Ask whether the user reads, then ask whether they read before sleep and give advice
    read_or_not = str(input("Do you have a habit of reading? Your answer: ")).strip().lower()
    if read_or_not == "yes":
        read_before_sleep = str(input("Do you usually read before sleep? Your answer: ")).strip().lower()
        if read_before_sleep == "yes":
            print("Amazing! Reading before sleep can have a positive impact on your mental health and well-being, "
                    "\nsuch as reducing stress and improving cognitive functions,"
                    "\nand it's a great habit to develop if you're looking to improve your sleep quality.")
        elif read_before_sleep == "no":
            print("It's already great if you have a habit of reading, however, reading before sleep can have a "
                    "\npositive impact on your mental health and well-being, such as reducing stress and improving "
                    "\ncognitive functions, and it's a great habit to develop if you're looking to improve your sleep quality.")
        else:
            print("Say either yes or no!")
            focus_reading()
    elif read_or_not == "no":
        print("That's awful! You should definitely develop a habit of reading, especially before you sleep. "
                "\nReading before sleep can have a positive impact on your mental health and well-being, "
                "\nsuch as reducing stress and improving cognitive functions,"
                "\nand it's a great habit to develop if you're looking to improve your sleep quality.")
    else:
        print("Say either yes or no!")
        focus_reading()
    print(
        "Remember: If you aren't sure what to read or what types of books suit you, make sure to search online for "
        "\ncountless recommendations from fellow readers!")
    # Ask whether the user would like to continue using the tool
    next = input("Would you like to choose another focus? Your answer: ").strip().lower()
    if next == "yes":
        print("Please restart the tool to choose another focus.")
    elif next == "no":
        exit()
    else:
        print("Say either yes or no!")
        focus_reading()

def focus_sleep():
    # Ask how many hours the user sleeps every day and give advice
    hours_slept = int(input("Around how many hours do you sleep each day? Your answer: "))
    if 8 <= hours_slept <= 10:
        print(f"You must be really healthy! "
              f"\nFor a {age} year old teenager, 8-10 hours of sleep is a must in order to enable your growth and development."
              "\nBy getting enough sleep, you can enhance your physical health, mental health, athletic performance, "
              "\nsocial life, and even your academic performance! That's why sleep is important for productivity.")
    if 5 <= hours_slept <= 7:
        print(f"That's not too good... \nFor a {age} year old teenager, 8-10 hours of sleep is a must in order to "
              "enable your growth and development. \nBy getting enough sleep, you can enhance your physical health, "
              "mental health, athletic performance, social life, and even your academic performance! \nThat's why "
              "sleep is crucial if you want to increase your productivity.")
    if 0 <= hours_slept <= 4:
        print(f"That's horrendous! \nFor a {age} year old teenager, 8-10 hours of sleep is a must in order to "
              "enable your growth and development. \nBy getting enough sleep, you can enhance your physical health, "
              "mental health, athletic performance, social life, and even your academic performance. \nMake sure to"
              "sleep more if you want to increase your productivity.")
    if hours_slept > 10:
        print("It's okay to sleep more than 10 hours occasionally, however, if you do this every day, it may increase"
              f"\nyour risk of getting illnesses and make you feel lethargic throughout the day. \nAs a {age} year old "
              "teenager, you should aim for 8-10 hours of sleep in order to maximize productivity.")
    if 0 > hours_slept or hours_slept > 24:
        print("There are 24 hours in a day! Enter a number between 0 and 24.")
    print("Remember:  It's important to find a healthy balance and aim for the optimal amount of sleep for your body."
          "\nToo less sleep as well as too much sleep will harm your body!")
    # Ask whether the user would like to continue using the tool
    next = input("Would you like to choose another focus? Your answer: ").strip().lower()
    if next == "yes":
        print("Please restart the tool to choose another focus.")
    elif next == "no":
        exit()
    else:
        print("Say either yes or no!")
        focus_sleep()

def focus_tidy_up():
    # Ask how often the user tidies up their room and give advice
    tidy_up_freq = int(input("How many times do you tidy up your room in one month on average? \n"
                             "For example, decluttering, dusting, wiping, and vacuuming your bedroom"))
    if 50 > tidy_up_freq >= 3:
        print("Your room must be very clean! \nWhen you vacuum and dust your bedroom regularly, you ensure the air "
              "is clear of allergens and dust particles. \nWhat's more, it also prevents bacteria and viruses from "
              "harboring in your home. \nWith clear and fresh air, your sleep will be better and healthier.")
    elif 0 <= tidy_up_freq < 3:
        print("You should clean your room more often. \nWhen you vacuum and dust your bedroom regularly, you ensure the "
              "air is clear of allergens and dust particles. \nWhat's more, it also prevents bacteria and viruses from "
              "harboring in your home. \nWith clear and fresh air, your sleep will be better and healthier. "
              "\nIt is advised that you clean your room every week to increase your productivity.")
    elif tidy_up_freq >= 50:
        print("How many times do you clean your room every day?! It's good to be clean, but that's too much")
    else:
        print("Please enter a positive number.")
    print("Remember, making your bed every morning can help you sleep better at night, so make sure you do that! Also,")







if routine_focus == routines[0]:
    print(f"Your age is {age}.")
    print(f"Your focus is: breakfast.")
    focus_breakfast()
elif routine_focus == routines[1]:
    print(f"Your age is {age}.")
    print(f"Your focus is: eat the frog.")
    focus_eat_frog()
elif routine_focus == routines[2]:
    print(f"Your age is {age}.")
    print(f"Your focus is: reading.")
    focus_reading()
elif routine_focus == routines[3]:
    print(f"Your age is {age}.")
    print(f"Your focus is: sleep.")
    focus_sleep()





