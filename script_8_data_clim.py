from fanpy import read_climate

import matplotlib.pylab as plt

home_dir = '/p/project/hai_hhhack/anand1/'

project_data_path = home_dir + 'Project_Data/forest-carbon-flux/'

plot_path = project_data_path+f'graphics/irr_hist.png'

fig, axes = plt.subplots(5,4, figsize = (20,16))

for i in range(5):
    for j in range(4):
        k = 4*i+j
        climate_file = project_data_path+f'climate_data/weather_sim_10000_{k}.txt'
        climate_data = read_climate(climate_file)

        precip = climate_data.values[365*1000:, 2]
        axes[i][j].hist(precip, bins = 100)
        axes[i][j].set_xlabel(f'irr  | Year {k}')
        #axes[i][j].set_xlim(left = 300, right = 1600)

plt.savefig(plot_path)