"""
This program is a Jeopardy-like quiz game.
Users are asked to identify a certain answer given a prompt.
There are two topics in the quiz: Geography and Math.
There is also a final, mystery question.
"""
__author__ = "Ryan Boyle"

import time


# This imports the time library to the program.
# Any functions in this library can now be used in the program.

def calculate_score(current_score, points_to_add):
    """
The function calculate_score() will update the player's score if they
earn points from answering a question.
It will also notify them how many points they have left until they reach
the winning score of 1400.
If they have already reached that point, the function will tell them
that they have enough points to win the game, but should keep playing.
    :param current_score: the player's current score
    :param points_to_add: the amount of points to add to current_score from
    answering a question.
    :return: returns the new current_score after adding points_to_add
    to it.
    """
    # The above line of code defines a function. It is called the
    # function header. The subsequent lines of code in the function
    # will be executed if the function statement is simply called.
    to_win = 1400

    # The function header also includes two parameters.
    # This means that a function call will also require two arguments to work.
    # In this case, the function calculate_score() will require both the
    # current score and the number of points added
    # for a correct answer in the parentheses.
    current_score += int(points_to_add)
    # The above line uses the int() function.
    # This converts a value to an integer.

    # The above line of code also includes a += shortcut operator.
    # This will set the variable before the operator equal to the value
    # after the operator plus the variable.

    # For example, if current_score was 50, then current_score += 100 would be
    # 100+50 = 150.
    # Another way to code this would be current_score = current_score + 100
    print("Your score is:", current_score, "points.")
    # The above line of code uses the print() function.
    # This outputs a certain message to the user's screen.
    points_left = to_win - current_score
    if current_score < to_win:
        # The above line of code includes an if statement.
        # This will execute subsequent lines of code within it
        # if a condition is true.

        # The above line of code also uses a less than operator.
        # The operator returns true if the value before it
        # is less than the value after it.
        print("You need", points_left, "more points to win.\n")
    # The new line character "\n" is used in the above line of code.
    # This creates a new text line in its place.
    elif current_score >= to_win:
        # The above line of code includes an elif statement.
        # If the condition in the if statement is false
        # but the condition here is true,
        # then the subsequent lines of code here will execute.

        # The above line of code also uses a greater than or equal to
        # operator. The operator returns true if the value before it is
        # greater than or equal to the value after it.
        print("You have enough points to win the game!")
        print("Continue playing to see how many points you can get!\n")
    return current_score


# The above line of code includes a return statement.
# This will return the updated score value as the output of the function.


def get_integer(prompt):
    """
The function get_integer() will verify if a user's given input is in the
form of an integer and can be successfully converted from string to int.
The function will do this by using try and except statements.
The input will be collected in the try statement, and if the input is not
in the form of an integer it will cause a ValueError.
The except statement, however, will catch this ValueError and tell the user
that they entered the wrong input without the program crashing.
If another error occurs, the except statement will also catch it.
The try and except statements are within a while loop which tests if the
try statement succeeds or not. It does this by checking to see if
a variable that changes after the input function's line in the
try block has changed or not. If the input function fails, the line after
it will never run.
    :param prompt: the output that should be shown to users
    when they are inputting a value.
    :return: returns the user's initial input if the try statement succeeds.
    """
    input_validation = 'not valid'
    while input_validation != 'valid':
        # The above line of code includes a while loop statement.
        # This allows subsequent lines of code within it to be repeated
        # until a condition is satisfied.

        # The above line of code also includes a not equal to operator. The
        # operator returns true if the values before and after it are not
        # equal.

        # In this case, the code below loops until user_input is an integer.
        # This is because input_validation cannot be defined as 'valid' if
        # the line above it fails to work.
        try:
            user_input = int(input(prompt))
            # The above line of code uses the input() function.
            # This allows data to be entered into the program by the user.
            input_validation = 'valid'
        except ValueError:
            print("You did not enter a whole number. Try again.")
        except:
            print("Error occurred. Try again.")
    return user_input
# The above lines of code create warnings in PyCharm, but I was told
# to ignore them.

# The lines of code above include try and except statements.
# These statements allow some lines of code to be "tried."
# If an error occurs in these lines, it will execute the code in the except
# block and prevent the program from crashing.

# In this case, the code will try to get an integer input from the user.
# If it does not, it will print the lines in the except block and not crash.


