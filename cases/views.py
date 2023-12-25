import requests
import subprocess

def reindex_files(case_id):
    url = f"http://127.0.0.1:5000/q/reindex_dossier/{case_id}"
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        # Construct the curl command
        curl_command = [
            'curl',
            '-X', 'POST',
            url,
            '-H', f'Content-Type: {headers["Content-Type"]}',
        ]

        # Execute the curl command
        subprocess.run(curl_command, check=True)

        # If the subprocess.run doesn't raise an exception, it means the curl command was successful
        print(f"Files for Case {case_id} reindexed successfully")
    except subprocess.CalledProcessError as e:
        # Handle the case where the curl command returns a non-zero exit code
        print(f"Error from external endpoint: {e.returncode}")