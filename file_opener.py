def run(runfile):
    with open(runfile,"r") as rnf:
        exec(rnf.read())


#run("python_copy_of_main.py")