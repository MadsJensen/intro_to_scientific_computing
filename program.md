# Program: Foundations of data-driven health science

Teaching is in the form of "interactive lectures", where students follow 
instructions to complete specific learning tasks introduced by the lecturers. 

## Teaching days

Monday 11 Sep, Tue 12 Sep, Fri 15 Sep, 2017

## Timetable

Each day from 9 am to 4 pm, with following breaks:

* 10:15 - 10:30
* 12:00 - 12:30 (Lunch)
* 14:14 - 14:30

## Preliminaries

Please install [VirtualBox 5.1](https://www.virtualbox.org/) on your laptop. Choose the download depending on your operating system:
* [Windows](http://download.virtualbox.org/virtualbox/5.1.26/VirtualBox-5.1.26-117224-Win.exe)
* [mac OS](http://download.virtualbox.org/virtualbox/5.1.26/VirtualBox-5.1.26-117224-OSX.dmg)

Optionally, browse through some of these links for inspiration/context.

### [New England Journal of Medicine Catalyst](http://catalyst.nejm.org/about/)

* [Mission statement](http://www.nejm.org/doi/pdf/10.1056/NEJMe1515517)
* [Why Every Health Care Organization Needs a Data Science Strategy](http://catalyst.nejm.org/healthcare-needs-data-science-strategy/)
    * >Of particular importance are “boundary spanners” who can establish links among data science staff, the organization’s management, and its clinicians. They can identify data query priorities that are both organizationally and clinically relevant and can help users of data understand the full range of analysis that is available to them (such as near real-time queries regarding particular patient populations, medications, or treatment outcomes).
* [Data scientists in healthcare](http://catalyst.nejm.org/case-data-scientists-inside-health-care/)
    * >the health care industry does not currently appreciate the inherent value of these data, which can only be fully harnessed through better data analytics.

# Content

[//]: # (Thought: Maybe it would be good to talk about "pipes" as a metaphor for linking functions.)

[//]: # (NB: below is likely to change order when we start writing the exercises!)

## Day 1: The anatomy of a computer and data

* What is "data science"?
    * what _is_ "data"!?
* What is a computer?
    * How are storage and computation achieved in computing devices? Some definitions.
    * Get to know your PC!
* Installing a scientific data-analysis "environment"
    * Linux on VirtualBox
* The Command Line: telling the computer what to do
    * Terminal & Bash
    * the OSEMN model
* Files and file system(s)
    * Textual vs. binary files
    * The PATH (to glory)
* Computer programmes
    * Introduction to variables and data types
    * Interactive development vs. scripts
    
## Day 2: The anatomy and building blocks of a program

* Variable types and manipulations
* Basic control flow
* Functions & arithmetic
* (computing) resources
* Introduction to programming assignment

[//]: # (General: assessment of resource usage associated with task/variable)

## Day 3: Programming to gain insight into data

* Data 'munging/scrubbing'
* Efficient manipulation of large textual data blocks
* Examples and suggestions for further study

[//]: # (Programming language choices, resources, visualisation, stats)

### Assignment: extracting information from log files

(_Brief description:_) We have generated a synthetic dataset based on a published study (Luck _et al., 2009)_ comparing reaction times (RT) of schizophrenic patients to those of normal controls, while the subjects were performing a particular task (details not relevant). The dataset consists of 40 log files (20 for each group), each a couple of thousand lines long. __Write a program__ to "parse" the 40 log files to extract median RT and accuracy values, and write out a single CSV file like this

|Subjid|Group|Cond|Median|Accuracy|
|:---:|:---:|---|---|---|
|{str}|Patient/Control|Freq/Rare|{float}|{float}|
|...|...|...|...|...|

Also write out summary stats for median and accuracy values, separately for each group and condition. Compare these to the results in the paper (Table 3).
