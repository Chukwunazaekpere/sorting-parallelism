"""
Author: Chukwunazaekpere Emmanuel Obioma
Lecture: Sorting
Nationality: Biafran
Email-1: chukwunazaekpere.obioma@ue-germany.de 
Email-2: ceo.naza.tech@gmail.com
************************************************
Implementation: to implement the sequential sorting of arrays, using the last-index sorting algorithm
Course: Multi-core Programming
Written: Nov 2nd 2024
Due: Nov 3rd 2024
"""

from multiprocessing import Pool, Process, cpu_count
import math
from datetime import datetime
import random
from time import time
import logging
logger = logging.getLogger(__name__)
log_date = datetime.now()
logging.basicConfig(level=logging.INFO)



class Last_Index_Sequential_Soerting():
    """The name of this sorting algorithm, as designed by me, is referred to as 'last-index' or 'Bende' sorting. The algorithm begins by comparing
    the element at index zero, to the last element in the array(or element at index: -1). If it 
    finds that the element at zero index, is greater than that at index -1, it swaps the indices of the 
    elements. Otherwise, it skips. Then, it moves to the element at index 1 and repeats. After going through the 
    elements for the first iteration, it reduces the length of the array by 1, as it no longer makes comparison with the 
    element at index -1. The second iteration is now, between the elements with that at index -2, which at this point, is
    likened as the element at the last index"""
    def __init__(self):
        self.list_length = 0

    def get_random_list_length(self):
        """Get input from user as to the length of the list to be generated"""
        logging.info(msg=f"\n\t {datetime.now()} This is the sequential sorting of the last-index sorting algorithm...")
        try:
            sort_list_length = input("\n\t Please enter a list length: ")
            self.list_length = int(sort_list_length)
        except Exception as err:
            return f"List length unacceptable. Please enter a number."

    def generate_random_list(self):
        """generate random list elements between 1 & 500"""
        list_to_sort = []
        while len(list_to_sort) < self.list_length:
            value = random.randint(1, 500) # random elements between 1 & 500
            list_to_sort.append(value)
        return list_to_sort
    
    def last_index_sorting(self, random_list):
        random_list_to_sort = random_list
        list_length = len(random_list_to_sort)
        while list_length > 1:
            current_last_index = -list_length+1
            for item_index, item in enumerate(random_list_to_sort):
                if item > random_list_to_sort[current_last_index]:
                    current_last_value = random_list_to_sort[current_last_index]
                    current_index_value = random_list_to_sort[item_index]
                    # Swap last index value, with current index value
                    random_list_to_sort[current_last_index] = current_index_value
                    random_list_to_sort[item_index] = current_last_value
            list_length-=1 # This automatically cuts down or reduces the length of the list to be compared
        return random_list_to_sort
    


if __name__ == "__main__":
    # print("Number of cpu :  ", multiprocessing.cpu_count())
    sort_list = Last_Index_Sequential_Soerting()
    random_list_length = sort_list.get_random_list_length()
    if random_list_length == None:
        with Pool(processes=(cpu_count()-1)) as pool:
            start_time = time()
            random_list = sort_list.generate_random_list()
            # logging.info(msg=f"\n\tThe generated random list of length {len(random_list)} is: {random_list}")
            sorted_list = pool.apply_async(sort_list.last_index_sorting, [random_list])
            # logging.info(msg=f"\n\tThe sorted list of length {len(random_list)} is: {sorted_list}") # without viewing results
            logging.info(msg=f"\n\tThe sorted list of length {len(random_list)} is: {sorted_list}") # viewing results
            end_time = time()
            logging.info(msg=f"\n\t total time taken: {(end_time-start_time)} secs")
    else:
        print(random_list_length)