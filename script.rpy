
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
            jump college_start
        "Job":
            $ life = "Job"
            jump job_start
        
#Start changes in script from here:

# Highschool starts here
label highschool_begin:
    scene bg_highschool_2
    
    if character_gender == "Male":
        show highschool_male at left
        "In the bustling town of CashVille, Alex, a typical high school student, stands at a crossroads, facing the daunting challenge of navigating the complexities of financial decision-making on his journey to college and beyond."
    elif character_gender == "Female":
        show highschool_female at left
        "In the bustling town of CashVille, Alexa, a typical high school student, stands at a crossroads, facing the daunting challenge of navigating the complexities of financial decision-making on her journey to college and beyond."

    menu:
        "Choose to immerse in fields such as literature, music, or visual arts.":
            $ option = "Cultural"
            jump highschool_cultural
        "Aim for careers in science, mathematics, or other academic disciplines.":
            $ option = "Academics"
            jump highschool_academics
        "Pursue something in the field of sports.":
            $ option = "Sports"
            jump highschool_sports


# Higschool cultural
label highschool_cultural:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male_sad at left
        "The Financial Struggle Begins:"

    elif character_gender == "Female":
        show highschool_female_sad at left
        "The Financial Struggle Begins:"

    menu:
        "Apply for loan to study in a prestigious and expensive private university":
            $ option = "Cultural_A"
            jump cultural_A
        "Attend a local community college while working part-time to save money.":
            $ option = "Cultural_B"
            jump cultural_B
        "Seeks out scholarships, grants, and alternative funding options to minimize student loan debt.":
            $ option = "Cultural_C"
            jump cultural_C

label cultural_A:
    scene bg_highschool

    if character_gender == "Male" :
        show highschool_male_sad at left
        "The weight of student loan debt begins to bear down on him, overshadowing his artistic pursuits."
        "As financial pressures mount, Alex's creativity and passion are stifled, and he finds himself forced to compromise on his dreams to manage his financial obligations."
        jump college_start

    elif character_gender == "Female":
        show highschool_female_sad at left
        "The weight of student loan debt begins to bear down on her, overshadowing her artistic pursuits."
        "As financial pressures mount, Alexa's creativity and passion are stifled, and she finds herself forced to compromise on her dreams to manage her financial obligations."
        jump college_start

label cultural_B:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male_happy at left
        "Alex saves money and prepares a strong portfolio, positioning himself for a successful transfer to a specialized school."
        "With minimal student loan debt and a solid foundation in place, Alex thrives in his chosen field, free to explore academics without the burden of financial instability."
        jump college_start

    elif character_gender == "Female":
        show highschool_female_happy at left
        "Alexa saves money and prepares a strong portfolio, positioning herself for a successful transfer to a specialized school."
        "With minimal student loan debt and a solid foundation in place, Alexa thrives in her chosen field, free to explore academics without the burden of financial instability."
        jump college_start

label cultural_C:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male_happy at left
        "Alex weighs the benefits of prestigious universities against the financial implications and decides to pursue more affordable alternatives."
        "By choosing a path that minimizes student loan debt while still prioritizing growth, Alex strikes a balance between his academics and financial stability."
        jump college_start

    elif character_gender == "Female":
        show highschool_female_happy at left
        "Alexa weighs the benefits of prestigious universities against the financial implications and decides to pursue more affordable alternatives."
        "By choosing a path that minimizes student loan debt while still prioritizing growth, Alexa strikes a balance between his academics and financial stability."
        jump college_start

#Highschool Academics
label highschool_academics:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male_sad at left
        "The Financial Struggle Begins:"

    elif character_gender == "Female":
        show highschool_female_sad at left
        "The Financial Struggle Begins:"

    menu:
        "Opt for an expensive private university.":
            $ option = "Academics_A"
            jump Academics_A
        "Secure a part-time job and attend a reputable community college":
            $ option = "Academics_B"
            jump Academics_B
        "Apply for scholarships and grants while exploring in-state public university options, striving to minimize financial burden.":
            $ option = "Academics_C"
            jump Academics_C

