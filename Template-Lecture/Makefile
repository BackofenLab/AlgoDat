NAME := Lecture
EXPORT_DIR := Lectures
CHAPTER_NAME := Chapters

MAKEFILE_PATH := $(word $(words $(MAKEFILE_LIST)), $(MAKEFILE_LIST))
ROOT_DIR := $(shell dirname "$(realpath $(MAKEFILE_PATH))")
FULL_NAME := $(shell basename "$(ROOT_DIR)")

LANGUAGE ?= eng
PROGLANG ?= python
DESIGN ?= plain

BUILD_NAME = $(NAME)_$(LANGUAGE)
BUILD_CHAPTER_NAME = $(CHAPTER_NAME)_$(LANGUAGE)

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
	@echo "	clean: Clean all build files"
	@echo "	build: Build the files in the specified language"
	@echo "	export: Build and export all files into the destination folders"
	@echo
	@echo "TeX: (General)"
	@echo "	build_server:"
	@echo "		Build the lecture into the source directory"
	@echo "	export_server: Build and export all files into the destination folders"

# ------------------------------------------------------------------------------
clean:
	@echo "Cleaning"
	@rm -r -f build

# ------------------------------------------------------------------------------
build: directories build/$(BUILD_NAME).pdf
export: build
	@echo "Exporting"
	@mkdir -p ../$(EXPORT_DIR)
	@cp build/$(BUILD_NAME).pdf ../$(EXPORT_DIR)/$(FULL_NAME)_$(LANGUAGE).pdf

# ------------------------------------------------------------------------------
build_server: directories_server build_server_forced
export_server: build_server
	@echo "Exporting (server)"
	@cp $(BUILD_NAME).pdf ../$(FULL_NAME)_$(LANGUAGE).pdf

# ------------------------------------------------------------------------------
directories:
	@echo "Creating directories"
#	@mkdir -p build/Lecture
	@mkdir -p build/Literature/General
	@mkdir -p build/Literature/$(LANGUAGE)

directories_server:
	@echo "Creating directories (server)"
	@mkdir -p build
	@mkdir -p Literature/General
	@mkdir -p Literature/$(LANGUAGE)

# ------------------------------------------------------------------------------
build/$(BUILD_CHAPTER_NAME).tex:
	@echo "Reading chapters ($(BUILD_CHAPTER_NAME))"
	@ls Lecture/Chapter/$(LANGUAGE)/*.tex | awk '{printf "\\input{%s}\n", $$1}' > build/$(BUILD_CHAPTER_NAME).tex

# ------------------------------------------------------------------------------
build/$(BUILD_NAME).pdf: build/$(BUILD_CHAPTER_NAME).tex
	@echo "Building $(BUILD_NAME).pdf"
	@
	@echo "Creating $(LANGUAGE) config"
	@echo '\def\LectureLanguage{$(LANGUAGE)}' > build/Config.tex
	@echo '\def\LectureProgLanguage{$(PROGLANG)}' >> build/Config.tex
	@echo '\def\LectureDesign{$(DESIGN)}' >> build/Config.tex
	@
	@echo "Copying literature-database"
	@cp -t build/Literature/General $(NAME)/Literature/General/*.bib || true
	@cp -t build/Literature/$(LANGUAGE) $(NAME)/Literature/$(LANGUAGE)/*.bib || true
	@
	@echo "Building"
	@latexmk -pdf -quiet -aux-directory=build -output-directory=build $(NAME).tex
	@
	@echo "Moving output"
	@mv build/$(NAME).pdf build/$(BUILD_NAME).pdf

# ------------------------------------------------------------------------------
# Server (Do everything manually)
build_server_forced: build/$(BUILD_CHAPTER_NAME).tex
	@echo "Building $(BUILD_NAME).pdf (server)"
	@
	@echo "Creating $(LANGUAGE) config"
	@echo '\def\LectureLanguage{$(LANGUAGE)}' > build/Config.tex
	@echo '\def\LectureProgLanguage{$(PROGLANG)}' >> build/Config.tex
	@echo '\def\LectureDesign{$(DESIGN)}' >> build/Config.tex
	@
	@echo "Copying literature-database"
	@cp -t Literature/General $(NAME)/Literature/General/*.bib || true
	@cp -t Literature/$(LANGUAGE) $(NAME)/Literature/$(LANGUAGE)/*.bib || true
	@
	@echo "Building (1st iteration)"
	@pdflatex -interaction=batchmode -disable-installer -quiet $(NAME).tex
	@
	@echo "Building (2nd iteration)"
	@pdflatex -interaction=batchmode -disable-installer -quiet $(NAME).tex
	@
	@echo "Running bibtex"
	@for T in $$(find *.btaux.aux -type f); do (bibtex $$T); done
	@
	@echo "Building (3rd iteration)"
	@pdflatex -interaction=batchmode -disable-installer -quiet $(NAME).tex
	@
	@echo "Building (4th iteration)"
	@pdflatex -interaction=batchmode -disable-installer -quiet $(NAME).tex
	@
	@echo "Moving output"
	@mv $(NAME).pdf $(BUILD_NAME).pdf
