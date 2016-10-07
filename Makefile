NAME_LECTURES = Lectures
NAME_EXERCISESHEETS = ExerciseSheets

ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
FULL_NAME := $(shell basename $(ROOT_DIR))

all: clean build

clean:
	@echo "Cleaning Lectures"
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

directories:
	@echo "Creating directories"
	@mkdir -p $(NAME_LECTURES)
	@mkdir -p $(NAME_EXERCISESHEETS)

build: directories build/lectures build/exercisesheets

build/lectures:
	@echo "Building lectures"
	@ls -d Lecture-* | awk '{system("$(MAKE) --directory="$$1" export");}'

build/exercisesheets:
	@echo "Building exercise-sheets"
	@ls -d ExerciseSheet-* | awk '{system("$(MAKE) --directory="$$1" export");}'

export:
	@echo "Exporting generated files"
	@mv $(NAME_LECTURES)/*.pdf .
	@mv $(NAME_EXERCISESHEETS)/*.pdf .

build_server: directories build_server/lectures build_server/exercisesheets
build_server/lectures:
	@echo "Building lectures (server)"
	@ls -d Lecture-* | awk '{system("$(MAKE) --directory="$$1" build_server/$(LANGUAGE)");}'

build_server/exercisesheets:
	@echo "Building exercise-sheets (server)"
	@ls -d ExerciseSheet-* | awk '{system("$(MAKE) --directory="$$1" build_server/$(LANGUAGE)");}'