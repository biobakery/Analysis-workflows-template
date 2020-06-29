from anadama2 import Workflow


workflow = Workflow(version="0.0.1", description="Analysis Template")
# Setting the custom arguments for run.py
workflow.add_argument(name="lines", desc="Number of lines to trim [default: 10]", default=10)
workflow.add_argument(name="sample-metadata", desc="Sample metadata for R analysis [default: input/demo_r/input/metadata.tsv]", default="input/demo_r/input/metadata.tsv")
args = workflow.parse_args()

# sample python analysis module task0 - input/demo_python/src/trim.py
workflow.add_task("python input/demo_python/src/trim.py --input "+args.input+" --output "+args.output+"/output_table.tsv --lines 10")

# sample python plots module task1 -- input/demo_python/src/plot.py
workflow.add_task("python input/demo_python/src/plot.py --input "+args.input+" --output "+args.output)

# sample R module task2 
workflow.add_task("Rscript input/demo_r/src/analysis_example.r -d "+args.sample_metadata+" -o "+args.output+"/r_output_table.tsv")

# Generate the pdf report from private analysis 
# document_file = workflow.name_output_files("report.pdf")
# document_vars = {"title":"Teddy Analysis Report",
#         "project":"Teddy Analysis",
#         "introduction_text":"This is a demo report.",
#         "file_model_output":model_output
#       }

# workflow.add_document(
#     templates=["template.py"],
#     targets=document_file,
#     vars=document_vars)

workflow.go()

