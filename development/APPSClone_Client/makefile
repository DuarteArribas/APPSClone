#variables
PYTHON    := python3
PIP       := pip3
MAIN_FILE := runClient.py
#files
idQueue     := idQueue
logs        := logs.log
#directories
testDir     := tests
inDir       := in
queuesDir   := queues
toUploadDir := toUploadRinex
logsDir     := logs
#paths
logsPath    := $(logsDir)/$(logs)
idQueuePath := $(queuesDir)/$(idQueue)

run:
	$(PYTHON) $(MAIN_FILE) $(a)

setup:
	$(PIP) install -r requirements.txt
	pip3 install https://pppx.gdgps.net/static/lib/gdgps-apps-1.0.0b2.tar.gz
	@mkdir -p $(queuesDir)
	@mkdir -p $(inDir)/$(toUploadDir)
	@mkdir -p $(logsDir)
	@touch $(logsPath)
	@touch $(idQueuePath)

test:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py > /dev/null

testPrint:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py

testAll:
	$(PYTHON) -m unittest $(testDir)/test_* > /dev/null

testAllPrint:
	$(PYTHON) -m unittest $(testDir)/test_*

.PHONY: run setup test testPrint testAll testAllPrint