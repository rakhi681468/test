from robot import run


def execute_tests():
    testcase_path = "TestSuite.robot"
    status = run(testcase_path, listener="allure_robotframework")
    # status = run.run(testcase_path, listener = "allure_robotframework")
    return status


execute_tests()
