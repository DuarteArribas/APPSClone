# == LOGGING STRINGS ==
# = Argument parser =
# Routines
getOptions                    = "Options for command line-arguments"
# Other
uploadArg                     = "Attempting to upload file"
downloadArg                   = "Attempting to download file"
unknownUploadOrDownloadArg    = "The argument '{arg}' is unknown"
rinexArg                      = "The file to upload is '{file}'"
unknownRinexArg               = "The file '{file}' does not exist"
noRinexArg                    = "There isn't an input file in the arguments"
upArg                         = "The value for the argument '{arg}' is '{argValue}'"
# = SSHConnection =
# Routines
sshConnect                    = "Connect to '{ip}:{port}', with user '{username}'"
# Other
sshConnectSuccessful          = "Successfully established a connection to the server"
sshConnectUnsuccessfulBadIP   = "Could not establish a connection to the server, because the ip '{ip}' is not valid or is unavailable"
sshConnectUnsuccessfulBadPort = "Could not establish a connection to the server, because the port '{port}' is not valid or is unavailable"
sshConnectUnsuccessfulBadUser = "Could not establish a connection to the server, because the user '{username}' is not valid or the password is incorrect"
criticalSSHException          = "Could not establish a connection to the server, because of an unknown reason"
scpGetSuccessful              = "Successfully copied remote file '{file}' to local directory '{df}'"
scpGetUnsuccessful            = "Could not copy remote file '{file}' to local directory '{df}'"
scpPutSuccessful              = "Successfully copied local file '{file}' to remote directory '{df}'"
scpPutUnsuccessful            = "Could not copy local file '{file}' to remote directory '{df}'"