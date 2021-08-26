# mintbot
Automatically queries Intuit Mint for display on 5in Raspberry Pi Screen <br />
<br />
![Alt text](https://github.com/athornton1618/mintbot/blob/main/mintbot_demo.jpg?raw=true)

# Materials
1. Raspberry Pi 4 (or Raspberry Pi Zero)
2. MicroSD card w/ Rpi OS
3. Elecrow 5in Rpi LCD Display https://www.elecrow.com/wiki/index.php?title=HDMI_Interface_5_Inch_800x480_TFT_Display
2. Intuit Mint account (It's free!) https://mint.intuit.com/

# Setup
0. Create an Intuit Mint account 
1. Setup Raspberry Pi w/ raspian OS
2. Install LCD display, follow driver setup instructions: https://www.elecrow.com/download/How%20to%20install%20the%20LCD%20driver.pdf

# Packages
sudo apt update <br />
sudo apt install python3 <br />
pip3 install pandas matplotlib numpy <br />

# Installation
cd ~/Documents <br />
git clone https://github.com/athornton1618/mintbot <br />
cd mintbot <br />
sudo chmod a+x mintbot.py <br />
nano mintbot.py 
> Write in Username where prompted <br />
> Write in Password where prompted <br />

sudo nano /etc/xdg/lxsession/LXDE/autostart <br />
> Add these lines 
>> @unclutter -idle 0 <br />
>> @/usr/bin/python /home/pi/Documents/mintbot.py <br />

sudo reboot <br />
That's it! Good to go. <br />

# NOTE
Occasionally Mint asks for multi-factor authentication <br />
Might want to set up VNC connection to Rpi to input code manually if that happens <br />

