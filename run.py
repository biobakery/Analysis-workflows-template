from anadama2 import Workflow
import subprocess

def execute_r(path2script):
    command = "Rscript"
    # Variable number of args in a list
    args = []
    # Build subprocess command
    cmd = [command, path2script]+args

    # check_output will run the command and store to result
    x = subprocess.check_output(cmd, universal_newlines=True)


workflow = Workflow(remove_options=["input"])

# Uncomment for R analysis
# execute_r("src/User_analysis/R/rAnalysis.R")


# Generate the pdf report from private analysis 
doc_task = workflow.add_document(
    templates="src/User_analysis/Python/pythonAnalysis.R",
    targets="output/pythonAnalysis.pdf",
    vars={"title": "<Put Study Title of the Analysis Here>",
          "project": "Demo Project",
          "introduction_text": "Introduction Text PlaceHolder"})
workflow.go()
