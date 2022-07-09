# == LOGGING STRINGS ==
# = Argument parser =
# Routines
getOptions                    = "Options for command line-arguments"
# Other
uploadArg                     = "Upload argument recognized"
downloadArg                   = "Download argument recognized"
unknownUploadOrDownloadArg    = "The argument '{arg}' is unknown"
rinexArg                      = "The file to upload is '{file}'"
unknownRinexArg               = "The file '{file}' does not exist. Please move the file to the correct upload folder (defined in config/client.cfg)"
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
# = APPSClone client =
# Routines
clientRun                     = "APPSClone client socket connection"
# Other
criticalSocket                = "Could not connect to socket on '{ip}:{port}'"
uploadInfoSent                = "Upload info of file {file} sent to APPSClone server"
responseReceived              = "A response has been received from the APPSClone server"
responseError                 = "The server responded with an error - '{errorMsg}'"
responseUploadSuccess         = "The upload of the file {file} was a success"
addToQueueSuccess             = "The id {id} was added to the queue successfully"
removeFromQueueSuccess        = "The id {id} was removed from the queue successfully"
fileRemovedSuccess            = "The file {file} was removed with success"
downloadInfoSent              = "Asking to download results of file with id {id} from APPSClone server"
noIds                         = "There are no ids to check"
someIds                       = "There are {numIds} ids in the queue"