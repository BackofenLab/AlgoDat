ALGO_BUILD_PREFIX := Lecture
ALGO_EXPORT_DIR := Lectures
ALGO_CHAPTER_NAME := Chapters

ALGO_MAKEFILE_PATH := $(word $(words $(MAKEFILE_LIST)), $(MAKEFILE_LIST))
ALGO_ROOT_DIR := $(shell dirname "$(realpath $(ALGO_MAKEFILE_PATH))")
ALGO_FULL_NAME := $(shell basename "$(ALGO_ROOT_DIR)")

ALGO_LANGUAGE ?= eng
ALGO_PROGLANG ?= python
ALGO_DESIGN ?= plain
ALGO_MODE ?= presentation

ALGO_BUILD_NAME = $(ALGO_BUILD_PREFIX)_$(ALGO_LANGUAGE)
ALGO_BUILD_CHAPTER_NAME = $(ALGO_CHAPTER_NAME)_$(ALGO_LANGUAGE)

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
	@echo "Mode:"
	@echo "	Use switch ALGO_MODE=<value> to set the presentation mode"
	@echo "	presentation: All animations are included"
	@echo "	handout: All animations are collapsed for a compact handout"
	@echo
	@echo "MikTeX: (Windows)"
	@echo "	clean: Clean all build files"
	@echo "	build: Build the files in the specified language"
	@echo "	export: Build and export all files into the destination folders"
	@echo
	@echo "TeX: (General)"
	@echo "	clean_server: Cleans the source directory"
	@echo "	build_server: Build the lecture into the source directory"
	@echo "	export_server: Build and export all files into the destination folders"

# ------------------------------------------------------------------------------
clean:
	@echo "Cleaning"
	@rm -r -f build

clean_server:
	@echo "Cleaning (server)"
	@rm -r -f build | true
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
	@cp build/$(ALGO_BUILD_NAME).pdf ../$(ALGO_EXPORT_DIR)/$(ALGO_FULL_NAME)_$(ALGO_LANGUAGE)_$(ALGO_MODE).pdf

# ------------------------------------------------------------------------------
build_server: directories_server build_server_forced
export_server: build_server
	@echo "Exporting (server)"
	@cp $(ALGO_BUILD_NAME).pdf ../$(ALGO_FULL_NAME)_$(ALGO_LANGUAGE)_$(ALGO_MODE).pdf

# ------------------------------------------------------------------------------
directories:
	@echo "Creating directories"
	@mkdir -p build/Literature/General
	@mkdir -p build/Literature/$(ALGO_LANGUAGE)

directories_server:
	@echo "Creating directories (server)"
	@mkdir -p build

# ------------------------------------------------------------------------------
# Create the index for all chapters
build/$(ALGO_BUILD_CHAPTER_NAME).tex:
	@echo "Reading chapters ($(ALGO_BUILD_CHAPTER_NAME))"
	@mkdir -p build | true
	@ls Chapter/$(ALGO_LANGUAGE)/*.tex | awk '{printf "\\input{%s}\n", $$1}' > build/$(ALGO_BUILD_CHAPTER_NAME).tex

# ------------------------------------------------------------------------------
# Build the pdf
build/$(ALGO_BUILD_NAME).pdf: build/$(ALGO_BUILD_CHAPTER_NAME).tex
	@echo "Building $(ALGO_BUILD_NAME).pdf"
	@
	@echo "Creating $(ALGO_LANGUAGE) config"
	@echo '\def\LectureLanguage{$(ALGO_LANGUAGE)}' > build/Config.tex
	@echo '\def\LectureProgLanguage{$(ALGO_PROGLANG)}' >> build/Config.tex
	@echo '\def\LectureDesign{$(ALGO_DESIGN)}' >> build/Config.tex
	@
ifeq ($(ALGO_MODE),presentation)
	@echo '\def\LectureMode{}' >> build/Config.tex
else
	@echo '\def\LectureMode{$(ALGO_MODE)}' >> build/Config.tex
endif
	@
	@echo "Copying literature-database"
	@cp -t build/Literature/General Literature/General/*.bib || true
	@cp -t build/Literature/$(ALGO_LANGUAGE) Literature/$(ALGO_LANGUAGE)/*.bib || true
	@
	@echo "Building"
	@latexmk -pdf -quiet -aux-directory=build -output-directory=build $(ALGO_BUILD_PREFIX).tex
	@
	@echo "Moving output"
	@mv build/$(ALGO_BUILD_PREFIX).pdf build/$(ALGO_BUILD_NAME).pdf

# ------------------------------------------------------------------------------
# Server (Do everything manually)
build_server_forced: build/$(ALGO_BUILD_CHAPTER_NAME).tex
	@echo "Building $(ALGO_BUILD_NAME).pdf (server)"
	@
	@echo "Creating $(ALGO_LANGUAGE) config"
	@echo '\def\LectureLanguage{$(ALGO_LANGUAGE)}' > build/Config.tex
	@echo '\def\LectureProgLanguage{$(ALGO_PROGLANG)}' >> build/Config.tex
	@echo '\def\LectureDesign{$(ALGO_DESIGN)}' >> build/Config.tex
	@
ifeq ($(ALGO_MODE),presentation)
	@echo '\def\LectureMode{}' >> build/Config.tex
else
	@echo '\def\LectureMode{$(ALGO_MODE)}' >> build/Config.tex
endif
	@
	@echo "Building (1st iteration)"
	@pdflatex -interaction=batchmode $(ALGO_BUILD_PREFIX).tex
	@
	@echo "Building (2nd iteration)"
	@pdflatex -interaction=batchmode $(ALGO_BUILD_PREFIX).tex
	@
	@echo "Running bibtex"
	@for T in $$(find *.btaux.aux -type f); do (bibtex $$T); done
	@
	@echo "Building (3rd iteration)"
	@pdflatex -interaction=batchmode $(ALGO_BUILD_PREFIX).tex
	@
	@echo "Building (4th iteration)"
	@pdflatex -interaction=batchmode $(ALGO_BUILD_PREFIX).tex
	@
	@echo "Moving output"
	@mv $(ALGO_BUILD_PREFIX).pdf $(ALGO_BUILD_NAME).pdf
