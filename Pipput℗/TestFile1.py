import Pipput as PIN

print(PIN.__doc__)

def Criteria_(v):
    try:
        int(v); return True
    except:
        return False
    
Message_ = "Input a digit: "    

PIN.pinput(Criteria_,Message_); variable = PIN.var

print(variable)

"""
▱ powershell terminal //




\Pipput℗> python3.11.exe .\TestFile1.py 

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

Input a digit: hello world
<> INVALID INPUT. Try again.
Input a digit: 1
1

"""