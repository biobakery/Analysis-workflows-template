from anadama2 import Workflow
from anadama2.tracked import TrackedExecutable

workflow = Workflow(version="0.0.1", description="Analysis Template")
# Setting the custom arguments for run.py
workflow.add_argument(name="lines", desc="Number of lines to trim [default: 10]", default=10)
workflow.add_argument(name="sample-metadata", desc="Sample metadata for R analysis [default: input/metadata.tsv]", default="input/metadata.tsv")
args = workflow.parse_args()

# sample python analysis module task0 - input/src/trim.py
workflow.add_task(
    "python src/trim.py --input input/data.tsv --output [targets[0]] --lines [args[0]]", 
    depends=[args.input],
    targets=args.output+"output_table.tsv",
    args=[args.lines])

# sample python visualization module task0 - input/src/trim.py
workflow.add_task(
    "python src/plot.py --input example/output/output_table.tsv --output [targets[0]]", 
    depends=[args.input],
    targets=args.output,
    args=[args.lines])

# sample R module task2 
workflow.add_task(
    "Rscript src/analysis_example.r -d "+args.sample_metadata+" -o [targets[0]]", 
    depends=[args.input],
    targets=[args.output+"/r_output_table.tsv"])

# Generate the pdf report from private analysis 
document_file = workflow.name_output_files("report.pdf")
document_vars = {"title":"Demo Analysis Report",
        "project":"Demo Analysis",
        "introduction_text":"This is a demo report.",
        "output":"example/output/output_table.tsv"
      }

workflow.add_document(
    templates=["src/template.py"],
    targets=document_file,
    vars=document_vars)

workflow.go()

