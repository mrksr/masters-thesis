OUTER_SRCS=../figures/tikz_common.tex ../figures/tikz_colors.tex ../figures/tikz_jumping.tex

%.fmt: $(OUTER_SRCS) $(wildcard *.tex) $(wildcard *.cls) $(wildcard *.sty)
	pdflatex -ini -job-name="$*" "&pdflatex $*.tex\dump"

all: precompile.fmt
