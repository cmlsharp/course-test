import check50

@check50.check()
def rustc_available():
    check50.run("cargo --version").exit(0)

