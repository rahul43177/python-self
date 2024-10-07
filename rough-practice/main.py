import random
array = [1, 2, 3, 4, 5]

flag = len(array) > 0
if flag:
    print("The array is not empty")
else:
    print("The array is empty")

def get_motivational_quote():
    quotes = [
        "I don't run to add days to my life, I run to add life to my days",
        "Running is not just about putting one foot in front of the other; it is about creating a healthy lifestyle and being the best version of yourself",
        "The miracle isn't that I finished. The miracle is that I had the courage to start",
        "Running is a mental sport, and we're all insane",
        "You don't have to be great to start, but you have to start to be great",
        "The only bad workout is the one that didn't happen",
        "I hate running. But I love the way I feel after a run",
        "Do something today that your future self will thank you for",
        "It does not matter how slowly you go as long as you do not stop",
        "You are capable of amazing things",
        "Running is the greatest metaphor for life. You get out of it what you put in",
        "You don't have to be fast. But you have to be consistent",
        "It's not about being the best, it's about being better than you were yesterday",
        "The most important thing in running is to have fun",
        "You are stronger than you seem, braver than you believe, and smarter than you think",
    ]
    print(random.choice(quotes))

get_motivational_quote()
