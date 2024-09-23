# Code to initialize debugger in container in case of DEBUG environment variable is set to True
# Extracted from blog entry https://lightrun.com/how-to-perform-python-remote-debugging/
from os import getenv


def initialize_debugger():
    if getenv("DEBUG") == "True":
        import multiprocessing

        if multiprocessing.current_process().pid > 1:
            import debugpy

            debugpy.listen(("0.0.0.0", 9000))
            print("Debugger is ready to be attached, press F5", flush=True)
            debugpy.wait_for_client()
            print("Visual Studio Code debugger is now attached", flush=True)
