DOCUMENTS = *.pdf 

all: $(DOCUMENTS) 
.PHONY: clean

# Use Pandoc to convert Markdown -> LaTeX PDF
%.pdf: %.md
	pandoc --top-level-division=section --toc -o $@ $<

