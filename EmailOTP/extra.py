# name =input("What is your name? ").strip().title()

# first ,last =name.split(" ")

# print(f" Hello {first} {last}")
 
 
# x=455+2222334
 
# print(f"{x:,}")  


# import random

# cards=["jack","queen","king","Ace"]

# random.shuffle(cards)

# for card in cards:
#     print(card)



# import sys

# try:
    
#     print("hello my name is ",sys.argv[1])
    
# except ValueError: 
#     print("error ",ValueError)    



# import cowsay

# cowsay.cow("hello sabko")

# my_fish=r'''

#      /`·.¸
#      /¸...¸`:·
#  ¸.·´  ¸   `·.¸.·´)
# : © ):´;      ¸  {
#  `·.¸ `·  ¸.·´\`·¸)
#      `\\´´\¸.·´




# '''

# cowsay.draw("helllo",my_fish)




# cowsay.daemon("keseho")
# cowsay.trex("keseho oooooooo")


import json
import requests
import sys


if(len(sys.argv)!=2):
    sys.exit()
    
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=11&term=" + sys.argv[1])


# print(json.dumps(response.json(),indent=2))


lst=response.json()

for result in lst["results"]:
    print(result["trackName"])

    