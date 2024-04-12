import blessed
import time
import unittest
import cpuinfo
import psutil

term = blessed.Terminal()

import os
base = os.path.dirname(os.path.abspath(__file__))

import json
with open(os.path.join(base, "tests", "tests.json")) as f:
    test_config = json.load(f)

def get_all_tests(test_suite_or_case, test_list):
    try:
        suite = iter(test_suite_or_case)
    except TypeError:
        test_list.add(test_suite_or_case)
    else:
        for test in suite:
            test_list = test_list | get_all_tests(test, test_list)
    return test_list

print("CPU: " + term.green + cpuinfo.get_cpu_info()["brand_raw"] + term.normal)
if not psutil.sensors_battery() or psutil.sensors_battery().power_plugged:
    print("Power: " + term.green + "Plugged in" + term.normal)
else:
    print("Power: " + term.yellow + "On battery" + term.normal)

print(term.bold + "[*] Starting tests\n-----" + term.normal)

full_total = 0
# get paths of all folders in tests/
test_folders = [os.path.join(base, "tests", folder) for folder in os.listdir(os.path.join(base, "tests")) if os.path.isdir(os.path.join(base, "tests", folder))]
for folder in test_folders:
    os.chdir(folder)
    loader = unittest.TestLoader()
    tests = get_all_tests(loader.discover(start_dir=folder, pattern='*'), set())
    test_total = 0
    x = 0
    y = len(tests)
    print(term.bold + "[*] Running tests from " + term.blue + term.bold(folder.split(os.path.sep)[-1]) + term.normal + term.bold + "... " + term.green + f"({x}/{y})" + term.normal) 
    # run tests
    for test in tests:
        print(term.clear_eol + "\r ┗━ Running " + term.bold + test._testMethodName + term.normal + "...", end="")
        start = time.time()
        test.run()
        end = time.time()
        test_total += end - start
        x += 1
        if x != y:
            print("\r" + term.move_up + term.clear_eol + "\r" + term.bold + "[*] Running tests from " + term.blue + term.bold(folder.split(os.path.sep)[-1]) + term.normal + term.bold + "... " + term.green + f"({x}/{y})" + term.normal)
    print("\r" + term.move_up + term.clear_eol + "\r" + term.bold + "[*] Ran tests from " + term.blue + term.bold(folder.split(os.path.sep)[-1]) + " " + term.green + f"({x}/{y})" + term.normal)
    print(term.clear_eol + "\r ┗━ " + f"Finished in {term.green}{test_total:.3f}s" + term.normal)
    full_total += test_total
    del loader, tests

print(term.bold + "-----\n[*] Ran all tests" + term.normal)
print(f" ┗━ Total time: {term.magenta}{full_total:.3f}s" + term.normal)

