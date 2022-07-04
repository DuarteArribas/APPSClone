from appsclone_client.uploadFileGenerator import *
from appsclone_client.utils.config        import *

def main():
  # read configuration from config file
  cfg = Config("config/generator.cfg")
  # create generator object
  gen = UploadFileGenerator()
  # ask inputs
  gen.askUploadFileInputs(cfg.getOutConfig("UPLOAD_FILES_DIR"))
  # generate upload file
  gen.generateUploadFile(cfg.getOutConfig("UPLOAD_FILES_DIR"))

if __name__ == '__main__':
  main()