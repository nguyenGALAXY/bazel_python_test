load(":run_tests.bzl", "run_tests")

TEST_LIST = (
    glob(["unit/*.py"]) +
    glob(["lib_test/*.py"]) +
    glob(["lib_test/test_cal/*.py"])
)

run_tests(
    test_list = TEST_LIST,
)
