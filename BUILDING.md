# Building Instructions

For building this project, there is only really two steps:

- Import the flows.json into the existing NodeRed setup
- Configure the NodeRed Alexa blocks and telegram blocks
- Configure the IP addresses of the Wake on LAN and TCP blocks
- Change the IP and port number of the main.py script to match your preference and PC.
- Change "PROJECT_PATH" variable as well to have the log file log in the wanted directory
- Modify the runSOLScript.bat to point to the repository main.py python script and the python executable
- Setup Virtual Environment and install requirements.txt
- Setup Task Scheduler to run the main.py the runSOLScript.bat on boot
- Enable Wake on LAN in BIOS and Windows; when doing this it is recommended to have wake on a magic packet to prevent
accidental pings waking up the PC

For understanding how to use the Task Scheduler, please follow the link listed below:

## Setting up Virtual Environment

```powershell
C:\Users\smgib_161\AppData\Local\Programs\Python\Python312\python.exe -m venv ./.venv # Hate windows :(
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Sleep on Lan Task Scheduler

![alt text](docs/task%20scheduler%20screenshots/image.png)
![alt text](docs/task%20scheduler%20screenshots/image-1.png)
![alt text](docs/task%20scheduler%20screenshots/image-2.png)

## Wake on Lan Settings

In order to set up the wake on LAN correctly, you will need to change the BIOS
settings alongside the windows settings. The snippets below are for Windows 10
and the ASUSPX979.

![alt text](docs/wake%20on%20lan%20settings/image.png)
![alt text](docs/wake%20on%20lan%20settings/image-1.png)

## Useful Links

- [Using Task Scheduler](https://www.jcchouinard.com/python-automation-using-task-scheduler/)
- [Enabling Wake on LAN](https://www.windowscentral.com/how-enable-and-use-wake-lan-wol-windows-10)
- [Bash Script and Task Scheduler](https://www.tutorialspoint.com/batch_script/batch_script_comments.htm)
