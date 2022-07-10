#variables
PYTHON         := python3
PIP            := pip3
MAIN_FILE      := main.py
#directories
testDir        := tests
outDir         := out
uploadFilesDir := uploadFiles

run:
	$(PYTHON) $(MAIN_FILE)

setup:
	$(PIP) install -r requirements.txt
	@mkdir -p $(outDir)
	@mkdir -p $(uploadFilesDir)

test:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py > /dev/null

testPrint:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py

testAll:
	$(PYTHON) -m unittest $(testDir)/test_* > /dev/null

testAllPrint:
	$(PYTHON) -m unittest $(testDir)/test_*

.PHONY: run setup test testPrint testAll testAllPrint