from anadama2 import Workflow
import subprocess

def r_to_python():
    command = "Rscript"
    path2script = "src/User_analysis/R/rAnalysis.R"

    # Variable number of args in a list
    args = []
    # Build subprocess command
    cmd = [command, path2script]+args

    # check_output will run the command and store to result
    x = subprocess.check_output(cmd, universal_newlines=True)


workflow = Workflow(remove_options=["input"])
r_to_python()
doc_task = workflow.add_document(
    templates="src/User_analysis/Python/pythonAnalysis.py",
    targets="/Users/sam1389/Desktop/pythonAnalysis.pdf",
    vars={"title": "<Put Study Title of the Analysis Here>",
          "project": "Demo Project",
          "introduction_text": "Introduction Text PlaceHolder"})
workflow.go()
