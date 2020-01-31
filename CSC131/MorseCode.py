####################################
# Eddie Grabert             2/24/18
# CSC 131-005               Lab 5
####################################
# define the differnt alphabets that are needed
english = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ',' ','.')
morse = ('.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..',' ','','')
# define q for when it is needed to end the program
q = 'q'
# set up the program so that it will end where it needs to ((I got this idea from the coin exchange problem on blackboard and
# i used it to stop the the program after the user inputs something to convert, because it kept starting over after the conversion))
terminate = False
# Welcome to the program/ introduction to its purpose.
print('This program will convert between English and Morse code.')
# intial choice between morse to english or english to morse.
choice = input('(E)nglish to Morse code, or (M)orse code to English? ')
#
while not terminate:# used to stop the program eventually
    gameover = False# used to stop the program eventually
    if choice == 'E' or choice == 'e':# check for valid input 
        print('Enter English message, one sentence per line.')# intro to english to morse
        print('End each sentence with a period (hit return when done): ')# intro to english to morse
        E = input('')# prompting the user for input
        E = E.upper()# making it uppercase to match the alphabet
        etotal = ('')# setting up an empty string so that the multiple sentences may be added together as one long string for conversion.
        while E != (''): # loop until empty string(return key) is pressed
            etotal = etotal + (' ') + E # etotal adds the user imput to past input so that it can be read as a string instead of a list, because in a
                                        # list the index conversion would not work.
            E = input('')# prompting the user for another input
            E = E.upper()# making it uppercase to match the alphabet
        for k in etotal:# for loop to read the user input
            index = english.index(k)# associates the different letters used in the string with the index number in the english alphabet
            print(morse[index])# converts the english indexes to morse indexes and prints out
        gameover = True# used to stop the program eventually
    elif choice == 'M' or choice == 'm':# check for valid input
        print('Enter morse-coded letters one per line.')# intro to morse to english
        print('Include one blank line between words, and two blank lines between sentences')# intro to morse to english
        print('(enter \'q\' when done): ')# intro to morse to english
        Mlst = []# sets up an empty list so that user inputs may be added
        M = str(input(''))# prompting the user for input
        while M != 'q':
            Mlst.append(M)# adds the morse letter to the list( since it is inputted letter by letter it can still be read for conversion in list form. 
            M = str(input(''))# prompting the user for another input
        for k in Mlst:# for loop to read the user input
            index = morse.index(k)# associates the different morse letters used in the list with the index number in the morse alphabet
            print(english[index],end='')# converts the morse indexes to english indexes and prints out( I tried many ways to format the print statement
                                         # so that it printed out one sentence per line with a period at the end, but i could not figure out how to make that work.
        gameover = True# used to stop the program eventually
    else:
        choice = input('(E)nglish to Morse code, or (M)orse code to English? ')# if input is invalid, prompts the user for a valid input.
        
    if gameover: # used to stop the program once conversion is complete
        terminate = True # used to stop the program once conversion is complete

        

    
