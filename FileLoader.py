import logging
from tkinter import filedialog
import pathlib
import os
#from PyScopeSettings import PyScopeSettings
#from PyScope import PyScope

class FileLoader(object):

    def __init__(self, my_files_dir):
        # Logging Parameters
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)

        self.raw_files_dir = my_files_dir
        self.logger.debug('FileLoader files DIR: --> %s' % self.raw_files_dir)
        self.get_files_list()
        #return

    def set_files_dir(self):
        # if base_location is None:
        # Check for config file
        #base_conf_file = 'base_loc_config.conf'
        p = pathlib.Path(os.getcwd() + '/config/')

        return

    def get_files_list(self):
        files_list = os.listdir(self.raw_files_dir)
        self.logger.debug('Number of files in DIR: --> %d' % len(files_list))

    def get_file(self):
        self.logger.debug('In File Load')
        #return file_object = open(self.raw_files_dir)

    def load_all_files_from_dir(self):
        return