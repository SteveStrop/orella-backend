import os
import re
import ptpy as pt
from shutil import rmtree
from .config import *


# JOBS_FOLDER = 'G:/Estate Agents'  # location of job folders
# CACHE = 'G:/Imports'  # location of local cache
# PREFIX = ('1000', 'HSS')  # list of job folder prefixes


class Grab:

    @staticmethod
    def download(name, folder, image):
        try:
            with open(os.path.join(folder, name), "wb") as photo:
                photo.write(image)
        except OSError:
            return 'Error writing photo to local drive'
        return 'OK'

    @staticmethod
    def get_destination_folders():
        """ :return a tuple of folders from the 'jobs_folder' with prefixes matching those stored in 'prefix'"""

        return [folder for folder in os.listdir(JOBS_FOLDER) for cond in PREFIX if re.match(cond, folder)]

    @staticmethod
    def quit():
        # empty the import folder
        try:
            rmtree(CACHE, ignore_errors=True)
        except TypeError:  # if no files have been imported cache is None
            pass

        # TODO move folders to in progress folders
        # TODO close open cmd windows
        # TODO open bridge


class Photo:

    def __init__(self, camera, handle):
        self.name = camera.camera.get_object_info(handle).Filename
        self.date = str(camera.camera.get_object_info(handle).CaptureDate).split()[0]
        self.data = camera.camera.get_object(handle).Data
        self.camera_folder = str(camera.camera.get_object_info(handle).ParentObject)
        self.local_folder = None

    def download(self):
        with open(os.path.join(self.local_folder, self.name), mode='wb') as f:
            f.write(self.data)

    def create_folder(self):
        try:
            os.makedirs(self.local_folder)
        except FileExistsError:
            pass


class Camera:
    """ contains a model of the folders and photos stored on the camera sd card"""

    def __init__(self):
        self.handles = None
        self.photos = None
        self.response = self.__camera_connect__()

    def read_photos(self):
        print('accessing camera storage...')
        with self.camera.session():
            self.handles = self.camera.get_object_handles(0, all_storage_ids=True, all_formats=True)
            self.photos = [Photo(self, handle) for handle in self.handles
                           if str(self.camera.get_object_info(handle).ParentObject).startswith('3')]

    def get_photos(self):
        print('downloading photos...')
        for photo in self.photos:
            photo.create_folder()
            photo.download()

    def set_local_folders(self):
        folders = sorted(set([photo.camera_folder for photo in self.photos]))
        d = {item: i for i, item in enumerate(folders)}
        for photo in self.photos:
            photo.camera_folder = f'ND8001{d[photo.camera_folder]:02}'
            photo.local_folder = os.path.join(CACHE, photo.camera_folder)

    def __camera_connect__(self):
        while True:
            print('connecting to camera')
            try:
                self.camera = pt.PTPy()
            except pt.ptp.PTPError:  # camera not connected
                print('Camera not connected. Connect camera then press any key to continue')
                return False
            else:
                self.read_photos()
                self.set_local_folders()
                self.get_photos()
                return True


if __name__ == '__main__':
    camera = Camera()
