# synchronized Save directory for Scrap Mechanic

This repository allows for synchronizing Scrap Mechanic worlds between friends. It is meant to provide an alternative to an always-on server hosted by one of the participants, as whoever is online may host an up-to-date state of the world. 
The principle it runs off of is utilization of the GitHub service to store game data and then updating local game files or being updated from local game files when Scrap Mechanic is run or a world is closed. This works with SM because user data is stored by a unique identifier, not by "host" or "non-host". What we are describing in this README is effectively how to set up a combination world data synchronizer and game launcher. 


## Table of Contents
+ [Requirements](#Requirements)
+ [Setting up the repository](#Setting-up-the-repository)
+ [Adding the script to the steam library](#Adding-the-script-to-the-steam-library)
+ [How to use](#How-to-use)


## Requirements

First up, this document presumes a Windows environment.

The following steps require you to have an installation of [git](https://git-scm.com/download/win), a Github account, and [Python](https://www.python.org/downloads/). Furthermore you need to add the directory containing your Steam executable (typically along the lines of `C:\Program Files (x86)\Steam`) to your PATH ([help](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) if you're unfimiliar with how to do this). 


## Setting up the repository

Before getting started you need to locate the directory where Scrap Mechanic stores your user-specific data (In File Explorer you can do this by typing `%appdata%` into the address bar, then navigating to `".\Axolot Games\Scrap Mechanic\User\User_x"`). Moving forward we will call this directory `User_x`.

> ![image](https://github.com/Junkyard-Logic-Studios/Save/assets/136197051/7432543a-2516-4628-8903-ee956e8c4891)

First you'll want to rename `User_x\Save`, for example into `User_x\Save_old`.
Next clone the repository into `User_x` (type cmd into the address bar once you are in the `User_x` folder, then enter `git clone https://github.com/Junkyard-Logic-Studios/Save` into the window that pops up).
You can then copy all the contents of `User_x\Save_old` into the newly created `User_x\Save` and delete `User_x\Save_old`.

> address bar in the `User_x` folder:  
![image](https://github.com/Junkyard-Logic-Studios/Save/assets/136197051/2cc80c50-eb8d-4db6-bd8b-6dac640ac7cd)

> having typed "cmd" into the address bar in the `User_x` folder:  
![image](https://github.com/Junkyard-Logic-Studios/Save/assets/136197051/f0c6a56b-aa0a-4fc7-930d-e2ef71c6de36)

> having typed or right clicked and pasted `git clone https://github.com/Junkyard-Logic-Studios/Save` into the terminal window that pops up (Note: Ctrl + V does not work in the terminal):   
![image](https://github.com/Junkyard-Logic-Studios/Save/assets/136197051/acf8f535-81b1-46fb-bdd0-d9044a24f8c8)


As the repository is now set up, you could from now on launch your game by navigating into `User_x\Save` and calling `python observer.py`, however a more convenient option is to add the script to your steam library.


## Adding the script to the Steam Library

In the Steam app, navigate to the Library tab. At the bottom left of the window click: `Add a Game` &rarr; `Add a Non-Steam Game...` &rarr; tick any of the boxes that it shows &rarr; `Add Selected Programs`.
Find and right-click your newly added program on the left of the Library tab and click: `Properties...`.
Once you do this, you may optionally give your program a more appropriate icon and name in the text field at the top, ideally something to associate it with SM (we chose to name it "Scrap Mechanic Online - SMO"). This is the name your combination synchronizer + game launcher will have on Steam.
Under `TARGET`, type: `python`.
Under `START IN` you'll want to paste the full path to the `User_x\Save` directory from before.
Under `LAUNCH OPTIONS`, type: `observer.py`.

> Ticking any of the options before pressing `Add Selected Programs`:  
![image](https://github.com/Junkyard-Logic-Studios/Save/assets/136197051/7d79574f-c074-45a6-8e4c-a9923405c10d)

> Having filled in the information after clicking Properties:  
![image](https://github.com/Junkyard-Logic-Studios/Save/assets/136197051/7b837c88-1ef9-4b2a-af18-92a92ff902ac)



If you now press the `PLAY` button on your installation in the Library you should see the observer script pulling the latest state of the repository, then launching Scrap Mechanic shortly after. 


## How to use

The observer script is set up to track all worlds whose names start with "git_", meaning all your old worlds should be unaffected. The names of all trackable files currently visible to the script will be logged to the console/terminal window. A similar message will show whenever a world has been opened or closed. Shortly after closing a tracked world the script will commit and push your changes to the remote repository. The script does not close itself after you exit Scrap Mechanic, so after you exit the game you must also exit the script.

A few things to keep in mind:
- When launching a world make sure you started/restarted the script somewhat **recently**, so your local state is up-to-date with the remote repository
- Two or more people playing on the same world in solo **will** resort in merge conflicts, therefore before launching the world yourself you should **always check** whether someone else is already hosting it, and if so, join them instead. If they want you to be the host, simply wait until their script says "world closed" (maximum ~1-2min after they close the world, typically less) and then relaunch the script on your end.
- Once you exit the Scrap Mechanic game, you **will** have to manually close the synchronizer, as it does not close itself when the game closes.
