"""create a function that take the no of daily new cases,recovered cases and active cases.
and return the no of days it will take to reach active case to 0.
1.ask user input the no of daily new cases and assign it to the variable newcases 
changing it to integer.
2.do the same with recovery and active cases.
3.declare the variable days and assign it with a valur 0
4.now run while loop until the active case is greater than 0 where active case
will change to active case+newcase recovered case..
5.increment the value of day by 1 after every loop.
6.print hte value of day after the loop ends.

"""

newcases=int(input("enter daily new cases "))
recovery=int(input("enter daily recovery cases "))
active=int(input("enter active cases "))
days=0
while active>0:
    active=active+newcases-recovery
    days=days+1
print("days needed to end corona is ",days)    