label Academics_A:
    scene bg_highschool_3

    if character_gender == "Male":
        show highschool_male_normal at left
        "The weight of student loan debt begins to bear down on him, overshadowing his academic pursuits."
        " As financial pressures mount, Alex's creativity and passion are stifled, and he finds himself forced to compromise on his dreams to manage his financial obligations."
        jump college_start

    elif character_gender == "Female":
        show highschool_female_normal at left
        "The weight of student loan debt begins to bear down on her, overshadowing her artistic pursuits."
        "As financial pressures mount, Alexa's creativity and passion are stifled, and she finds herself forced to compromise on her dreams to manage her financial obligations."
        jump college_start

label Academics_B:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male at left
        "Alex saves money and prepares a strong portfolio, positioning himself for a successful transfer to a specialized school."
        "With minimal student loan debt and a solid foundation in place, Alex thrives in his chosen field, free to explore academics without the burden of financial instability."
        jump college_start

    elif character_gender == "Female":
        show highschool_female at left
        "Alexa saves money and prepares a strong portfolio, positioning herself for a successful transfer to a specialized school."
        "With minimal student loan debt and a solid foundation in place, Alexa thrives in her chosen field, free to explore academics without the burden of financial instability."
        jump college_start

label Academics_C:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male at left
        "Alex weighs the benefits of prestigious universities against the financial implications and decides to pursue more affordable alternatives."
        "By choosing a path that minimizes student loan debt while still prioritizing growth, Alex strikes a balance between his academics and financial stability."
        jump college_start

    elif character_gender == "Female":
        show highschool_female at left
        "Alexa weighs the benefits of prestigious universities against the financial implications and decides to pursue more affordable alternatives."
        "By choosing a path that minimizes student loan debt while still prioritizing growth, Alexa strikes a balance between her academics and financial stability."
        jump college_start

#Highschool Sports
label highschool_sports:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male_sad at left
        "The Financial Struggle Begins:"

    elif character_gender == "Female":
        show highschool_female_sad at left
        "The Financial Struggle Begins:"

    menu:
        "Accept a scholarship offer from an elite academy without considering the long-term financial implications":
            $ option = "sports_A"
            jump sports_A
        "Balancing athletic pursuits with financial responsibility":
            $ option = "sports_B"
            jump sports_B
        "Evaluate college offers that provide a combination of athletic scholarships and academic merit aid.":
            $ option = "sports_C"
            jump sports_C

label sports_A:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male_sad at left
        "With limited support beyond athletic expenses, Alex struggles to cover personal costs and experiences financial instability."
        "The pressure to perform on the field intensifies as Alex grapples with the burden of financial insecurity."
        jump college_start

    elif character_gender == "Female":
        show highschool_female_sad at left
        "With limited support beyond athletic expenses, Alexa struggles to cover personal costs and experiences financial instability."
        "The pressure to perform on the field intensifies as Alexa grapples with the burden of financial insecurity."
        jump college_start

label sports_B:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male_happy at left
        "Alex successfully secures scholarships and grants to support his athletic endeavors, maintaining financial stability while excelling in his sport."
        "With a solid financial foundation, Alex can focus on achieving his athletic goals without the worry of financial strain."
        jump college_start

    elif character_gender == "Female":
        show highschool_female_happy at left
        "Alexa successfully secures scholarships and grants to support his athletic endeavors, maintaining financial stability while excelling in his sport."
        "With a solid financial foundation, Alexa can focus on achieving his athletic goals without the worry of financial strain."
        jump college_start

label sports_C:
    scene bg_highschool

    if character_gender == "Male":
        show highschool_male_happy at left
        "By choosing a college that values his athletic talent and academic achievements, Alex sets himself up for success on and off the field."
        "With financial stability ensured, he can pursue his passion for sports with confidence and dedication."
        jump college_start

    elif character_gender == "Female":
        show highschool_female_happy at left
        "By choosing a college that values her athletic talent and academic achievements, Alexa sets hi up herself or success on and off the field."
        "With financial stability ensured, she can pursue her passion for sports with confidence and dedication."
        jump college_start



label college_start:
    scene bg_college_2
    if character_gender == "Male":
        show casual_male at left
    elif character_gender == "Female":
        show casual_female at left

    menu:
        "Choose your character Journey!"

        "Part-Time Job Seeker":
            $ life = "Part-Time Job Seeker"
            jump college_part_time
        "Entrepreneur":
            $ life = "Entrepreneur"
            jump college_entrepreneur
        "Aim for higher studies":
            $ life = "Job"
            jump college_higher_studies
        

