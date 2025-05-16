import requests
import json
import os
import time

food_list = [
    "banana", "apple", "orange", "rice", "chicken breast", "beef steak", "pork chop",
    "salmon", "egg", "bread", "milk", "cheese", "yogurt", "potato", "carrot", "tomato",
    "broccoli", "spinach", "avocado", "almonds", "walnuts", "peanut butter", "oatmeal",
    "pasta", "pizza", "hamburger", "fried rice", "noodles", "tofu", "lentils", "chickpeas",
    "black beans", "green beans", "cucumber", "onion", "garlic", "mushrooms", "shrimp",
    "crab", "lobster", "turkey", "duck", "bacon", "sausage", "butter", "olive oil",
    "sugar", "honey", "chocolate", "cake", "cookie", "ice cream", "coffee", "tea",
    "orange juice", "apple juice", "beer", "wine", "watermelon", "grapes", "pineapple",
    "strawberry", "blueberry", "raspberry", "peach", "pear", "plum", "cherry",
    "corn", "sweet potato", "pumpkin", "zucchini", "cauliflower", "kale", "lettuce",
    "beetroot", "cabbage", "radish", "green peas", "edamame", "quinoa", "chia seeds",
    "flax seeds", "coconut", "almond milk", "soy milk", "cream", "mayonnaise",
    "ketchup", "mustard", "salsa", "soup", "sandwich", "fried chicken", "meatball",
    "fish", "sushi", "ramen", "dumplings"
]

API_KEY = "48f7782a551f4b57ae1dcda35b8cb189"

def download_multiple_food_data(food_list, api_key, save_path="data/calorie_data_all.json"):
    url = "https://api.spoonacular.com/recipes/guessNutrition"
    all_data = []

    for food in food_list:
        params = {
            "title": food,
            "apiKey": api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            calories = data.get("calories", {}).get("value")
            unit = data.get("calories", {}).get("unit")
            if calories is not None:
                food_info = {
                    "food": food,
                    "calories": calories,
                    "unit": unit
                }
                all_data.append(food_info)
                print(f"✔ {food}: {calories} {unit}")
            else:
                print(f"⚠ Không có dữ liệu calo cho món: {food}")

        except requests.exceptions.RequestException as e:
            print(f"Lỗi API với món '{food}': {e}")

        time.sleep(0.5)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    print(f"\nĐã lưu dữ liệu {len(all_data)} món vào '{save_path}'")

if __name__ == "__main__":
    download_multiple_food_data(food_list, API_KEY)
