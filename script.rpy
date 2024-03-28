
# Define characters
define male = Character("Male Character", image="./images/male.png")
define female = Character("Female Character", image="./images/female.png")
image splash =  "main_photo_intro.png"
label splashscreen:

    scene black
    with Pause(0.2)

    play sound "audio/Final_intro_audio.mp3"
    show splash with dissolve
    with Pause(2)

    show text "{size=+70}{b}Cash Ville{/b}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "{size=+40}By - A Bit to the Right" with dissolve
    with Pause(2)

    hide text with dissolve
    # with Pause(1)

    return

## Start of the game ##


# Character Selection
label start:
    play music "audio/lofi_music.mp3"
    scene splash1
    menu:
        
        "Choose your character to get started!"

        "Male":
            $ character_gender = "Male"
            jump life_choose

        "Female":
            $ character_gender = "Female"
            jump life_choose

# Gender Selection
label life_choose:
    scene splash1
    
    if character_gender == "Male":
        show casual_male at left
    elif character_gender == "Female":
        show casual_female at left


    menu:
        "Choose your character Journey!"
        "Highschool":
            $ life = "Highschool"
            jump highschool_begin
        "College":
            $ life = "College"
            jump college_begin
        "Job":
            $ life = "Job"
            jump job_begin
        


# Highschool starts here
label highschool_begin:
    scene highschoool
    
    if character_gender == "Male":
        show highschool_male at left
        "As the sun rises over the tranquil town of Rivertown, we meet our protagonist, Alex, a diligent high school student with dreams of a bright future."
        "But little does Alex know that his journey towards financial literacy is about to begin."
        "Alex sits in his classroom, half-listening to the teacher drone on about quadratic equations. His mind wanders to his upcoming weekend plans. Suddenly, the bell rings, and Alex gathers his things to head home."
        "On his way home, Alex encounters three different scenarios:"
        "1. He sees his friend, Mark, excitedly showing off his new gaming console. Mark urges Alex to join him in purchasing the latest game, promising endless fun and excitement."
        "2. Alex's neighbor, Mrs. Johnson, asks him to help with gardening chores in exchange for a small payment. She mentions that saving money is crucial for future financial security."
        "3. At the local convenience store, Alex spots an advertisement for a credit card with enticing rewards and perks. The idea of instant gratification tempts him."
    elif character_gender == "Female":
        show highschool_female at left
        "As the sun rises over the tranquil town of Rivertown, we meet our protagonist, Alexa, a diligent high school student with dreams of a bright future."
        "But little does Alex know that her journey towards financial literacy is about to begin."
        "Alex sits in her classroom, half-listening to the teacher drone on about quadratic equations. Her mind wanders to her upcoming weekend plans. Suddenly, the bell rings, and Alexa gathers her things to head home."
        "On her way home, Alexa encounters three different scenarios:"
        "1. She sees her friend, Mark, excitedly showing off his new gaming console. Mark urges Alex to join him in purchasing the latest game, promising endless fun and excitement."
        "2. Alexa's neighbor, Mrs. Johnson, asks her to help with gardening chores in exchange for a small payment. She mentions that saving money is crucial for future financial security."
        "3. At the local convenience store, Alexa spots an advertisement for a credit card with enticing rewards and perks. The idea of instant gratification tempts her."


    menu:
        "Accept Mark's invitation and buy the new game.":
            $ option = "A"
            jump highschool_ends_a
        "Help Mrs. Johnson with the gardening chores.":
            $ option = "B"
            jump highschool_ends_b
        "Apply for the credit card to enjoy the rewards.":
            $ option = "C"
            jump highschool_ends_c


# Higschool 1st ending
label highschool_ends_a:
    scene bg_highschool
    
    if character_gender == "Male":
        show highschool_male_normal at left
        "Alex chooses to buy the game with Mark, he spends all his savings, neglecting Mrs. Johnson's advice. His grades suffer as he spends more time gaming, and he misses out on valuable opportunities for personal growth."
        "Mark eventually loses interest in the console, leaving Alex regretful of his impulsive decision. The game gathers dust on the shelf, serving as a reminder of the importance of thoughtful spending."
    elif character_gender == "Female":
        show highschool_female_normal at left
        "Alexa chooses to buy the game with Mark, she spends all her savings, neglecting Mrs. Johnson's advice. Her grades suffer as she spends more time gaming, and she misses out on valuable opportunities for personal growth."
        "Mark eventually loses interest in the console, leaving Alexa regretful of her impulsive decision. The game gathers dust on the shelf, serving as a reminder of the importance of thoughtful spending."
    
    menu:
        "Click here to start college.":
            jump college_begin


