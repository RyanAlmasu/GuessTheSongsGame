from project import select_music, question, get_result


def test_select_music():
    assert select_music(['I dont love you (2006)']) == ('I dont love you', '2006')
    assert select_music(['I dont love you (200)']) == None
    assert select_music(['I dont love you 2006']) == None
    assert select_music(['I dont love you(2006)']) == None


def test_question():
    assert question('Helena') == ['_','_','_','_','_','_']
    assert question('Helena') == ['_','_','_','_','_','_']
    assert question('Helena 2') == ['_','_','_','_','_','_', ' ', '_']
    assert question('Helena: 2') == ['_','_','_','_','_','_', ':', ' ', '_']


def test_get_result():
    assert get_result(True) == 'Correct!'
    assert get_result(False) == 'Incorrect, try again!'