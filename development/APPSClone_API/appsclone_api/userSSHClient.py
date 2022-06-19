class UserSSHClient:
  """A user, which will connect via ssh."""
  # == Methods ==
  def __init__(self,username,password):
    """Initialize a user"""
    self.username = username
    self.password = password