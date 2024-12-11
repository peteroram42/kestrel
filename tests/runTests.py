
from .unitTests import run_unit_tests
from .integTests import run_integ_tests

def run_all_tests(mode="silent"):
    if mode == "debug":
        print("Entering debug mode...")

    if run_unit_tests(mode) and run_integ_tests(mode):
        return True
    else:
        return False