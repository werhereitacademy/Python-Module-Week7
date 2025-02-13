import sys  # Import the 'sys' module, which provides access to system-specific parameters and functions.
import os   # Import the 'os' module, which provides a way to interact with the operating system (e.g., file paths, directories).

# Get the absolute path of the 'PyBackend' folder by joining the directory of the current file with 'PyBackend'.
pybackend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "PyBackend"))

# Add the 'PyBackend' folder path to the system path so that Python can locate and import modules from it.
sys.path.append(pybackend_path)

# Import the 'login_b' module from the 'PyBackend' folder.
import login_b

# Check if this script is being run as the main program (not imported as a module).
if __name__ == "__main__":
    # Call the 'start_login_app' function from the 'login_b' module to start the login application.
    login_b.start_login_app()