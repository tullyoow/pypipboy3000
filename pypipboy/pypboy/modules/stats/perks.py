from pypipboy import pypboy


class Module(pypboy.SubModule):

    label = "Perks"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
