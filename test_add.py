#!/venv/Scripts/python

# # content of test_class.py
# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x
from todo_functions import add_task


class TestClass:
    def test_add_task_success(self):
        test_str = "add new pytask"
        test_file_path = "test.txt"
        add_task(test_file_path, test_str)

        with open("test.txt", "r") as file:
            cont = file.read()

        assert test_str[4::].capitalize() in cont
