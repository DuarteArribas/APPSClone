#variables
PYTHON              := python3
PIP                 := pip3
MAIN_FILE           := runServer.py
MAIN_FILE_SPECIAL   := handleUploadFiles.py
#files
appsIdQueue         := apps_id_queue
rinexQueue          := rinex_queue
idQueue             := idQueue
regularUsersIdQueue := regularUsersIDQueue
logs                := logs.log
logs2               := logsServer.log
#directories
testDir             := tests
inDir               := in
outDir              := out
toDownloadDir       := to_download
toUploadDir         := to_upload
toUploadRegDir      := to_upload_regular
resultsDir          := results
resultsRegDir       := results_regular
queuesDir           := queues
logsDir             := logs
#paths
toDownloadPath      := $(inDir)/$(toDownloadDir)
toUploadPath        := $(inDir)/$(toUploadDir)
toUploadRegPath     := $(inDir)/$(toUploadRegDir)
resultsPath         := $(outDir)/$(resultsDir)
resultsRegPath      := $(outDir)/$(resultsRegDir)
appsIdQueuePath     := $(queuesDir)/$(appsIdQueue)
rinexQueuePath      := $(queuesDir)/$(rinexQueue)
idQueuePath         := $(queuesDir)/$(idQueue)
regUsersQueuePath   := $(queuesDir)/$(regularUsersIdQueue)
logsPath            := $(logsDir)/$(logs)
logsPath2           := $(logsDir)/$(logs2)

run:
	$(PYTHON) $(MAIN_FILE)

runSpecial:
	$(PYTHON) $(MAIN_FILE_SPECIAL)

setup:
	$(PIP) install -r requirements.txt
	pip3 install https://pppx.gdgps.net/static/lib/gdgps-apps-1.0.0b2.tar.gz
	@mkdir -p $(toDownloadPath)
	@mkdir -p $(toUploadPath)
	@mkdir -p $(toUploadRegPath)
	@mkdir -p $(resultsPath)
	@mkdir -p $(resultsRegPath)
	@mkdir -p $(queuesDir)
	@mkdir -p $(logsDir)
	@touch $(appsIdQueuePath)
	@touch $(rinexQueuePath)
	@touch $(idQueuePath)
	@touch $(regUsersQueuePath)
	@touch $(logsPath)

test:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py > /dev/null

testPrint:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py

testAll:
	$(PYTHON) -m unittest $(testDir)/test_* > /dev/null

testAllPrint:
	$(PYTHON) -m unittest $(testDir)/test_*

.PHONY: run setup test testPrint testAll testAllPrint clean clearLogs