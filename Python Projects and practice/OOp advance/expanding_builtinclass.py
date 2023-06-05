"""--------------------------Expanding the builtin classes-------------------------"""


'''class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate().lower())'''


class TaskList(list):

    def append_chars(self, object):
        print("Append called")
        super().append(object)


list = TaskList()
list.append_chars("1")


