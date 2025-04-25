import os
import PIL
import google.generativeai as genai
import json
import prompt
import random

config = open('config.json')
config = json.load(config)
# do not reveal your api key when submitting the assignment
GOOGLE_API_KEY = config['key']
genai.configure(api_key=GOOGLE_API_KEY)


def list_genai_models():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)


def read_file_as_string(filename):
    with open(filename, "r") as f:
        content = f.read()
    return content


def detect_object(model, filepath):
    img = PIL.Image.open(filepath)
    prompt = "list objects in the image in this way: 1. ing 2. ing 3. ing etc"
    response = model.generate_content([prompt, img])
    print(response.text)


def checking():
    string_data = read_file_as_string("output.txt")


if __name__ == "__main__":
    list_genai_models()
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    with open('input.json', 'r') as json_file:
        input_json = json.load(json_file)
    dish_ingredient = {}
    for category in input_json:
        for item in category['menu']:
            dish_ingredient[item['dish']] = item['ingredients']
    i=0
    for key, value in dish_ingredient.items():
        print(f"{key} ********")
        prompt_value = '3'
        if prompt_value == '1':
            prompt_final = f"{prompt.dish_name} {key} {prompt.ingredients} {value} {prompt.prompt1}"
        if prompt_value == '2':
            prompt_final = f"{prompt.prompt2}"
            prompt_final = prompt_final.split('***')
            prompt_final = " ".join(prompt_final[:1] + [f'{key} :{value}'] + prompt_final[1:])
            prompt_final = prompt_final.split('$$$')
            prompt_final = " ".join(prompt_final[:1] + [f'{key}'] + prompt_final[1:])
        if prompt_value =="3":
            prompt_final =f"{prompt.p3_1} {key} {prompt.p3_2} {value}  {prompt.prompt3}"
        if prompt_value =='4':
            prompt_final =f"{prompt.p4} \n now you have to prepare dish {key} and required ingredients are {value}"
            prompt_final=f"""
                Given the dish name {key} and the list of ingredients: {value}, please generate a comprehensive task tree in the specified JSON format, considering the available kitchen items.

Your attention to detail and adherence to the format are paramount for the success of this task. Provide clear and accurate representations of each step in the cooking process to ensure seamless execution in the kitchen.Also, if a ingredient or similar is not present, the output should be as dish cannot be prepared.

            """

        response = model.generate_content(prompt_final)
        import time
        res = response.text
        # org =model.generate_content(f"Please give me proper json format from this data {res}.I just need only json not additional quotes and other extra data.please rember this output format {prompt.ex1} if there is no proper data please create json ")
        # res=org.text
        try:
            if "``` JSON" in res:
                json_opt = res.split("``` JSON")[1]
                data = json.loads(json_opt)
            elif "```json" in res:
                json_opt = res.split("```json")[1]
                data = json.loads(json_opt)
            elif "```JSON" in res:
                json_opt = res.split("```JSON")[1]
                data = json.loads(json_opt)
            elif "```" in res:
                json_opt = res.split("```")[1]
                data = json.loads(json_opt)
            else:
                data = json.loads(res)
            # print(data,"envjiwe99999999999999999999")
            # break
            with open(f'{key}.json', 'w') as f:
                json.dump(data, f, indent=2)
            print(f'{key}.json file is created.')
        except:
            print("^^^^^^^^^^^^^^^^^^^^")
            print(response.text)
            file_path = f"{key}.txt"
            with open(file_path, "w") as file:
                # Write the string to the file
                file.write(response.text)

