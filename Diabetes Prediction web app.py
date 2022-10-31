import numpy as np
import pickle 
import streamlit as st
import time

# loading the saved model
loaded_model = pickle.load(open('C:/Users/DILANKA/Desktop/Project/trained_model.sav','rb'))



# creating a function for Prediction

def diabetes_prediction(input_data):
    
    arr = np.array(input_data).reshape(1,8)
    arr
    #arr=np.array(6,148,72,35,0,33.6,0.627,50).reshape(0,7)
    #print(arr)
    finalOutput = loaded_model.predict(arr)
    print(finalOutput)
    
    
    #width of the bar
    col1 , col2 = st.columns([1,100])

    progress_bar = col2.progress(0)

    for perc_completed in range(100):
        time.sleep(0.00005)
        progress_bar.progress(perc_completed+1)
        
    col2.success("Generating Outcome")
    
    

    if (finalOutput == 1):
        return 'The person is diabetic.'
    else :
        return 'The person is not diabetic.'
    
####################################################
   


def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    

    
    
## only this main function will run from command prompt    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
## Read More 

with st.expander("Click to read more"):
    st.markdown(""" ### 11 Ways to Prevent Type 2 Diabetes""")
    
    st.write('''Type 2 diabetes is a chronic medical condition that 
             affects millions of people worldwide. Unmanaged diabetes 
             may lead to blindness, kidney failure, heart disease, 
             and other serious conditions.
             Before diagnosis, your blood sugar levels may be high — but not high enough to indicate diabetes. This is known as prediabetes. Taking a test like this oneTrusted Source can help you figure out your risk factors for this condition.
             It’s estimated that up to 37% of people with untreated prediabetes develop type 2 diabetes within 4 years (1Trusted Source).
             Progressing from prediabetes to diabetes isn’t inevitable. Although you can’t change certain factors like your genes or age, several lifestyle and dietary modifications may reduce your risk.
             Here are 11 ways to lower your risk of getting diabetes.''')
    st.markdown(""" ##### 1. Reduce your total carb intake""")
    st.write(''' The quantity and quality of your carb intake are both important factors to consider when making dietary changes to help prevent diabetes.
Your body breaks down carbs into small sugar molecules, which are absorbed into your bloodstream. The resulting rise in blood sugar stimulates your pancreas to produce insulin, a hormone that helps sugar move from your bloodstream into your cells.
In people with prediabetes, the body’s cells are resistant to insulin, so blood sugar remains high. To compensate, the pancreas produces more insulin, attempting to bring blood sugar down.
Over time, this can lead to progressively higher blood sugar and insulin levels until the condition turns into type 2 diabetes.
Many studies link frequent added sugar or refined carb intake and diabetes risk. What’s more, replacing these items with foods that have less of an effect on blood sugar may reduce your risk (2Trusted Source, 3Trusted Source, 4Trusted Source).
However, all carb sources — not just sugar and refined carbs — stimulate the release of insulin. Although refined carbs are digested more rapidly than complex carbs, there’s mixed evidence that a food’s blood sugar increase is correlated with diabetes risk (5Trusted Source).
Therefore, managing overall carb intake and choosing carbs that are high in fiber are likely better solutions for preventing diabetes than just limiting highly processed carbs.
Examples of foods and drinks high in added sugars or refined carbs include soda, candy, dessert, white bread, pasta, and sweetened breakfast cereal.
Non-starchy vegetables like broccoli and mushrooms, whole fruit, oatmeal, and whole grain bread and pasta are healthier swaps. These options are higher in fiber, which helps mitigate spikes in blood sugar.
Lean proteins like fish and healthy fats from olive oil, avocado, nuts, and seeds also have less of an effect on blood sugar. They’re great additions to your diet to help prevent type 2 diabetes (4Trusted Source). ''')
    

    st.markdown(""" ##### 2. Exercise regularly""")
    st.write(''' Doing physical activity regularly may help prevent diabetes.
People with prediabetes often have reduced insulin sensitivity, also known as insulin resistance. In this state, your pancreas has to make more insulin to get sugar out of your blood and into cells (6Trusted Source).
Exercise increases the insulin sensitivity of your cells, meaning that you need less insulin to manage your blood sugar levels (7Trusted Source).
Many types of physical activity have been shown to reduce insulin resistance and blood sugar in adults with prediabetes or type 2 diabetes. These include aerobic exercise, high intensity interval training (HIIT), and strength training (8Trusted Source, 9Trusted Source, 10Trusted Source, 11Trusted Source).
One study in 29 people with type 2 diabetes found that HIIT, which involves bursts of intense activity followed by brief recoveries, led to improved blood sugar management and longer sessions of endurance training (8Trusted Source).
However, you don’t need to do HIIT to reap benefits. Short exercise bouts that last as little as 10 minutes, such as brisk walking, are great options. If you’re just beginning an exercise routine, start with short workouts and work up to 150 minutes per week (12).''')

    st.markdown(""" ##### 3. Drink water as your primary beverage""")
    st.write(''' Sticking with water as your drink of choice will help you limit beverages that are high in sugar.
Sugary beverages like soda and sweetened fruit juice have been linked to an increased risk of both type 2 diabetes and latent autoimmune diabetes of adults (LADA).
One large observational study in 2,800 people found that those who drank more than 2 servings of sugary beverages per day had a 99% and 20% increased risk of LADA and type 2 diabetes, respectively (13Trusted Source).
In addition, one review found that 1 serving of sugar-sweetened drinks per day may increase the incidence of type 2 diabetes by 18% (14Trusted Source).
In contrast, increased water intake may lead to better blood sugar management and insulin response (15Trusted Source, 16Trusted Source).
One 24-week study showed that adults with overweight who replaced diet sodas with water while following a weight loss program experienced a decrease in insulin resistance, fasting blood sugar, and insulin levels (16Trusted Source).''')
    

    st.markdown(""" ##### 4. Try to lose excess weight""")
    st.write('''Carrying extra weight may increase your risk of type 2 diabetes.
In particular, visceral fat — excess weight in your midsection and around your abdominal organs — is associated with insulin resistance, inflammation, prediabetes, and type 2 diabetes (17Trusted Source, 18Trusted Source).
Notably, losing even a small amount of weight — as little as 5–7% — may help lower your risk of type 2 diabetes if you have prediabetes, overweight, or obesity (19Trusted Source, 20Trusted Source).
A randomized, 2-year study in more than 1,000 people at increased risk of type 2 diabetes showed that exercise, diet, and weight loss interventions significantly reduced the risk of this disease by 40% to 47%, compared with a control group (20Trusted Source).
Many healthy weight loss strategies exist. Preparing a balanced plate with non-starchy vegetables, lean proteins, complex carbs, and healthy fats is a great place to start.
''')


    st.markdown(""" ##### 5. Quit smoking""")
    st.write(''' Smoking has been shown to cause or contribute to many serious health conditions, including heart disease, chronic obstructive pulmonary disease (COPD), and lung and intestinal cancers (21Trusted Source).
Research also links smoking to type 2 diabetes. While the mechanisms aren’t fully understood, it’s thought that smoking may increase insulin resistance and inhibit insulin secretion (22Trusted Source, 23Trusted Source, 24Trusted Source).
Plus, heavy, more frequent smoking is linked to a higher risk of diabetes than smoking fewer cigarettes (23Trusted Source, 25Trusted Source).
Importantly, studies suggest that quitting smoking may reduce diabetes risk (25Trusted Source).
One large study in more than 53,000 Japanese adults found that diabetes risk in those who smoke decreases over time after quitting. Smoking cessation for 10 or more years may even decrease this risk to about the same level as those who never smoked (25Trusted Source).''')

    st.markdown(""" ##### 6. Reduce your portion sizes""")
    st.write(''' Eating portion sizes appropriate for your needs may also help prevent diabetes.
Eating too much food at one time has been shown to cause higher blood sugar and insulin levels in people at risk of diabetes (26Trusted Source).
Conversely, eating smaller portions may lead to reduced calorie intake and subsequent weight loss, which may in turn lower your risk of diabetes.
While there are few studies on the effects of portion management in people with prediabetes, research in those with type 2 diabetes offers some insight.
A study in adults with overweight or obesity, including some with type 2 diabetes, found that following a meal plan with portion-managed meal replacements and appropriate portions of other healthy foods led to weight loss and reductions in body fat (27Trusted Source).
What’s more, guidelines for the prevention and management of type 2 diabetes support portion management as a way to help individuals maintain a healthy weight (28Trusted Source).
To manage your portion sizes, make your plate half non-starchy vegetables, a quarter lean protein, and a quarter complex carbs like fruit or whole grains. If you’re at a restaurant that serves large portions, choose an appetizer for your main course or ask for a half portion.
Plus, instead of eating snacks straight out of the bag, place your desired amount into a separate dish.''')

    st.markdown(""" ##### 7. Cut back on sedentary behaviors""")
    st.write('''It’s important to avoid sedentary behaviors, such as getting very little physical activity or sitting during most of the day, to help prevent diabetes.
Observational studies consistently link sedentary behavior and an increased risk of type 2 diabetes (29Trusted Source).
One study in more than 6,000 older women found that those who had the highest amount of sedentary time per day — 10 or more hours — were more than twice as likely to develop diabetes than those with 8.3 hours or less of sedentary time (30).
Changing sedentary behavior can be as simple as standing up from your desk and walking around for a few minutes every half hour. Wearing a fitness watch or device that reminds you to walk at least 250 steps per hour may also be helpful.
Still, it can be hard to reverse firmly entrenched habits. One study that gave young adults at risk of diabetes a 12-month program designed to change sedentary behavior found that they hadn’t reduced sitting time (31Trusted Source).
As such, it’s important to set realistic and achievable goals, such as standing while talking on the phone or taking the stairs instead of the elevator. ''')


    st.markdown(""" ##### 8. Follow a high fiber diet""")
    st.write('''Eating plenty of fiber is beneficial for gut health and weight management. It may also help prevent diabetes.
Studies in people with prediabetes and older women with obesity show that this nutrient helps keep blood sugar and insulin levels low (32Trusted Source, 33Trusted Source).
Fiber can be divided into two broad categories: soluble, which absorbs water, and insoluble, which doesn’t.
Soluble fiber and water form a gel in your digestive tract that slows down food absorption, leading to a more gradual rise in blood sugar. Thus, eating more soluble fiber may reduce fasting blood sugar and insulin levels (34Trusted Source, 35Trusted Source).
Insoluble fiber has also been linked to reductions in blood sugar levels (36Trusted Source).
While many studies on fiber and diabetes use fiber supplements instead of high fiber foods, getting more fiber from foods is likely beneficial. ''')


    st.markdown(""" ##### 9. Optimize your vitamin D levels""")
    st.write(''' Vitamin D is important for blood sugar management.
Indeed, studies link vitamin D deficiency to insulin resistance and type 2 diabetes (37Trusted Source, 38Trusted Source).
Some studies also show that vitamin D supplements may improve many aspects of blood sugar management in people with prediabetes, compared with control groups (38Trusted Source, 39Trusted Source, 40Trusted Source).
However, current research is mixed on whether vitamin D supplements prevent the progression from prediabetes to type 2 diabetes (40Trusted Source, 41Trusted Source).
Still, maintaining adequate vitamin D levels is important for your health, especially if you’re deficient. Good food sources include fatty fish and cod liver oil. In addition, sun exposure can increase vitamin D levels.
For some people, supplementing with vitamin D daily may be necessary to achieve and maintain optimal levels. Speak with a doctor to get your vitamin D levels checked before starting a supplement.''')


    st.markdown(""" ##### 10. Minimize your intake of highly processed foods""")
    st.write('''Lowering your intake of heavily processed foods benefits several aspects of health.
Many foods undergo some form of processing. Thus, processed foods, which include plain yogurt and frozen vegetables, aren’t inherently unhealthy.
Yet, highly processed foods have undergone significantly more processing and often contain added sugars, unhealthy fats, and chemical preservatives. Examples include hot dogs, chips, frozen desserts, sodas, and candy bars.
Observational research associates diets high in ultra-processed foods with a higher risk of type 2 diabetes (42Trusted Source).
Conversely, cutting back on packaged foods that are high in vegetable oils, refined grains, and additives may help reduce your risk of diabetes (43Trusted Source, 44Trusted Source).
This may be partly due to the anti-diabetes effects of whole foods like nuts, vegetables, and fruits. One study found that diets high in processed foods increased diabetes risk by 30% but that eating nutritious whole foods reduce this risk (44Trusted Source). ''')


    st.markdown(""" ##### 11. Drink coffee or tea""")
    st.write(''' Although it’s best to make water your primary beverage, research suggests that including coffee or tea in your diet may help you avoid diabetes.
Studies report that daily coffee intake reduces type 2 diabetes risk by up to 54%, with the greatest effect generally seen in people with the highest consumption (45Trusted Source).
Another study linked daily green tea intake to a lower risk of type 2 diabetes (46Trusted Source).
Coffee and tea have antioxidants known as polyphenols that may help protect against diabetes (47Trusted Source).
It’s best to serve these beverages plain or with a splash of milk. Added sugars and syrups may increase blood sugar levels and detract from their protective effects.''')

    st.markdown(""" ##### Let us AVOID Diabetic..""")
    st.write(''' When it comes to preventing diabetes, there are many steps you can take.
Rather than viewing prediabetes as a stepping stone to diabetes, it may be helpful to see it as a motivator for making changes that can help reduce your risk.
Eating the right foods and adopting other lifestyle behaviors that promote healthy blood sugar and insulin levels will give you the best chance of avoiding diabetes.''')


