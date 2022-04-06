import os
import tarfile

from robot import run


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


def tardir(path, tar_name):
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))
    tar_handle.close()


execute_tests()
tardir('output', 'sample.tar.gz')
list_files()

