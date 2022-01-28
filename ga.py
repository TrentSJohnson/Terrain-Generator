import itertools
import os

import numpy as np
from PIL import Image
from geneal.genetic_algorithms import BinaryGenAlgSolver
from tqdm import tqdm

image_size = (1596*2,1078*2)

def num_arr_to_im_arr(num_arr):
    numbersnp = np.zeros(image_size[::-1]).astype(np.int32)
    i = 0
    for p in range(int(len(num_arr) / 4)):
        num = bit_im[tuple(num_arr[4 * p:4 * p + 4])]
        r=int(p / image_letter_size[0])*7
        c=(p % image_letter_size[0])*7
        numbersnp[r:r+7,c:c+7] = num

    return numbersnp

if __name__ == '__main__':
    image_size_str = str(image_size[0]) + '_' + str(image_size[1])
    image_letter_size = (int(image_size[0] / 7), int(image_size[1]/7))
    for file_name in tqdm(os.listdir(f'landscapes_{image_size_str}/')):
        if '.jpg' in file_name:
            number_pngs = os.listdir('number_pngs')
            bit_im = {}

            for i, bit_arr in enumerate(list(itertools.product([0, 1], repeat=4))):
                if i < len(number_pngs) - 1:
                    im_ = Image.open('number_pngs/' + number_pngs[i + 1])
                else:
                    im_ = Image.open('number_pngs/_.png')
                bit_im[bit_arr] = np.average(np.array(im_.getdata()), axis=-1).reshape(im_.size[0], im_.size[1]).astype(np.int32)

            reference = Image.open(f'landscapes_{image_size_str}/' + file_name)
            #print(np.array(reference.getdata()).shape)
            reference_arr = np.average(np.array(reference.getdata()), axis=-1).reshape(reference.size[0],
                                                                                       reference.size[1]).astype(np.int32)
            reference_arr_flat = reference_arr.flatten()

            #print(reference.size)
            def fit_func(spec):
                numbersnp = num_arr_to_im_arr(spec)
                flat_numbers = numbersnp.flatten()
                error = np.sum((flat_numbers - reference_arr_flat) ** 2)
                return -error


            solver = BinaryGenAlgSolver(
                n_genes=int(image_size[0] * image_size[1] / 49),  # number of variables defining the problem
                n_bits=4,
                fitness_function=fit_func,
                max_gen=20,
                plot_results=True,
                verbose=True
            )

            best = solver.solve()[0]
            best_im = num_arr_to_im_arr(best)
            num_im = Image.fromarray(best_im).convert('RGB')
            num_im.save(f'landscapes_{image_size_str}_number/{file_name}')