#Highschool 2nd ending

label highschool_ends_b:
    scene bg_highschool
    
    if character_gender == "Male":
        show highschool_male_happy at left
        "Alex helps Mrs. Johnson, he earns a modest amount of money and learns the value of hard work and saving. He begins to understand the importance of delayed gratification and sets aside some money for future endeavors."
        "Alex discovers a newfound sense of responsibility and discipline. He begins to budget his money wisely, setting financial goals for himself and planning for his future."
    elif character_gender == "Female":
        show highschool_female_happy at left
        "Alexa helps Mrs. Johnson, she earns a modest amount of money and learns the value of hard work and saving. She begins to understand the importance of delayed gratification and sets aside some money for future endeavors."
        "Alexa discovers a newfound sense of responsibility and discipline. She begins to budget her money wisely, setting financial goals for herself and planning for her future."

    menu:
        "Click here to start college.":
            jump college_begin

#Highschool 3rd ending
label highschool_ends_c:
    scene bg_highschool
    
    if character_gender == "Male":
        show highschool_male_sad at left
        "Alex applies for the credit card, he quickly falls into the trap of overspending and accumulating debt. The allure of rewards blinds him to the high interest rates and hidden fees, leading to financial strain and stress."
        "Alex faces the consequences of his reckless spending. However, with determination and perseverance, he seeks financial guidance and learns to manage his debt responsibly, eventually freeing himself from the shackles of debt."
    elif character_gender == "Female":
        show highschool_female_sad at left
        "Alexa applies for the credit card, he quickly falls into the trap of overspending and accumulating debt. The allure of rewards blinds him to the high interest rates and hidden fees, leading to financial strain and stress."
        "Alexa faces the consequences of her reckless spending. However, with determination and perseverance, she seeks financial guidance and learns to manage her debt responsibly, eventually freeing herself from the shackles of debt."

    menu:
        "Click here to start college.":
            jump college_begin

# College starts here
label college_begin:
    scene bg_college
    
    if character_gender == "Male":
        show college_male at left
        "In the vibrant campus of Ivywood University, we meet our protagonist, Alex, a bright and ambitious college student with dreams of success. Despite his busy schedule of classes and extracurricular activities, Alex yearns to gain financial literacy and independence."
        "As Alex rushes to his morning lecture, his mind buzzes with thoughts of student loans, part-time jobs, and future career prospects. Today, he faces a critical decision that could shape his financial future. Suddenly, his phone buzzes with a notification - it's a reminder to review his monthly budget."
        "During his break between classes, Alex encounters three different scenarios:"
        "1. Alex's friend, Sarah, tells him about a lucrative part-time job opportunity that pays well but requires long hours, potentially affecting his academic performance."
        "2. Alex receives an email about refinancing his student loans at a lower interest rate. However, it involves extending the repayment period, resulting in higher overall interest payments."
        "3. While browsing online, Alex comes across a flash sale for designer clothing with steep discounts. The temptation to splurge on trendy items beckons him"

    elif character_gender == "Female":
        show college_female at left
        "In the vibrant campus of Ivywood University, we meet our protagonist, Alexa, a bright and ambitious college student with dreams of success. Despite her busy schedule of classes and extracurricular activities, Alexa yearns to gain financial literacy and independence."
        "As Alexa rushes to her morning lecture, her mind buzzes with thoughts of student loans, part-time jobs, and future career prospects. Today, she faces a critical decision that could shape her financial future. Suddenly, her phone buzzes with a notification - it's a reminder to review her monthly budget."
        "During her break between classes, Alexa encounters three different scenarios:"
        "1. Alexa's friend, Sarah, tells her about a lucrative part-time job opportunity that pays well but requires long hours, potentially affecting her academic performance."
        "2. Alexa receives an email about refinancing her student loans at a lower interest rate. However, it involves extending the repayment period, resulting in higher overall interest payments."
        "3. While browsing online, Alexa comes across a flash sale for designer clothing with steep discounts. The temptation to splurge on trendy items beckons her."


    menu:
        "Accept the part-time job offer for higher pay despite the potential impact on academics.":
            $ option = "A"
            jump college_ends_a
        "Refinance student loans at a lower interest rate but with a longer repayment period.":
            $ option = "B"
            jump college_ends_b
        "Succumb to impulsive spending and splurge on discounted designer clothing.":
            $ option = "C"
            jump college_ends_c


