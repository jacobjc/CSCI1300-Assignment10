# Author: Jacob Christiansen
# Recitation: 104 - Vipra Gupta
#
# Assignment 10


# PART 1

#this function reads in a file of authors and books and makes listRB
#the returned list contains sub - lists of title&author pairs
#if the filename is empty, the function will return a list that is empty
#if the file can't open, the function will return None
#the fuction also swaps the author,title format to title,author to get the correct output
def read_books(filename):
    try:
        with open(filename, 'r') as fr:
            listRB = []
            for line in fr:
                if(line == ""):
                    listRB = []
                    return listRB
                else:
                    line = line.rstrip()
                    tempL = line.split(',')
                    tempL[0], tempL[1] = tempL[1], tempL[0]
                    listRB.append(tempL)
            return listRB
    except(IOError):
        return None

#this function reads in a file with users the ratings they gave books.
#Then it makes a dictionary out of that, in which the keys are users and
#the values are a list of the user ratings
#if the file is empty, the function will return an empty dictionary
def read_users(filename):
    try:
        with open(filename, 'r') as fr:
            dictRU = {}
            for line in fr:
                if(line == ""):
                    dictRU = {}
                    return dictRU
                else:
                    line = line.rstrip()
                    tempL = line.split(' ')
                    keyN = tempL[0]
                    newL = tempL[1:]
                    newL = map(int, newL)
                    dictRU[keyN] = newL
            return dictRU
    except(IOError):
        return None

#this function takes in the dictionary of ratings and makes it into a listoflists
#it finds the average ratings for every book by adding up all the indivdual book ratings
#and then dividing the sum by the number of ratings (not including 0 ratings)
#then the fuction puts all the averages into a list
def calculate_average_rating(rDict):
    listoflists = []
    avgL = []
    for i in rDict:
        rList = rDict[i]
        listoflists.append(rList)

    for i in range(len(listoflists[0])):
        tot = 0
        div = 0
        for j in range(len(listoflists)):
            if(listoflists[j][i] != 0):
                div += 1
                tot += listoflists[j][i]
        if(tot == 0):
            avgL.append(0.0)
        else:
            avg = float(tot)/div
            avgL.append(avg)
    return avgL

#this function checks the average rating for a given book index and returns
# that book title, author and avg rating in a string
def lookup_average_rating(index, book_list, avg_ratings_list):
    book = book_list[index][0]
    author = book_list[index][1]
    rating = avg_ratings_list[index]
    rStr = "("+format(rating,".2f")+") "+book+" by "+author
    return rStr

#PART 1 MAIN TESTING FUCTIONS
def main():
    bList = read_books("C:/Users/jacob/Dropbox/1300ProgramsCSCI/Ass10/book.txt")
    uDict = read_users("C:/Users/jacob/Dropbox/1300ProgramsCSCI/Ass10/ratings.txt")
    # print bList
    # print uDict
    # testDict = ({'A':[0,1,2,3,4,5], 'J':[0,2,4,6,8,10]})
    avgList = calculate_average_rating(uDict)
    print round(avgList[0],3)
    print round(avgList[19],3)
    print lookup_average_rating(0, bList, avgList)

if __name__ == "__main__":
    main()

#
#
#
#
#PART 2

#class start and then construcctor, taking 2 file names and initializing lists/dicts
class Recommender:
    def __init__(self, books_filename, ratings_filename):
        self.book_list = []
        self.read_books(books_filename)
        self.user_dictionary = {}
        self.read_users(ratings_filename)
        self.average_rating_list = []
        self.calculate_average_rating()


#this function reads in a file of authors and books and makes listRB
#the returned list contains sub - lists of title&author pairs
#if the filename is empty, the function will return a list that is empty
#if the file can't open, the function will return None
#the fuction also swaps the author,title format to title,author to get the correct output
    def read_books(self, books_filename):
        try:
            with open(books_filename, 'r') as fr:
                self.book_list = []
                for line in fr:
                    if(line == ""):
                        self.book_list = []
                        return self.book_list
                    else:
                        line = line.rstrip()
                        tempL = line.split(',')
                        tempL[0], tempL[1] = tempL[1], tempL[0]
                        self.book_list.append(tempL)
                return self.book_list
        except:
            return None

#this function reads in a file with users the ratings they gave books.
#Then it makes a dictionary out of that, in which the keys are users and
#the values are a list of the user ratings
#if the file is empty, the function will return an empty dictionary
    def read_users(self, ratings_filename):
        try:
            with open(ratings_filename, 'r') as fr:
                self.user_dictionary = {}
                for line in fr:
                    if(line == ""):
                        self.user_dictionary = {}
                        return self.user_dictionary
                    else:
                        line = line.rstrip()
                        tempL = line.split(' ')
                        keyN = tempL[0]
                        newL = tempL[1:]
                        newL = map(int, newL)
                        self.user_dictionary[keyN] = newL
                return self.user_dictionary
        except:
            return None

