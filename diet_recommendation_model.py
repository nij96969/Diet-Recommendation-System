"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You are diet recommendation system .  You have to provide recommendation based on the the input i provide . Inputs are Age , Height , Weight , Gender , Activity , Weight loss plan and Meals per day , Diet type . Here Activity will be in {Little/No Exercise , Little Exercise , Moderate Exercise(3 to 5 days) , Very active(6-7 days) , Extra Active (very active and physical Job) . For weight loss plan type will be Maintain Weight , Mild Weight Loss , Weight Loss , Extreme weight loss . Meal per day can be 3 to 5 . Based on this input you will output of \nBody Mass Index (BMI) (kg / m^2) and tell whether it is Normal or Obese . Based on the weight loss plan you use Calories Calculator which shows Calorie Intake per day. Based on the Meals per day show recommendation of foods and intake . Diet type can be vegetarian or non-vegetarian . You will also show the nutritional value of it Calories . Nutritional values will include FatContent , SaturatedFatContent , CholesterolContent , SodiumContent , CarbohydrateConten , FiberContent , SugarContent , ProteinContent .The output should be in json format and Important note : Nutritional Values should be string format not in numerical . Make sure to recommend new diet every time this is very important .",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Age 21 , Height 190 cm , Gender Male ,  Activity Very active , Weight loss plan Maintain Weight , Meals per day 3",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"BMI\": 24.81,\n  \"BMI_Category\": \"Normal\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 3000\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Oatmeal with berries and nuts (1 cup oatmeal, 1/2 cup berries, 1/4 cup nuts)\",\n        \"2 boiled eggs\",\n        \"1 glass of milk\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 15g,\n        \"SaturatedFatContent\": 5g,\n        \"CholesterolContent\": 300mg,\n        \"SodiumContent\": 200mg,\n        \"CarbohydrateContent\": 60g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 15g,\n        \"ProteinContent\": 25g\n      },\n      \"Calories\": 500\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Grilled chicken salad (4oz grilled chicken, 1 cup mixed greens, 1/2 cup vegetables, 2 tbsp dressing)\",\n        \"1 whole-wheat roll\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 18g,\n        \"SaturatedFatContent\": 5g,\n        \"CholesterolContent\": 80mg,\n        \"SodiumContent\": 500mg,\n        \"CarbohydrateContent\": 40g,\n        \"FiberContent\": 8g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 30g\n      },\n      \"Calories\": 550\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Salmon with roasted vegetables (4oz salmon, 1 cup roasted vegetables)\",\n        \"1 cup brown rice\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 20g,\n        \"SaturatedFatContent\": 5g,\n        \"CholesterolContent\": 80mg,\n        \"SodiumContent\": 200mg,\n        \"CarbohydrateContent\": 50g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 35g\n      },\n      \"Calories\": 600\n    }\n  }\n}\n```\n\n**Explanation:**\n\n* **BMI:** Calculated using the formula BMI = weight (kg) / height (m)^2.  A BMI of 24.81 falls within the \"Normal\" range.\n* **Calories_Calculator:**  For a \"Very active\" male maintaining weight, an estimated daily calorie intake of 3000 is recommended.\n* **Meal_Recommendations:**  Each meal is designed to provide a balanced mix of macronutrients (protein, carbohydrates, fats) and essential vitamins and minerals. \n\n**Please note:** \n\n* These are just examples, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\n* It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "The Explanation you provided should be included at the end of json format",
        "Make sure that all the parameters Age , Weight , Height , Gender , Activity , Weight Loss Plan , Meals per day are provided . If any is missing ask for that parameter ",
        "Age 50 , Weight 63 kg , Height 160 cm , Gender Female , Activity No Exercise , Weight Loss Plan Maintain Weight , Meals per day 3  ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"BMI\": 24.61,\n  \"BMI_Category\": \"Normal\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 1800\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Oatmeal with fruit and nuts (1 cup oatmeal, 1/2 cup berries, 1/4 cup nuts)\",\n        \"1 glass of low-fat milk\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 10g,\n        \"SaturatedFatContent\": 3g,\n        \"CholesterolContent\": 150mg,\n        \"SodiumContent\": 150mg,\n        \"CarbohydrateContent\": 50g,\n        \"FiberContent\": 8g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 15g\n      },\n      \"Calories\": 350\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Tuna salad sandwich (2 oz tuna, 1 slice whole-wheat bread, 1/4 cup vegetables)\",\n        \"1 piece of fruit\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 12g,\n        \"SaturatedFatContent\": 3g,\n        \"CholesterolContent\": 50mg,\n        \"SodiumContent\": 400mg,\n        \"CarbohydrateContent\": 35g,\n        \"FiberContent\": 5g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 400\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Chicken stir-fry (4 oz chicken, 1 cup vegetables, 1/2 cup brown rice)\",\n        \"1 cup salad\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 15g,\n        \"SaturatedFatContent\": 4g,\n        \"CholesterolContent\": 70mg,\n        \"SodiumContent\": 300mg,\n        \"CarbohydrateContent\": 45g,\n        \"FiberContent\": 8g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 25g\n      },\n      \"Calories\": 450\n    }\n  },\n  \"Explanation\": \"The provided diet plan is tailored for a 50-year-old female weighing 63 kg and standing at 160 cm. With a BMI of 24.61, she falls into the 'Normal' category. Since she has 'No Exercise' and aims to 'Maintain Weight', an estimated daily calorie intake of 1800 is recommended.  The meal plan includes three meals a day, each offering a balanced mix of macronutrients and essential vitamins and minerals.  These are just examples, and the food choices and portions can be adjusted based on individual needs and preferences. It is crucial to consult a registered dietitian or healthcare professional for personalized advice.\"\n}\n```\n\n**Explanation:**\n\n* **BMI:** Calculated using the formula BMI = weight (kg) / height (m)^2.  A BMI of 24.61 falls within the \"Normal\" range.\n* **Calories_Calculator:**  For a \"No Exercise\" female maintaining weight, an estimated daily calorie intake of 1800 is recommended.\n* **Meal_Recommendations:**  Each meal is designed to provide a balanced mix of macronutrients (protein, carbohydrates, fats) and essential vitamins and minerals. \n* **Explanation:** This section provides a detailed explanation of how the diet plan was created, including the factors considered and the rationale behind the recommendations. \n\n**Key Points:**\n\n* This is just an example, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\n* It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Age 21 , Height 190 cm , Gender Male ,  Activity Very active , Weight loss plan Maintain Weight , Meals per day 3 , Diet type vegeterain",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"BMI\": 24.81,\n  \"BMI_Category\": \"Normal\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 3000\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Oatmeal with berries and nuts (1 cup oatmeal, 1/2 cup berries, 1/4 cup nuts)\",\n        \"Tofu scramble with vegetables (1/2 cup tofu, 1 cup vegetables)\",\n        \"1 glass of soy milk\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 15g,\n        \"SaturatedFatContent\": 4g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 200mg,\n        \"CarbohydrateContent\": 60g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 15g,\n        \"ProteinContent\": 25g\n      },\n      \"Calories\": 500\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Lentil soup (1 cup lentil soup)\",\n        \"2 slices of whole-wheat bread with hummus\",\n        \"1 apple\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 10g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 400mg,\n        \"CarbohydrateContent\": 50g,\n        \"FiberContent\": 15g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 550\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Quinoa salad with vegetables and chickpeas (1 cup quinoa, 1 cup vegetables, 1/2 cup chickpeas)\",\n        \"1 cup mixed greens salad with vinaigrette dressing\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 12g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 250mg,\n        \"CarbohydrateContent\": 55g,\n        \"FiberContent\": 12g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 600\n    }\n  },\n  \"Explanation\": \"This vegetarian diet plan caters to a 21-year-old male, standing at 190 cm, with a BMI of 24.81, falling under the 'Normal' category. As a 'Very active' individual aiming to 'Maintain Weight', a daily calorie intake of 3000 is recommended. This plan consists of three meals, each offering a balanced mix of protein, carbohydrates, and healthy fats. The meals are rich in fiber and essential nutrients, supporting a healthy and active lifestyle. It's important to note that these are just examples, and the food choices and portions can be adjusted based on individual needs and preferences. It is crucial to consult a registered dietitian or healthcare professional for personalized advice.\"\n}\n```\n\n**Explanation:**\n\n* **BMI:** Calculated using the formula BMI = weight (kg) / height (m)^2.  A BMI of 24.81 falls within the \"Normal\" range.\n* **Calories_Calculator:**  For a \"Very active\" male maintaining weight, an estimated daily calorie intake of 3000 is recommended.\n* **Meal_Recommendations:**  Each meal is designed to provide a balanced mix of macronutrients (protein, carbohydrates, fats) and essential vitamins and minerals while adhering to a vegetarian diet. \n* **Explanation:** This section provides a detailed explanation of how the diet plan was created, including the factors considered and the rationale behind the recommendations. \n\n**Key Points:**\n\n* This is just an example, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\n* It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "keep the Explanation and key points and keep it only in json which you are doing it correctly do not add extra information out side the json",
        "Age 21 , Weight 80 kg , Height 190 cm , Gender Male ,  Activity Very active , Weight loss plan Maintain Weight , Meals per day 3 , Diet type vegeterain",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"BMI\": 22.18,\n  \"BMI_Category\": \"Normal\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 3000\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Oatmeal with berries and nuts (1 cup oatmeal, 1/2 cup berries, 1/4 cup nuts)\",\n        \"Tofu scramble with vegetables (1/2 cup tofu, 1 cup vegetables)\",\n        \"1 glass of soy milk\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 15g,\n        \"SaturatedFatContent\": 4g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 200mg,\n        \"CarbohydrateContent\": 60g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 15g,\n        \"ProteinContent\": 25g\n      },\n      \"Calories\": 500\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Lentil soup (1 cup lentil soup)\",\n        \"2 slices of whole-wheat bread with hummus\",\n        \"1 apple\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 10g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 400mg,\n        \"CarbohydrateContent\": 50g,\n        \"FiberContent\": 15g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 550\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Quinoa salad with vegetables and chickpeas (1 cup quinoa, 1 cup vegetables, 1/2 cup chickpeas)\",\n        \"1 cup mixed greens salad with vinaigrette dressing\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 12g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 250mg,\n        \"CarbohydrateContent\": 55g,\n        \"FiberContent\": 12g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 600\n    }\n  },\n  \"Explanation\": \"This vegetarian diet plan caters to a 21-year-old male, standing at 190 cm, with a BMI of 22.18, falling under the 'Normal' category. As a 'Very active' individual aiming to 'Maintain Weight', a daily calorie intake of 3000 is recommended. This plan consists of three meals, each offering a balanced mix of protein, carbohydrates, and healthy fats. The meals are rich in fiber and essential nutrients, supporting a healthy and active lifestyle. It's important to note that these are just examples, and the food choices and portions can be adjusted based on individual needs and preferences. It is crucial to consult a registered dietitian or healthcare professional for personalized advice.\",\n  \"Key Points\": [\n    \"This is just an example, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\",\n    \"It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations.\"\n  ]\n}\n```\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "you can provide different recommendation every time , you don't necessarily have to stick to one type of diet",
        "Age 21 , Weight 80 kg , Height 190 cm , Gender Male , Activity Very active , Weight loss plan Maintain Weight , Meals per day 3 , Diet type vegeterain",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"BMI\": 22.18,\n  \"BMI_Category\": \"Normal\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 3000\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Tofu scramble with spinach and mushrooms (1/2 cup tofu, 1 cup spinach, 1/2 cup mushrooms)\",\n        \"Whole-wheat toast with avocado (2 slices whole-wheat toast, 1/4 avocado)\",\n        \"1 glass of almond milk\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 18g,\n        \"SaturatedFatContent\": 4g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 250mg,\n        \"CarbohydrateContent\": 50g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 550\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Chickpea and vegetable curry (1 cup chickpea curry, 1/2 cup brown rice)\",\n        \"Mixed greens salad with lemon vinaigrette dressing (1 cup mixed greens, 2 tbsp lemon vinaigrette)\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 12g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 350mg,\n        \"CarbohydrateContent\": 60g,\n        \"FiberContent\": 15g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 25g\n      },\n      \"Calories\": 600\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Black bean burgers on whole-wheat buns (2 black bean burgers, 2 whole-wheat buns)\",\n        \"Sweet potato fries (1/2 cup sweet potato fries)\",\n        \"1 cup mixed greens salad\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 20g,\n        \"SaturatedFatContent\": 5g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 400mg,\n        \"CarbohydrateContent\": 65g,\n        \"FiberContent\": 12g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 30g\n      },\n      \"Calories\": 650\n    }\n  },\n  \"Explanation\": \"This vegetarian diet plan caters to a 21-year-old male, standing at 190 cm, with a BMI of 22.18, falling under the 'Normal' category. As a 'Very active' individual aiming to 'Maintain Weight', a daily calorie intake of 3000 is recommended. This plan consists of three meals, each offering a balanced mix of protein, carbohydrates, and healthy fats. The meals are rich in fiber and essential nutrients, supporting a healthy and active lifestyle. It's important to note that these are just examples, and the food choices and portions can be adjusted based on individual needs and preferences. It is crucial to consult a registered dietitian or healthcare professional for personalized advice.\",\n  \"Key Points\": [\n    \"This is just an example, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\",\n    \"It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations.\"\n  ]\n}\n```\n\n**Key Changes for this recommendation:**\n\n* **Meal 1:**  Includes a tofu scramble with spinach and mushrooms, which is a more protein-rich and fiber-rich option compared to the previous recommendation.\n* **Meal 2:** Offers a chickpea and vegetable curry with brown rice for a more diverse flavor profile and a good source of complex carbohydrates.\n* **Meal 3:** Features black bean burgers on whole-wheat buns for a satisfying and plant-based protein source. \n\nRemember, these recommendations are just starting points. You can customize them based on your preferences and dietary needs.  Always consult with a healthcare professional before making significant changes to your diet. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Age 25 , Weight 70 kg , Height 170 cm , Gender female , Activity Little Execise , Weight loss plan Maintain Weight , Meals per day 3 , Diet type vegeterain",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"BMI\": 24.22,\n  \"BMI_Category\": \"Normal\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 1800\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Overnight oats with chia seeds and berries (1/2 cup rolled oats, 1/4 cup chia seeds, 1/2 cup berries, 1/2 cup almond milk)\",\n        \"1 slice whole-wheat toast with avocado (1 slice whole-wheat toast, 1/4 avocado)\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 15g,\n        \"SaturatedFatContent\": 3g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 150mg,\n        \"CarbohydrateContent\": 50g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 15g\n      },\n      \"Calories\": 400\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Lentil salad with quinoa and vegetables (1 cup lentils, 1/2 cup quinoa, 1 cup vegetables, 2 tbsp lemon vinaigrette)\",\n        \"1 apple\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 10g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 250mg,\n        \"CarbohydrateContent\": 55g,\n        \"FiberContent\": 15g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 450\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Vegetable stir-fry with tofu (1 cup vegetables, 1/2 cup tofu, 1/2 cup brown rice)\",\n        \"1 cup mixed greens salad with vinaigrette dressing\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 12g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 300mg,\n        \"CarbohydrateContent\": 50g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 500\n    }\n  },\n  \"Explanation\": \"This vegetarian diet plan caters to a 25-year-old female, standing at 170 cm, with a BMI of 24.22, falling under the 'Normal' category. As an individual with 'Little Exercise' aiming to 'Maintain Weight', a daily calorie intake of 1800 is recommended. This plan consists of three meals, each offering a balanced mix of protein, carbohydrates, and healthy fats. The meals are rich in fiber and essential nutrients, supporting a healthy lifestyle. It's important to note that these are just examples, and the food choices and portions can be adjusted based on individual needs and preferences. It is crucial to consult a registered dietitian or healthcare professional for personalized advice.\",\n  \"Key Points\": [\n    \"This is just an example, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\",\n    \"It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations.\"\n  ]\n}\n``` \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Age 21 , Weight 80 kg , Height 190 cm , Gender Male , Activity Very active , Weight loss plan Maintain Weight , Meals per day 3 , Diet type vegeterain recommend a new diet",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"BMI\": 22.18,\n  \"BMI_Category\": \"Normal\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 3000\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Smoothie with fruit, spinach, and protein powder (1 cup fruit, 1 cup spinach, 1 scoop protein powder, 1/2 cup almond milk)\",\n        \"1 slice whole-wheat toast with almond butter (1 slice whole-wheat toast, 1 tbsp almond butter)\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 15g,\n        \"SaturatedFatContent\": 3g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 200mg,\n        \"CarbohydrateContent\": 55g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 15g,\n        \"ProteinContent\": 25g\n      },\n      \"Calories\": 500\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Black bean and corn salad with quinoa (1 cup black beans, 1/2 cup corn, 1/2 cup quinoa, 1/2 cup chopped vegetables, 2 tbsp lime juice, 1 tbsp olive oil)\",\n        \"1 cup mixed greens salad with vinaigrette dressing\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 12g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 250mg,\n        \"CarbohydrateContent\": 60g,\n        \"FiberContent\": 15g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 550\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Lentil and vegetable curry with brown rice (1 cup lentil and vegetable curry, 1/2 cup brown rice)\",\n        \"1 small banana\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 10g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 300mg,\n        \"CarbohydrateContent\": 65g,\n        \"FiberContent\": 12g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 25g\n      },\n      \"Calories\": 600\n    }\n  },\n  \"Explanation\": \"This vegetarian diet plan caters to a 21-year-old male, standing at 190 cm, with a BMI of 22.18, falling under the 'Normal' category. As a 'Very active' individual aiming to 'Maintain Weight', a daily calorie intake of 3000 is recommended. This plan consists of three meals, each offering a balanced mix of protein, carbohydrates, and healthy fats. The meals are rich in fiber and essential nutrients, supporting a healthy and active lifestyle. It's important to note that these are just examples, and the food choices and portions can be adjusted based on individual needs and preferences. It is crucial to consult a registered dietitian or healthcare professional for personalized advice.\",\n  \"Key Points\": [\n    \"This is just an example, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\",\n    \"It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations.\"\n  ]\n}\n```\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Age 21 , Weight 80 kg , Height 190 cm , Gender Male , Activity Very active , Weight loss plan Maintain Weight , Meals per day 3 , Diet type vegeterain new diet",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"BMI\": 22.18,\n  \"BMI_Category\": \"Normal\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 3000\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Tofu and vegetable stir-fry with brown rice (1/2 cup tofu, 1 cup vegetables, 1/2 cup brown rice)\",\n        \"1 cup mixed greens salad with lemon vinaigrette dressing (1 cup mixed greens, 2 tbsp lemon vinaigrette)\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 12g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 250mg,\n        \"CarbohydrateContent\": 60g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 25g\n      },\n      \"Calories\": 550\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Chickpea and vegetable soup (1 cup chickpea and vegetable soup)\",\n        \"2 slices of whole-wheat bread with hummus (2 slices whole-wheat bread, 2 tbsp hummus)\",\n        \"1 apple\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 10g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 350mg,\n        \"CarbohydrateContent\": 50g,\n        \"FiberContent\": 12g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 15g\n      },\n      \"Calories\": 450\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Black bean burgers on whole-wheat buns (2 black bean burgers, 2 whole-wheat buns)\",\n        \"Sweet potato fries (1/2 cup sweet potato fries)\",\n        \"1 cup mixed greens salad\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 18g,\n        \"SaturatedFatContent\": 4g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 400mg,\n        \"CarbohydrateContent\": 60g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 25g\n      },\n      \"Calories\": 600\n    }\n  },\n  \"Explanation\": \"This vegetarian diet plan caters to a 21-year-old male, standing at 190 cm, with a BMI of 22.18, falling under the 'Normal' category. As a 'Very active' individual aiming to 'Maintain Weight', a daily calorie intake of 3000 is recommended. This plan consists of three meals, each offering a balanced mix of protein, carbohydrates, and healthy fats. The meals are rich in fiber and essential nutrients, supporting a healthy and active lifestyle. It's important to note that these are just examples, and the food choices and portions can be adjusted based on individual needs and preferences. It is crucial to consult a registered dietitian or healthcare professional for personalized advice.\",\n  \"Key Points\": [\n    \"This is just an example, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\",\n    \"It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations.\"\n  ]\n}\n```\n\n**Key Changes for this recommendation:**\n\n* **Meal 1:** Includes a tofu and vegetable stir-fry with brown rice, providing a good balance of protein, complex carbs, and fiber.\n* **Meal 2:**  Features a hearty chickpea and vegetable soup for a warm and filling meal, along with whole-wheat bread for additional carbohydrates. \n* **Meal 3:** Keeps the black bean burgers and sweet potato fries, but includes a side of mixed greens salad for added nutrients and fiber. \n\nRemember, these are just starting points. You can customize these meals based on your preferences and dietary needs.  Always consult with a healthcare professional before making significant changes to your diet. \n\n\n",
      ],
    },
  ]
)

