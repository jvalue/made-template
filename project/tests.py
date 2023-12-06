import subprocess
import os

def test_system():
    # Run the data pipeline
    subprocess.run(["python", "parking.py"])

    # Validate the output files
    output_directory = "data"
    if os.path.exists(output_directory) and os.path.isdir(output_directory):
        print("Output directory exists.")

        # Check if there are any files in the output directory
        output_files = os.listdir(output_directory)
        if output_files:
            print("Output files exist. System test passed.")
        else:
            print("No output files found. System test failed.")
            assert False  # Raise an AssertionError for test failure
    else:
        print("Output directory does not exist. System test failed.")
        assert False  # Raise an AssertionError for test failure

if __name__ == "__main__":
    test_system()
