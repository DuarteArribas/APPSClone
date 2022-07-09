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
	@mkdir -p $(queuesDir)
	@mkdir -p $(inDir)/$(toUploadDir)
	@mkdir -p $(logsDir)
	@touch $(queuesDir)/$(idQueue)
	@touch $(logsDir)/$(logs)

test:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py > /dev/null

testPrint:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py

testAll:
	$(PYTHON) -m unittest $(testDir)/test_* > /dev/null

testAllPrint:
	$(PYTHON) -m unittest $(testDir)/test_*

.PHONY: run setup test testPrint testArgs testArgsPrint testAll testAllPrint