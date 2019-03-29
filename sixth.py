def maxSequence(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

if __name__ == "__main__":
    print maxSequence([])
    # test.describe("Tests")
    # test.it('should work on an empty array')   
    # test.assert_equals(maxSequence([]), 0)
    # test.it('should work on the example')
    # test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)