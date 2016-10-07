# Algorithms and Data Structures 

This course comprises of a 2 SWS lecture and a 2 SWS exercise class in English, generally for Bachelor students (ESE und IEMS). 

This repository stores the source code that is required for the Algorithms and Data Structures course containing source code and images for the lecture and the exercises. Each semester, the people responsible for teaching a course usually want to modify and personalize the existing teaching material. In the past this has been an extremely painful and error-prone process. This repository should help with keeping track of "bug fixes" and personal modifications to make life easier for future teaching tasks. Our [teaching webpage](http://www.bioinf.uni-freiburg.de/Lehre/index.html?en) contains all compiled versions of previous lectures and this repository should contain the corresponding source code.

This material is loosly based on the material of [Prof. Hannah Bast](https://ad.informatik.uni-freiburg.de/staff/bast)

## Lecturer
Prof. Dr. Rolf Backofen

# Usage
In order to ensure that this repository stays clean and easy to use, please follow and, if required, optimize the following instructions. It is important that your source code can compile after fetching it from the repository using the file structure within the respository. Any deviations must be well documented.

## Introduction
The official version of the course is stored in the master branch. The aim of this repository is that you can clone the original course material and then create your own branch for any changes. Please do not change the original files in the master branch unless you are Rolf or are certain that the changes must be passed on to the following term (e.g. bugfixes, new course material, general improvements endorsed by Rolf or a person in charge). The aim is that the master branch contains Rolf's updated version of the lecture. If you have personalized the lecture and you think your changes will be useful for future teachers, then push your branch to github.

*Always create your own branch and work in that branch*

*Immediately correct bugs you find in the master branch*

### Build slides and excercies

It's easy, just do make:

```
make
```

Ok, you need to have the Latex world installed and you need to have the Corporate Design latex package available. More information can be found here: http://www.zuv.uni-freiburg.de/service/cd ... ok maybe not so easy.


## Clone repository 
`$ git clone https://github.com/BackofenLab/BioinformaticsI.git`

## Creating your own branch
Use the material in the master branch as a starting point and make your changes in your branch. First create your own branch

`$ git checkout -b [your-branch]`

Push your branch to GitHub

`$ git push origin [your-branch]`

Then make any change required in your branch. This includes any branch-specific figures. Add and commit your changes to the repository.

`$ git add <file>`
`$ git commit -m "made some clever changes to my branch"`

Finally push all your commited your changes to your branch

`$ git push origin [your-branch]`

## Getting the current official version in your branch

First update your master branch

`$ git pull origin master`

Checkout your branch

`$ git checkout [your-branch]`

Then merge master with your branch

`$ git merge master`

## Creating your own tags
When completing a semester, you might want to tag this. Here are some further [tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging) instructions.

`$ git tag "tag-name"`

List all tags

`$ git tag`

Remove a tag
`$ git tag -d "tag-name"`

Checkout a tag to a certain branch
`git checkout -b [branchname] [tagname]`
