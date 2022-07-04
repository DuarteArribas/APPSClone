# APPSClone - Generate upload files

This subproject corresponds to the generation of upload files to be used by the **APPSClone** server.

An *upload file* is an ascii-based file that is sent to the server, so that it can, automatically, download Receiver Independent Exchange Format (**RINEX**) files from your server, process them and return the results back. It contains the following information:

```
The 'path' of the RINEX file of your server (absolute or home path)
The 'directory' to upload the results to (directory absolute or home path)
The 'IP' (IPV4) of your server
The 'username' to connect to the server to
The 'password' that corresponds to the given username
The 'processing mode'
The 'processing product'
The 'troposphere model'
The 'ocean loading' choice
The 'model tides' choice
The 'elevation dependent weighting' scheme
The 'elevation angle cutoff'
The 'solution period'
```

This program generates upload files by asking the user for this information in an interactive graphical user interface (GUI).
## Features

This project contains the following features:

* Manually generate upload files;
* Verify input (such as paths and the IP);
* Interaction via GUI.

## Possible future implementations

Possible future implementations include:

* Argument checking in case of elevation angle cutoff and solution period);
* GUI improving with real GUI.
## Installation

Setup the project by installing its dependencies and creating initial directories:

```bash
make setup
```

To change default directories or configurations, edit the `config/generator.cfg file`.
    
## Run

To run the project, type:

```bash
make run
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

This is the recommended testing type for this project, because the GUI will only be shown if printing is active.

To run all tests, run:

```bash
make testAll
```

To run all tests and print the output, run:
```bash
make testAllPrint
```
## Demo

<img src="[https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif](https://user-images.githubusercontent.com/61360702/177223351-5778b7ad-9336-4bf5-8fe6-5b03f3999a0a.gif)" width="40" height="40" />


## Documentation

The documentation for APPSClone upload file generator can be found [here](https://github.com/DuarteArribas/APPSClone/tree/main/development/APPSClone_UploadFileGenerator/docs).


## FAQ

#### Why not write the upload file without this tool?

You can! In fact, if automation is wished, it should be done without this tool. The problem is for people who don't know the exact upload arguments, e.g., and wish to use this tool as a means to not fail to write them.

## Lessons Learned

Working with [curses](https://docs.python.org/3/howto/curses.html) was a new experience and, while using [pick](https://pypi.org/project/pick/), resetting windows was a must. The tool revealed to be very important in not making mistakes when creating upload files for [APPSClone](https://github.com/DuarteArribas/APPSClone).
