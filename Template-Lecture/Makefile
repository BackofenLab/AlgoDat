NAME := Lecture
EXPORT_DIR := Lectures
CHAPTER_NAME := Chapters

MAKEFILE_PATH := $(word $(words $(MAKEFILE_LIST)), $(MAKEFILE_LIST))
ROOT_DIR := $(shell dirname "$(realpath $(MAKEFILE_PATH))")
FULL_NAME := $(shell basename "$(ROOT_DIR)")

all: clean build

# ------------------------------------------------------------------------------
clean:
	@echo "Cleaning"
	@rm -r -f build

help:
	@echo "Targets:"
	@echo "	clean: Cleans the workspace"
	@echo "	----------------------------------------------------------"
	@echo "	build/LANG: Builds the files in the specified language"
	@echo "	build -> build/eng: Builds the english files"
	@echo "	----------------------------------------------------------"
	@echo "	rebuild/LANG: Rebuilds the files in the specified language"
	@echo "	rebuild -> rebuild/eng: Rebuilds the english files"
	@echo "	----------------------------------------------------------"
	@echo "	export/LANG: Builds and exports the specified language"
	@echo "	export -> export/eng: Builds and exports the english files"
	@echo "	----------------------------------------------------------"
	@echo "	export_now/LANG: Only exports the specified language"
	@echo "	export_now -> export_now/eng: Only exports the english files"
	@echo "	----------------------------------------------------------"
	@echo "	build_server/LANG: Builds all files (forced) in the current dir"

build: build/eng
export: export/eng
export_now: export_now/eng

build_server: build_server/eng

# ------------------------------------------------------------------------------
build/eng: NEXT_TARGET := do_build
build/eng: config/eng

build/deu: NEXT_TARGET := do_build
build/deu: config/deu

build_server/eng: NEXT_TARGET := do_build_server
build_server/eng: config/eng

build_server/deu: NEXT_TARGET := do_build_server
build_server/deu: config/deu

rebuild/eng: clean build/eng

rebuild/deu: clean build/deu

export/eng: NEXT_TARGET := do_export
export/eng: config/eng

export/deu: NEXT_TARGET := do_export
export/deu: config/deu

export_now/eng: NEXT_TARGET := do_export_now
export_now/eng: config/eng

export_now/deu: NEXT_TARGET := do_export_now
export_now/deu: config/deu

# ------------------------------------------------------------------------------
do_export_now:
	@echo "Exporting"
	@mkdir -p ../$(EXPORT_DIR)
	@cp build/$(BUILD_NAME).pdf ../$(EXPORT_DIR)/$(FULL_NAME)_$(LANGUAGE).pdf

do_export_now_server:
	@echo "Exporting (server)"
	@mkdir -p ../$(EXPORT_DIR)
	@cp $(BUILD_NAME).pdf ../$(EXPORT_DIR)/$(FULL_NAME)_$(LANGUAGE).pdf

# ------------------------------------------------------------------------------
do_export: do_build do_export_now

# ------------------------------------------------------------------------------
do_build: build/$(BUILD_NAME).pdf
do_build_server: do_build_server_forced do_export_now_server

# ------------------------------------------------------------------------------
directories:
	@echo "Creating directories"
#	@mkdir -p build/Lecture
	@mkdir -p build/Literature/General
	@mkdir -p build/Literature/$(LANGUAGE)

# Currently unused
directories_server:
	@echo "Creating directories (server)"
	@mkdir -p build
	@mkdir -p Literature/General
	@mkdir -p Literature/$(LANGUAGE)

# ------------------------------------------------------------------------------
config: directories
	@echo "Configuring to $(LANGUAGE_NAME) ($(NAME)_$(LANGUAGE), $(CHAPTER_NAME)_$(LANGUAGE))"
	@$(MAKE) --no-print-directory $(NEXT_TARGET) LANGUAGE=$(LANGUAGE) LANGUAGE_NAME=$(LANGUAGE_NAME) BUILD_NAME="$(NAME)_$(LANGUAGE)" BUILD_CHAPTER_NAME="$(CHAPTER_NAME)_$(LANGUAGE)"

config/eng:
	@$(MAKE) --no-print-directory config NEXT_TARGET=$(NEXT_TARGET) LANGUAGE=eng LANGUAGE_NAME=english

config/deu:
	@$(MAKE) --no-print-directory config NEXT_TARGET=$(NEXT_TARGET) LANGUAGE=deu LANGUAGE_NAME=german

# ------------------------------------------------------------------------------
build/$(BUILD_NAME).pdf: build/$(BUILD_CHAPTER_NAME).tex
	@echo "Building $(BUILD_NAME).pdf (server)"
	@
	@echo "Creating $(LANGUAGE_NAME) config"
	@echo '\def\LectureLanguage{$(LANGUAGE)}' > build/Config.tex
	@echo '\def\LectureLanguageName{$(LANGUAGE_NAME)}' >> build/Config.tex
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
build/$(BUILD_CHAPTER_NAME).tex:
	@echo "Reading chapters ($(BUILD_CHAPTER_NAME))"
	@ls Lecture/Chapter/$(LANGUAGE)/*.tex | awk '{printf "\\input{%s}\n", $$1}' > build/$(BUILD_CHAPTER_NAME).tex

# ------------------------------------------------------------------------------
# Server (Do everything manually)
do_build_server_forced: directories_server build/$(BUILD_CHAPTER_NAME).tex
	@echo "Building $(BUILD_NAME).pdf (server)"
	@
	@echo "Creating $(LANGUAGE_NAME) config"
	@echo '\def\LectureLanguage{$(LANGUAGE)}' > build/Config.tex
	@echo '\def\LectureLanguageName{$(LANGUAGE_NAME)}' >> build/Config.tex
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
