import os

if os.path.exists("ipOutput.txt"):
    def test_checkTextFileLength():
            assert os.stat("ipOutput.txt").st_size != 0