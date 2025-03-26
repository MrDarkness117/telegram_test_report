def test_assert_correct():
    correct_result = "Чеддер"
    assert correct_result == "Чеддер"


def test_assert_wrong():
    correct_result = "Монолит - это архитектура"
    assert correct_result == "Монолит - это такая группировка в S.T.A.L.K.E.R."
