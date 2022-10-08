# Building Instructions

For building this project, there is only really two steps:
- Import the flows.json into the existing NodeRed setup
- Configure the NodeRed Alexa blocks and telegram blocks
- Configure the IP addresses of the Wake on LAN and TCP blocks
- Change the IP and port number of the main.py script to match your preference and PC.
- Change "PROJECT_PATH" variable as well to have the log file log in the wanted directory
- Modify the runSOLScript.bat to point to the repository main.py python script and the python executable
- Setup Task Scheduler to run the main.py the runSOLScript.bat on boot
- Enable Wake on LAN in BIOS and Windows; when doing this it is recommended to have wake on a magic packet to prevent 
accidental pings waking up the PC


For understanding how to use the Task Scheduler, please follow the link listed below:

# Useful Links
- [Using Task Scheduler](https://www.jcchouinard.com/python-automation-using-task-scheduler/)
- [Enabling Wake on LAN](https://www.windowscentral.com/how-enable-and-use-wake-lan-wol-windows-10)
- [Bash Script and Task Scheduler](https://www.tutorialspoint.com/batch_script/batch_script_comments.htm)