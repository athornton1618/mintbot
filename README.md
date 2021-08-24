# mintbot
Automatically queries Intuit Mint for display on 5in Raspberry Pi Screen

# Materials
1. Raspberry Pi 4 (or Raspberry Pi Zero)
2. MicroSD card w/ Rpi OS
3. Elecrow 5in Rpi LCD Display https://www.elecrow.com/wiki/index.php?title=HDMI_Interface_5_Inch_800x480_TFT_Display
2. Intuit Mint account (It's free!) https://mint.intuit.com/


# Setup
0. Create an Intuit Mint account 
1. Setup Raspberry Pi w/ raspian OS
2. Install LCD display, follow driver setup instructions: https://www.elecrow.com/download/How%20to%20install%20the%20LCD%20driver.pdf

# Installation
cd ~/Documents
git clone https://github.com/athornton1618/mintbot
sudo nano /etc/xdg/lxsession/LXDE/autostart
    //Add these lines
    @unclutter -idle 0
    @/usr/bin/python /home/pi/Documents/mintbot.py
sudo reboot
That's it! Good to go.

# NOTE
Occasionally Mint asks for multi-factor authentication
Might want to set up VNC connection to Rpi to input code manually if that happens