#this function takes in the dictionary of ratings and makes it into a listoflists
#it finds the average ratings for every book by adding up all the indivdual book ratings
#and then dividing the sum by the number of ratings (not including 0 ratings)
#then the fuction puts all the averages into a list
    def calculate_average_rating(self):
        listoflists = []
        rList = []
        for i in self.user_dictionary:
            rList = self.user_dictionary[i]
            listoflists.append(rList)

        for i in range(len(listoflists[0])):
            tot = 0
            div = 0
            for j in range(len(listoflists)):
                if(listoflists[j][i] != 0):
                    div += 1
                    tot += listoflists[j][i]
            if(tot == 0):
                self.average_rating_list.append(0.0)
            else:
                avg = float(tot)/div
                self.average_rating_list.append(avg)
        return self.average_rating_list

#this function checks the average rating for a given book index and returns
# that book title, author and avg rating in a string
    def lookup_average_rating(self, index):
        book = self.book_list[index][0]
        author = self.book_list[index][1]
        rating = self.average_rating_list[index]
        rStr = "("+format(rating,".2f")+") "+book+" by "+author
        return rStr

#this function takes in 2 userIDs and compares the two
#this is done by adding the products of each of their matching ratings
#resulting in the similarity score, which is returned
    def calc_similarity(self, user1, user2):
        count = 0
        u1Rate = self.user_dictionary[user1]
        u2Rate = self.user_dictionary[user2]
        for n in range(len(u1Rate)):
            count += (u1Rate[n]*u2Rate[n])
        return count

#this function takes a userID and uses calc_similarity to find MOST similar user
#to the given user by the fuction. That user's nameID is returned
#to do this, the userID's carresponding name must not be a part of any comparisons
    def get_most_similar_user(self,current_user_id):
        highU = ""
        highS = 0
        for n in self.user_dictionary:
            if(n != current_user_id):
                temp = self.calc_similarity(current_user_id, n)
                if(temp > highS):
                    highS = temp
                    highU = n
        return highU

#this function takes in a userID and uses get_most_similar_user to find MOST similar user
#it returns a list of all the books read by the best matched user (which aren't read by the given userID) and are rated higher than a 3
#it also uses lookup_average_rating to put the strings into the proper output format. Finally the function puts each string into a returned
#list of recommended books
    def recommend_books(self,current_user_id):
        bookIndexList = []
        recBookList = []
        simUser = self.get_most_similar_user(current_user_id)
        for i in range(len(self.user_dictionary[simUser])):
            if(self.user_dictionary[simUser][i] >= 3):
                if(self.user_dictionary[current_user_id][i] == 0):
                    bookIndexList.append(i)
        for i in bookIndexList:
            recBookList.append(self.lookup_average_rating(i))
        return recBookList


#PART 2 MAIN TESTING FUCTIONS
def main():
    bFile = "C:/Users/jacob/Dropbox/1300ProgramsCSCI/Ass10/book.txt"
    uFile =  "C:/Users/jacob/Dropbox/1300ProgramsCSCI/Ass10/ratings.txt"
    recTest = Recommender(bFile, uFile)

    print recTest.lookup_average_rating(0) #3.83 tHGttG by DA
    print recTest.lookup_average_rating(10) #0.90 tPD by MC
    print recTest.lookup_average_rating(44) #3.00 SJS by S

    print recTest.calc_similarity('Megan', 'Cust8') #304
    print recTest.calc_similarity('Ben', 'Boxxy') #35
    print recTest.calc_similarity('Apollo', 'Shannon') #-5

    print recTest.get_most_similar_user('Rudy_Ann') #ROFLOL
    print recTest.get_most_similar_user('Boxxy') #Cust8
    print recTest.get_most_similar_user('Cust8') #Shannon

    print recTest.recommend_books('Ben') #['(1.70) Watership Down by Richard Adams', '(1.36) Lord of the Flies by William Golding', '(2.62) Flowers For Algernon by Daniel Keyes', '(4.00) Sabriel by Garth Nix', '(3.04) The Lord of the Rings by J R R Tolkien']
    print recTest.recommend_books('Cust8') #['(1.62) Naruto by Masashi Kishimoto']
    print recTest.recommend_books('Mark') #['(0.33) Practical Magic by Alice Hoffman', '(2.83) Nineteen Eighty-Four (1984) by George Orwell', '(2.76) The Golden Compass by Philip Pullman', '(3.61) Harry Potter Series by J.K. Rowling', '(3.00) Shonen Jump Series by Shueisha', '(2.85) The Hobbit by J R R Tolkien']


    return 0

if __name__ == "__main__":
    main()
