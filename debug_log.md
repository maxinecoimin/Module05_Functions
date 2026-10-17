# debug_log.md
# Author: Maxine Coimin

## Bug 1
Error type: Key Error: 'amount'
File + line: "/home/maxine/ism3232/module05_functions/week8_buggy.py" + line 21 & line 12
What the error means: a typo was made
What I told the duck: when working through the lines of code we want to verify that all of the words used are spelled correctly. Line 12 is gets the recorded amounts so that they can be added together to create the total. Once the total is returned, the next two lines of code 15-16 compare it to 1000 to determine if it needs to be reviewed for approval and 18-19 formats how the inital part of the review message is printed.
What I tried: correcting the typo in line 12
How I fixed it: correcting the typo

## Bug 2
Error type: TypeError: '>' not supported between instances of 'int' and 'str'
File + line: "/home/maxine/ism3232/module05_functions/week8_buggy.py" + Line 16 & Line 23 
What the error means: It can’t compare a number to a word
How I fixed it: removing '' around the amount to make both numbers

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Not all 5 at first but I was able to use the error (as well as some trial and error with the >=) and got all 5 to pass

## AI Literacy Reflection
Did I use AI?  No, I used my classmates and myself. I wanted to feel more prepared and to make sure I wasn’t relying too much on AI for the problems I was coming across. 
If yes -- exact prompt I used: ___
What AI explained: ___
What I changed myself: ___
Can I explain every fixed line? Yes, the error message was pretty clear in indicating what was wrong

## What I learned
I learned that trial and error is a great teacher because I kept trying to run it after the first error without actually saving. I also learned that >= works better for border numbers.