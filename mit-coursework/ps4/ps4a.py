# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations_2(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    def permutation_sub(seq, index, ans):
        if index == len(seq):
            ans.append(seq)

        else:
            # print(seq, index, ans)
            # input('-----')
            for x in range(index, len(seq)):
                new_seq = seq
                if x != index:
                    # print(seq[:index], seq[x], seq[index+1:x], seq[index], seq[x+1:])
                    new_seq = seq[:index] + seq[x] + seq[index+1:x] + seq[index] + seq[x+1:]
                permutation_sub(new_seq, index+1, ans)

    ans = []
    permutation_sub(sequence, 0, ans)
    return ans

def get_permutations(sequence):
    if not sequence:
        return []
    elif len(sequence) == 1:
        return [sequence]
    else:
        sub_list = get_permutations_2(sequence[1:])
        ans = []
        for item in sub_list:
            for i in range(0, len(item)+1):
                new_sequence = item[:i] + sequence[0] + item[i:]
                ans.append(new_sequence)
        return ans


if __name__ == '__main__':
#    #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))

   data = {
       '': 0,
       'a': 1,
       'ab': 2,
       'abc': 6,
       'abcd': 24,
       'abcde': 120
   }

   for k, v in data.items():
       ans = get_permutations(k)
       assert len(ans) == v,  'Fail: the size of permutation of {} should be {}, but get {}'.format(k, v, len(ans))

   print('test success')
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # pass #delete this line and replace with your code here