def get_alpha(prompt):
    """
The function get_alpha() will verify if a user's given input contains
only letters and spaces.
The function first starts a while loop that stops when a user's input
contains only letters and spaces.
Within the loop, the function will gather the user's input and set it to
all lowercase letters. This makes the quiz questions case-sensitive.
Then, the function will remove all spaces within the user's input so that
it can use the isalpha() method, which checks to see if a string contains
only alphabetical letters. This method is contained in the while loop.
Within the while loop, however, there is also an if statement that will
check if the revised input contains only letters or not. If it does not,
then the function will tell the user to re-enter an input that only has
letters and spaces.
The while loop will end when the revised input contains only letters
with spaces.
    :param prompt: the output that should be shown to users
    when they are inputting a value.
    :return: returns the original user input when the function confirms
    that it only contains letters and spaces
    """
    remove_spaces = '7'
    user_input = ""
    while not (remove_spaces.isalpha()):
        # The above line of code includes an isalpha() method. This method
        # returns true if the string it is checking contains only letters.

        # The above line of code also uses the not Boolean operator.
        # This operator returns true if the statement inside is false.

        # In this case, the code below loops until user_input has only letters.
        user_input = input(prompt).lower()
        # The above line of code includes the lower() method.
        # This converts the string input to all lowercase letters, making the
        # quiz questions not case-sensitive.
        # I thank W3Schools for information on this method.
        remove_spaces = user_input.replace(" ", "")
        # The above line of code includes the replace() method.
        # This replaces certain values with other values.
        # Here, this removes every space from the user input.
        # Therefore, the function will disregard spaces when checking if
        # the input is only comprised of letters.
        # I thank W3Schools for information on this method.
        if not (remove_spaces.isalpha()):
            print("You entered characters other than letters with spaces. Try "
                  "again.")
    # This if statement will notify the user if they entered characters other
    # than letters with spaces.
    return user_input


def extra_requirements():
    """
The function get_alpha() fulfills any other requirements that did not fit 
in the other parts of the function.
These extra requirements are chiefly the -= and *= shortcut operators.
Examples of these requirements being used are shown in this function.
    """
    print("\nExtra Requirements:")
    number = 5
    number -= 3
    # The above line of code includes a -= shortcut operator.
    # This will set the variable before the operator equal to this variable
    # minus the value after the operator.
    print("5 - 3 is", number)
    number2 = number
    number2 *= 2
    # The above line of code includes a *= shortcut operator.
    # This will set the variable before the operator equal to the value
    # after the operator times the variable.
    print(number, "* 2 is", number2)


