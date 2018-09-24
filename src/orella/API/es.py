import os

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


if __name__ == '__main__':
    print(*Grab.get_destination_folders(), sep='\n')