# College 1st ending
label college_ends_a:
    scene bg_college
    
    if character_gender == "Male":
        show college_male_happy at left
        "He juggles his coursework with the demanding job, sacrificing sleep and social time to earn extra income. However, the stress and exhaustion take a toll on Alex's mental and physical health, leading to academic struggles and burnout."
        "He realizes that academic success is his top priority and decides to prioritize his studies over additional income. He learns to seek balance in his commitments and explores alternative ways to manage his finances without compromising his education."
    elif character_gender == "Female":
        show college_female_happy at left
        "She juggles her coursework with the demanding job, sacrificing sleep and social time to earn extra income. However, the stress and exhaustion take a toll on Alexa's mental and physical health, leading to academic struggles and burnout."
        "Alexa realizes that academic success is her top priority and decides to prioritize her studies over additional income. She learns to seek balance in her commitments and explores alternative ways to manage her finances without compromising her education."

    
    menu:
        "Click here to start job.":
            jump job_begin


#College 2nd ending

label college_ends_b:
    scene bg_college
    
    if character_gender == "Male":
        show college_male_normal at left
        "He lowers his monthly payments by extending the repayment period, providing temporary relief on his budget. However, over time, Alex realizes that he ends up paying more in total interest due to the extended term. "
        "He acknowledges the importance of researching and understanding the terms of financial agreements before making decisions. He resolves to be more diligent in evaluating loan options and seeks guidance from financial advisors to make informed choices about debt management."
    elif character_gender == "Female":
        show college_female_normal at left
        "She lowers her monthly payments by extending the repayment period, providing temporary relief on her budget. However, over time, Alexa realizes that she ends up paying more in total interest due to the extended term."
        "Alexa acknowledges the importance of researching and understanding the terms of financial agreements before making decisions. She resolves to be more diligent in evaluating loan options and seeks guidance from financial advisors to make informed choices about debt management."

    menu:
        "Click here to start job.":
            jump job_begin

#Job 3rd ending
label college_ends_c:
    scene bg_college
    
    if character_gender == "Male":
        show college_male_sad at left
        "He indulges in the thrill of purchasing discounted designer clothing, satisfying his immediate desires. However, the excitement fades quickly, and Alex is left with guilt and regret as he struggles to justify the unnecessary expenses. "
        "He reflects on his spending habits and commits to practicing restraint and discipline in his purchases. He embraces the concept of delayed gratification and sets financial goals to prioritize saving and investing for his future."
    elif character_gender == "Female":
        show college_female_sad at left
        "She indulges in the thrill of purchasing discounted designer clothing, satisfying her immediate desires. However, the excitement fades quickly, and Alexa is left with guilt and regret as she struggles to justify the unnecessary expenses."
        "Alexa reflects on her spending habits and commits to practicing restraint and discipline in her purchases. She embraces the concept of delayed gratification and sets financial goals to prioritize saving and investing for her future."

    menu:
        "Click here to start job.":
            jump job_begin


