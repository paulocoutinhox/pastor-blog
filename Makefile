PY?=
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_REPO?=paulocoutinhox/pastor-blog
STORK_VERSION="v1.5.0"

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make devserver-global               regenerate and serve on 0.0.0.0    '
	@echo '   make setup                          setup everything to make it work   '
	@echo '   make git                            upload content to git repository   '
	@echo '   make format                         format all files                   '
	@echo '   make cloudflare                     clear cloudflare cache             '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

devserver-global:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -b 0.0.0.0

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	@cd $(OUTPUTDIR) && \
	git init . && \
	git add . && \
	git commit -m "published new version"; \
	git push "git@github.com:$(GITHUB_REPO).git" master:gh-pages --force && \
	rm -rf .git
	make cloudflare

setup:
    # brew
	brew bundle

    # python
	python3 -m pip install -r requirements.txt --upgrade

    # vendor
	rm -rf vendor
	mkdir -p vendor/themes

    # theme
	git clone https://github.com/alexandrevicenzi/Flex.git vendor/themes/flex
	git clone https://github.com/paulocoutinhox/nid.git vendor/themes/nid

    #stork
	mkdir -p content/static/{js,css}
	curl -o content/static/js/stork.js https://files.stork-search.net/releases/${STORK_VERSION}/stork.js
	curl -o content/static/js/stork.js.map https://files.stork-search.net/releases/${STORK_VERSION}/stork.js.map
	curl -o content/static/js/stork.wasm https://files.stork-search.net/releases/${STORK_VERSION}/stork.wasm
	curl -o content/static/css/stork.css https://files.stork-search.net/basic.css
	curl -o content/static/css/stork-dark.css https://files.stork-search.net/dark.css

format:
	black .

git:
	git add --all && git commit -am "updated content" && git push origin master

cloudflare:
	curl -X DELETE \
      https://api.cloudflare.com/client/v4/zones/ed2995b035640a4f3acc7d3895dcece6/purge_cache \
      -H 'Authorization: Bearer ${PRS_CLOUDFLARE_TOKEN}' \
      -H 'Content-Type: application/json' \
      -d '{ "purge_everything": true }'

.PHONY: html help clean regenerate serve serve-global devserver publish setup git format cloudflare
