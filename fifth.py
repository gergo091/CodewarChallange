def get_middle(s):
    length = len(s)
    mid = length % 2
    res = length / 2
    if (mid == 0):
        return s[(res-1):res+1]
    else:
        return s[res]



if __name__ == "__main__":
    print get_middle("of")
    # Test.assert_equals(get_middle("test"),"es")
    # Test.assert_equals(get_middle("testing"),"t")
    # Test.assert_equals(get_middle("middle"),"dd")
    # Test.assert_equals(get_middle("A"),"A")
    # Test.assert_equals(get_middle("of"),"of")