# Bring your packages onto the path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme

add_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
add_json = open("src/json/in/add.json")
pr = problem_scheme.Problem.json_decode_f(add_json)
''' 
add_run_pr_str = '''
pr.run_iterative()
'''

add_complex_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
add_json = open("src/json/in/add_complex.json")
pr = problem_scheme.Problem.json_decode_f(add_json)
''' 
add_complex_run_pr_str = '''
pr.run_iterative()
'''

mult_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
mult_json = open("src/json/in/mult.json")
pr = problem_scheme.Problem.json_decode_f(mult_json)
''' 
mult_run_pr_str = '''
pr.run_iterative()
'''
mult_complex_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
mult_json = open("src/json/in/mult_complex.json")
pr = problem_scheme.Problem.json_decode_f(mult_json)
''' 
mult_complex_run_pr_str = '''
pr.run_iterative()
'''

quot_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
quot_json = open("src/json/in/quot.json")
pr = problem_scheme.Problem.json_decode_f(quot_json)
''' 
quot_run_pr_str = '''
pr.run_iterative()
'''

quot_complex_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
quot_json = open("src/json/in/quot_complex.json")
pr = problem_scheme.Problem.json_decode_f(quot_json)
''' 
quot_complex_run_pr_str = '''
pr.run_iterative()
'''

rem_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
rem_json = open("src/json/in/rem.json")
pr = problem_scheme.Problem.json_decode_f(rem_json)
''' 
rem_run_pr_str = '''
pr.run_iterative()
'''

rem_complex_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
rem_json = open("src/json/in/rem_complex.json")
pr = problem_scheme.Problem.json_decode_f(rem_json)
''' 
rem_complex_run_pr_str = '''
pr.run_iterative()
'''

sub_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
sub_json = open("src/json/in/sub.json")
pr = problem_scheme.Problem.json_decode_f(sub_json)
''' 
sub_run_pr_str = '''
pr.run_iterative()
'''

sub_complex_setup_pr_str = '''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
sub_json = open("src/json/in/sub_complex.json")
pr = problem_scheme.Problem.json_decode_f(sub_json)
''' 
sub_complex_run_pr_str = '''
pr.run_iterative()
'''


import timeit
import numpy as np
num_runs = 100
num_repetions = 3
#add
duration = timeit.Timer(stmt=add_run_pr_str, setup=add_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=add_run_pr_str, setup=add_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the add problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

duration = timeit.Timer(stmt=add_complex_run_pr_str, setup=add_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=add_complex_run_pr_str, setup=add_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the add_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')
#mult
duration = timeit.Timer(stmt=mult_run_pr_str, setup=mult_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=mult_run_pr_str, setup=mult_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the mult problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

duration = timeit.Timer(stmt=mult_complex_run_pr_str, setup=mult_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=mult_complex_run_pr_str, setup=mult_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the mult_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')
#quot
duration = timeit.Timer(stmt=quot_run_pr_str, setup=quot_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=quot_run_pr_str, setup=quot_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the quot problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

duration = timeit.Timer(stmt=quot_complex_run_pr_str, setup=quot_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=quot_complex_run_pr_str, setup=quot_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the quot_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')
#rem
duration = timeit.Timer(stmt=rem_run_pr_str, setup=rem_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=rem_run_pr_str, setup=rem_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the rem problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

duration = timeit.Timer(stmt=rem_complex_run_pr_str, setup=rem_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=rem_complex_run_pr_str, setup=rem_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the rem_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')
#sub
duration = timeit.Timer(stmt=sub_run_pr_str, setup=sub_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=sub_run_pr_str, setup=sub_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the sub problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

duration = timeit.Timer(stmt=sub_complex_run_pr_str, setup=sub_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=sub_complex_run_pr_str, setup=sub_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
avg_duration = duration/num_runs
print(f'On average the sub_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')