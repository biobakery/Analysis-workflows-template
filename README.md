##### [Replace the contents this README.MD file with the appropriate "Users manual" needed for the workflow.]  
   
# Private Analysis Workflows Template

## Introduction

> This page gives details concerning guiding principles and formatting required for private analysis workflows and reproducing papers. 

## Requirements
- #### Git and Github accounts
    Follow this installation guide [HERE](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install Git in your local machine. Additionally, direct to Github [sign up](https://github.com/join?source=header-home) page if you do not have the account. 

- #### Python(version>2.7 or >3.0)
     
## Installation

> Getting started with the Analysis Workflow Template: 
- Direct to [Analysis-workflow-template](https://github.com/biobakery/Analysis-workflows-template) github page. 
- Click on "**Use this Template**" button and fill out the new repository informations (name/description/access). 
- Finally click on "**Create repository from template**" and you now have a new repository based on the Analysis workflow Template following the standard layouts. 

Alternatively, 
- Direct to [Github Create New Repository](https://github.com/organizations/biobakery/repositories/new) and select the "**biobakery/Analysis-workflows-template**". Fill out other information (Repository name/description/access)
- Finally click on "**Create repository**" and you now have a new repository based on the Private Analysis workflow template. 

**NOTE**: Make your repository "**Private**" unless it is ready to be released publicly.

## Getting started with a private analysis workflow 
### Setting up local development environment
- Clone your recently created repository in your local development environment either using:
    ``` 
        git clone https://github.com/biobakery/<Name of your repository>
    ```
    or using the "**Clone or Download**" button. 
- Install all the requirements for the workflow.
    ```
    pip install -r requirements.txt
    ```
- Install pdflatex for PDF report generation of the Python/R analysis. 
    ``` 
    brew cask install basictex - for pdf generation
    ```
### Running the workflow
Use the `-o` flag to set the path of the output files. 
``` 
python3 run.py -o output/    
```