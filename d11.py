
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird

a = int(input())
if a%2!=0:
    print("Weird")
if a%2==0 and a in range(2,5):
    print("Not Weird")
if a%2==0 and a in range(6,21):
    print("Weird")
if a%2==0 and a>20:
    print("Not Weird")

    