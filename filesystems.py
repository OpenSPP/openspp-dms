import io

from pyftpdlib.filesystems import AbstractedFS


class OpenSPPFS(AbstractedFS):
    def open(self, filename, mode):
        # TODO: Save the file in memory and upload to openspp
        mem_file = self.save_to_memory(filename, mode)
        self.upload_to_openspp(mem_file)
        return mem_file

    def save_to_memory(self, filename, mode):
        with open(filename, mode) as source_file:
            data = source_file.read()
        return io.StringIO(data)

    def upload_to_openspp(self, file):
        pass

    def listdir(self, path):
        """Don't return anything."""
        return []
