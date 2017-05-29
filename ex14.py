from sys import argv

script, user_name, ai_name = argv
prompt = 'WTF>>> '

print("Hi %s, I'm %s." % (user_name, ai_name))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
        Alright, so you said %r about liking me.
        You live in %r. Not sure where that is.
        And you have a %r computer. Nice.
        """ % (likes, lives, computer))
