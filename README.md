# Getting your course wise schedule from the PDF published on NSU Website
###### Just run it!

### How it works?

- [x] Uses PyPDF2 module to read all the text in the PDF file
- [x] Then a brute force algorithm that searches the entire file, all the text, one by one.
- [x] Search params : courseID and section number. Apparently that's what you use to look for right?
- [x] If your course is found, will return courseID, section, date, time and room number of exam
- [x] Since a brute force algorithm runs in, it's slow. It was a quick hack, so no optimization. (You can if you want,
    contributions are welcome!)

### Usage

- [x] Clone the repo or download as a zip
- [x] Get into the folder
    `cd "Final Exam Schedule Getter" `
- [x] Then run the following command in your command line to make sure you have the necessary modules ready(skip if you
    already know how to get modules from a requirements file)

    `pip install -r requirements.txt`
     (If you're using anaconda then instead of pip,
     use [this shell script to do things](https://gist.github.com/ShawonAshraf/1ee95026b80838d3f51776a5bdfcd2d4))

     **However** if you're on Windows, shell scripts are of no use. so run this to install the module directly

     - `conda install -c conda-forge pypdf2=1.26.0`

- [x] Then navigate to sources folder
    `cd sources`

- [x] Run the Python script :
    `python schedule_getter.py [params]`
    params are : your courseId and section, separated by a space

    __Example :__
    `python schedule_getter.py CSE327 3 CSE418 1 CSE323 2 PHY108 3`

    **Make sure courseID has no space in it, e.g. typing CSE 327 instead of CSE327 is an error here**
