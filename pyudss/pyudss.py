import win32com.client
import pathlib
import numpy as np
from win32com.client import makepy
import sys

class OpenDSS_network:
    def __init__(self, net_name):
        self.DSSObj = win32com.client.Dispatch("OpenDSSEngine.DSS")
        self.DSSObj.Start(0)
        self.DSSText = self.DSSObj.Text
        self.DSSCircuit = self.DSSObj.ActiveCircuit
        self.DSSSolution = self.DSSCircuit.Solution
        self.DSSLoads = self.DSSCircuit.Loads
        self.DSSText.Command = 'Compile "' + str(pathlib.Path().resolve()) + '\\' + net_name + '"';
        self.DSSText.Command = 'solve'
               
    def get_loads(self):
        loads = dict.fromkeys(self.DSSLoads.AllNames) 
        flag = self.DSSLoads.First
        while flag != 0:
            loads[self.DSSLoads.Name] = [self.DSSLoads.kW, self.DSSLoads.kvar]
            flag = self.DSSLoads.Next 
        return loads
    
    def set_loads(self, loads):
        item = self.DSSLoads.First
        while item != 0:
            self.DSSLoads.kW = loads[self.DSSLoads.Name][0]
            self.DSSLoads.kvar = loads[self.DSSLoads.Name][1]
            item = self.DSSLoads.Next
            
    def get_ln_voltages(self, keys):
        buses = dict.fromkeys(keys) 
        for item in buses:
            self.DSSCircuit.SetActiveBus(item)
            buses[item] = list(self.DSSCircuit.ActiveBus.VMagAngle[0:6:2])
        return buses
        
    def get_complex_voltages(self, keys):
        buses = dict.fromkeys(keys) 
        for item in buses:
            self.DSSCircuit.SetActiveBus(item)
            buses[item] = list(self.DSSCircuit.ActiveBus.Voltages)
        return buses
        
    def get_currents(self):
        lines = dict.fromkeys(self.DSSCircuit.Lines.AllNames) 
        flag = self.DSSCircuit.Lines.First
        while flag != 0:
            DSSActiveCktElement = self.DSSObj.ActiveCircuit.ActiveCktElement
            curr = DSSActiveCktElement.Currents
            lines[self.DSSCircuit.Lines.Name] = [np.sqrt(curr[0]**2 + curr[1]**2), 
                                                 np.sqrt(curr[2]**2 + curr[3]**2), 
                                                 np.sqrt(curr[4]**2 + curr[5]**2)]
            flag = self.DSSCircuit.Lines.Next 
        return lines
    
    def get_losses(self):
        return self.DSSCircuit.Losses
        
    def solve(self):
        self.DSSText.Command = 'solve'
        return self.DSSSolution.Converged
        
    def get_lines(self):
        lines = dict.fromkeys(self.DSSCircuit.Lines.AllNames) 
        flag = self.DSSCircuit.Lines.First
        while flag != 0:
            lines[self.DSSCircuit.Lines.Name] = [self.DSSCircuit.Lines.LineCode, self.DSSCircuit.Lines.Length]
            flag = self.DSSCircuit.Lines.Next 
        return lines
        
    def set_lines(self, lines): # Lines interface
        flag = self.DSSCircuit.Lines.First
        while flag != 0:            
            self.DSSCircuit.Lines.LineCode = lines[self.DSSCircuit.Lines.Name][0]
            self.DSSCircuit.Lines.Length = lines[self.DSSCircuit.Lines.Name][1]
            flag = self.DSSCircuit.Lines.Next
    

 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        