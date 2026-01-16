WD        := /home/manfucci/github.com/amanfucci/sistemi-informativi
BUILD_DIR := $(WD)/presentation/build
BUILD_DIR_TIKZ := $(BUILD_DIR)/build_tikz/
MAIN      := $(WD)/presentation/main.tex
MAIN_HANDOUT      := $(WD)/presentation/handout.tex
SLIDES    := $(WD)/presentation/manfucci_alessandro_progetto_si_2025_slides.pdf
HANDOUT   := $(WD)/presentation/manfucci_alessandro_progetti_si_2025_handout.pdf
TEXFILES  := $(wildcard $(WD)/presentation/*.tex) $(wildcard $(WD)/presentation/*.latex)
IMAGES    := $(wildcard $(WD)/images/*)
FIGURES   := $(wildcard $(WD)/figures/*)
PLOTS     := $(wildcard $(WD)/plots/*)
TIKZ	  := $(WD)/graphs.tikzdefs $(WD)/graphs.tikzstyles $(WD)/tikzit.sty
BIB       := $(WD)/biblio.bib

all: slides handout clean

slides: clean $(SLIDES)

handout : clean $(HANDOUT)

$(SLIDES): $(MAIN) $(TEXFILES) $(IMAGES) $(FIGURES) $(PLOTS) $(TIKZ) $(BIB) | $(BUILD_DIR_TIKZ) $(BUILD_DIR)
	TEXINPUTS=$(WD)/images:$(WD)/figures:$$TEXINPUTS: \
	BIBINPUTS=$(WD):$$BIBINPUTS \
	latexmk -bibtex -pdf -shell-escape -output-directory=$(BUILD_DIR) $(MAIN)
	mv $(BUILD_DIR)/main.pdf $(SLIDES)

$(HANDOUT): $(MAIN) $(TEXFILES) $(IMAGES) $(FIGURES) $(PLOTS) $(TIKZ) $(BIB) | $(BUILD_DIR_TIKZ) $(BUILD_DIR)
	TEXINPUTS=$(WD)/images:$(WD)/figures:$$TEXINPUTS: \
	BIBINPUTS=$(WD):$$BIBINPUTS \
	latexmk -bibtex -pdf -shell-escape -jobname=handout -output-directory=$(BUILD_DIR) $(MAIN_HANDOUT)
	mv $(BUILD_DIR)/handout.pdf $(HANDOUT)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(BUILD_DIR_TIKZ): $(BUILD_DIR)
	mkdir -p $(BUILD_DIR_TIKZ)

clean:
	rm -rf $(BUILD_DIR)

.PHONY: slides handout clean