import os
import shutil
import tempfile


def check_name(name):
    tmp_dir = tempfile.mkdtemp()
    try:
        open(os.path.join(tmp_dir, name), "a").close()
    except IOError:
        return False
    finally:
        shutil.rmtree(tmp_dir)
    return True
