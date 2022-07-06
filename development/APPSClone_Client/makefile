#variables
PYTHON         := python3
PIP            := pip3
MAIN_FILE      := main.py
#directories
testDir        := tests

run:
	$(PYTHON) $(MAIN_FILE)

runArgs:
	$(PYTHON) $(MAIN_FILE) $(a)

setup:
	$(PIP) install -r requirements.txt

test:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py > /dev/null

testPrint:
	$(PYTHON) -m unittest $(testDir)/test_$(tf).py

testAll:
	$(PYTHON) -m unittest $(testDir)/test_* > /dev/null

testAllPrint:
	$(PYTHON) -m unittest $(testDir)/test_*

.PHONY: run runArgs setup test testPrint testArgs testArgsPrint testAll testAllPrint