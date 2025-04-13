#command line automation

import os

#resp = os.system('fhgfgf')

#if resp == 0:
#    print("successfulyy executed")
#else:
#    print("failed to execute")


def run_command(cmd):
    try:
        resp = os.system(cmd)
        if resp == 0:
            print("successfully executed")
        else:
            print("failed to execute")
    except Exception as e:
        raise Exception ("failed to exceute: exception occured")
    
run_command("sdhfkdhf")
