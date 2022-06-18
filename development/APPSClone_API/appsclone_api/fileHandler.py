import os.path
from os import listdir

class FileHandler:
  """
  """
  # == Attributes ==
  # == Methods ==
  @staticmethod
  def getUploadFiles(uploadFilesDirectory):
    uploadFiles = os.listdir(uploadFilesDirectory)
    uploadFiles = FileHandler.getValidatedListOfUploadFiles(uploadFiles)
    return 

  @staticmethod
  def isValidUploadFile(uploadFile):
    if os.path.isfile(uploadFile):
      with open(file,"r") as f:
        lines = f.readlines()
        lines = FileHandler.cleanEmptyFieldsInList(lines)
        if lines[0].strip() != "" and lines[1].strip() != "" and lines[2].strip() != "":
          pass
    else:
      return False

  @staticmethod
  def cleanEmptyFieldsInList(lst):
    """Clean the empty (stripped) fields in a list.

    Parameters
    ----------
    lst : list
      The list to cleanup

    Returns
    ----------
    list
      The list without any empty (stripped) fields
    """
    return [item for item in lst if item.strip()]


  @staticmethod
  def parseUploadFile(file):
    with open(file,"r") as f:
      lines              = f.readlines()
      pathToDownloadFrom = lines[0]
      pathToUploadTo     = lines[1]
      ipToConnect        = lines[2]
      return pathToDownloadFrom,pathToUploadTo,ipToConnect

