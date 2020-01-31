#####################################
# Eddie Grabert               2/28/18
# CSC 131-005                   Lab 6
#####################################

# Semester GPA Calculation
# Purpose: This program will calculate a student’s semester grade
# by using the students previous credits/GPA and then asking the student
# for their letter grades and the matching credit hours for that grade.
# The program will print out the students semester GPA followed by a
# cumulative GPA

# User Defined Functions
#####################################
# Function Name: getGrades
#
# Purpose: To get all of the semester grades the user would like to use in 
# the calculation. We will handle prompting the user for the letter grade
# and the credit hours, for as many classes as they want. We will do error
# handling to make sure it is a correct letter grade. We are going to store
# the grades and credit hours in a list of sublists.
#
# Parameters or Arguments: none
#
# Return: The value returned is a list of sublists, in which each sublists
# contains the letter grade for a given course and the associated number of
# credits, for example [[‘A’,3], [‘B’,4],[‘A’,3],[‘C’,3]

def getGrades():
    # Create a list to hold each of the (grade,points) pairings 
    semester_info = []
    # Create a Boolean flag to handle how many times we prompt the user 
    more_grades = True
    # Use the empty string variable to determine when the user is done 
    empty_str = ''
    # While the user still wants to enter more_grades
    while more_grades:
        #Prompt for first Grade
        course_grade = input('Enter grade (hit Enter if done): ')
        
        # While Loop to check for valid inputs
        while course_grade not in ('A', 'B', 'C', 'D', 'F', empty_str):
            course_grade = input('Enter the letter grade received: ')
            
        # If the user didn’t enter a grade they must be done 
        if course_grade == empty_str:
            more_grades = False
        else:
            # Since they entered a grade, We need to ask for credits
            num_credits = int(input('Enter number of credits: '))
            semester_info.append([num_credits, course_grade])
            
    # Return list of grades and credits back to main
    return semester_info
#-------------------------------------------------------------------------------
# Function Name: convertGrade
#
# Purpose: To convert a letter grade to its corresponding numerical value.
# This value is used to calculate the quality points that are used to
# calculate the GPA
#
# Parameters or Arguments: a string containing the letter grade, called grade
#
# Return: an integer value containing the corresponding quality points

def convertGrade(grade):
    if grade == 'F':
        return 0
    else:
        # Calculation for quality points
        return 4 - (ord(grade) - ord('A'))
    
# Note: For the function convertGrade we do not have to do any error
# handling because we are going to guarantee that the grade given is
# a valid letter before we call this funciton 
#-------------------------------------------------------------------------------
# Function Name: calculateGPA
#
# Purpose: To get all of the semester grades the user would like to use in
# the calculation. We will handle prompting the user for the letter grade
# and the credit hours, for as many classes as they want. We will do error
# handling to make sure it is a correct letter grade. We are going to store
# the grades and credit hours in a list of sublists.
#
# Parameters or Arguments: the semester grades, and the cumulative gpa info
# we got earlier.
#
# Return: The value returned is a list of sublists, in which each sublists
# contains the letter grade for a given course and the associated number of
# credits

def calculateGPA(sem_grades_info, cumulative_gpa_info):
    # Two variables for the credit hours and quality points
    # used for summing up totals
    sem_quality_pts = 0
    sem_credits = 0
    
    # Create two variables that hold a copy from the tuple we passed in
    # tuple can’t be changed, so we must make a copy that we can update
    current_cumulative_gpa, total_credits = cumulative_gpa_info
    
    # For each of the credit,grade pairings in the list
    for k in range(len(sem_grades_info)):
        num_credits, letter_grade = sem_grades_info[k]
        
        # Totaling up the quality points using the numcredits and
        # our helper function to give us the quality points of that grade 
        sem_quality_pts = sem_quality_pts + num_credits * convertGrade(letter_grade)
        
        # Totaling up the credits for the semester
        sem_credits = sem_credits + num_credits

    # Calculation for the semester gpa
    sem_gpa = sem_quality_pts / sem_credits

    # Calculation for the cumulative gpa
    new_cumulative_gpa = (current_cumulative_gpa * total_credits +\
                          sem_gpa * sem_credits) / (total_credits + sem_credits)
    
    # Return the semester gpa and the new cumulative gpa
    return (sem_gpa, new_cumulative_gpa)
    
#-------------------------------------------------------------------------------


# Main Section
#####################################

def main():
    # Program Greeting
    print('This program calculates semester and cumulative GPAs\n')
    #Check if first semester
    first_semester = str(input('Is this your first semester (y/n)? '))
    terminate = False # Tells when while loop for the yes/no of the first semester question ends
    # The while loop so the invalid inputs will not end the program and the user will be prompted again.
    while not terminate:
        gameover = False # Boolean for terminating the loop
        # The while loop for the yes/no answers and for invalid inputs. 
        while not gameover:
            if first_semester == 'Y' or first_semester == 'y':

                cumulative_gpa_info =(0,0) # Sets it up so that the 2 intial questions are ignored if it is the users first semester. 

                gameover = True # Boolean for terminating the loop
            
            elif first_semester == 'N' or first_semester == 'n':
                # Get current GPA info 
                total_credits = int(input('Enter total number of earned credits: '))
                cumulative_gpa = float(input('Enter your current cumulative GPA: '))
                
                cumulative_gpa_info = (cumulative_gpa, total_credits)
                
                print()# Spacing

                gameover = True # Boolean for terminating the loop

            else:
                # Invalid Input Handling
                print('INVALID INPUT')
                first_semester = str(input('Is this your first semester (y/n)? '))
        # If statement to end the loop and continue the rest of main()
        if gameover:
            terminate = True
        
    semester_grades = getGrades()

    semester_gpa, cumulative_gpa = calculateGPA(semester_grades, cumulative_gpa_info)
    # display semester gpa and new cumulative gpa 
    print('\nYour semester GPA is', format(semester_gpa, '.2f'))
    print('Your new cumulative GPA is', format(cumulative_gpa, '.2f'))
    
main()





