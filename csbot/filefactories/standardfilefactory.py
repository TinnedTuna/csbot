
class StandardFileFactory():

    def __init__(self, base_dir=None):
        if (base_dir is not None):
             self.base_dir = base_dir
        else:
            base_dir = ''

    def open_file(file_name, mode):
        return open(base_dir+'/'+file_name, mode)
