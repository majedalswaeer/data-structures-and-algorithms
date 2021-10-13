from code_challenges.array_insert_shift_lab02.insert_shift_lab02 import insertShiftArray


def test_one_insertShiftArray():
    example=[1,2,3]
    middle_value=0
    expected=[1,2,0,3]
    actual=insertShiftArray(example,middle_value)
    assert actual==expected


def test_two_insertShiftArray():
    example=[1,2,3,4,5,6]
    middle_value=1
    expected=[1,2,3,1,4,5,6]
    actual=insertShiftArray(example,middle_value)
    assert actual==expected