def main():
    """
The function main() contains the integral parts of the program.
Most importantly, it contains all the Jeopardy questions. There are three
geography questions, four math questions, and the final history question.
The program begins by welcoming the user to the project and describing the
question categories and point system to them. It then has them confirm
that they are ready and asks them the aforementioned questions.
The questions make use of the calculate_score() function to keep track
of the user's score and the get_integer() and get_alpha() functions to
ensure the user is entering answers in the correct forms.
After the final question, the function will determine if their final score
is greater than or equal to the 1400 points needed to win Jeopardy. If
this is determined to be true, then the function will congratulate the user
and give them a monetary prize. This prize is equal to ten times their
score in dollars. If they received less than the score needed to win, then
the function will tell them that they did not win anything.
The function then prints "Thank you for playing Jeopardy!" three times and
calls the extra_requirements() function.
    """
    print("Welcome to my Integration Project: Jeopardy!\n")
    time.sleep(3)
    # The above line of code will delay the execution of further code
    # by a certain amount of seconds.
    print("You will be asked questions in two separate categories:")
    print("Geography and Math. \n")
    time.sleep(3)
    print("There will also be a final, mystery question.\n")
    time.sleep(3)

    print("Earn at least 1400 points to win!\n")

    time.sleep(3)

    continue_input = input('Type "Ready!" to continue: ').lower()

    while continue_input != "ready!":
        # In this case, the code below loops until continue_input is equal to
        # "Ready!"
        continue_input = input(
            'Ok, type "Ready!" when you want to continue: ').lower()

    score = 0

    print("\nFirst Category: Geography \n")

    time.sleep(3)

    print("Question 1 (100 points):")
    time.sleep(1)
    print("Vienna is the capital of this country.")
    print("Enter letter words only.")
    geography_input1 = get_alpha("What is... ")
    if geography_input1 == "austria":

        # The above line also includes an equal to operator. This operator
        # returns true if the values before and after it are equal.
        print("Correct! The correct answer is: Austria.")
        score = calculate_score(score, 100)
    else:
        # The above line of code is an else statement.
        # If the condition in the if statement is false, the subsequent
        # lines of code here will execute.
        print("That answer is incorrect. The correct answer is: Austria.")
        score = calculate_score(score, 0)

    time.sleep(3)

    print("Question 2 (200 points):")
    time.sleep(1)
    print("This nation owns Greenland, the largest island in the world.")
    print("Enter letter words only.")
    geography_input2 = get_alpha("What is... ")
    if geography_input2 == "denmark":
        print("Correct! The correct answer is: Denmark.")
        score = calculate_score(score, 200)
    else:
        print("That answer is incorrect. The correct answer is: Denmark.")
        score = calculate_score(score, 0)

    time.sleep(3)

    print("Question 3 (300 points):")
    time.sleep(1)
    print("In French Polynesia, there is a tiny island ", end='')
    # The above line of code uses an "end=" argument. This prevents a new line
    # from being made after the end of a print statement.
    print("that has become a world renown vacation spot.")
    print("The name of the island consists of a singular word repeated twice.")
    print("Enter one word with letters only.")
    geography_input3 = get_alpha("What is... ")
    island_name = (geography_input3.capitalize() + " ") * 2
    # The above line uses the "+" string operator.
    # This operator concatenates, or connects, multiple strings together.

    # The above line also uses the capitalize() method.
    # This capitalizes the first letter of a user's input.
    # I thank W3Schools for information on this method.

    # The above line also uses the "*" string operator. This repeats a string
    # placed before the operator a certain amount of times.
    # It is used here in order to turn the user's response, which is one word
    # into what would be the island's name. "Bora" would become "Bora Bora"
    # here. A space was concatenated to geography_input3 before multiplying
    # so that the string could be "Bora Bora " instead of "BoraBora".
    if geography_input3 == "bora":
        print("Correct! The correct answer is: Bora, ", end='')
        print("referring to the island of Bora Bora.")
        score = calculate_score(score, 300)
    elif geography_input3 == "bora bora":
        print("You got the right name, but were supposed to enter one word.")
        print("Your answer would now be the name ", island_name, ".", sep='')
        # The above line of code uses a "sep=" argument.
        # This removes the space created when concatenating variables
        # with a comma.
        print("As a result, you will receive half the points.")
        score = calculate_score(score, 150)
    else:
        print("Sorry, that answer is incorrect. The correct answer is: Bora.")
        print("This results in Bora Bora as the island's name.")
        score = calculate_score(score, 0)

    time.sleep(3)

    print("\nWe will now move on to the next category: Math.\n")

    time.sleep(3)

    print("Question 1 (100 points):")
    time.sleep(1)
    print("This number equals 8 when cubed.")
    print("Enter whole numbers only.")
    math_input1 = get_integer("What is... ")
    math_user_solution1 = math_input1 ** 3
    # The above line of code uses the "**" numeric operator,
    # or the power operator. This raises an integer or float
    # to the power of another integer or float.
    # The user's input is being cubed in the above line to see if their input
    # results in a value of 8 or not.
    math_answer1 = 8 ** (1 / 3)
    # In the above line, the cube root of 8 is being taken in order to find
    # the solution to the original question, which is 2.
    if math_input1 == math_answer1:
        print("Correct! The answer is: ", int(math_answer1), ".", sep='')
        score = calculate_score(score, 100)
    else:
        print("Incorrect. The answer is: ", int(math_answer1), ".", sep='')
        print("Your response was: ", math_input1, ".", sep='')
        print("This yields a result of: ", math_user_solution1, ".\n", sep='')
        score = calculate_score(score, 0)

    time.sleep(3)

    print("Question 2 (300 points):")
    time.sleep(1)
    print("In the expression ((x+11)/3)*4, ", end='')
    print("this value of x will result in a solution of 68.")
    print("Enter whole numbers only.")
    math_input2 = get_integer("What is... ")
    math_user_solution2 = ((math_input2 + 11) / 3) * 4
    # The above line is plugging in the user's input into the expression.
    # This will evaluate what solution their input yields. It should be 68.

    # The above line uses the "+" numeric operator, or the addition operator.
    # This adds multiple integers or floats together.

    # This line also uses the "*" numeric operator, or the multiplication
    # operator. This multiplies various integers or floats together.

    # Finally, this line uses the "/" numeric operator, or the division
    # operator. This finds the quotient of certain integers or floats.
    math_answer2 = ((68 / 4) * 3) - 11
    # The above line uses the "-" numeric operator, or the subtraction
    # operator. This finds the difference between certain integers or floats.
    # The expression is being solved backwards here in order to get the value
    # of x. This value is 40.

    if math_input2 == math_answer2:
        print("Correct! The answer is: ", int(math_answer2), ".", sep='')
        score = calculate_score(score, 300)
    else:
        print("Incorrect. The answer is: ", int(math_answer2), ".", sep='')
        print("Your response was: ", math_input2, ".", sep='')
        print("This yields a result of: ", math_user_solution2, ".\n", sep='')
        score = calculate_score(score, 0)

    time.sleep(3)

    print("Question 3 (200 points):")
    time.sleep(1)
    print("After dividing 200 by 7, the remainder is this number.")
    print("Enter whole numbers only.")
    math_input3 = get_integer("What is... ")
    math_answer3 = 200 % 7
    # The above line of code uses the "%" numeric operator, or the modulus
    # operator. This finds the remainder after dividing one integer or float
    # by another.

    if math_input3 == math_answer3:
        print("Correct! The correct answer is: ", math_answer3, ".", sep='')
        score = calculate_score(score, 200)
    else:
        print("Incorrect. The correct answer is: ", math_answer3, ".", sep='')
        print("Your response was: ", math_input3, ".\n", sep='')
        score = calculate_score(score, 0)

    time.sleep(3)
    # The above lines of code create a weak warning in PyCharm, but I was told
    # to ignore it.

    print("BONUS (200 points):")
    time.sleep(1)
    print("Ignoring the remainder, you get this when dividing 200 by 7.")
    print("In other words, use floor division.")
    print("Enter whole numbers only.")
    bonus_input = get_integer("What is... ")
    bonus_answer = 200 // 7
    # The above line uses the "//" numeric operator, or the floor division
    # operator. This finds the quotient of two numbers while disregarding
    # any remainder.

    if bonus_input == bonus_answer:
        print("Correct! The correct answer is: ", bonus_answer, ".", sep='')
        score = calculate_score(score, 200)
    else:
        print("Incorrect. The correct answer is: ", bonus_answer, ".", sep='')
        print("Your response was: ", bonus_input, ".\n", sep='')
        score = calculate_score(score, 0)

    time.sleep(3)
    # The above lines of code create a weak warning in PyCharm, but I was told
    # to ignore it.

    print("It's time for Final Jeopardy! (500 points)")
    time.sleep(2)
    print("The topic for Final Jeopardy will be: History.")
    time.sleep(2)
    print("You will need to enter two answers to get the full 500 points.\n")
    time.sleep(2)
    print("Two Founding Fathers died on July 4th, 1826.")
    print("This date was exactly 50 years after the signing of the ", end='')
    print("Declaration of Independence.")
    print("What were the names of these two Founding Fathers?")
    print("Enter letter words only.")
    final1 = get_alpha("First Founding Father: Who was... ")
    final2 = get_alpha("Second Founding Father: Who was... ")
    ja = "john adams"
    tj = "thomas jefferson"
    if not (final1 == final2):
        # The above code ensures that the following lines of code will not
        # execute if the same answer is entered twice.
        if (final1 == ja or final1 == tj) and (final2 == ja or final2 == tj):
            # The above line of code uses the or Boolean operator. This
            # operator returns true if at least one of the conditions given
            # is true.

            # The above code returns true if both Thomas Jefferson and John
            # Adams are entered in any order.

            # The above line of code also uses the and Boolean operator.
            # This operator returns true if both of the conditions given are
            # true.
            print("Congratulations! Your response is correct!")
            score += 500
        elif (final1 == ja or final1 == tj) or (final2 == ja or final2 == tj):
            # The above line of code returns true if at least one answer is
            # correct. It will not execute if both answers are correct as it
            # is an elif statement. The if statement before it checks for
            # that.
            print("You only got one of the responses correct.")
            print(
                "The correct responses were John Adams and Thomas Jefferson.")
            print("As a result, you will only receive half of the points.")
            score += 250
        else:
            print("Sorry, that answer is incorrect.")
            print(
                "The correct responses were John Adams and Thomas Jefferson.")
            print("As a result, you will not receive any points.")
    else:
        print("You can't enter the same answer twice!")
        print("Now you will not receive any points.\n")
    # Essentially, the user will receive 500 points if they enter both
    # Thomas Jefferson and John Adams in any order.
    # They will receive 250 points if they enter one of the correct names.
    # Finally, they will receive 0 points if they enter no correct answers
    # or enter the same answer twice.
    print("Your final score is:", score, "points.\n")

    time.sleep(3)

    to_win = 1400

    if score >= to_win:
        prize = score * 10
        print("Congratulations, you have over 1400 points ", end='')
        print("and have won Jeopardy!")
        print("You will receive $", prize, ".\n", sep='')

    if score < to_win:
        print("Sorry, you did not reach the winning score of 1400 points!")
        print("You will not receive any money.\n")
        print("Good luck next time!")

    time.sleep(3)

    for x in range(3):
        # The above line of code includes a for loop statement.
        # This allows subsequent lines of code within it to be repeated
        # a specified amount of times.

        # The above line of code also includes an in statement. This permits
        # the for loop to execute if the variable before it is within the
        # list after it

        # Finally, the above line includes the range() function.
        # This specifies within what range the loop should execute in.

        # Simply, this for loop repeats a phrase three times.
        print("Thank you for playing Jeopardy!")

    time.sleep(3)

    extra_requirements()


if __name__ == "__main__":
    main()
# As all the questions are within the main() function, calling to main()
# will let the game run.
