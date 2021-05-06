import coverage

if __name__ == "__main__":
    cov = coverage.Coverage(source=["src"])
    cov.erase()
    cov.set_option("run:relative_files", True)
    cov.start()
    from src import foo
    foo.bar()
    cov.stop()
    cov.xml_report(outfile="cov_sdk.xml")