def extract_content_from_response(response_text):
    start_index = response_text.find("```json") + len("```json") + 1
    end_index = response_text.find("```", start_index)
    # print(f"start Index {start_index} , end index {end_index}")
    extracted_content = response_text[start_index:end_index]

    return extracted_content

# age = 20
# weight = 75
# height = 170
# gender = "female"
# activity = "Moderate Exercise"
# weight_loss_plan = "Weight Loss"
# meals_per_day = 3
# diet_type = "vegeterain"

# def recommendation_response():
#     input = f"Age {age} , Weight(kg) {weight} , Height(cm) {height} , Gender {gender} , Activity {activity} , Weight Loss Plan {weight_loss_plan} , Meals Per Day {meals_per_day} , Diet Type {diet_type} new diet"
#     response = chat_session.send_message(input)
#     print(response.text + "\n\n\n\n\n\n\n\n")
#     print(extract_content_from_response(response_text = response.text))

# input = f"Age {age} , Weight(kg) {weight} , Height(cm) {height} , Gender {gender} , Activity {activity} , Weight Loss Plan {weight_loss_plan} , Meals Per Day {meals_per_day} , Diet Type {diet_type} new diet"
# response = chat_session.send_message(input)
# print(extract_content_from_response(response_text = response.text))

model2 = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You have to validate the json in the format that i provide ",
)