#College Begins
label college_part_time:
    scene bg_college
    
    if character_gender == "Male":
        show college_male_sad at left
        "Alex arrives at college excited but quickly realizes the financial burden of tuition and living expenses."

    elif character_gender == "Female":
        show college_female_sad at left
        "Alexa arrives at college excited but quickly realizes the financial burden of tuition and living expenses."


    menu:
        "Accept a low-paying job without considering future financial goals":
            $ option = "A"
            jump college_part_a
        "Part-time job with a focus on career advancement while learning about budgeting.":
            $ option = "B"
            jump college_part_b
        "Explore various part-time job options, setting aside a portion for savings.":
            $ option = "C"
            jump college_part_c

label college_part_a:
    scene bg_college

    if character_gender == "Male":
        show college_male_sad at left
        "Alex finds it challenging to cover expenses and fails to save for the future, leading to financial instability and missed opportunities for growth."
        jump job_start

    elif character_gender == "Female":
        show college_female_sad at left
        "By choosing a college that values his athletic talent and academic achievements, Alexa sets himself up for success on and off the field."
        "With financial stability ensured, he can pursue his passion for sports with confidence and dedication."
        jump job_start


label college_part_b:
    scene bg_college

    if character_gender == "Male":
        show college_male_sad at left
        "Alex finds it challenging to cover expenses and fails to save for the future, leading to financial instability and missed opportunities for growth."
        jump job_start

    elif character_gender == "Female":
        show college_female_sad at left
        "By prioritizing career growth and financial education, Alexa builds valuable skills and networks, setting the stage for future success."
        "With careful budgeting and strategic investments, Alexa achieves financial stability and lays a strong foundation for long-term financial health."
        jump job_start


label college_part_c:

    scene bg_college

    if character_gender == "Male":
        show college_male_sad at left
        "Alex finds it challenging to cover expenses and fails to save for the future, leading to financial instability and missed opportunities for growth."
        jump job_start

    elif character_gender == "Female":
        show college_female_sad at left
        "Alexa takes a balanced approach, considering both immediate financial needs and long-term goals."
        "While not maximizing immediate earnings, this approach allows Alexa to maintain financial stability while also preparing for future opportunities."
        jump job_start


#College Entrepreneur

label college_entrepreneur:
    scene bg_college
    
    if character_gender == "Male":
        show college_male_sad at left
        "Alex arrives at college excited but quickly realizes the financial burden of tuition and living expenses."

    elif character_gender == "Female":
        show college_female_sad at left
        "Alexa arrives at college excited but quickly realizes the financial burden of tuition and living expenses."


    menu:
        "Dive into entrepreneurship without proper financial planning":
            $ option = "A"
            jump entrepreneur_a
        "Conduct market research and develop a comprehensive plan.":
            $ option = "B"
            jump entrepreneur_b
        "Start a small-scale business with minimal initial investment":
            $ option = "C"
            jump entrepreneur_c

label entrepreneur_a:
    scene bg_college

    if character_gender == "Male":
        show college_male_sad at left
        "Alex's venture faces financial challenges and struggles to generate profit, resulting in loss of personal savings and potential debt. Ultimately the business fails."
        jump job_start

    elif character_gender == "Female":
        show college_female_sad at left
        "Alexa's venture faces financial challenges and struggles to generate profit, resulting in loss of personal savings and potential debt. Ultimately the business fails."
        jump job_start


label entrepreneur_b:
    scene bg_college

    if character_gender == "Male":
        show college_male_happy at left
        "By taking a strategic approach to entrepreneurship, Alex's venture gains traction and achieves sustainable growth."
        "With proper financial planning and risk management, Alex navigates challenges effectively and builds a successful business."
        jump job_start

    elif character_gender == "Female":
        show college_female_happy at left
        "By taking a strategic approach to entrepreneurship, Alexa's venture gains traction and achieves sustainable growth."
        "With proper financial planning and risk management, Alexa navigates challenges effectively and builds a successful business."
        jump job_start


