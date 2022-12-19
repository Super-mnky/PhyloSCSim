# -*- coding: utf-8 -*-
"""
Neel Sanghvi and Jerry Jones IV
CMSC829A
Updated: 18DEC2022

Runs the SCSilicon package to simulate single-cell data under various 
conditions. 
"""
import scsilicon as scs

# Set up the simulator. 
params = scs.SCSiliconParams()
snv_simulator = scs.SNVSimulator()
t_count = 8 # computer has 10. 8 are safe to use here. 

# Three main parameters to play with: coverage, cell number, and snv number.
# snv_simulator.set_params(cell_no = 1, snv_no = 100)
# print("Testing coverage effect on runtime...")

# params.set_params(coverage = 1, threads = t_count, out_dir = './SNVs_coverage_1')
# snv_simulator.sim_samples(params)
# # took 3 min 18 sec (8 threads)

# params.set_params(coverage = 5, threads = t_count, out_dir = './SNVs_coverage_5')
# snv_simulator.sim_samples(params)
# # took 4 min 54 sec (8 threads)

# params.set_params(coverage = 10, threads = t_count, out_dir = './SNVs_coverage_10')
# snv_simulator.sim_samples(params)
# # took 6 min and 20 sec (8 threads)

# params.set_params(coverage = 50, threads = t_count, out_dir = './SNVs_coverage_50')
# snv_simulator.sim_samples(params)
# # took 13 min and 16 sec (8 threads)

print("Testing mutation (SNV) number effect on runtime...")

# params.set_params(coverage = 5, threads = t_count, out_dir = './SNVs_SNVnumber_10')
# snv_simulator.set_params(cell_no = 1, snv_no = 10)
# snv_simulator.sim_samples(params)
# # took 4 min 51 sec (8 threads)

# params.set_params(coverage = 5, threads = t_count, out_dir = './SNVs_SNVnumber_100')
# snv_simulator.set_params(cell_no = 1, snv_no = 100)
# snv_simulator.sim_samples(params)
# # took 4 min 49 sec (8 threads)

# params.set_params(coverage = 5, threads = t_count, out_dir = './SNVs_SNVnumber_1000')
# snv_simulator.set_params(cell_no = 1, snv_no = 1000)
# snv_simulator.sim_samples(params)
# # took 4 min 45 sec (8 threads)

# params.set_params(coverage = 5, threads = t_count, out_dir = './SNVs_SNVnumber_10000')
# snv_simulator.set_params(cell_no = 1, snv_no = 10000)
# snv_simulator.sim_samples(params)
# took 4 min 55 sec (8 threads)

print("Testing cell number effect on runtime...")

# params.set_params(coverage = 5, threads = t_count, out_dir = './SNVs_cellnumber_1')
# snv_simulator = scs.SNVSimulator(cell_no = 1, snv_no = 100)
# snv_simulator.sim_samples(params)
# # took 5 min 0 sec (8 threads)

# params.set_params(coverage = 5, threads = t_count, out_dir = './SNVs_cellnumber_2')
# snv_simulator = scs.SNVSimulator(cell_no = 2, snv_no = 100)
# snv_simulator.sim_samples(params)
# # took ... (8 threads)

params.set_params(coverage = 5, threads = t_count, out_dir = './SNVs_cellnumber_5')
snv_simulator = scs.SNVSimulator(cell_no = 5, snv_no = 100)
snv_simulator.sim_samples(params)
# took 24 min 50 sec (8 threads)

# params.set_params(coverage = 5, threads = t_count, out_dir = './SNVs_cellnumber_10')
# snv_simulator = scs.SNVSimulator(cell_no = 10, snv_no = 100)
# snv_simulator.sim_samples(params)
# took ... (8 threads)