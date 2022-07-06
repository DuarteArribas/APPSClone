class Helper:
  """Helper methods to other classes."""
  # == Methods ==
  @staticmethod
  def getFileFromPath(path):
    """Get a file, given its path.

    Parameters
    ----------
    path : str
      The path to gather the file from

    Returns
    ----------
    str
      The file from the file path
    """
    return path.split("/")[-1]

# ✓    unit tested
# ✓ feature tested