# This code is meant to solve a problem on a CTF. The problem was called funsum.
# Technically, the code should work to find the the number 12345 in a list of sequential number.
# The problem is that I am basically brute forcing the function that finds all of the possible combinations of a list of numbers.
# After a few digists into the list, the calculations become to expensive for the CPU.
# Please help make this better.
# The commented out generator below is meant to provide the code with starting point
# num_list = [num for num in range(13, 20)] 
num_list = [13, 14, 15, 16, 17, 18, 19]


def base_args(lst: list):
    """Returns a list of single digit nums in string format"""
    temp_lst = [[num for num in str(element)] for element in lst]
    num_list = sum(temp_lst, [])
    num_list = [num_list]
    return num_list


def perm(ref_lst: list, main_list: list,  reference: int):
    """Creates a list of lists of some of the possible numbers
    Also, this kinda brute forces the list so it will get expensive quick"""
    for num, _ in enumerate(ref_lst):
        index = num
        temp_list = ref_lst.copy()
        temp_list[index:index + reference-1] = [''.join(temp_list[index:index+reference-1])]
        if temp_list not in main_list and '' not in temp_list:
            main_list.append(temp_list)
            temp_list = []
        else:
            temp_list = []


def create(nums: list):
    """Returns the full list of lists of all possible number combinations"""
    round = 0
    ref = len(nums[0])
    try:
        while True:
            for ref_num in range(3, ref+1):
                perm(nums[round], nums, ref_num)
            round += 1
    except IndexError:
        print('Done')
    return nums


def funsum(str_list: list):
    """This simply adds all elements of a list together"""
    num_list = [int(num) for num in str_list]
    return sum(num_list)


def main():
    count = 2
    results = {}
    for _ in range(len(num_list)):
        start_list = base_args(num_list[:count])
        fun_list = create(start_list)
        ser_list = [funsum(item) for item in fun_list]
        results.update({num_list[count-1]: ser_list})
        if 12345 in results[num_list[count-1]]:
            print(results)
            break
        else:
            count += 1
            results = {}
            continue


if __name__ == '__main__':
    main()
