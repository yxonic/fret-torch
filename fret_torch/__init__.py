import torch
import fret.common


class FretTorchPlugin(fret.common.Plugin):
    def apply(self, ws):
        setattr(ws, 'save_to_file', torch.save)
        setattr(ws, 'load_from_file', torch.load)


fret_torch_plugin = FretTorchPlugin()
