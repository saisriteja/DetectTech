import gdown

import os

# os.mkdir('/dataset')

url = 'https://googledrive.com/host/1a2oHjcEcwXP8oUF95qiwrqzACb2YlUhn'
output = 'train.zip'
gdown.download(url, output, quiet=False)


url = 'https://googledrive.com/host/1bxK5zgLn0_L8x276eKkuYA_FzwCIjb59'
output = 'val.zip'
gdown.download(url, output, quiet=False)

url = 'https://googledrive.com/host/1PFdW_VFSCfZ_sTSZAGjQdifF_Xd5mf0V'
output = 'test.zip'
gdown.download(url, output, quiet=False)