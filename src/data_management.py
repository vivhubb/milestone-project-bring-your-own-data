import os


def split_train_validation_test_data(my_data_dir, train_set_ratio, validation_set_ratio, test_set_ratio):

    if train_set_ratio + validation_set_ratio + test_set_ratio != 1.0:
        print("train_set_ratio + validation_set_ratio + test_set_ratio should sum to 1.0")
        return

    if 'test' in os.listdir(my_data_dir):
        return
    else:
        ratio = 0
        prev_ratio = 0

        for folder in ['train', 'validation', 'test']:
            os.makedirs(name=my_data_dir + '/' + folder )

            if folder == 'train':
                ratio = data.shape[0] - int((data.shape[0] * train_set_ratio))
            elif folder == 'validation':
                ratio = data.shape[0] - int((data.shape[0] * validation_set_ratio))                
            else:
                ratio = data.shape[0] - int((data.shape[0] * test_set_ratio))

            with open(my_data_dir + f'/{folder}/{folder}.csv', 'w') as f:
                f.write(','.join(list(data.keys()[1:])) + '\n')

                for line in [x[1:] for x in data.values.tolist()[prev_ratio: prev_ratio + ratio]]:
                    f.write(','.join([str(x) for x in line]) + '\n')


            prev_ratio = ratio
