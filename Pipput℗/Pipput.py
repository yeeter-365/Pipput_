"""
PIPPUT.py                                                          Copyright 2023. By HANEEF RAHMAN, XI-K

<> Python module for Perfect Input


Python function that operates on Criteria()* and Message** and inputs value of var*** from user,
checks if Criteria(x) is True and breaks if so, otherwise displays an "<> INVAID INPUT" note to user,
Repeats the loop till valid input given. A basic idea of it:

    while True:
      var = input(Message)
      if Criteria(var) == True:
          break
      else:
          print("<> INVALID INPUT")

*Criteria(): Criteria that var has to hold True. <Given by programmer>
**Message: The message that will be displayed before asking for a variable. <Given by programmer>
***var: Variable name that holds the value entered in the while loop. <Given by user>



<> HOW TO USE:

    import [MOD]Pipput as PIN               // Ensure valid directory is entered

    PIN.pinput(Criteria_,Message_); variable = var               // Input Format

    def Criteria_(v):                                         // Function Format
        if v > 10:                                                   // Criteria
            return True                                           // Valid input
        else:
            return False                                        // Invalid input

    Message_ = "Input value var = "                                   // Message



<!> PLEASE OBEY THE FORMAT FOR CORRECT RESULTS                                                 28-SEP-2023
"""

var = None
def pinput(Criteria,Message):
    global var
    while True:
        var = input(Message)
        if Criteria(var) == True:
            break
        else:
            print("<> INVALID INPUT. Try again.")