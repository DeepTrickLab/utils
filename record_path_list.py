import os
import argparse
import glob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_folder', type=str)
    parser.add_argument('--output_filename')
    opts = parser.parse_args()
    nestedpath = glob.glob(os.path.join(opts.dataset_folder,'/*/*.jpg'))

    with open(os.path.join(opts.output_filename),'w') as infile:
        infile.write('')
        
    with open(os.path.join(opts.output_filename),'a') as infile:
        for path in list(nestedpath):
            infile.write(path)
            infile.write('\n')
