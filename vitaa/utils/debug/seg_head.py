import numpy as np
from PIL import Image
import os

from vitaa.utils.debug.utils import mkdir

def get_palette(n):
    palette = [0,] * (n*3)
    for i in range(n):
        lab = i
        palette[i*3 + 0] = 0
        palette[i*3 + 1] = 0
        palette[i*3 + 2] = 0
        j = 0
        while lab:
            palette[i*3 + 0] |= (((lab >> 0) & 1) << (7-j))
            palette[i*3 + 1] |= (((lab >> 1) & 1) << (7-j))
            palette[i*3 + 2] |= (((lab >> 2) & 1) << (7-j))
            j = j + 1
            lab >>= 3
    return palette

def save_seg_head(seg_feats, save_dir, image_path_list):
    palette = get_palette(256)
    seg_feats =seg_feats.cpu().numpy().astype(np.uint8).copy()
    seg_head_name_set = set()

    for i in range(seg_feats.shape[0]):
        if image_path_list[i] not in seg_head_name_set:
            seg_head_name_set.add(image_path_list[i])
            seg_feat = seg_feats[i]
            save_seg = Image.fromarray(seg_feat)
            save_seg.putpalette(palette)


            relative_file_name, file_name = '/'.join(image_path_list[i].split('/')[:-1]), image_path_list[i].split('/')[-1]
            file_name = file_name.split('.')[0]
            path = os.path.join(save_dir, relative_file_name)
            mkdir(path)
            save_seg.save(os.path.join(path ,file_name+'.png'))