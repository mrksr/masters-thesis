EXPLICIT_INPUTS=\
	packages.tex \
	../figures/tikz_common.tex \
	../figures/tikz_colors.tex \
	../figures/tikz_jumping.tex \
	../../thesis/preamble/abbreviations.tex

PDFLATEX=pdflatex -interaction=nonstopmode -file-line-error

all: precompile.fmt

%.fmt: %.tex | $(EXPLICIT_INPUTS) $(wildcard *.tex) $(wildcard *.cls) $(wildcard *.sty)
	$(PDFLATEX) -ini -job-name="$*" "&pdflatex $*.tex\dump"

precompile.tex: | $(EXPLICIT_INPUTS)
	$(file >$@) $(foreach INPT,$(EXPLICIT_INPUTS),$(file >>$@,\input{$(INPT)}))
