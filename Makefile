NAME_LECTURES = Lectures
NAME_EXERCISESHEETS = ExerciseSheets

ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
FULL_NAME := $(shell basename $(ROOT_DIR))

LANGUAGE ?= eng
PROGLANG ?= python
DESIGN ?= plain

all: clean build

# ------------------------------------------------------------------------------
help:
	@echo "Language:"
	@echo "	Use switch LANGUAGE=<value> to set the language"
	@echo "	eng: english"
	@echo
	@echo "Programming Language:"
	@echo "	Use switch PROGLANG=<value> to set the language"
	@echo "	java: Java"
	@echo "	cpp: C++"
	@echo "	python: Python"
	@echo
	@echo "Design:"
	@echo "	Use switch DESIGN=<value> to set the lecture design"
	@echo "	ufcd: Design of University of Freiburg"
	@echo "	plain: Standard design of the beamer template"
	@echo
	@echo "MikTeX: (Windows)"
	@echo "	clean/lectures: Clean all lectures"
	@echo "	clean/exercisesheets: Clean all exercisesheets"
	@echo "	clean/full: Clean all build folders erasing all build files"
	@echo "	build: Build all files into the build directories"
	@echo "	build/lectures: Build all lectures into the build directories"
	@echo "	build/exercisesheets: Build all exercisesheets into the build directories"
	@echo
	@echo "TeX: (General)"
	@echo "	clean: Clean only the export folders"
	@echo "	build_server:"
	@echo "		Build all files of a language into the source directory"
	@echo "	build_server/lectures:"
	@echo "		Build all lectures of a language into the source directory"
	@echo "	build_server/exercisesheets:"
	@echo "		Build all exercisesheets of a language into the source directory"
	@echo "	export: Move all build files into the root directory"

# ------------------------------------------------------------------------------
clean:
	@echo "Cleaning"
	@rm -r -f $(NAME_LECTURES)
	@rm -r -f $(NAME_EXERCISESHEETS)

clean/lectures:
	@echo "Cleaning Lectures"
	@ls -d Lecture-* | awk '{system("$(MAKE) --directory="$$1" clean");}'

clean/exercisesheets:
	@echo "Cleaning ExerciseSheets"
	@ls -d ExerciseSheet-* | awk '{system("$(MAKE) --directory="$$1" clean");}'

clean/full: clean clean/lectures clean/exercisesheets
	@rm -f ./*.pdf

# ------------------------------------------------------------------------------
directories:
	@echo "Creating directories"
	@mkdir -p $(NAME_LECTURES)
	@mkdir -p $(NAME_EXERCISESHEETS)

# ------------------------------------------------------------------------------
build: directories build/lectures build/exercisesheets

build/lectures:
	@echo "Building lectures"
	@ls -d Lecture-* | awk '{system("$(MAKE) --directory="$$1" LANGUAGE=$(LANGUAGE) PROGLANG=$(PROGLANG) DESIGN=$(DESIGN) export");}'

build/exercisesheets:
	@echo "Building exercise-sheets"
	@ls -d ExerciseSheet-* | awk '{system("$(MAKE) --directory="$$1" LANGUAGE=$(LANGUAGE) PROGLANG=$(PROGLANG) DESIGN=$(DESIGN) export");}'

# ------------------------------------------------------------------------------
build_server: directories build_server/lectures build_server/exercisesheets
build_server/lectures:
	@echo "Building lectures (server)"
	@ls -d Lecture-* | awk '{system("$(MAKE) --directory="$$1" LANGUAGE=$(LANGUAGE) PROGLANG=$(PROGLANG) DESIGN=$(DESIGN) export_server");}'

build_server/exercisesheets:
	@echo "Building exercise-sheets (server)"
	@ls -d ExerciseSheet-* | awk '{system("$(MAKE) --directory="$$1" LANGUAGE=$(LANGUAGE) PROGLANG=$(PROGLANG) DESIGN=$(DESIGN) export_server");}'

export:
	@echo "Exporting generated files"
	@mv $(NAME_LECTURES)/*.pdf .
	@mv $(NAME_EXERCISESHEETS)/*.pdf .