label entrepreneur_c:

    scene bg_college

    if character_gender == "Male":
        show college_male_normal at left
        "While initial growth may be slower, this cautious approach allows Alex to minimize financial risk and learn valuable lessons along the way."
        "By gradually scaling the business and reinvesting profits, Alex lays a solid foundation for future expansion."
        jump job_start

    elif character_gender == "Female":
        show college_female_normal at left
        "While initial growth may be slower, this cautious approach allows Alexa to minimize financial risk and learn valuable lessons along the way."
        "By gradually scaling the business and reinvesting profits, Alexa lays a solid foundation for future expansion."
        jump job_start

#college Higher Studies

label college_higher_studies:
    scene bg_college
    
    if character_gender == "Male":
        show college_male at left
        "Alex arrives at college excited but quickly realizes the financial burden of tuition and living expenses."

    elif character_gender == "Female":
        show college_female at left
        "Alexa arrives at college excited but quickly realizes the financial burden of tuition and living expenses."


    menu:
        "Pursue higher studies without considering the financial implications":
            $ option = "A"
            jump higher_studies_a
        "Research scholarship and financial aid options.":
            $ option = "B"
            jump higher_studies_b
        " Balance academic aspirations with financial responsibilities":
            $ option = "C"
            jump higher_studies_c

#Higher studies options

label higher_studies_a:
    scene bg_college

    if character_gender == "Male":
        show college_male_sad at left
        "Alex graduates with significant student loan debt and struggles to find employment opportunities that align with academic qualifications, leading to financial stress and uncertainty."
        jump job_start

    elif character_gender == "Female":
        show college_female_sad at left
        "Alexa graduates with significant student loan debt and struggles to find employment opportunities that align with academic qualifications, leading to financial stress and uncertainty."
        jump job_start


label higher_studies_b:
    scene bg_college

    if character_gender == "Male":
        show college_male_happy at left
        "By actively seeking out financial assistance and gaining practical experience, Alex graduates with minimal student loan debt and valuable skills."
        "With a clear plan for repayment and career advancement, Alex transitions smoothly into the workforce or further education."
        jump job_start

    elif character_gender == "Female":
        show college_female_happy at left
        "By actively seeking out financial assistance and gaining practical experience, Alex graduates with minimal student loan debt and valuable skills."
        "With a clear plan for repayment and career advancement, Alexa transitions smoothly into the workforce or further education."
        jump job_start


label higher_studies_c:

    scene bg_college

    if character_gender == "Male":
        show college_male_happy at left
        "With careful financial planning and budgeting, Alex completes the program with manageable debt and sets a course for future financial success."
        "Additionally, Alex begins investing early to build wealth and secure a stable financial future."
        jump job_start

    elif character_gender == "Female":
        show college_female_happy at left
        "With careful financial planning and budgeting, Alex completes the program with manageable debt and sets a course for future financial success."
        "Additionally, Alexa begins investing early to build wealth and secure a stable financial future."
        jump job_start





#Job start


label job_start:
    scene bg_college_2
    if character_gender == "Male":
        show casual_male at left
    elif character_gender == "Female":
        show casual_female at left

    menu:
        "Alex is navigating through various job opportunities after completing his college degree."
        "He's faced with a crucial decision that will impact his financial future."

        "Seek for a job":
            $ life = "Part-Time Job Seeker"
            jump job_seek
        "Start a business":
            $ life = "Entrepreneur"
            jump business
        # "Work for a big corporate company":
        #     $ life = "Job"
        #     jump corporate

#Job seeking
label job_seek:
    scene job_bg
    if character_gender == "Male":
        show job_male_sad at left
        "Alex is excited but for opportunities but quickly realizes the financial burden of tuition and living expenses."

    elif character_gender == "Female":
        show job_female_sad at left
        "Alexa is excited but for opportunities but quickly realizes the financial burden of tuition and living expenses."


    menu:
        "Accept a low-paying job without considering future financial goals":
            $ option = "A"
            jump job_seek_a
        "Secure a job with growth potential and invest in further development.":
            $ option = "B"
            jump job_seek_b
        "Explore various job opportunities and choose wisely.":
            $ option = "C"
            jump job_seek_c

label job_seek_a:

    scene job_bg

    if character_gender == "Male":
        show job_male_sad at left
        "Without considering long-term financial goals, Alex finds it challenging to cover expenses and save for the future."
        "This leads to financial instability and missed opportunities for career growth."
        jump end_game

    elif character_gender == "Female":
        show job_female_sad at left
        "Without considering long-term financial goals, Alexa finds it challenging to cover expenses and save for the future."
        "This leads to financial instability and missed opportunities for career growth."
        jump end_game


