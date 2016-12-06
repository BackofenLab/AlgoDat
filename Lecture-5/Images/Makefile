
all: tex_vers_internall
clean: tex_vers_internclean
cleanall: tex_vers_interncleanall

MAKEDIR = $(FIGURESDIR)/generic-Makefiles/
RULES = $(MAKEDIR)/figures.Makefile-rules.mk
RULES_TEX_VERSION = $(MAKEDIR)/tex_version.Makefile-rules.mk
GLOBALDEPS = $(MAKEDIR)/figures.Makefile-globaldep.mk
GLOBALDEPS_TEX_VERSION = $(MAKEDIR)/tex_version.Makefile-globaldep.mk
SUBDIRSEXCLUDE=Figures SingleSlides

STDPSTEX=
STDEEPIC=
STDLATEX=
CONVERT=
DRAFTS=no
SUBCLIPSDIM=
LINKS=

#SVGEXPORTRES=
SPLITSVG=
SPLITSVGZ=

ALLCONVERT=no
ALLCOMPRESSED=yes
COMPRESSEDFORMATS=

ALLTEXPDF=yes
# TEXPS=
# TEXPDF=

VERSION_FOR_FILES=
VERSION_SEP=+++
VERSIONLINKS=yes

include $(RULES)
include $(GLOBALDEPS)

include $(RULES_TEX_VERSION)
include $(GLOBALDEPS_TEX_VERSION)


