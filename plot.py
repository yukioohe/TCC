import time 
import matplotlib.pyplot as plt
import ADS1256
import AD9850
import config_AD9850
import numpy as np
from matplotlib.widgets import Button,RadioButtons, CheckButtons, TextBox, Cursor
frequency = 5
amostra = 221
def get_samples():
    x,y = [], []
    i = 0
    while(i<amostra):
        x.append(i)
        ADC = ADS1256.ADS1256()
        ADC_Value = ADC.ADS1256_GetChannalValue(0)
        value = ADC_Value*5.0/0x7fffff
        y.append(value)
        i = i+1
        
def update_frequency(text):
    frequency = text
    print(frequency)
    config_AD9850.set_freq(frequency)
 
def plot():
    config_AD9850.init_AD9850(frequency)
    time.sleep(0.1)
    ADC = ADS1256.ADS1256()
    x,y = [], []
    i = 0
    
    while(i<amostra):
        x.append(i)
        ADC_Value = ADC.ADS1256_GetChannalValue(0)
        value = ADC_Value*5.0/0x7fffff
        y.append(value)
        i = i+1    
    
    fig = plt.figure()
    ax = fig.subplots()
    plt.subplots_adjust(left = 0.2, bottom = 0.3)
    p, = ax.plot(x, y, color = 'b', label = 'Plot')
    plt.title("Monitoramento")
    plt.xlabel("Amostras")
    plt.ylabel("Tensão (V)")

    #------BUTTON------

    ax_button0 = plt.axes([0.02,0.425,0.08,0.05]) #xposition, yposition, width, height

    #priperties of the button
    grid_button = Button(ax_button0, 'Grid', color='white', hovercolor = 'grey')

    #enabling/disabling the grid
    def grid(val):
        ax.grid()
        fig.canvas.draw() #redraw the figure
    grid_button.on_clicked(grid) #triggering event is the  clicking
    
    #-------ACQUIRE-----------
    
    ax_button1 = plt.axes([0.02,0.525,0.08,0.05]) #xposition, yposition, width, height

    #priperties of the button
    acquire_button = Button(ax_button1, 'Get', color='white', hovercolor = 'grey')

    #enabling/disabling the grid
    def acquire(val):
        get_samples()
        fig.canvas.draw() #redraw the figure
    acquire_button.on_clicked(acquire) #triggering event is the  clicking

    #------RADIO BUTTONS-------
    ax_color = plt.axes([0.02, 0.625, 0.11, 0.15])
    color_button = RadioButtons(ax_color, ['red', 'green', 'blue', 'black'], [False, False, True, False], activecolor = 'r')

    #function for changing the plot color
    def color(labels):
        p.set_color(labels)
        fig.canvas.draw()
    color_button.on_clicked(color)
    
    #------TEXT BOX-------
    ax_box = plt.axes([0.045, 0.825, 0.12, 0.05])
    
    textbox = TextBox(ax_box,'Freq:', initial = '1000')
    textbox.on_submit(update_frequency)
    
    #------Cursor-------
    cursor = Cursor(ax, horizOn = True, vertOn = True, useblit = True,
                    color = 'r', linewidth = 1)
    #Creating an annotate
    annot = ax.annotate("", xy=(0,0), xytext=(-40,40),textcoords="offset points",
                    bbox=dict(boxstyle='round4', fc='linen',ec='k',lw=1),
                    arrowprops=dict(arrowstyle='-|>'))
    annot.set_visible(False)
    # Function for storing and showing the clicked values
    coord = []
    def onclick(event):
#         global coord
        coord.append((event.xdata, event.ydata))
        x = event.xdata
        y = event.ydata
        
        # printing the values of the selected point
        print([x,y]) 
        annot.xy = (x,y)
        text = "({:.2g}, {:.2g})".format(x,y)
        annot.set_text(text)
        annot.set_visible(True)
        fig.canvas.draw() #redraw the figure
        
    fig.canvas.mpl_connect('button_press_event', onclick)

    plt.show()


