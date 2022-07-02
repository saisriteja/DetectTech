import gdown

import os

# os.mkdir('/dataset')

url = 'https://drive.google.com/uc?id=1a2oHjcEcwXP8oUF95qiwrqzACb2YlUhn'
output = '/dataset/train.zip'
gdown.download(url, output, quiet=False)


url = 'https://drive.google.com/uc?id=1bxK5zgLn0_L8x276eKkuYA_FzwCIjb59'
output = '/dataset/val.zip'
gdown.download(url, output, quiet=False)

url = 'https://drive.google.com/uc?id=1PFdW_VFSCfZ_sTSZAGjQdifF_Xd5mf0V'
output = '/dataset/test.zip'
gdown.download(url, output, quiet=False)