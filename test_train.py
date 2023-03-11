import os
import random
import shutil
import argparse

def split_data(source, training_pct, output_folder):
    files = []
    for filename in os.listdir(source):
        file_path = os.path.join(source, filename)
        if os.path.getsize(file_path) > 0:
            files.append(filename)
        else:
            print('{} is zero length, so ignoring.'.format(filename))


    training_count = int(len(files) * training_pct)
    test_count = len(files) - training_count
    shuffled_files = random.sample(files, len(files))
    training_files = shuffled_files[:training_count]
    test_files = shuffled_files[-test_count:]

    train_folder = os.path.join(output_folder, 'train')
    test_folder = os.path.join(output_folder, 'test')
    os.makedirs(train_folder)
    os.makedirs(test_folder)

    # Copy training files to train folder
    print('Copying {} files to {}'.format(len(training_files), train_folder))
    for filename in training_files:
        this_file_path = os.path.join(source, filename)
        destination_path = os.path.join(train_folder, filename)
        shutil.copyfile(this_file_path, destination_path)

    # Copy test files to test folder
    print('Copying {} files to {}'.format(len(test_files), test_folder))
    for filename in test_files:
        this_file_path = os.path.join(source, filename)
        destination_path = os.path.join(test_folder, filename)
        shutil.copyfile(this_file_path, destination_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='data', help='Path to the source directory')
    parser.add_argument('--training_pct', type=float, default=0.8, help='Percentage of files to use for training')
    parser.add_argument('--output_folder', type=str, default='output', help='Name of the output folder')
    args = parser.parse_args()

    split_data(args.source, args.training_pct, args.output_folder)

