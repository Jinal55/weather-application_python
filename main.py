import requests
import json
import subprocess

city = input("enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=8bbebd860ec040419e4133627240607&q={city}"
r = requests.get(url)
print(r.text)
weatherdictionary = json.loads(r.text)
w = weatherdictionary["current"]["temp_c"]
print(w)

ps_command = f"Add-Type -AssemblyName System.Speech; $jinal = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $jinal.Speak('The current weather in the {city} is {w} degrees')"

subprocess.run(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', '-command', ps_command],
               shell=True)
