import re
from urllib.request import urlopen

url = input("Enter a website to scan: (include http(s)://)\n")
website = urlopen(url).read().decode('utf-8')


# REGEX OF PHONE:
# https://softhints.com/regex-phone-number-find-validation-python/
# https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script


# https://en.wikipedia.org/wiki/Telephone_number#:~:text=A%20telephone%20number%20serves%20as,signaling%20to%20a%20telephone%20exchange

print()
print()
print("Phone Numbers: ")
numbers = (re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", website))
# numbers = (re.findall(r"\d\d\d-\d\d\d-\d\d\d\d", website))
# numbers = (re.findall(r"(\d\d\d-)?\d\d\d-\d\d\d\d", website))
print(', '.join(map(str, numbers)))


print()
print()

print("Emails: ")
emails = (re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", website))
print(', '.join(map(str, emails)))