chat_session2 = model2.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "{\n  \"BMI\": 25.95,\n  \"BMI_Category\": \"Overweight\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 1600\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Overnight oats with chia seeds and berries (1/2 cup rolled oats, 1/4 cup chia seeds, 1/2 cup berries, 1/2 cup almond milk)\",\n        \"1 slice whole-wheat toast with avocado (1 slice whole-wheat toast, 1/4 avocado)\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 12g,\n        \"SaturatedFatContent\": 3g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 150mg,\n        \"CarbohydrateContent\": 40g,\n        \"FiberContent\": 8g,\n        \"SugarContent\": 10g,\n        \"ProteinContent\": 12g\n      },\n      \"Calories\": 350\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Lentil soup with whole-wheat bread (1 cup lentil soup, 1 slice whole-wheat bread)\",\n        \"Mixed greens salad with vinaigrette dressing (1 cup mixed greens, 2 tbsp vinaigrette dressing)\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 8g,\n        \"SaturatedFatContent\": 1g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 300mg,\n        \"CarbohydrateContent\": 45g,\n        \"FiberContent\": 10g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 18g\n      },\n      \"Calories\": 350\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Quinoa bowl with roasted vegetables and chickpeas (1/2 cup quinoa, 1 cup roasted vegetables, 1/2 cup chickpeas)\",\n        \"1 cup mixed greens salad with lemon vinaigrette dressing\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": 10g,\n        \"SaturatedFatContent\": 2g,\n        \"CholesterolContent\": 0mg,\n        \"SodiumContent\": 200mg,\n        \"CarbohydrateContent\": 50g,\n        \"FiberContent\": 12g,\n        \"SugarContent\": 5g,\n        \"ProteinContent\": 20g\n      },\n      \"Calories\": 450\n    }\n  },\n  \"Explanation\": \"This vegetarian diet plan caters to a 20-year-old female, standing at 170 cm, with a BMI of 25.95, falling under the 'Overweight' category. As an individual with 'Moderate Exercise' aiming for 'Weight Loss', a daily calorie intake of 1600 is recommended. This plan consists of three meals, each offering a balanced mix of protein, carbohydrates, and healthy fats. The meals are rich in fiber and essential nutrients, supporting a healthy lifestyle and weight management. It's important to note that these are just examples, and the food choices and portions can be adjusted based on individual needs and preferences. It is crucial to consult a registered dietitian or healthcare professional for personalized advice.\",\n  \"Key Points\": [\n    \"This is just an example, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\",\n    \"It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations.\"\n  ]\n}",
        "Correct ::",
        "{\n  \"BMI\": 25.95,\n  \"BMI_Category\": \"Overweight\",\n  \"Calories_Calculator\": {\n    \"Calorie_Intake_per_day\": 1600\n  },\n  \"Meal_Recommendations\": {\n    \"Meal_1\": {\n      \"Food_Items\": [\n        \"Overnight oats with chia seeds and berries (1/2 cup rolled oats, 1/4 cup chia seeds, 1/2 cup berries, 1/2 cup almond milk)\",\n        \"1 slice whole-wheat toast with avocado (1 slice whole-wheat toast, 1/4 avocado)\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": \"12g\",\n        \"SaturatedFatContent\": \"3g\",\n        \"CholesterolContent\": \"0mg\",\n        \"SodiumContent\": \"150mg\",\n        \"CarbohydrateContent\": \"40g\",\n        \"FiberContent\": \"8g\",\n        \"SugarContent\": \"10g\",\n        \"ProteinContent\": \"12g\"\n      },\n      \"Calories\": 350\n    },\n    \"Meal_2\": {\n      \"Food_Items\": [\n        \"Lentil soup with whole-wheat bread (1 cup lentil soup, 1 slice whole-wheat bread)\",\n        \"Mixed greens salad with vinaigrette dressing (1 cup mixed greens, 2 tbsp vinaigrette dressing)\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": \"8g\",\n        \"SaturatedFatContent\": \"1g\",\n        \"CholesterolContent\": \"0mg\",\n        \"SodiumContent\": \"300mg\",\n        \"CarbohydrateContent\": \"45g\",\n        \"FiberContent\": \"10g\",\n        \"SugarContent\": \"5g\",\n        \"ProteinContent\": \"18g\"\n      },\n      \"Calories\": 350\n    },\n    \"Meal_3\": {\n      \"Food_Items\": [\n        \"Quinoa bowl with roasted vegetables and chickpeas (1/2 cup quinoa, 1 cup roasted vegetables, 1/2 cup chickpeas)\",\n        \"1 cup mixed greens salad with lemon vinaigrette dressing\"\n      ],\n      \"Nutritional_Values\": {\n        \"FatContent\": \"10g\",\n        \"SaturatedFatContent\": \"2g\",\n        \"CholesterolContent\": \"0mg\",\n        \"SodiumContent\": \"200mg\",\n        \"CarbohydrateContent\": \"50g\",\n        \"FiberContent\": \"12g\",\n        \"SugarContent\": \"5g\",\n        \"ProteinContent\": \"20g\"\n      },\n      \"Calories\": 450\n    }\n  },\n  \"Explanation\": \"This vegetarian diet plan caters to a 20-year-old female, standing at 170 cm, with a BMI of 25.95, falling under the 'Overweight' category. As an individual with 'Moderate Exercise' aiming for 'Weight Loss', a daily calorie intake of 1600 is recommended. This plan consists of three meals, each offering a balanced mix of protein, carbohydrates, and healthy fats. The meals are rich in fiber and essential nutrients, supporting a healthy lifestyle and weight management. It's important to note that these are just examples, and the food choices and portions can be adjusted based on individual needs and preferences. It is crucial to consult a registered dietitian or healthcare professional for personalized advice.\",\n  \"Key Points\": [\n    \"This is just an example, and you may need to adjust the food choices and portion sizes based on your individual preferences and needs.\",\n    \"It's always best to consult with a registered dietitian or healthcare professional for personalized diet recommendations.\"\n  ]\n}\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The JSON you provided is valid.  It's well-structured and follows the rules of JSON syntax. \n\nHowever, you're asking for validation in a specific format, but you haven't actually provided that format. Please provide the format you're looking for, and I can validate the JSON against it. \n\nFor example, if you want to validate that all the \"Nutritional_Values\" values are strings, you can specify that format. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Yes make all Nutritional Values as JSON ",
      ],
    },
  ]
)

# response2 = chat_session2.send_message(response.text)

# print(response2.text)

import json

# Example response
def jsonify(response_text):
  response_text = extract_content_from_response(response_text.text)  # Replace with actual response text
  # print(response_text)  # Check the content before parsing

  try:
      json_data = json.loads(response_text)
      # print(json_data["BMI"])
      # print(json_data["BMI_Category"])
  except json.JSONDecodeError as e:
      print("JSONDecodeError:", e)
  return json_data

def response_generator(age,weight,height,gender,activity,weight_loss_plan,meals_per_day,diet_type):
    input = f"Age {age} , Weight(kg) {weight} , Height(cm) {height} , Gender {gender} , Activity {activity} , Weight Loss Plan {weight_loss_plan} , Meals Per Day {meals_per_day} , Diet Type {diet_type} new diet"
    response = chat_session.send_message(input)
    # print(extract_content_from_response(response_text = response.text))
    response2 = chat_session2.send_message(response.text)
    json_data=jsonify(response2)
    return json_data