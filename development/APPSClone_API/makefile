#variables
PYTHON          := python3
PIP             := pip3
MAIN_FILE       := main.py
#files
appsIdQueue     := apps_id_queue
rinexQueue      := rinex_queue
logs            := logs.log
#directories
testDir         := tests
inDir           := in
outDir          := out
toDownloadDir   := to_download
toUploadDir     := to_upload
resultsDir      := results
queuesDir       := queues
logsDir         := logs
#paths
toDownloadPath  := $(inDir)/$(toDownloadDir)
toUploadPath    := $(inDir)/$(toUploadDir)
resultsPath     := $(outDir)/$(resultsDir)
appsIdQueuePath := $(queuesDir)/$(appsIdQueue)
rinexQueuePath  := $(queuesDir)/$(rinexQueue)
logsPath        := $(logsDir)/$(logs)

run:
	$(PYTHON) $(MAIN_FILE)

setup:
	$(PIP) install -r requirements.txt

test:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py

clean:
	@rm $(toDownloadPath)/*
	@rm $(toUploadPath)/*
	@rm $(resultsPath)/*
	@echo -n "" > $(appsIdQueuePath)
	@echo -n "" > $(rinexQueuePath)

clearLogs:
	@echo -n "" > $(logsPath)

.PHONY: run setup test clean clearLogs