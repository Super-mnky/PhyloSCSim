#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:50:22 2022

@author: sanghvins, Jerry Jones IV
Makes a bar chart plot for the runtimes vs various variables. 
"""
import pandas as pd
import matplotlib.pyplot as plt

scs_data = pd.read_csv('runtime_results.csv', header = 0)

fig, (ax1, ax2, ax3) =  plt.subplots(nrows = 3, ncols = 1, 
                                     sharex=False, sharey= False, 
                                     figsize=(8,12))

var_cellno = scs_data.loc[0:3, ['cell_no', 'SCSilicon runtime (min)', 'CellCoal runtime (min)']]
var_cellno.plot.bar(x='cell_no', ax = ax1, rot=0)
ax1.set_ylabel('Runtime (min)')
ax1.legend(['SCSilicon', 'CellCoal'])

var_cov = scs_data.loc[4:7, ['coverage', 'SCSilicon runtime (min)', 'CellCoal runtime (min)']]
var_cov.plot.bar(x='coverage', ax = ax2, legend = False, rot=0)
ax2.set_ylabel('Runtime (min)')

var_cov = scs_data.loc[8:11, ['SNV_no', 'SCSilicon runtime (min)', 'CellCoal runtime (min)']]
var_cov.plot.bar(x='SNV_no', ax = ax3, legend = False, rot=0)
ax3.set_ylabel('Runtime (min)')

fig.savefig('runtime_results.png', dpi=300)