import time 
import matplotlib.pyplot as plt

def plot(value):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.show()

    i = 0
    x, y = [], []
    x.append(i)
    y.append()
    
    ax.plot(x, y, color='b')
    
    fig.canvas.draw()
    
    ax.set_xlim(left=max(0, i-5), right=i+5)
    
    time.sleep(0.1)
    i += 0.1

plt.close()