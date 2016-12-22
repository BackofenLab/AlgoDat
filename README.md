# Algorithms and Data Structures 

This course comprises of a 2 SWS lecture and a 2 SWS exercise class in English, generally for Bachelor students (ESE und IEMS). 

This repository stores the source code that is required for the Algorithms and Data Structures course containing source code and images for the lecture and the exercises. Each semester, the people responsible for teaching a course usually want to modify and personalize the existing teaching material. In the past this has been an extremely painful and error-prone process. This repository should help with keeping track of "bug fixes" and personal modifications to make life easier for future teaching tasks. Our [teaching webpage](http://www.bioinf.uni-freiburg.de/Lehre/index.html?en) contains all compiled versions of previous lectures and this repository should contain the corresponding source code.

This material is loosly based on the material of [Prof. Hannah Bast](https://ad.informatik.uni-freiburg.de/staff/bast)

## Lecturer
Prof. Dr. Rolf Backofen

# Usage
In order to ensure that this repository stays clean and easy to use, please follow and, if required, optimize the following instructions. It is important that your source code can compile after fetching it from the repository using the file structure within the respository. Any deviations must be well documented.

## Introduction
The official version of the course is stored in the master branch. The aim of this repository is that you can clone the original course material and then create your own branch / fork for any changes. Please do not change the original files in the master branch unless you are Rolf or are certain that the changes must be passed on to the following term (e.g. bugfixes, new course material, general improvements endorsed by Rolf or a person in charge). The aim is that the master branch contains Rolf's updated version of the lecture. If you have personalized the lecture and you think your changes will be useful for future teachers, then push your branch to github.

```
Always fork this project and work in that repository.
Help to correct bugs you find by creating a merge request to update the main repository.
```

### Add a corporate design (e.g. from University of Freiburg)
Before building the slides a corporate design has to be added. For example the University of Freiburg design can be selected by providing the 'ALGO_DESIGN=ufcd' option to the make command.

More information can be found here: http://www.zuv.uni-freiburg.de/service/cd

Either use the add_ufcd_linux.sh script provided in scripts, or the following commands. If wget failed, download the ip files through your browser to the directory and skip wget commands:
```
# Create texmf and change into folder
mkdir ~/texmf
cd ~/texmf

# Download University of Freiburg Corporate Design (access restricted to university IP range):
wget http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd.tds.zip
wget http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd-logo-uni.tds.zip
wget http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd-logo-iif.tds.zip
wget http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd-logo-imtek.tds.zip

unzip ufcd.tds.zip
unzip ufcd-logo-uni.tds.zip
unzip ufcd-logo-iif.tds.zip
unzip ufcd-logo-imtek.tds.zip

# Make the corporate design files available to latex
texhash ~/texmf
```

### Build slides and excercies

You need the following localy installed:

```
Windows:
MikTeX + Cygwin + Make

Linux:
TeXlive + Make
```

It's easy, just use `make` in the root directory. Use `make help` to retrieve a usage info.
If you want to only build one lecture / exercise sheet use the command in the desired subdirectory.
```
Windows:
make build

Linux:
make build_server
```

The lecture is provided in different languages / designs / programming languages. Use the respective switches to adjusted the settings.
```
Windows:
make ALGO_DESIGN=ufcd ALGO_PROGLANG=python ALGO_LANGUAGE=eng

Linux:
make build_server ALGO_DESIGN=ufcd ALGO_PROGLANG=python ALGO_LANGUAGE=eng
```
### Working with source files
The Makefile creates a folder called `build` with two LaTeX files. These will be both included to build the document.
```
The * is a placeholder for the language the slides / sheets will be build for:
build/Config.tex
build/Chapters_*.tex or build/Exercises_*.tex
```

`build/Config.tex` contains the active switches passed to the make command.
`build/Chapters_*.tex` or `build/Exercises_*.tex` contains include-lines for all
LaTeX-files present in the `Chapters/*` or `Exercises/*` directory.
```
If you add / remove a file from these directories use `make` to recreate the index!
```

After the first build with the `make` command the slides / exercise sheets can be built by executing the PDFLaTeX compiler
on the main source file `Lecture.tex` or `ExerciseSheet.tex`.

### Clean editing with Windows
If you are using MikTeX on Windows you have to append `-output-directory=build` as switch to the PDFLaTeX command to build
the lecture / sheet into the build directory.

If you have TeX-studio installed append this switch to your PDFLaTeX command under
`Options -> Configure TeXstudio ... -> Commands -> PDFLaTeX`:
```
pdflatex.exe -synctex=1 -output-directory=build -interaction=nonstopmode %.tex
```
You also have to update the search path for the output-file under `Options -> Configure TeXstudio ... -> Commands -> Build`:
Change the following options under `Additional Search Paths`:
```
Log File: ./build
PDF File: ./build
```
Your editor will now compile into the `build` directory and create the temporary files in there.
```
Caution:
If no 'build'-directory exists the editor will show an error on compilation!
```

## Fork / Clone repository
Click on `Fork` in the upper right corner to create a writeable copy of this repositotry.
If you switched to your forked repository you can clone it onto your PC into a local working folder.
Click on `Clone or Download` in the upper right cornder to get the repository URL.
To download the content into a directory named ```AlgoDat``` execute the following commands:
```
SSH:
git clone YOUR_COPIED_SSH_OR_HTTPS_URL
git remote add source https://github.com/BackofenLab/AlgoDat.git
```

### Updating / Saving your work
Use the material in the master branch as a starting point and make any changes required.
Add and commit your changes to the repository to create a snapshot of your work:
```
git add <file> --all
git commit -m "Made some clever changes to my version"
```
Now you can update your committed changes to your online-repository with:
```
git fetch source master
git rebase source/master
git push origin master
```
Click on `Create pull request` to initiate an update of the original source. 

### Getting the current official version in your branch

Download the changes from the source repository and update the base files with:
```
git fetch source master
git rebase source/master
```

### Creating your own tags
When completing a semester, you might want to tag this. Here are some further [tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging) instructions.
```
Create a tag:
git tag "tag-name"

List all tags:
git tag

Remove a tag:
git tag -d "tag-name"

Checkout a tag to a certain branch:
git checkout -b [branchname] [tagname]
```
