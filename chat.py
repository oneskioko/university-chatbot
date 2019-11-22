import aiml
import os
import time 

BRAIN_FILE="brain.dump"

k = aiml.Kernel()

# Create the kernel and learn AIML files
#kernel = aiml.Kernel()
#kernel.learn("std_startup.xml")
#kernel.respond("load aiml b")

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std_startup.xml", commands="LOAD AIML B")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

# Endless loop which passes the input to the bot and prints
# its response
while True:
     input_text = raw_input("You: ")
     response = k.respond(input_text)
     print("University Corr:" + response)

# Press CTRL-C to break this loop
#while True:
	#print kernel.respond(raw_input("Enter your message >> "))