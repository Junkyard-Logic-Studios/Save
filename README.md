# synchronized Save directory for Scrap Mechanic

This repository allows for synchronizing Scrap Mechanic worlds between friends. It is meant to provide an alternative to an always-on server hosted by one of the participants, as whoever is online may host an up-to-date state of the world.


## Requirements

First up, this document presumes a Windows environment.

The following steps require you to have an installation of [git](https://git-scm.com/download/win), a Github account, and [Python](https://www.python.org/downloads/). Furthermore you need to add the directory containing your Steam executable (typically along the lines of `C:\Program Files (x86)\Steam`) to your PATH ([help](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) if you're unfimiliar with how to do this). 


## Setting up the repository

Before getting started you need to locate the directory where Scrap Mechanic stores your user-specific data (In File Explorer you can do this by typing `%appdata%` into the address bar, then navigating to `".\Axolot Games\Scrap Mechanic\User\User_x"`). Moving forward we will call this directory `User_x`.

First you'll want to rename `User_x\Save`, for example into `User_x\Save_old`.
Next clone the repository into `User_x` (open a terminal in `User_x` and enter `git clone https://github.com/Junkyard-Logic-Studios/Save`).
You can then copy all the contents of `User_x\Save_old` into the newly created `User_x\Save` and delete `User_x\Save_old`.

As the repository is now set up, you could from now on launch your game by navigating into `User_x\Save` and calling `python observer.py`, however a more convenient option is to add the script to your steam library.


## Adding the script to the steam library

In the steam - library tab, click: `Add a Game` &rarr; `Add a Non-Steam Game...` &rarr; tick literally any one box &rarr; `Add Selected Programs`.
Right-click your newly added program on the left and click: `Properties...`.
First you might want to give your program a more appropriate icon and name in the text field at the top, ideally something to associate it with SM. 
Under `TARGET`, type: `python`.
Under `START IN` you'll want to paste the full path to the `User_x\Save` directory from before.
Under `LAUNCH OPTIONS`, type: `observer.py`.

If you now press the `PLAY` button you should see the observer script pulling the latest state of the repository, then launching Scrap Mechanic shortly after. 


## How to use

The observer script is set up to track all worlds whose names start with "git_", meaning all your old worlds should be unaffected. The names of all trackable files currently visible to the script will be logged to the console. A similar message will show whenever a world has been opened or closed. Shortly after closing a tracked world the script will commit and push your changes to the remote repository. When exiting the game simply exit the script too.

A few implications to keep in mind:
- when launching a world make sure you started/restarted the script somewhat recently, so your local state is up-to-date with the remote repository
- two or more people playing on the same world in solo will resort in merge conflicts, therefore before launching the world yourself you should always check whether someone else is already hosting it, and if so, join them instead
