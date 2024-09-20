reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

# keywords = ["good", "excellent", "bad", "poor", "average"]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "Poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

#Question 1 Task 1
def new_reviews():
    
    new_review = reviews[0].replace("good", "GOOD")
    print(new_review)
    new_review0 = reviews[1].replace("excellent", "EXCELLENT")
    print(new_review0)
    new_review1 = reviews[2].replace("bad", "BAD")
    print(new_review1)
    new_review2 = reviews[3].replace("Poor", "POOR")
    print(new_review2)
    new_review3 = reviews[4].replace("average", "AVERAGE")
    print(new_review3)


#Question 1 Task 2

def pos_tally_count(positive_words, reviews):
    tally = 0
    for substring in positive_words:
        temp = list(reviews)
        for string in temp:
            if substring in string:
                reviews.remove(string)
                tally+=1
    print("Number of positive words is: " + str(tally))
    return tally

def neg_tally_count(negative_words, reviews):
    tally = 0
    for substring in negative_words:
        temp = list(reviews)
        for string in temp:
            if substring in string:
                reviews.remove(string)
                tally+=1
    print("Number of negative words is: " + str(tally))
    return tally

def reviews_summary():
    summarized_review = reviews[0][:32]
    print(summarized_review, end = "...")

def all_new_reviews():
    new_reviews()
    pos_tally_count(positive_words, reviews)
    neg_tally_count(negative_words, reviews)
    reviews_summary()

all_new_reviews()