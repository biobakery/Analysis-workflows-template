from anadama2 import Workflow

workflow = Workflow(remove_options=["input"])
workflow.do("ls /usr/bin/ | sort > [t:global_exe.txt]")
doc_task = workflow.add_document(
    templates="src/User_analysis/Python/pythonAnalysis.py",
    targets="sample.pdf",
    vars={"title": "Demo Title",
              "project": "Demo Project",
              "targets": "analysis_document.pdf",
              "introduction_text": "This is a demo document."})
workflow.go()
