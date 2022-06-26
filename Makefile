# Sphinx用変数
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build


test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish

doc-help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
doc-update-module:
	sphinx-apidoc -f -o ./docs ./commando

html-build:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html-publish:
	git add -f docs/_build/html/
	git commit -m "update: commando document(github pages)"
	git subtree push --force --prefix docs/_build/html origin gh-pages
