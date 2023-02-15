_base_ = './faster_rcnn_orpn_r50_fpn_1x_ms_rr_dota10.py'

# model
model = dict(pretrained='torchvision://resnet101', backbone=dict(depth=101))
