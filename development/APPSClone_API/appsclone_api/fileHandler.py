
class FileHandler:
  """
  """
  # == Attributes ==
  # == Methods ==
  def __init__(self,settingsFile,downloadDirectory,loggingFile,maxLogs):
    """Connects to APPS and initalizes the logger."""
    self.apps              = APPS(settings_file = settingsFile,download_directory = downloadDirectory)
    self.logger            = Logs(loggingFile,maxLogs)