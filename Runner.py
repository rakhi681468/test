from robot import run
import os


def execute_tests():
    testcase_path = "TestSuite.robot"
    status = run(testcase_path, listener="allure_robotframework")
    # status = run.run(testcase_path, listener = "allure_robotframework")
    return status

def list_files():
    files = os.listdir(os.curdir)
    print(files)
    files = os.listdir('output')
    print(files)
    files = os.listdir('output/allure')
    print(files)


execute_tests()
list_files()
