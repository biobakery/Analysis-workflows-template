from anadama2 import Workflow
from anadama2.tracked import TrackedExecutable

# Setting the version of the workflow and short description
workflow = Workflow(
    version="0.0.1",                    #Update the version as needed
    description="Analysis Template"     #Update the description as needed
    ) 

# Setting the custom arguments for run.py
workflow.add_argument(
    name="lines", 
    desc="Number of lines to trim [default: 10]", 
    default=10)

# Parsing the workflow arguments
args = workflow.parse_args()

#Loading the config setting
args.config = 'etc/config.ini'

# Task0 sample python analysis module  - src/trim.py
workflow.add_task(
    args.config['task0']['cmd']+" --input "+args.input+" --output [targets[0]] --lines [args[0]]",
    depends=[TrackedExecutable(args.output)],
    targets=args.output,
    args=[args.lines])

# Task1 sample python visualization module - src/plot.py
workflow.add_task(
    args.config['task1']['cmd']+" --input " +args.input+" --output [targets[0]]", 
    depends=[TrackedExecutable(args.output)],
    targets=args.output)

# Task2 sample R module  - src/analysis_example.r
workflow.add_task(
    args.config['task2']['cmd']+" -d "+args.config['task2']['metadata']+" -o [targets[0]]", 
    depends=[TrackedExecutable(args.output)],
    targets=args.output)

# Add the document to the workflow
workflow.add_document(
    templates=[args.config['report']['template']],
    targets=args.config['report']['document_file'],
    vars={
        title: args.config['report']['title'],
        project: args.config['report']['project'],
        introduction_text: args.config['report']['introduction_text']
    })

# Run the workflow
workflow.go()