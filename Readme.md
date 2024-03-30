##### [Replace the contents this README.MD file with the appropriate "Users manual" needed for the workflow.]

# Private Analysis Workflows Template


#### Introduction
> This page gives details concerning guiding principles and formatting required for private analysis workflows and reproducing papers.


#### Directory Structure

- The `run.py` is the configurable `Anadama2 workflow` example file showing the initialization, creation, addition of the workflow tasks of Python and R modules including its PDF report generation.

- The `/input` directory contains the sample input files and Python/R analysis modules. Each of the python analysis should be a standalone command line executable module. In the example file, the module is packaged using `ArgumentParser`

- The `/doc` directory contains the documentation usage on the executable modules and the template for the report generation.

- The `/pregenerated-output` directory contains all the example output files generated by the template. The `anadama.log` are included in the `output` directory after a run.

- The `etc/config.ini` directory contains the default config setting for the template demo run. Feel free to change the settings based on the workflow use case.

- The src directory is the main source directory for all the `python/R analysis` executables for the workflow.



#### Requirements

- ##### Git and Github accounts

Follow this installation guide [HERE](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install Git in your local machine. Additionally, direct to Github [sign up](https://github.com/join?source=header-home) page if you do not have the account.

- ##### Python(version>2.7 or >3.0)

- ##### R version 3.6.3

#### Installation

> Getting started with the Analysis Workflow Template:

- Direct to [Analysis-workflow-template](https://github.com/biobakery/Analysis-workflows-template) github page.

- Click on "**Use this Template**" button and fill out the new repository informations (name/description/access).

- Finally click on "**Create repository from template**" and you now have a new repository based on the Analysis workflow Template following the standard layouts.


Alternatively,

- Direct to [Github Create New Repository](https://github.com/organizations/biobakery/repositories/new) and select the "**biobakery/Analysis-workflows-template**". Fill out other information (Repository name/description/access)

- Finally click on "**Create repository**" and you now have a new repository based on the Private Analysis workflow template.

  

**NOTE**: Make your repository "**Private**" unless it is ready to be released publicly.

  

##  Demo a private analysis workflow

  
####  Cloning Repo
  

- Clone your recently created repository in your local development environment either using:
```
git clone https://github.com/biobakery/<Name of your repository>
```
or using the "**Clone or Download**" button.

##### Usage:

##### Converting Python and R analysis source code to the executables:
```
Add the following line at the top of the file.
Python: `#!/usr/local/bin/python3`
R: `#!/usr/bin/env Rscript`
```

##### Demo Run:
```
python run.py --input input/data.tsv --output output --lines 10 --metadata input/metadata.tsv 
```
```python run.py --help```

```
usage: run.py [-h] [--version] [--lines LINES]
[--sample-metadata SAMPLE_METADATA] -o OUTPUT [-i INPUT]
[--config CONFIG] [--local-jobs JOBS] [--grid-jobs GRID_JOBS]
[--grid GRID] [--grid-partition GRID_PARTITION]
[--grid-benchmark {on,off}] [--grid-options GRID_OPTIONS]
[--grid-environment GRID_ENVIRONMENT]
[--grid-scratch GRID_SCRATCH] [--dry-run] [--skip-nothing]
[--quit-early] [--until-task UNTIL_TASK]
[--exclude-task EXCLUDE_TASK] [--target TARGET]
[--exclude-target EXCLUDE_TARGET]
[--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
```
#### Configuration:

The `etc/config.ini` directory contains the default configuration setting for the template demo run. Feel free to change the settings based on the workflow use case.

  

#### Document Report Generation:

The `docs/template.py` is a sample Pweave example template (Markdown + Python) for the PDF report generation of the existing tasks/Python/R modules.

## Gcloud VM build + Workshop Tutorial
https://github.com/biobakery/biobakery/wiki/biobakery_advanced#5-build-biobakery-google-cloud
