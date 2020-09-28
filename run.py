from anadama2 import Workflow
from anadama2.tracked import TrackedExecutable
import configparser
import os

#Loading the config setting
config = configparser.ConfigParser()
config.read('etc/config.ini')

workflow = Workflow(version="0.0.1", description="Analysis Template")
workflow = Workflow(remove_options=["input","output"])
# Setting the custom arguments for run.py
workflow.add_argument(name="lines", desc="Number of lines to trim [default: 10]", default=10)
args = workflow.parse_args()

# Task0 sample python analysis module  - src/trim.py
workflow.add_task(
    config['task0']['cmd']+" --input "+config['task0']['input']+" --output [targets[0]] --lines [args[0]]",
    depends=[TrackedExecutable(config['task0']['cmd'])],
    targets=config['task0']['output'],
    args=[args.lines])

# Task1 sample python visualization module - src/plot.py
workflow.add_task(
    config['task1']['cmd']+" --input " +config['task1']['input']+" --output [targets[0]]", 
    depends=[TrackedExecutable(config['task1']['cmd'])],
    targets=config['task1']['output'])

# # Task2 sample R module  - src/analysis_example.r
workflow.add_task(
    config['task2']['cmd']+" -d "+config['task2']['input']+" -o [targets[0]]", 
    depends=[TrackedExecutable(config['task2']['cmd'])],
    targets=config['task2']['output'])

# Setting the values for the pdf reports
document_file = os.path.dirname(os.path.abspath(__file__))+config['report']['name']
document_vars = {"title":"Demo Analysis Report",
        "project":"Demo Analysis",
        "introduction_text":"This is a demo report.",
        "output":config['task0']['output']
      }
# Add the document to the workflow
workflow.add_document(
    templates=[config['report']['template']],
    targets=document_file,
    vars=document_vars)

# Run the workflow
workflow.go()