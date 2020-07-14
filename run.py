from anadama2 import Workflow
from anadama2.tracked import TrackedExecutable

workflow = Workflow(version="0.0.1", description="Analysis Template")
# Setting the custom arguments for run.py
workflow.add_argument(name="lines", desc="Number of lines to trim [default: 10]", default=10)
workflow.add_argument(name="sample-metadata", desc="Sample metadata for R analysis [default: input/data/metadata.tsv]", default="input/demo_r/input/metadata.tsv")
args = workflow.parse_args()

# sample python analysis module task0 - input/src/trim.py
workflow.add_task(
    "[depends[0]] --input [depends[1]] --output [targets[0]] --lines [args[0]]", 
    depends=[TrackedExecutable("trim.py"),args.input],
    targets=[args.output+"example/output_table.tsv"],
    args=[args.lines])

# sample python plots module task1 -- input/src/plot.py
# workflow.add_task(
#     "[depends[0]] --input [depends[1]] --output [targets[0]] --lines [args[0]]", 
#     depends=[TrackedExecutable("plot.py"),args.input],
#     targets=[args.output+"example"])


# sample R module task2 
# workflow.add_task(
#     "[depends[0]] --input [depends[1]] --output [targets[0]] --lines [args[0]]", 
#     depends=[TrackedExecutable("plot.py"),args.input],
#     targets=[args.output+"example"])
# workflow.add_task("Rscript input/demo_r/src/analysis_example.r -d "+args.sample_metadata+" -o "+args.output+"/r_output_table.tsv")

# Generate the pdf report from private analysis 
# document_file = workflow.name_output_files("report.pdf")
# document_vars = {"title":"Demo Analysis Report",
#         "project":"Demo Analysis",
#         "introduction_text":"This is a demo report."
#       }

# workflow.add_document(
#     templates=["template.py"],
#     targets=document_file,
#     vars=document_vars)

workflow.go()

