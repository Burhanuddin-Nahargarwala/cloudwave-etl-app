import os
import subprocess

def test_script_runs_and_creates_output():
    """Integration test to ensure the main script executes and produces a file."""
    # Define the output file path relative to the script's location
    output_file = "output/processed_users.csv"

    # If the output file exists from a previous run, remove it
    if os.path.exists(output_file):
        os.remove(output_file)

    # Run the ETL script as a separate process
    # We use python -u for unbuffered output to see prints immediately
    result = subprocess.run(["python", "-u", "etl_script.py"], capture_output=True, text=True)
    
    # Check that the script ran successfully (exit code 0)
    assert result.returncode == 0, f"Script failed with error: {result.stderr}"
    
    # Check that the script printed the completion message
    assert "ETL process complete!" in result.stdout
    
    # Check that the output file was actually created
    assert os.path.exists(output_file)