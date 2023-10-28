import argparse
import subprocess
import os

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Run Bazel tests with flexible target selection.")

    # Define the --test-list argument to accept multiple test targets
    parser.add_argument("--test-list", nargs='+', metavar='test_target', help="List of test targets")

    # Parse the command-line arguments
    args, bazel_args = parser.parse_known_args()
    # Collect all Python test files in the specified directories
    test_files = []
    for test_dir in args.test_list:
        if os.path.isdir(test_dir):
            for root, _, files in os.walk(test_dir):
                for file in files:
                    if file.endswith('.py'):
                        test_files.append(file.replace('.py', ''))
    print("test_files:")
    print(test_files)
    if test_files:
        test_targets = ["//:" + target for target in test_files]
        bazel_command = ["bazelisk", "test"] + test_targets + bazel_args + ["--test_output=all"]

        # Run the Bazel command
        print(f"Running command: {' '.join(bazel_command)}")
        try:
            subprocess.run(bazel_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Bazel: {e}")
    else:
        print("Not found unit test files")

if __name__ == "__main__":
    main()

