import random
import string
from colorama import Fore, Back, Style, init
import pyfiglet
text = pyfiglet.figlet_format("PASSWORD GENERATOR")
length = int(input(f"{Fore.GREEN}Enter the Length of password: {Style.RESET_ALL}"))
characters = string.ascii_letters + string.digits + string.punctuation

print(text)
password = ""

for i in range(length):
    char = random.choice(characters)
    password = password + char
Thank_you_for_using = pyfiglet.figlet_format("Thank you !")
print(f"\t\t\t\t{Fore.YELLOW}Generated Password: {Style.RESET_ALL}{password}")
print(Thank_you_for_using)
#By XXTRACER 
