import diet_recommendation_model 
age = 20
weight = 75
height = 170
gender = "female"
activity = "Moderate Exercise"
weight_loss_plan = "Weight Loss"
meals_per_day = 3
diet_type = "vegeterain"
json_data=diet_recommendation_model.response_generator(age,weight,height,gender,activity,weight_loss_plan,meals_per_day,diet_type)
print(json_data["BMI"])