label job_seek_b:

    scene job_bg

    if character_gender == "Male":
        show job_male_happy at left
        "By prioritizing career growth and financial education, Alex advances steadily in the chosen field."
        "With careful budgeting and strategic investments, Alex achieves financial stability and lays a strong foundation for long-term success."
        jump end_game

    elif character_gender == "Female":
        show job_female_happy at left
        "By prioritizing career growth and financial education, Alex aadvances steadily in the chosen field."
        "With careful budgeting and strategic investments, Alexa achieves financial stability and lays a strong foundation for long-term success."
        jump end_game


label job_seek_c:

    scene job_bg

    if character_gender == "Male":
        show job_male_normal at left
        "Alex takes a balanced approach, considering both immediate financial needs and long-term career goals."
        "While not maximizing immediate earnings, this approach allows Alex to maintain financial stability while also preparing for future advancement opportunities."
        jump end_game

    elif character_gender == "Female":
        show job_male_normal at left
        "Alex takes a balanced approach, considering both immediate financial needs and long-term career goals."
        "While not maximizing immediate earnings, this approach allows Alexa to maintain financial stability while also preparing for future advancement opportunities."
        jump end_game

label business:

    scene job_bg
    if character_gender == "Male":
        show job_male at left
        "Alex is excited but quickly realizes the financial burden of living expenses."

    elif character_gender == "Female":
        show job_female at left
        "Alexa is excited but quickly realizes the financial burden of living expenses."


    menu:
        " Dive into entrepreneurship without proper financial planning or risk assessment.":
            $ option = "A"
            jump business_a
        "Conduct market research and develop a comprehensive plan.":
            $ option = "B"
            jump business_b
        "Start a small-scale business with minimal initial investment.":
            $ option = "C"
            jump business_c






label business_a:
    scene job_bg

    if character_gender == "Male":
        show job_male_sad at left
        "Alex's venture faces financial challenges and struggles to generate profit, resulting in loss of personal savings and potential debt."
        " Without a solid financial plan, the business flounders and fails to reach its potential."
        jump end_game

    elif character_gender == "Female":
        show job_female_sad at left
        "Without considering long-term financial goals, Alexa finds it challenging to cover expenses and save for the future."
        "This leads to financial instability and missed opportunities for career growth."
        jump end_game


label business_b:

    scene job_bg

    if character_gender == "Male":
        show job_male_happy at left
        "By taking a strategic approach to entrepreneurship, Alex's venture gains traction and achieves sustainable growth."
        "With proper financial planning and risk management, Alex navigates challenges effectively and builds a successful business."
        jump end_game

    elif character_gender == "Female":
        show job_female_happy at left
        "By taking a strategic approach to entrepreneurship, Alexa's venture gains traction and achieves sustainable growth."
        "With proper financial planning and risk management, Alexa navigates challenges effectively and builds a successful business."
        jump end_game




label business_c:

    scene job_bg

    if character_gender == "Male":
        show job_male_happy at left
        "While initial growth may be slower, this cautious approach allows Alex to minimize financial risk and learn valuable lessons along the way."
        "By gradually scaling the business and reinvesting profits, Alex lays a solid foundation for future expansion and ensures prudent financial management."
        jump end_game

    elif character_gender == "Female":
        show job_female_happy at left
        "While initial growth may be slower, this cautious approach allows Alexa to minimize financial risk and learn valuable lessons along the way."
        "By gradually scaling the business and reinvesting profits, Alexa lays a solid foundation for future expansion and ensures prudent financial management."
        jump end_game


label end_game:
    scene main_image
    
    if character_gender == "Male":
        show job_male_happy at left
        "While Alex gains valuable experience in his new role, he realizes the importance of financial planning and budgeting to make ends meet on his lower salary."
        "This choice teaches him the importance of being proactive in managing his finances, even in challenging situations."
    elif character_gender == "Female":
        show job_female_happy at left
        "While Alexa gains valuable experience in her new role, she realizes the importance of financial planning and budgeting to make ends meet on her lower salary."
        "This choice teaches her the importance of being proactive in managing her finances, even in challenging situations."
    menu:
        "The End.":
            jump end

# End of game
label end:
    "Thank you for playing CashVille: The Financial Literacy Adventure!"









