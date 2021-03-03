PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_REPO?=paulo-coutinho/pastor-blog

DEBUG ?= 1
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
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
	@echo '   make ssh-upload                     upload the web site via SSH        '
	@echo '   make rsync-upload                   upload the web site via rsync+ssh  '
	@echo '   make git-upload                     upload content to git repository   '
	@echo '   make get-vendor                     get all pelican plugins            '
	@echo '   make format                         format all files                   '
	@echo '   make submodule-update               update all git submodules          '
	@echo '   make install-plugins                install plugins into vendor folder '
	@echo '   make python-deps                    install required dependencies      '
	@echo '   make cloudflare-clear-cache         clear cloudflare cache             '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b 0.0.0.0
endif


devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	@cd $(OUTPUTDIR) && \
	git init . && \
	git add . && \
	git commit -m "published new version"; \
	git push "git@github.com:$(GITHUB_REPO).git" master:gh-pages --force && \
	rm -rf .git
	make cloudflare-clear-cache

get-vendor:
	test -d "vendor" || git submodule add https://github.com/getpelican/pelican-plugins.git vendor

submodule-update:
	git submodule update -f --init

format:
	black *conf.py
	black content/
	black plugins/

git-upload:
	git add --all && git commit -am "updated content" && git push origin master

install-plugins:
	git clone --recursive https://github.com/getpelican/pelican-plugins vendor

python-deps:
	pip install -r requirements.txt --upgrade

cloudflare-clear-cache:
	curl -X DELETE \
      https://api.cloudflare.com/client/v4/zones/ed2995b035640a4f3acc7d3895dcece6/purge_cache \
      -H 'Authorization: Bearer ${PRS_CLOUDFLARE_TOKEN}' \
      -H 'Content-Type: application/json' \
      -d '{ "purge_everything": true }'

.PHONY: html help clean regenerate serve serve-global devserver publish 
