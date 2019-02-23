  The code in hw3.py was modified from hw2.py to fit the criteria specified in this assignment.
This program requires the packages math, numpy and matplotlib to run properly. All 3 are imported 
at the beginning of the program. 

  For each test case there is an included script and plot, both of which were generated using bash 
in an Ubuntu shell. All percentage inputs must be entered as a number within the bounds specified on the
instruction sheet for hw3. These bounds are listed below for reference:

* # of reinforcement events (0-3)
* % of initial force level at which a reinforcement occurs (10% - 80%)
* reinforcement force size as % of initial force level (10% - 50%)
* lethality coefficient of the new troops.

  Program hw3.py was written so that the input value for each variable that must fall within certain 
bounds is not checked. Rather, the program will automatically bound the input such that it stays within 
the bounds. For example:

* an input of '5' for x reinforcement events will be capped at the maximum of 3
* an input of '2' for y reinforcement size will change to 10

The scripts for all three test cases was modified for readability **only**, neither input nor output 
values were changed from the initial creation of each script. The three test cases, and their respective 
output graphs, are explained below:

output1 (script1):

  The test case for this plot used the same inputs as the test case for hwtwo.py. This examples shows
conditions where not all the reinforcement events occur for the x side. This is because x never reaches
the reduction condition more than once before all of the y forces are wiped out.

output2 (script2):
  
  The test case for this plot used similar inputs as the previous test case only there are two key differences.
The first is that the lethality coefficient for both y initial troops and y reinforcement troops is less than x.
The second is that x has **no** reinforcement events, while y has three. This demonstrates that given enough 
reinforcement events, even a group with a lower lethality coefficient than the other can win a battle.

output3 (script3):

  tfinal (end time) has to be increased to 10 from 5 for this final test output. This demonstrates what 
can occur when reinforcements with a higher lethality coefficient than the opposing side are introduced.
At no point does the y side ever recieve MORE troops in reinforcements, the percentages are the same and 
y initial troops are less than x. However, the y side wins out in the end because the reinforcements 
introduced have a much higher lethality coefficient than the x side.






  
