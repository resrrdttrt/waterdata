# run_all.py

# Import the necessary modules
from subprocess import run

# List of scripts to run
scripts = [
    'DataHoThuyDien.py',  # Replace with the actual name of the first script
    'DataHoThuyLoi.py',  # Replace with the actual name of the second script
    'DataLuongMua.py',  # Replace with the actual name of the third script
    'DataMucNuocThuyVan.py'   # Replace with the actual name of the fourth script
]

# Function to run each script
def run_scripts():
    for script in scripts:
        print(f"Running {script}...")
        result = run(['python', script], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

if __name__ == "__main__":
    run_scripts()
