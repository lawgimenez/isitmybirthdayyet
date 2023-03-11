from datetime import date
import datetime
import requests
import config

print("Running isitmybirthdayyet.py v0.1")

def getDadJoke():
	url = "https://dad-jokes.p.rapidapi.com/random/joke"
	headers = {
		"X-RapidAPI-Host": config.apiHost,
		"X-RapidAPI-Key": config.apiKey
	}
	response = requests.request("GET", url, headers=headers)
	data = response.json()
	# print(data)
	body = data["body"]
	for item in body:
		setup = item["setup"]
		punchline = item["punchline"]
		print(setup)
		answer = input("Ready for the punchline?\n")
		if "y" in answer:
			print(punchline)
		

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

today = date.today()
if today.month == 4 and today.day == 18:
	hex = "4861707079204269727468646179204c617721"
	message = bytes.fromhex(hex).decode("utf-8")
	print(message)
else:
	birthDate = datetime.datetime(1986, 4, 18)
	age = calculateAge(birthDate)
	print("Currently you are", age, "years old.")
	# Compute days until the birth date
	print(today.year)
	birthDateThisYear = datetime.datetime(today.year, 4, 18)

	print("Not your birthday yet.")
	answer = input("Wanna here a dad joke instead?\n")
	if "y" in answer:
		getDadJoke()
