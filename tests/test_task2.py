import pytest
from lab4_oop.tasks.task2 import Root, Linear, Square, Reader, print_result


def test_root_is_abstract():
    with pytest.raises(TypeError):
        Root()


def test_derived_classes():
    assert issubclass(Linear, Root)
    assert issubclass(Square, Root)


def test_linear_one_root():
    lin = Linear(2, -4)
    lin.calc_roots()
    assert lin.roots == [2.0]
    assert "x = 2.0" in str(lin)


def test_linear_no_roots():
    lin = Linear(0, 5)
    lin.calc_roots()
    assert lin.roots == []
    assert "корней нет" in str(lin)


def test_linear_any_number():
    lin = Linear(0, 0)
    lin.calc_roots()
    assert lin.roots == []
    assert "любое число" in str(lin)


def test_square_two_roots():
    sq = Square(1, -3, 2)
    sq.calc_roots()
    assert sq.roots == [1.0, 2.0]
    assert "x1 = 1.0, x2 = 2.0" in str(sq)


def test_square_one_root():
    sq = Square(1, 2, 1)
    sq.calc_roots()
    assert sq.roots == [-1.0]
    assert "x = -1.0" in str(sq)


def test_square_no_roots():
    sq = Square(1, 0, 1)
    sq.calc_roots()
    assert sq.roots == []
    assert "действительных корней нет" in str(sq)


def test_square_a_is_zero():
    sq = Square(0, 2, 1)
    sq.calc_roots()
    assert sq.roots == []
    assert "не квадратное уравнение" in str(sq)


def test_show(capsys):
    lin = Linear(2, -4)
    lin.calc_roots()
    lin.show()
    assert capsys.readouterr().out.strip() == str(lin)


def test_print_result(capsys):
    lin = Linear(2, -4)
    print_result(lin)
    assert lin.roots == [2.0]
    assert "x = 2.0" in capsys.readouterr().out


def test_print_result_list(capsys):
    equations = [Linear(2, -4), Square(1, -3, 2)]
    for eq in equations:
        print_result(eq)
    out = capsys.readouterr().out
    assert "x = 2.0" in out
    assert "x1 = 1.0, x2 = 2.0" in out


def test_reader_read_float(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "3.5")
    assert Reader().read_float("a = ") == 3.5
