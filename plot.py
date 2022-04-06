import time 
import matplotlib.pyplot as plt
import ADS1256

    
def plot(value):
    ADC = ADS1256.ADS1256()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    fig.show()

    i = 0
    x, y = [], []
    while 1:
        ADC_Value = ADC.ADS1256_GetChannalValue(0)
        value = ADC_Value*5.0/0x7fffff
        x.append(i)
        y.append(value)
        
        ax.plot(x, y, color='b')
        
        fig.canvas.draw()
        
        ax.set_xlim(left=max(0, i-50), right=i+50)
        
        time.sleep(0.1)
        i += 1

plt.close()