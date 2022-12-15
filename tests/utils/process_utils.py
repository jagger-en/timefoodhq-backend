import subprocess


def run_command(cmd):
    result = subprocess.check_output(cmd)
    return result
