# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
"""Centralized catalog of paths."""

import os


class DatasetCatalog(object):
    DATA_DIR = "datasets"
    DATASETS = {
        "vnpersonsearch3k_train": {
            "img_dir": "vn_person_search_3k",
            "ann_file": "vn_person_search_3k/annotations/train.json"
        },
        "vnpersonsearch3k_valid": {
            "img_dir": "vn_person_search_3k",
            "ann_file": "vn_person_search_3k/annotations/val.json"
        },
        "vnpersonsearch3k_test": {
            "img_dir": "vn_person_search_3k",
            "ann_file": "vn_person_search_3k/annotations/test.json"
        },
        # "market1501_train": {
        #     "img_dir": "market1501",
        #     "ann_dir": "market1501/annotations"
        # },
        # "market1501_test": {
        #     "img_dir": "market1501",
        #     "ann_dir": "market1501/annotations"
        # },
        # "dukemtmc_train": {
        #     "img_dir": "dukemtmc",
        #     "ann_dir": "dukemtmc/annotations"
        # },
        # "dukemtmc_test": {
        #     "img_dir": "dukemtmc",
        #     "ann_dir": "dukemtmc/annotations"
        # },
    }

    @staticmethod
    def get(name):
        if "vnpersonsearch3k" in name:
            data_dir = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                root=os.path.join(data_dir, attrs["img_dir"]),
                ann_file=os.path.join(data_dir, attrs["ann_file"]),
            )
            return dict(
                factory="VNpersonsearch3k",
                args=args,
            )
        # elif "market1501" in name:
        #     data_dir = DatasetCatalog.DATA_DIR
        #     attrs = DatasetCatalog.DATASETS[name]
        #     args = dict(
        #         root=os.path.join(data_dir, attrs["img_dir"]),
        #         ann_root=os.path.join(data_dir, attrs["ann_dir"]),
        #     )
        #     return dict(
        #         factory="Market1501Dataset",
        #         args=args,
        #     )
        # elif "dukemtmc" in name:
        #     data_dir = DatasetCatalog.DATA_DIR
        #     attrs = DatasetCatalog.DATASETS[name]
        #     args = dict(
        #         root=os.path.join(data_dir, attrs["img_dir"]),
        #         ann_root=os.path.join(data_dir, attrs["ann_dir"]),
        #     )
        #     return dict(
        #         factory="DukeMTMCDataset",
        #         args=args,
        #     )
        raise RuntimeError("Dataset not available: {}".format(name))