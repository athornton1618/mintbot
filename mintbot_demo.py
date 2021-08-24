#mintbot_demo.py
#Demo of mintbot, with no account
#Copyright A. Thornton 2021

import tkinter as tk
import pandas as pd
import os
import mintapi
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def call_mint():
    #API to Intuit Mint
    mint = mintapi.Mint(
    '********',  # YOUR MINT EMAIL HERE
    '********',  # YOUR MINT PASSWORD HERE
    # Optional parameters
    mfa_method='sms',  # Can be 'sms' (default), 'email', or 'soft-token'.
                       # if mintapi detects an MFA request, it will trigger the requested method
                       # and prompt on the command line.
    headless=False,  # Whether the chromedriver should work without opening a
                     # visible window (useful for server-side deployments)
    mfa_input_callback=None,  # A callback accepting a single argument (the prompt)
                              # which returns the user-inputted 2FA code. By default
                              # the default Python `input` function is used.
    intuit_account=None, # account name when multiple accounts are registered with this email.
                         # None will use the default account.
    session_path=None, # Directory that the Chrome persistent session will be written/read from.
                       # To avoid the 2FA code being asked for multiple times, you can either set
                       # this parameter or log in by hand in Chrome under the same user this runs
                       # as.
    imap_account=None, # account name used to log in to your IMAP server
    imap_password=None, # account password used to log in to your IMAP server
    imap_server=None,  # IMAP server host name
    imap_folder='INBOX',  # IMAP folder that receives MFA email
    wait_for_sync=False,  # do not wait for accounts to sync
    wait_for_sync_timeout=300,  # number of seconds to wait for sync
    use_chromedriver_on_path=True,  # True will use a system provided chromedriver binary that
                                     # is on the PATH (instead of downloading the latest version)
    )
    #Only care about Net Worth, can update later for credit score, etc
    Net_Worth = np.round(mint.get_net_worth(),2)
    mint.close()
    return Net_Worth

class GUI:

    def __init__(self,Running_nw):
        #Setup a fresh GUI after each update
        #Only uses labels so tear it down and call __inti__ each time

        #Setup GUI
        self.tk = tk.Tk()
        self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.frame = tk.Frame(self.tk)
        self.frame.pack()
        self.state = True
        self.tk.attributes("-fullscreen", True)
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.tk.configure(background='black')

        #Fresh call to Mint API
        #Net_Worth = call_mint()
        Net_Worth = 69420.69

        # Create labels
        #Newline label
        np.set_printoptions(precision=2)
        l_1 = tk.Label(self.tk, text = "\n",fg='green', bg='black')
        l_1.config(font =("Courier", 10))
        l_1.pack()

        #Net Worth label
        l_2 = tk.Label(self.tk, text = "$" + "{:,}".format(Net_Worth),fg='green', bg='black')
        l_2.config(font =("Courier", 80))
        l_2.pack()

        #Delta label
        last_nw = Running_nw[-2] #updates 2x daily, so back 2 for yesterday
        if Net_Worth - last_nw >=0:
            l_3 = tk.Label(self.tk, text = "+$" + "{:,}".format(np.round(Net_Worth-last_nw,2)),fg='green', bg='black')
        else:
            l_3 = tk.Label(self.tk, text = "-$" + "{:,}".format(np.round(last_nw-Net_Worth,2)),fg='red', bg='black')
        l_3.config(font =("Courier", 35))
        l_3.pack()

        #Timestamp label
        l_4 = tk.Label(self.tk, text = "\nLast Updated: " + pd.Timestamp("today").strftime('%Y-%m-%d %X'),fg='white', bg='black')
        l_4.config(font =("Courier", 10))
        l_4.pack()

        #Copyright statement label
        l_5 = tk.Label(self.tk, text = "\u00a9" + " A. Thornton 2021",fg='white', bg='black')
        l_5.config(font =("Courier", 10))
        l_5.pack()

        #Update running Net Worth table
        #Pop oldest value, Push fresh value
        Running_nw[:-1] = Running_nw[1:]
        Running_nw[-1] = Net_Worth

        #Plot running Net Worth
        fig = plt.figure()
        fig.set_size_inches(4,1.5)
        ax = fig.add_subplot(1, 1, 1) # nrows, ncols, index
        chart = FigureCanvasTkAgg(fig, self.tk)
        chart.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)
        start = Running_nw[0]*np.ones(Running_nw.size) # Dashed red line for starting value 
        plt.plot(Running_nw, 'g',start,'r--')
        ax.set_facecolor('k')
        fig.patch.set_facecolor('k')
        ax.spines['bottom'].set_color('k')
        ax.spines['top'].set_color('k') 
        ax.spines['right'].set_color('k')
        ax.spines['left'].set_color('k')

        ax.tick_params(
            axis='both',          # changes apply to the x-axis
            which='both',         # both major and minor ticks are affected
            bottom=False,         # ticks along the bottom edge are off
            top=False,            # ticks along the top edge are off
            labelbottom=False)    # labels along the bottom edge are off

        #Close chromium
        os.system("pkill chromium")

        #Re-round to nearest penny
        self.Running_nw = np.round(Running_nw,2)

        #Reset 2x a day, kill GUI and remake
        reset = 1000*60*60*12
        self.tk.after(reset, lambda: self.tk.destroy())


    def clearFrame(self):
        # destroy all widgets from frame
        for label in self.labels:
            label.destroy()

    def toggle_fullscreen(self, event=None):
        #F11 to enter fullscreen, Escape to exit to Desktop
        self.state = not self.state 
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"


if __name__ == '__main__':
    #Running_nw = np.zeros(28) #show last 2 weeks, updates 2x a day, init to 0's
    Running_nw = np.random.rand(28)*3000 + 60000 + np.linspace(60000, 69000, num=28)
    #Main loop
    while 1:
        print(Running_nw[-1])

        w = GUI(Running_nw) #Init new GUI
        Running_nw = w.Running_nw #Save updated Net Worth history

        #Run GUI until reset every 12 hours
        w.tk.mainloop()