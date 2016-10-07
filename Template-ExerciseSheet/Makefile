NAME := ExerciseSheet
EXPORT_DIR := ExerciseSheets

ROOT_DIR := $(shell dirname "$(realpath $(lastword $(MAKEFILE_LIST)))")
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
	@echo "	build/LANGUAGE: Builds the files in the specified language"
	@echo "	build -> build/eng: Builds the english files"
	@echo "	----------------------------------------------------------"
	@echo "	rebuild/LANGUAGE: Rebuilds the files in the specified language"
	@echo "	rebuild -> rebuild/eng: Rebuilds the english files"
	@echo "	----------------------------------------------------------"
	@echo "	export/LANGUAGE: Builds and exports the specified language"
	@echo "	export -> export/eng: Builds and exports the english files"
	@echo "	----------------------------------------------------------"
	@echo "	export_now/LANGUAGE: Only exports the specified language"
	@echo "	export_now -> export_now/eng: Only exports the english files"

build: build/eng
export: export/eng
export_now: export_now/eng

# ------------------------------------------------------------------------------
build/eng: NEXT_TARGET := do_build
build/eng: config/eng

build/deu: NEXT_TARGET := do_build
build/deu: config/deu

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

# ------------------------------------------------------------------------------
do_export: do_build do_export_now

# ------------------------------------------------------------------------------
do_build: build/$(BUILD_NAME).pdf

# ------------------------------------------------------------------------------
directories:
	@echo "Creating directories"
	@mkdir -p build

# ------------------------------------------------------------------------------
config: directories
	@echo "Configuring to $(LANGUAGE_NAME) ($(NAME)_$(LANGUAGE))"
	@$(MAKE) --no-print-directory $(NEXT_TARGET) LANGUAGE=$(LANGUAGE) LANGUAGE_NAME=$(LANGUAGE_NAME) BUILD_NAME="$(NAME)_$(LANGUAGE)"

config/eng:
	@$(MAKE) --no-print-directory config NEXT_TARGET=$(NEXT_TARGET) LANGUAGE=eng LANGUAGE_NAME=english

config/deu:
	@$(MAKE) --no-print-directory config NEXT_TARGET=$(NEXT_TARGET) LANGUAGE=deu LANGUAGE_NAME=german

# ------------------------------------------------------------------------------
build/$(BUILD_NAME).pdf:
	@echo "Building $(BUILD_NAME).pdf"
	@
	@echo "Creating $(LANGUAGE_NAME) config"
	@echo '\def\SettingsLanguage{$(LANGUAGE)}' > build/Config.tex
	@echo '\def\SettingsLanguageName{$(LANGUAGE_NAME)}' >> build/Config.tex
	@
	@echo "Building (1st iteration)"
	@latexmk -pdf -quiet -aux-directory=build -output-directory=build $(NAME).tex
	@
	@echo "Moving output"
	@mv build/$(NAME).pdf build/$(BUILD_NAME).pdf