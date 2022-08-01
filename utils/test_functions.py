import pytest

from coursework2_source.utils import read_function

file_param = [
    (list, r"C:\Users\anna1\skypro_lessons\Cours_work_3\coursework2_source\data\data.json"),
    # (FileNotFoundError, r"C:\Users\anna1\skypro_lessons\Cours_work_3\coursework2_source\data\dat.json"),
    # (ValueError, r"C:\Users\anna1\skypro_lessons\Cours_work_3\coursework2_source\data\test.json"),
    (str, r"C:\Users\anna1\skypro_lessons\Cours_work_3\coursework2_source\utils\utils.py"),
]

@pytest.mark.parametrize("typeof_, path_", file_param)
def test_reading_function(typeof_, path_):
    assert type(read_function(path_)) == typeof_

file_param_except = [
    (FileNotFoundError, r"C:\Users\anna1\skypro_lessons\Cours_work_3\coursework2_source\data\dat.json"),
    (ValueError, r"C:\Users\anna1\skypro_lessons\Cours_work_3\coursework2_source\data\test.json"),
]
@pytest.mark.parametrize("exception, path_", file_param_except)
def test_reading_function_except(exception, path_):
    with pytest.raises(exception):
        read_function(path_)