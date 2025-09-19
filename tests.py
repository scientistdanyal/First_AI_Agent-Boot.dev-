from functions.get_file_content import get_file_content
from functions.write_file_content import write_file

from functions.run_python import run_python_file


def main():
 
        # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
        # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
        # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))    # spacin


        


    cases = [
        ("calculator", "main.py", []),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py", []),
        ("calculator", "../main.py", []),
        ("calculator", "nonexistent.py", []),
    ]

    for wd, fp, args in cases:
        print(f"==== run_python_file({wd!r}, {fp!r}, {args!r}) ====")
        print(run_python_file(wd, fp, args))
        print()


if __name__ == "__main__":
    main()



