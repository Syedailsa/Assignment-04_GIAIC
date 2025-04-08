#Joke bot

import random

jokes:str = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why don't programmers like nature? It has too many bugs.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why do Python programmers need glasses? Because they can't C!",
    "What do you call a programmer from Finland? Nerdic.",
    "Why did the programmer quit their job? They didn't get arrays (a raise)!",
    "What's the object-oriented way to become wealthy? Inheritance!",
    "Why did the developer go broke? They used up all their cache!",
    "How do you comfort a JavaScript bug? You console it!",
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
    "What's a programmer's favorite hangout place? Foo Bar!",
    "Why was the JavaScript developer sad? They didn't know how to 'null' their feelings!",
    "What do you call a programmer who doesn't comment code? A future job applicant!",
    "Why did the database administrator leave his wife? She had one-to-many relationships!",
    "What's the difference between a programmer and a politician? When a programmer says 'Hello world', they actually mean it!"
]

print("""
                 @@  @@ 
                ,-@@~@-.   
 _              (_, O _/   
| Y~.            (__d._)    
| r.|    Y@oooood@@@@@@@@oooo@F 
 Y ||   _Y@@@@@@P   "V"  Y@@@@f 
 | t_\_/ _)@@@@@          @@@@f  __     ,--,
  \  `. / ~@@@@@    . .   @@@@  (_ `---'  ~~)
   `-._/)   @@@@b__|@_@|_d@@@    _l,'~   ~~)
      (,db   (   _  `-' _   )  ,d@_)---~~~~
         Yb.  \ '|\____/|` / od@P 
          Y@b  \ | nn  /','d@@P 
            Y@b `\`---'/'od@P 
             ~@@@@`---'@@@P~
               Y@@@@@@@@@~
                @@@@@@@@
      """)

def Joke_Bot(user_input:str):
    if user_input.lower() == "yes":
        while True:    
            joke = random.choice(jokes)
            print(f"\nJoke for you: {joke}")
            if input("\nWant to hear more? (Y/N): ").lower() != "y":
                break
    else:
        print("\nSorry i cant help, i just tell jokes! :(")

Joke_Bot(input("\nHey im a joke bot want to here a joke? (yes/no): "))