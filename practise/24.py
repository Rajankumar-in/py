# detect that the any special word (rajan) is available in the sentence (or post )or not

post = input("enter the post")

if ("Rajan" in post): # ye formate case sensetive hai , esme word same to same hona cahiye
    print("this post is talking about Rajan")
else:
     print("this post is not talking about Rajan")

     # ye wala case sencetive methid nahi hai due to .lower method
if("Rajan".lower() in post.lower()):
    print("this post is talking about Rajan")
else:
    print("this post is not talking about Rajan")
