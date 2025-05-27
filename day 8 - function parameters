############### Exercise 1: Life in Weeks ###################

def life_in_weeks(age):
    years_left = (90-age)*52
    print(f"You have {years_left} weeks left.")
    
life_in_weeks(12)


  ############### Exercise 2: Love Calculator ###################
def calculate_love_score(name1, name2):
    true_word = "true"
    love_word = "love"
    true_ocurrences = [0, 0, 0 ,0]
    love_ocurrences = [0, 0, 0 ,0]
    for index, t in enumerate(true_word):
        if t in name1:
            true_ocurrences[index] += name1.count(t)
        if t in name2:
            true_ocurrences[index] += name2.count(t)
    
    for index, l in enumerate(love_word):
         if l in name1:
            love_ocurrences[index] += name1.count(l)
         if l in name2:
            love_ocurrences[index] += name2.count(l)
    
    sum_true = 0
    for occur in true_ocurrences:
        sum_true += occur
    sum_love = 0
    for occur in love_ocurrences:
        sum_love += occur
    combine = f"{sum_true}{sum_love}"
    print(combine)
    
calculate_love_score("Kanye West", "Kim Kardashian")
