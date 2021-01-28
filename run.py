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
    "trim.py --input [args.input] --output [args.targets[0]] --lines [args[0]]",
    depends=[TrackedExecutable("trim")],
    targets="output_table.tsv",
    args=[args.lines])

# Task1 sample python visualization module - src/plot.py
workflow.add_task(
    "plot.py --input [args.input] --output [args.output]", 
    depends=[TrackedExecutable("plot")],
    targets=args.output)

# Task2 sample R module  - src/analysis_example.r
workflow.add_task(
    "analysis.R -d [args.config['task2']['metadata']] -o [args.targets[0]]", 
    depends=[TrackedExecutable("analysis")],
    targets="r_output_table.tsv")

# Task3 add_task_group  - AnADAMA2 example to execute a task on multiple input files/dependencies
workflow.add_task_group('cp [args.input] [args.output]',
    depends=[TrackedExecutable("cp")],
    targets=args.output)

# Task4 add_task  - AnADAMA2 example to usage of python task function 
workflow.add_task(
    remove_end_tabs_function,
    depends="r_output_table.tsv",
    targets="r_output_table.tsv.notabs",
    name="remove_end_tabs")

# Task5 add_task  - AnADAMA2 example workflow.do
workflow.do("ls /usr/bin/ | sort > [t:global_exe.txt]")
workflow.do("ls $HOME/.local/bin/ | sort > [t:local_exe.txt]")
workflow.do("join [d:global_exe.txt] [d:local_exe.txt] > [t:match_exe.txt]")

# Add the document to the workflow
workflow.add_document(
    templates=[args.config['report']['template']],
    targets=args.config['report']['document_file'],
    vars={
        title: args.config['report']['title'],
        project: args.config['report']['project'],
        introduction_text: args.config['report']['introduction_text']
    })

def remove_end_tabs_function(task):
    with open(task.targets[0].name, 'w') as file_handle_out:
        for line in open(task.depends[0].name):
            file_handle_out.write(line.rstrip() + "\n")

# Run the workflow
workflow.go()