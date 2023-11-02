# Importing required libraries
import numpy as np
from pyudss import pyudss

# Defining the network object
net = pyudss.OpenDSS_network('Res_cigre.dss')

# Solving the power flow problem
net.solve()

# Getting network lines
lines = net.get_lines()
print(lines)

# Getting network loads
loads = net.get_loads()
print(loads)

# Getting selected nodes line to neutral voltages and complex voltages
nodes = ['r0', 'r1', 'r11', 'r15', 'r16', 'r17', 'r18']
vol = net.get_ln_voltages(nodes)
print(vol)
vol_complex = net.get_complex_voltages(nodes)
print(vol_complex)

# Getting line currents
currents = net.get_currents()
print(currents)

# Getting losses
losses = net.get_losses()
print(losses)
    
# Modifying lines
lines['r9_r10'][0] = 'UG3'
lines['r9_r10'][1] = 0.5    
net.set_lines(lines)
new_lines = net.get_lines()
print(new_lines)

# Modifying loads
loads['r16_b'] = [20.0, 17.5] 
net.set_loads(loads)
new_loads = net.get_loads()
print(new_loads)
    
    
    
    
    