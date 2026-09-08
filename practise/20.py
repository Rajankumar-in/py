#detect the spam message if any one of them finds in the comments("make a lot of money"  "buy now"  "subscribe this" "click here")

p1 = "make a lot of money" 
p2 = "buy now" 
p3 = "subscribe this" 
p4 = "click here"

message = input("enter your comments:" )

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is spam")
else:
    print("this comment is not spam")


