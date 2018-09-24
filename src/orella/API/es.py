import os
import base64

# location of folders used to store photos
parent_folder = os.path.join('G:/', 'Estate Agents')
# prefixes of folders used to store photos
# 1000: Key Agent, Taylor Made & Bespoke
# HSS: House simple
prefix = ('1000', 'HSS')


class Grab:

    @staticmethod
    def get_destination_folders():
        """ :return a tuple of folders from the 'parent_folder' with prefixes matching those stored in 'prefix'"""

        return [folder for folder in os.listdir(parent_folder) for cond in prefix if cond in folder]

    @staticmethod
    def upload(file):
        with open(os.path.join(file['folder'], file['name']), "wb") as photo:
            print(photo.write(base64.decodebytes(file['file'].encode())))


if __name__ == '__main__':
    print(*Grab.get_destination_folders(), sep='\n')
