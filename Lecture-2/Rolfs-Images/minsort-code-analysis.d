minsort-code-analysis.svg-gen:  minsort-code-analysis-o1.svg minsort-code-analysis-o2.svg minsort-code-analysis-o3.svg minsort-code-analysis-o4.svg
 minsort-code-analysis-o1.svg minsort-code-analysis-o2.svg minsort-code-analysis-o3.svg minsort-code-analysis-o4.svg: minsort-code-analysis.svg
	~backofen/bin/svg_layers.sh minsort-code-analysis.svg -combine

minsort-code-analysis-o1.png: minsort-code-analysis-o1.svg
minsort-code-analysis-o1.pdf: minsort-code-analysis-o1.svg
minsort-code-analysis-o2.png: minsort-code-analysis-o2.svg
minsort-code-analysis-o2.pdf: minsort-code-analysis-o2.svg
minsort-code-analysis-o3.png: minsort-code-analysis-o3.svg
minsort-code-analysis-o3.pdf: minsort-code-analysis-o3.svg
minsort-code-analysis-o4.png: minsort-code-analysis-o4.svg
minsort-code-analysis-o4.pdf: minsort-code-analysis-o4.svg

SVG2PDF := $(sort $(SVG2PDF)  minsort-code-analysis-o1.pdf minsort-code-analysis-o2.pdf minsort-code-analysis-o3.pdf minsort-code-analysis-o4.pdf)
SVG2PNG := $(sort $(SVG2PNG)  minsort-code-analysis-o1.png minsort-code-analysis-o2.png minsort-code-analysis-o3.png minsort-code-analysis-o4.png)
