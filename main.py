from math import floor
def love():
    checker = input("Type your name here: ")
    crush = input("Type your crush's name here: ")
    conc = checker + crush
    word = input("Type a comparison word: ")
    num_list = name_check(conc, word)
    percent_list = adder(num_list)
    percent = str(percent_list[0]) + str(percent_list[1])
    string = checker + " " + word + " " + crush + " " + percent + "%"
    print("")
    print(string.upper())

def name_check(name, word):
    num_list = []
    for letter in word:
        num_list.append(0)
    for letter in name: #for every letter in the name you need to compare it to each letter in the word
        i = 0 # set index to 0 so you can add to the 0th spot in the list (resets for every time there is a new letter)
        for char in word:
            if letter == char:
                old = num_list[i]
                new = old + 1
                num_list[i] = new
            i += 1
    #print(num_list)
    return(num_list)

def adder(nums):
    while len(nums) > 2:
        for i in range(len(nums) - 1):
            sum = nums[i] + nums[i + 1]
            nums[i] = sum
        nums.pop()
        over_ten_index = []
        for i in range(len(nums)): # this just acts as a checker and the next loop replaces
            index = 0
            if nums[i] > 100:
                print("Cannot do this computation")
            if (nums[i] > 9) and (nums[i] < 100):
                over_ten_index.append(i)
                #print(over_ten_index)
        for index in over_ten_index:
            num = nums[index]
            ones = num % 10
            tens = int((num - ones)/10)
            nums[index] = tens
            nums.insert(index + 1, ones)
        #print(nums)
    return(nums)



love()


