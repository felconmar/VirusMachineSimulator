# Bring your packages onto the path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme

common_setup_str = '''
import sys
import os
from random import randint
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import data_structure, problem_scheme
'''

common_run_pr_str = '''
pr.run_iterative()
'''



common_3_digit = '''
hosts = pr.get_hosts()
hosts["h1"].set_virus(randint(100, 999))
hosts["h2"].set_virus(randint(100, 999))
pr.set_hosts(hosts)
'''

common_6_digit = '''
hosts = pr.get_hosts()
hosts["h1"].set_virus(randint(100000, 999999))
hosts["h2"].set_virus(randint(100000, 999999))
pr.set_hosts(hosts)
'''

add_setup_pr_str = common_setup_str + '''
add_json = open("src/json/in/add.json")
pr = problem_scheme.Problem.json_decode_f(add_json)
''' 

add_complex_setup_pr_str = common_setup_str + '''
add_json = open("src/json/in/add_complex.json")
pr = problem_scheme.Problem.json_decode_f(add_json)
''' + common_3_digit

add_complex_2_setup_pr_str = common_setup_str + '''
add_json = open("src/json/in/add_complex_2.json")
pr = problem_scheme.Problem.json_decode_f(add_json)
''' + common_6_digit

mult_setup_pr_str = common_setup_str + '''
mult_json = open("src/json/in/mult.json")
pr = problem_scheme.Problem.json_decode_f(mult_json)
''' 

mult_complex_setup_pr_str = common_setup_str + '''
mult_json = open("src/json/in/mult_complex.json")
pr = problem_scheme.Problem.json_decode_f(mult_json)
''' + common_3_digit

mult_complex_2_setup_pr_str = common_setup_str + '''
mult_json = open("src/json/in/mult_complex_2.json")
pr = problem_scheme.Problem.json_decode_f(mult_json)
hosts = pr.get_hosts()
hosts["h1"].set_virus(randint(100000, 999999))
hosts["h2"].set_virus(randint(10, 99))
pr.set_hosts(hosts)
'''

quot_setup_pr_str = common_setup_str + '''
quot_json = open("src/json/in/quot.json")
pr = problem_scheme.Problem.json_decode_f(quot_json)
''' 

quot_complex_setup_pr_str = common_setup_str + '''
quot_json = open("src/json/in/quot_complex.json")
pr = problem_scheme.Problem.json_decode_f(quot_json)
''' + common_3_digit

quot_complex_2_setup_pr_str = common_setup_str + '''
quot_json = open("src/json/in/quot_complex_2.json")
pr = problem_scheme.Problem.json_decode_f(quot_json)
''' + common_6_digit

rem_setup_pr_str = common_setup_str + '''
rem_json = open("src/json/in/rem.json")
pr = problem_scheme.Problem.json_decode_f(rem_json)
''' 

rem_complex_setup_pr_str = common_setup_str + '''
rem_json = open("src/json/in/rem_complex.json")
pr = problem_scheme.Problem.json_decode_f(rem_json)
''' + common_3_digit

rem_complex_2_setup_pr_str = common_setup_str + '''
rem_json = open("src/json/in/rem_complex_2.json")
pr = problem_scheme.Problem.json_decode_f(rem_json)
''' + common_6_digit

sub_setup_pr_str = common_setup_str + '''
sub_json = open("src/json/in/sub.json")
pr = problem_scheme.Problem.json_decode_f(sub_json)
''' 

sub_complex_setup_pr_str = common_setup_str + '''
sub_json = open("src/json/in/sub_complex.json")
pr = problem_scheme.Problem.json_decode_f(sub_json)
''' + common_3_digit

sub_complex_2_setup_pr_str = common_setup_str + '''
sub_json = open("src/json/in/sub_complex_2.json")
pr = problem_scheme.Problem.json_decode_f(sub_json)
''' + common_6_digit


import timeit
import numpy as np
num_runs = 1
num_repetions = 100
#add
#duration = timeit.Timer(stmt=common_run_pr_str, setup=add_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=add_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the add problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

#duration = timeit.Timer(stmt=common_run_pr_str, setup=add_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=add_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the add_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

ex_time = timeit.Timer(stmt=common_run_pr_str, setup=add_complex_2_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
print(f'On average the add_complex_2 problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

#quot
#duration = timeit.Timer(stmt=common_run_pr_str, setup=quot_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=quot_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the quot problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

#duration = timeit.Timer(stmt=common_run_pr_str, setup=quot_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=quot_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the quot_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')


ex_time = timeit.Timer(stmt=common_run_pr_str, setup=quot_complex_2_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
print(f'On average the quot_complex_2 problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

#rem
#duration = timeit.Timer(stmt=common_run_pr_str, setup=rem_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=rem_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the rem problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

#duration = timeit.Timer(stmt=common_run_pr_str, setup=rem_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=rem_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the rem_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

ex_time = timeit.Timer(stmt=common_run_pr_str, setup=rem_complex_2_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
print(f'On average the rem_complex_2 problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

#sub
#duration = timeit.Timer(stmt=common_run_pr_str, setup=sub_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=sub_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the sub problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

#duration = timeit.Timer(stmt=common_run_pr_str, setup=sub_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=sub_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the sub_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

ex_time = timeit.Timer(stmt=common_run_pr_str, setup=sub_complex_2_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
print(f'On average the sub_complex_2 problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

#mult
#duration = timeit.Timer(stmt=common_run_pr_str, setup=mult_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=mult_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the mult problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

#duration = timeit.Timer(stmt=common_run_pr_str, setup=mult_complex_setup_pr_str).timeit(number = num_runs)
ex_time = timeit.Timer(stmt=common_run_pr_str, setup=mult_complex_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
#avg_duration = duration/num_runs
print(f'On average the mult_complex problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')

ex_time = timeit.Timer(stmt=common_run_pr_str, setup=mult_complex_2_setup_pr_str).repeat(repeat=num_repetions, number =num_runs)
print(f'On average the mult_complex_2 problem took {np.sum(np.divide(ex_time,num_runs))/num_repetions} seconds')
