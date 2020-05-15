# -*- coding: utf-8 -*-

import aiml
import os
import random
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
# Press CTRL-C to break this loop
while True:
    print(kernel.respond(input("Enter your message >> ")))