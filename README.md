# Sleep and Wake On LAN

# Summary
This project contains a system in which Node Red is used to turn on and off any Windows based PC using NodeRed and 
python to do it. To do this, the following systems are needed:

- Smart Home Agent (Alexa, Google Home)
- [Windows Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)
- [Node-RED](https://nodered.org/)

# Architecture
The system works by using a Raspberry Pi as the central control system running NodeRed in Docker. This Raspberry Pi then 
communicates with other Smart Home devices such as alexa and then the Windows PC running the Sleep on LAN script. The 
architecture of the system is shown below:

![System Architecture](docs/System Architecture.png)

The Task Scheduler in Windows is used to run the Python script which is waiting for a TCP socket connection and then 
once it receives the correct command, it will put the computer to sleep. The reason Task Scheduler is used is that it
allows the python script to always run.

# Node Red Flows

Inside Node-RED there is the following flow which uses both Telegram and Alexa Nodes, the reason is for this is that. 
The Desk in which the computer is connected to have its own smart plug for the monitors. When the PC is turned off and on, 
the monitors also need to be turned on and off.

The PC is refgistered as an alexa devie using the node-red-contrib-alexa-home-skill node which then feeds a function for 
the turnOn and off requests. This then sends the apropriate command to the sleep on LAN script as well as the wake on 
LAN node provided by Node-RED. 

![Node-RED Flow](docs/NodeRED Flow.PNG)

# Software Requirements
The following pieces of software are required for the system to work:
- [Node-RED](https://nodered.org/)
- [node-red-contrib-alexa-home-skill](https://flows.nodered.org/node/node-red-contrib-alexa-home-skill)
- [node-red-contrib-telegrambot](https://flows.nodered.org/node/node-red-contrib-telegrambot)
- [node-red-contrib-alexa-cakebaked](https://flows.nodered.org/node/node-red-contrib-alexa-cakebaked)
- [Windows Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)
- [Portainer](https://www.portainer.io/)
- [Docker](https://www.docker.com/)
- 