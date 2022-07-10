
# APPSClone - APPSClone server

This subproject corresponds **APPSClone** client, which is able to handle two types of requests to RINEX files:
* Automatic RINEX download, post-process and, consequent, result upload;
* Manual RINEX download with automatic post-process and, consequent, manual result upload.

The program can be run as a server, where the client (https://github.com/DuarteArribas/APPSClone/tree/main/APPSClone_Client) can upload RINEX files or download their results.

The program can be run as a script (e.g., in crontab), where it will:

* Check for state changes on already uploaded files;
* Handle new states of uploaded files (e.g., if a file changes from the state submitted to the state verified, the program will approve it for processing);
* Upload back any results downloaded in the previous point (if the file state was available);
* Download new upload files (which contain information as in (https://github.com/DuarteArribas/APPSClone/tree/main/APPSClone_UploadFileGenerator));
* Upload new files downloaded in the last step to APPS.

## Features

This project contains the following features:

* RINEX file validation;
* CRUD operations on the files with verifications;
* Manual and automatic upload system;
* Logging system.

## Possible future implementations

Possible future implementations include:

* More verification;
* Better RINEX validation;
* Error handling in case of network failure;
* Encrypt socket connections;
* Prettify the logging system;
* Setup in makefile, according to the config file;
* Encrypt files, such as logging file, config file, etc.

## Installation

Setup the project by installing its dependencies and creating initial directories:

```bash
make setup
```

To change default directories or configurations, edit the `config/appsclone.cfg file`.
    
## Run

To run the server, type:

```bash
make run
```

To run the file handling, type:

```bash
make runSpecial
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

The documentation for the APPSClone server can be found [here](https://github.com/DuarteArribas/APPSClone/tree/main/APPSClone_Server/docs).
