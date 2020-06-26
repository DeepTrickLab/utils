import os
import glob
import argparse
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_folder', type=str)
    parser.add_argument('--dist_folder', type=str)
    opts = parser.parse_args()

    file_list = glob.glob(os.path.join(opts.dataset_folder, '*.jpg'))
    file_list = [filename.split('/')[-1] for filename in list(file_list)]
    file_class = list(set([filename.split('-')[0] for filename in file_list]))
    cls_dict = {className.split('-')[0]: [] for className in file_class}
    for filename in file_list:
        cls_dict[filename.split('-')[0]].append(filename)
    for className in cls_dict:
        class_path = (os.path.join(opts.dist_folder,className))
        if not os.path.exists(class_path):
            os.makedirs(class_path)
        for filename in cls_dict[className]:
            print("source: "+ os.path.join(opts.dataset_folder, filename))
            print("dist: " + class_path)
            shutil.copyfile(os.path.join(opts.dataset_folder, filename), os.path.join(class_path, filename))
        