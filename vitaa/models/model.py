import torch
from torch import nn

from .backbones.resnet import build_resnet
from .backbones.lstm import build_lstm
from .embeddings.embed import build_embed
from vitaa.utils.debug.seg_head import save_seg_head

class ViTAA(nn.Module):

    def __init__(self, cfg):
        super(ViTAA, self).__init__()
        self.visual_model = build_resnet(cfg)
        self.textual_model = build_lstm(cfg, bidirectional=True)
        self.embed_model = build_embed(
            cfg,
            self.visual_model.out_channels,
            self.textual_model.out_channels
        )

    def forward(self, images, captions, only_img=False):
        visual_feat = self.visual_model(images)
        textual_feat = self.textual_model(captions)
        attributes = [caption.get_field('attribute') for caption in captions]
        attribute_feat = self.textual_model(attributes)
        
        seg_head_name_list = [caption.get_field('img_path') for caption in captions]

        outputs_embed, losses_embed = self.embed_model(
            visual_feat, textual_feat, attribute_feat, captions)

        if self.training:
            losses = {}
            losses.update(losses_embed)
            return losses
        else:
            save_seg_head(seg_feats=outputs_embed[5], 
                    save_dir="./output/debug_ouput", 
                    image_path_list = seg_head_name_list)
        
        

        return outputs_embed


def build_model(cfg):
    return ViTAA(cfg)