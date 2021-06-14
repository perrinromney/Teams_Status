# Teams_Status
Displays TKinter window Green if not in call and red if in call on teams.
This project borrows heavily from the work done by Alex Reed on areed1192/ms-graph-python-client. All credit for development should go to him.
From his project, most scopes were deleted and the API version was altered to "beta" instead of "v1.0". A presence class was written in the format of his other classes and all other classes were removed.
Note: Alex's project works for personal accounts. This project works for business accounts. Some adjustment will need to be done if using a personal microsoft account, and this project has not been verified with personal accounts.

## Files
client.py         from Alex Reed's work (minor changes)
session.py        from Alex Reed's work (minor changes)
write_config.py   from Alex Reed's work (minor changes)
presence.py       imitation of Alex Reed's class format
test_client.py    contains the fetching formula for teams status
main_status.py    main code to run - contains TKinter window and initiates all other files.

## Functional Overview
This is essentially a Daemon that continually updates the teams status. The goal would be to use this for a hardware application in lieu of TKinter. I plan to port this to be used on an ESP32.

## Setup
A Microsoft Azure AD application must be registered. From this you will need the client ID, client Secret, and redirect url. I use http://localhost:5001/graph-login.
Enter the information into write_config.py in the correct locations.
Run write_config.py. this should create a "config.ini" file in the same directory.

## First Run
Run main_status.py. the terminal will give you a URL (and open a blank TKinter window). Leaving the TKinter window open and while logged into your microsoft account, go to this url in your browser. Provide approval for any permissions, then once the redirect fails out, copy the url from the address bar in chrome and paste it into the terminal and press enter. Alex Reed has a youtube video showing this process which is highly recommended. 

Once you have pasted the url and pressed enter, the TKinter window should change color to match your status. it should update every 5 seconds.
