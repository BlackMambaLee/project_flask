import subprocess

def hostname_call():
    return subprocess.check_output(["hostname"])