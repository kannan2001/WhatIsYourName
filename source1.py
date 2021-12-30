# What's Your Name? in Python - HackerRank Solution
def print_full_name(a, b):

    # What's Your Name? in Python - HackerRank Solution START
    a = []
    b = []
    a.append(first)
    b.append(last)
    line = " ".join(a) +" " + " ".join(b)
    line = line + "!"
    print("Hello" ,line, "You just delved into python.")
    # What's Your Name? in Python - HackerRank Solution END
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
