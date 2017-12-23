# AutoUpass
Automates the process of renewing the BC Upass

This Python script utilizes Selenium and the PhantomJS headless webdriver.
In order to run this script automatically, you would need to use a scheduler such as Cronjob, Windows Task Scheduler, or anything else that automates running the script in a given time-interval. If you do so, you need to hard-code the username and password variables with your credentials so that the script does not prompt for your credentials during every run. 

## Requirements
The script requires the machine to have Selenium and the PhantomJS webdriver installed.
