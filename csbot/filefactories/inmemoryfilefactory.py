

class MemoryFile():
    def __init__(self, file_name, mode):
        self.file_name = file_name;
        self.mode = mode;
        self.contents = ''
        self.current_line = 0

    def write(self, inStr):
        self.contents = self.contents + inStr;

    def flush(self) :
        # This is not applicable to this obj.
        pass
  
    def readline(self):
       curr_line = string.split(self.contents, '\n')[self.current_line] 
       self.current_line += 1
       return curr_line


class InMemoryFileFactory():

  def __init__(self, base_dir=None):
    pass # We ignore the base_directory
    self.files = []

  def open_file(self, file_name, mode):
    curr = MemoryFile(file_name, mode)
    self.files.append(curr)
    return curr
