
# APPSClone client

This subproject corresponds **APPSClone** client, which is able to upload RINEX files to the APPSClone server to be post-processed and, consequently, download the results of them back.

## Features

This project contains the following features:

* Upload RINEX files to the APPSClone server;
* User command-line arguments to specify upload arguments;
* Verify input;
* Download the results of the post-processed files;
* Logging system.

## Possible future implementations

Possible future implementations include:

* Implement a GUI;
* Encrypt socket connections;
* Prettify the logging system;
* Setup in makefile, according to the config file;
* Encrypt files, such as logging file, config file, etc.

## Installation

Set up the project by installing its dependencies and creating initial directories:

```bash
make setup
```

To change default directories or configurations, edit the `config/client.cfg file` and, consequently, make sure those directories exist.
    
## Run

To run the project, type:

```bash
make run a="arguments"
```

The `a` variable will contain command-line arguments, which will specify what the program will do. The following shows the usage of the program (can also be shown by running `make run a="-h"`):

```
usage: runClient.py [-h] [-r R] [-m M] [-p P] [-t T] [--ocean_loading] [--model_tides] [-w W] [-a A] [-s S] option

The APPSClone client. Upload RINEX files to the server and download back the results!

positional arguments:
  option           upload | download.

optional arguments:
  -h, --help       show this help message and exit
  -r R             The name of the RINEX file to upload.
  -m M             The processing mode. 1 means static, 2 means kinematic. Default is static.
  -p P             The product. 1 means real time, 2 means ultra, 3 means rapid, 4 means final, 5 means best. Default is best.
  -t T             The troposphere model. 1 means vmf1, 2 means gmf, 3 means gpt2. Default is gmf.
  --ocean_loading  To load or not the ocean model. Default is true.
  --model_tides    To model or not the tides. Default is true.
  -w W             The elevation dep weighting. 1 means flat, 2 means sine, 3 means root sine. Default is root sine.
  -a A             The elevation angle cutoff. A floating-point number. Default is 7.5.
  -s S             The solution period. An integer. Default is 300.
  ```


## Testing

To run a specific test, run:

```bash
make test tf=nameOfTestFile
```

The `nameOfTestFile` shall not contain `test_` at the start and shall not end in `.py`; the makefile automatically handles that.

To run a specific test and print the output, run:

```bash
make testPrint tf=nameOfTestFile
```

To run all tests, run:

```bash
make testAll
```

To run all tests and print the output, run:
```bash
make testAllPrint
```

## Documentation

The documentation for the APPSClone client can be found [here](https://github.com/DuarteArribas/APPSClone/tree/main/development/APPSClone_Client/docs).
