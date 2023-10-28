load("@rules_python//python:defs.bzl", "py_test")

def run_tests(test_list):
    # Create a list of py_test targets based on the test_list
    py_test_targets = []
    for test_file_path in test_list:
        # Extract the file name from the path
        test_file = test_file_path.split("/")[-1]
        target_name = test_file.replace(".py", "")
        py_test_targets.append(
            py_test(
                name = target_name,
                srcs = [test_file_path],
            )
        )
    return py_test_targets