# Job starts here
label job_begin:
    scene job_bg
    
    if character_gender == "Male":
        show job_male at left
        "In the bustling city of Metropolis, we meet our protagonist, Alex, a diligent young man who works tirelessly at his job in a prestigious financial firm."
        "Despite his busy schedule, Alex dreams of achieving financial stability and securing a bright future for himself."
        "As Alex settles into his office cubicle, his mind races with thoughts of bills to pay and savings to grow."
        "Today, he faces a critical decision that could shape his financial journey. Suddenly, his phone buzzes with a notification - it's a reminder to review his monthly budget."
        "During his lunch break, ALex encounters three different scenarios:"
        "1. Alex's colleague, Jason, excitedly shares news about a high-risk investment opportunity with potentially high returns. He urges Alex to join him in investing a significant portion of him savings."
        "2. Alex's boss, Mr. Thompson, offers him a promotion with a substantial salary increase. However, it comes with longer work hours and increased stress levels."
        "3. While window shopping during his break, Alex spots a stunning designer watch on sale. The temptation to indulge in a luxury purchase beckons him."
    elif character_gender == "Female":
        show job_female at left
        "In the bustling city of Metropolis, we meet our protagonist, ALexa, a diligent young woman who works tirelessly at her job in a prestigious financial firm."
        "Despite her busy schedule, Alexa dreams of achieving financial stability and securing a bright future for herself."
        "As Alexa settles into her office cubicle, her mind races with thoughts of bills to pay and savings to grow."
        "Today, she faces a critical decision that could shape her financial journey. Suddenly, her phone buzzes with a notification - it's a reminder to review her monthly budget."
        "During her lunch break, Alexa encounters three different scenarios:"
        "1. Alexa's colleague, Jason, excitedly shares news about a high-risk investment opportunity with potentially high returns. He urges Mia to join him in investing a significant portion of her savings."
        "2. ALexa's boss, Mr. Thompson, offers her a promotion with a substantial salary increase. However, it comes with longer work hours and increased stress levels."
        "3. While window shopping during her break, Mia spots a stunning designer watch on sale. The temptation to indulge in a luxury purchase beckons her."


    menu:
        "Accept Jason's investment proposal and invest a significant portion of savings.":
            $ option = "A"
            jump job_ends_a
        "Accept the promotion from Mr. Thompson and embrace the longer work hours and stress.":
            $ option = "B"
            jump job_ends_b
        "Splurge on the designer watch, indulging in a luxury purchase.":
            $ option = "C"
            jump job_ends_c


# Job 1st ending
label job_ends_a:
    scene job_bg
    
    if character_gender == "Male":
        show job_male at left
        "He takes the risk and invests his savings in the high-risk opportunity. However, the investment fails, and Alex loses a substantial portion of his hard-earned money."
        "Despite the setback, Alex resolves to learn from his mistakes and adopts a more cautious approach to investing. He seeks guidance from financial experts and educates himself on prudent investment strategies, setting himself on a path towards long-term financial success."
    elif character_gender == "Female":
        show highschool_female at left
        "She takes the risk and invests her savings in the high-risk opportunity. However, the investment fails, and Alexa loses a substantial portion of her hard-earned money."
        "Despite the setback, Alexa resolves to learn from her mistakes and adopts a more cautious approach to investing. She seeks guidance from financial experts and educates herself on prudent investment strategies, setting herself on a path towards long-term financial success."
    
    menu:
        "The End":
            jump end


# Job 2nd ending

label job_ends_b:
    scene job_bg
    
    if character_gender == "Male":
        show job_male at left
        "He dedicates himself to his job, sacrificing his personal time and well-being for career advancement. However, the increased stress takes a toll on Alex's health and relationships, leaving him feeling burnt out and unfulfilled."
        "Alex realizes that career advancement should not come at the expense of his well-being. He reevaluates his priorities and takes steps to regain balance in his life, prioritizing his health and happiness above all else."
    elif character_gender == "Female":
        show job_female at left
        "She dedicates herself to her job, sacrificing her personal time and well-being for career advancement. However, the increased stress takes a toll on Alexa's health and relationships, leaving her feeling burnt out and unfulfilled."
        "Alexa realizes that career advancement should not come at the expense of her well-being. She reevaluates her priorities and takes steps to regain balance in her life, prioritizing her health and happiness above all else."

    menu:
        "The End.":
            jump end

#Job 3rd ending
label job_ends_c:
    scene job_bg
    
    if character_gender == "Male":
        show job_male_sad at left
        "He indulges in the momentary pleasure of owning the luxury item. However, the excitement fades quickly, and Alex is left with regret as he struggles to justify the extravagant purchase."
        "Alex acknowledges his lapse in judgment and commits to making more mindful financial decisions in the future. He creates a budget, tracks his expenses, and cultivates discipline in his spending habits, empowering himself to achieve his financial goals with patience and perseverance."
    elif character_gender == "Female":
        show job_female_sad at left
        "She indulges in the momentary pleasure of owning the luxury item. However, the excitement fades quickly, and Alexa is left with regret as she struggles to justify the extravagant purchase."
        "Alexa acknowledges her lapse in judgment and commits to making more mindful financial decisions in the future. She creates a budget, tracks her expenses, and cultivates discipline in her spending habits, empowering herself to achieve her financial goals with patience and perseverance."

    menu:
        "The End.":
            jump end

# End of game
label end:
    "Thank you for playing CashVille: The Financial Literacy Adventure!"









