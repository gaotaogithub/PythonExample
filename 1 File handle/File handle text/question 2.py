"""Write a method/function DISPLAYWORDS() in python to read lines
 from a text file STORY.TXT,
 using read function
and display those words, which are less than 4 characters."""

print("Hey!! You can print the word which are less then 4 characters")


def display_words(file_path):
    try:
        with open(file_path) as F:
            words = F.read().split()  #read and split into words,default spolit by space
            words_less_than_40 = list(filter(lambda word: len(word) < 4, words))  #lambda function 匿名函数 用于过滤  filter函数 过滤器,过滤可迭代对象

            for word in words_less_than_40:
                print(word)

        return (
            "The total number of the word's count which has less than 4 characters",
            (len(words_less_than_40)),
        )

    except FileNotFoundError:   #FileNotFoundError 文件未找到错误  内置异常  当尝试打开一个不存在的文件时引发，其他内置异常还有 ValueError,TypeError,IndexError 等，如何查看所有内置异常  https://docs.python.org/3/library/exceptions.html
        print("File not found")


# BaseException
#  ├── BaseExceptionGroup
#  ├── GeneratorExit
#  ├── KeyboardInterrupt
#  ├── SystemExit
#  └── Exception
#       ├── ArithmeticError
#       │    ├── FloatingPointError
#       │    ├── OverflowError
#       │    └── ZeroDivisionError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ExceptionGroup [BaseExceptionGroup]
#       ├── ImportError
#       │    └── ModuleNotFoundError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       │    └── UnboundLocalError
#       ├── OSError
#       │    ├── BlockingIOError
#       │    ├── ChildProcessError
#       │    ├── ConnectionError
#       │    │    ├── BrokenPipeError
#       │    │    ├── ConnectionAbortedError
#       │    │    ├── ConnectionRefusedError
#       │    │    └── ConnectionResetError
#       │    ├── FileExistsError
#       │    ├── FileNotFoundError
#       │    ├── InterruptedError
#       │    ├── IsADirectoryError
#       │    ├── NotADirectoryError
#       │    ├── PermissionError
#       │    ├── ProcessLookupError
#       │    └── TimeoutError
#       ├── ReferenceError
#       ├── RuntimeError
#       │    ├── NotImplementedError
#       │    ├── PythonFinalizationError
#       │    └── RecursionError
#       ├── StopAsyncIteration
#       ├── StopIteration
#       ├── SyntaxError
#       │    └── IndentationError
#       │         └── TabError
#       ├── SystemError
#       ├── TypeError
#       ├── ValueError
#       │    └── UnicodeError
#       │         ├── UnicodeDecodeError
#       │         ├── UnicodeEncodeError
#       │         └── UnicodeTranslateError
#       └── Warning
#            ├── BytesWarning
#            ├── DeprecationWarning
#            ├── EncodingWarning
#            ├── FutureWarning
#            ├── ImportWarning
#            ├── PendingDeprecationWarning
#            ├── ResourceWarning
#            ├── RuntimeWarning
#            ├── SyntaxWarning
#            ├── UnicodeWarning
#            └── UserWarning

print("Just need to pass the path of your file..")

file_path = input("Please, Enter file path: ")

if __name__ == "__main__":
    print(display_words(file_path))


# with open 
#F.read().split() 读取文件内容并按空格拆分成单词列表，单个空格或多个空格都可以拆分，换行符也会被视为空格
#filter(lambda word: len(word) < 4, words)
#list包裹filter函数的返回值,将其转换为列表,为什么需要list包裹呢？因为filter函数返回的是一个迭代器对象，而不是一个列表。如果你想要一个列表形式的结果，就需要使用list()函数将其转换为列表。
#len(words_less_than_40) 计算列表中元素的数量