def find_it(seq):
    for x in seq:
        odd = seq.count(x)
        if (odd % 2 != 0):
            result = x
            break
    return result


if __name__ == "__main__":
    #test.describe("Example")
    #test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5) 
    print find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) 