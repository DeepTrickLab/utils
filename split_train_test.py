import os
import argparse
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    parser.add_argument('--percentage', type=int, default=0.8)
    parser.add_argument('--ds_name', type=str, default='')
    parser.add_argument('--output_name', type=str, default='list')
    opts = parser.parse_args()

    img_list = []
    with open(list_filename, 'r') as infile:
        for line in infile.readlines():
            img_path = line.strip()
            img_list.append(img_path)

    classes = sorted(list(set([path.split('/')[0] for path in img_list])))
    n_cls = len(classes)
    n_train_cls = round(n_cls * opts.percentage)
    n_test_cls = n_cls - n_train_cls
    train_classes = random.choices(classes, k=n_train_cls)
    test_classes = [i for i in classes if i not in train_classes]

    list_name = opts.ds_name + '_' + opts.output_name
    train_list_name = list_name + '_' + 'train.txt'
    test_list_name = list_name + '_' + 'test.txt'
    with open(train_list_name, 'r') as infile, open(test_list_name, 'r') as infile2:
        infile.write('')
        infile2.write('')

    with open(train_list_name, 'a') as train_file, open(test_list_name, 'a') as test_file:
        for img_path in img_list:
            img_class = img_path.split('/')[0]
            kind = ''
            if img_class in train_classes:
                train_file.write(img_path)
                train_file.write('\n')
                kind = 'train'
            else:
                test_file.write(img_path)
                test_file.write('\n')
                kind = 'test'
            print('%s in %s' % (img_path, kind))
