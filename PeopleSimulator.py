import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import random

# Initial values
initialpopulation = 1000
initialfood = 200000
foodconsumption = 10
farmerpercent = 50
rateoffood = 20
deathrate = 10
reproductionrate = 1.2
num_years = 100
variation = 0.005

print('Food per person is amount of food consumed per person')
print('Farmer % is percentage of people creating food')
print('Food rate is amount of food coming from each farmer')
print('Death rate is % of population per year that die NATURALLY')
print('Reprodcution Rate is multiplication factor of population')
print('*NOTE* A little inherit randomness is included, so results won\'t be exactly the same everytime')

# Simulation function (fixed parameter name)
def simulate(initialpopulation, initialfood, foodconsumption, farmerpercent, rateoffood, deathrate, reproductionrate, num_years, variation):
    time = [0]
    population = [initialpopulation]
    food = [initialfood]

    for i in range(int(num_years)):
        food.append(random.uniform(1-variation, 1+variation)*2/3*max(1, food[-1] + farmerpercent / 100 * population[-1] * rateoffood - population[-1] * foodconsumption))
        population.append(random.uniform(1-variation, 1+variation)*
            population[-1] * (1 - deathrate / 100) * reproductionrate -
            max(0, population[-1] - food[-1] / foodconsumption)
        )
        time.append(i + 1)
    return time, population

# Initial simulation
time, population = simulate(initialpopulation, initialfood, foodconsumption, farmerpercent, rateoffood, deathrate, reproductionrate, num_years, variation)

# Plot setup
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.55)
line, = ax.plot(time, population, 'b-', label='Population')
ax.set_xlabel('Years')
ax.set_ylabel('Population')
ax.set_title('Population Simulator')
ax.grid(True)
ax.legend()

# Slider positions
axcolor = 'lightgoldenrodyellow'
slider_axes = {
    'initialpopulation': plt.axes([0.25, 0.48, 0.65, 0.03], facecolor=axcolor),
    'initialfood': plt.axes([0.25, 0.44, 0.65, 0.03], facecolor=axcolor),
    'foodconsumption': plt.axes([0.25, 0.40, 0.65, 0.03], facecolor=axcolor),
    'farmerpercent': plt.axes([0.25, 0.36, 0.65, 0.03], facecolor=axcolor),
    'rateoffood': plt.axes([0.25, 0.32, 0.65, 0.03], facecolor=axcolor),
    'deathrate': plt.axes([0.25, 0.28, 0.65, 0.03], facecolor=axcolor),
    'reproductionrate': plt.axes([0.25, 0.24, 0.65, 0.03], facecolor=axcolor),
    'num_years': plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor),
    'variation': plt.axes([0.25, 0.16, 0.65, 0.03], facecolor=axcolor),
}

# Sliders
sliders = {
    'initialpopulation': Slider(slider_axes['initialpopulation'], 'Initial Pop', 100, 10000, valinit=initialpopulation, valstep=100),
    'initialfood': Slider(slider_axes['initialfood'], 'Initial Food', 10000, 500000, valinit=initialfood, valstep=1000),
    'foodconsumption': Slider(slider_axes['foodconsumption'], 'Food per Person', 1, 50, valinit=foodconsumption),
    'farmerpercent': Slider(slider_axes['farmerpercent'], 'Farmer %', 0, 100, valinit=farmerpercent),
    'rateoffood': Slider(slider_axes['rateoffood'], 'Food Rate', 1, 100, valinit=rateoffood),
    'deathrate': Slider(slider_axes['deathrate'], 'Death Rate %', 0, 100, valinit=deathrate),
    'reproductionrate': Slider(slider_axes['reproductionrate'], 'Reproduction Rate', 0.5, 3.0, valinit=reproductionrate),
    'num_years': Slider(slider_axes['num_years'], 'Years', 10, 1000, valinit=num_years, valstep=1),
    'variation': Slider(slider_axes['variation'], 'Variation', 0, 0.5, valinit=variation, valstep=0.001),
}

# Update function
def update(val):
    values = {key: slider.val for key, slider in sliders.items()}
    time, population = simulate(**values)
    line.set_xdata(time)
    line.set_ydata(population)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

# Connect sliders to update
for slider in sliders.values():
    slider.on_changed(update)

plt.show()
