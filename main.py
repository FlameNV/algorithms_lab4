from utils.word_counter import final_count
from utils.reader import read

if __name__ == '__main__':
    with open("wchain1.out", "w") as file:
        file.write(f'{final_count(sorted(read("wchain1.in"), key=len), {})}')
    with open("wchain2.out", "w") as file:
        file.write(f'{final_count(sorted(read("wchain2.in"), key=len), {})}')
    with open("wchain3.out", "w") as file:
        file.write(f'{final_count(sorted(read("wchain3.in"), key=len), {})}')
