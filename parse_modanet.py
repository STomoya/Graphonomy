
import os
import glob
from tqdm import tqdm

from networks import deeplab_xception_transfer
from exp.inference.inference import inference

images = glob.glob('/usr/src/data/modanet/images/*')
print('total images :'. len(images))

net = deeplab_xception_transfer.deeplab_xception_transfer_projection_savemem(n_classes=20,
                                                                                hidden_layers=128,
                                                                                source_classes=7, )

x = torch.load('inference.pth')
net.load_source_model(x)
net.cuda()
use_gpu = True

output_folder = '/usr/src/data/modanet/parse'

for path in tqdm(images):
    inference(
        net, path, output_folder,
        os.path.basename(path).split('.')[0], use_gpu
    )
