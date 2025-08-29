
# Instructions to Run the Script and Install Required Packages

## Step 1: Install Python
Make sure Python is installed on your system. You can download Python from [python.org](https://www.python.org/).

## Step 2: Install Required Packages
Open a terminal or command prompt in the directory containing the files and run the following command:
bash python install_requirements.py

This will automatically install all the required Python packages listed in `requirements.txt`.

## Step 3: Run Your Script
After installing the dependencies, you can run your script using:
bash python your_script_name.py


## Notes:
- Ensure that Python and pip are added to your system's PATH.
- For best practices, you may create a virtual environment:
  bash python -m venv myenv
  source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
  python install_requirements.py
