ALGO_NAME := ExerciseSheet
ALGO_EXPORT_DIR := ExerciseSheets
ALGO_EXERCISES_NAME := Exercises

ALGO_MAKEFILE_PATH := $(word $(words $(MAKEFILE_LIST)), $(MAKEFILE_LIST))
ALGO_ROOT_DIR := $(shell dirname "$(realpath $(ALGO_MAKEFILE_PATH))")
ALGO_FULL_NAME := $(shell basename "$(ALGO_ROOT_DIR)")

ALGO_LANGUAGE ?= eng
ALGO_PROGLANG ?= python
ALGO_DESIGN ?= plain

ALGO_BUILD_NAME = $(ALGO_NAME)_$(ALGO_LANGUAGE)
ALGO_BUILD_EXERCISES_NAME = $(ALGO_EXERCISES_NAME)_$(ALGO_LANGUAGE)

all: clean build

# ------------------------------------------------------------------------------
help:
	@echo "Language:"
	@echo "	Use switch ALGO_LANGUAGE=<value> to set the language"
	@echo "	eng: english"
	@echo
	@echo "Programming Language:"
	@echo "	Use switch ALGO_PROGLANG=<value> to set the language"
	@echo "	java: Java"
	@echo "	cpp: C++"
	@echo "	python: Python"
	@echo
	@echo "Design:"
	@echo "	Use switch ALGO_DESIGN=<value> to set the lecture design"
	@echo "	ufcd: Design of University of Freiburg"
	@echo "	plain: Standard design of the beamer template"
	@echo
	@echo "MikTeX: (Windows)"
	@echo "	clean: Clean all build files"
	@echo "	build: Build the files in the specified language"
	@echo "	export: Build and export all files into the destination folders"
	@echo
	@echo "TeX: (General)"
	@echo "	clean_server: Cleans the source directory"
	@echo "	build_server: Build the sheet into the source directory"
	@echo "	export_server: Build and export all files into the destination folders"

# ------------------------------------------------------------------------------
clean:
	@echo "Cleaning"
	@rm -r -f build

clean_server:
	@echo "Cleaning (server)"
	@rm -f *.log
	@rm -f *.aux
	@rm -f *.bbl
	@rm -f *.fls
	@rm -f *.nav
	@rm -f *.out
	@rm -f *.snm
	@rm -f *.toc
	@rm -f *.fdb_latexmk

# ------------------------------------------------------------------------------
build: directories build/$(ALGO_BUILD_NAME).pdf
export: build
	@echo "Exporting"
	@mkdir -p ../$(ALGO_EXPORT_DIR)
	@cp build/$(ALGO_BUILD_NAME).pdf ../$(ALGO_EXPORT_DIR)/$(ALGO_FULL_NAME)_$(ALGO_LANGUAGE).pdf

build_server: directories_server build_server_forced
export_server: build_server
	@echo "Exporting (server)"
	@cp $(ALGO_BUILD_NAME).pdf ../$(ALGO_FULL_NAME)_$(ALGO_LANGUAGE).pdf

# ------------------------------------------------------------------------------
directories:
	@echo "Creating directories"
	@mkdir -p build

directories_server:
	@echo "Creating directories (server)"
	@mkdir -p build

# ------------------------------------------------------------------------------
# Create the index for all exercises
build/$(ALGO_BUILD_EXERCISES_NAME).tex:
	@echo "Reading chapters ($(ALGO_BUILD_EXERCISES_NAME))"
	@ls Exercises/$(ALGO_LANGUAGE)/*.tex | awk '{printf "\\input{%s}\n", $$1}' > build/$(ALGO_BUILD_EXERCISES_NAME).tex

# ------------------------------------------------------------------------------
# Build the pdf
build/$(ALGO_BUILD_NAME).pdf: build/$(ALGO_BUILD_EXERCISES_NAME).tex
	@echo "Building $(ALGO_BUILD_NAME).pdf"
	@
	@echo "Creating $(ALGO_LANGUAGE) config"
	@echo '\def\SettingsLanguage{$(ALGO_LANGUAGE)}' > build/Config.tex
	@echo '\def\SettingsProgLanguage{$(ALGO_PROGLANG)}' >> build/Config.tex
	@echo '\def\SettingsDesign{$(ALGO_DESIGN)}' >> build/Config.tex
	@
	@echo "Building"
	@latexmk -pdf -quiet -aux-directory=build -output-directory=build $(ALGO_NAME).tex
	@
	@echo "Moving output"
	@mv build/$(ALGO_NAME).pdf build/$(ALGO_BUILD_NAME).pdf

# ------------------------------------------------------------------------------
# Server (Do everything manually)
build_server_forced: build/$(ALGO_BUILD_EXERCISES_NAME).tex
	@echo "Building $(ALGO_BUILD_NAME).pdf (server)"
	@
	@echo "Creating $(ALGO_LANGUAGE) config"
	@echo '\def\SettingsLanguage{$(ALGO_LANGUAGE)}' > build/Config.tex
	@echo '\def\SettingsProgLanguage{$(ALGO_PROGLANG)}' >> build/Config.tex
	@echo '\def\SettingsDesign{$(ALGO_DESIGN)}' >> build/Config.tex
	@
	@echo "Building (1st iteration)"
	@pdflatex -interaction=batchmode $(ALGO_NAME).tex
	@
	@echo "Building (2nd iteration)"
	@pdflatex -interaction=batchmode $(ALGO_NAME).tex
	@
	@echo "Building (3rd iteration)"
	@pdflatex -interaction=batchmode $(ALGO_NAME).tex
	@
	@echo "Moving output"
	@mv $(ALGO_NAME).pdf $(ALGO_BUILD_NAME).pdf