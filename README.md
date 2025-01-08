# Minecraft Server Query w/ Email

This script uses the MCStatus Python library to check the status of each server in the `hosts.csv` file. Servers that are down send an email automatically to the one specified in `email_credentials.csv`, with the login specified in the same file.

## Installation

1. You must have Python3 and PIP installed on the device you are running the program on.
2. Clone / Download MC-Query.
3. Install `mcstatus` with pip.
4. Edit `hosts.csv` and `email_credentials.csv`.
5. Run with Python3, `python3 main,py`

## Hosts & Credentials Files

### Hosts

1. Put the hostname / ip address **and** the port, default for Minecraft servers being 25565.
2. Leave line 1 of the `hosts.csv` file, which serves as an example of what you need to type in.

### Email Credentials

This program is specifically setup for use with Gmail. You can use any other email service by changing the SMTP server to the one you want to use. For this guide, I'll be detailing it with instructions for Gmail, as it's very quick to setup an account. We will be using app-passwords for the password, and [here](https://support.google.com/mail/answer/185833?hl=en) is a link to the google article detailing what app-passwords are, incase there were security concerns.

1) Create a Gmail app password. Either use the article linked above, and read about app-passwords, and click the link in the official Google article, or click this link [here](https://myaccount.google.com/apppasswords).
   1) Type in the app name, it can be what ever you want, it is not refrenced by this program.
   2) Copy the provided password either straight into the `email_credentials.csv`, or into a notepad, because once you click done, you can not see the password again. The password will have spaces in it, and that is fine for copying into the CSV file, nothing special needs to be done for that.
2) In the `email_credentials.csv` file, change the prefilled info on line 2 to your info, leaving line 1 how it is. Receiver email does not need to be a gmail, however be careful with the emails going into your junk.

## Running

After you setup the CSV files, run `main.py`. It is reccomended to put in a fake / dead minecraft server in the hosts.csv file, just to ensure that the script is running correctly and that you receive an email. Please check your junk folder if it does not appear to show up.

## Automation

Below is the basic instructions for Windows automation with this program. Task scheduler has many options, so please set it for your use case. For Linux, either use cron, or another similar program for Linux, depending on your usecase.

In this repo is a `start.bat` script. Upon running the bat file, it runs the python script, and closes the command prompt immedietly after running. We can utilize Task Scheduler, built into Windows to schedule this.

1) Edit the directory in `start.bat` to the directory the downloaded repository is in.
2) Open Task Scheduler
3) Click Create Task on right side of window
   1) General
      1) Name
      2) Configure For: Windows 10
      3) OPTIONAL: Turn on run whether the user is logged in or not, and provide your account password to the pop up window. This allows the script to run without opening a command prompt automatically.
   2) Triggers
      1) New
      2) Set the times for how you want. If you want hourly, leave it at one time, and click the checkbox for repeat task every hour, and change the duration to indefinite.
      3) Recomended to check stop task if it runs longer than 30 minutes, as this is a very quick script, so incase theres a syntax error, it won't keep running.
   3) Actions
      1) New
      2) Start a program
      3) Set the program/script option to the `start.bat` in this repo. No extra arguments / options needed.
   4) Settings
      1) Change any as needed for how you want this to run.

*Last edited on 01-08-2025*
