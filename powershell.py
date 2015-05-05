import subprocess, sys

class IISPowerShell:
    def run(script):
        """Run a PowerShell Script

        :param str script: path to script
        """

        p = subprocess.Popen(["powershell.exe", script], stdout=sys.stdout)
