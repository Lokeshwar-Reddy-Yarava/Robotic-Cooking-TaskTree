

def read_file_as_string(filename):
  with open(filename, "r") as f:
    content = f.read()
  return content

kitchen_itmes = read_file_as_string('kitchen.txt')
ex1=read_file_as_string('sample_output1.json')
ex2=read_file_as_string('sample_output2.json')
dish_name="I want to cook"
ingredients="using the following ingredients:"
prompt1=f"""The kitchen items available are: {kitchen_itmes}

If any ingredients required for the dish are not available in the kitchen, please suggest suitable substitutes.

If you are not able to find any substitute then tell me i can not prepare since there is no required items.

Generate a task tree in JSON format for preparing this dish, incorporating the available ingredients and kitchen items. If substitutions are needed, include them in the task tree with a note explaining the substitution.

The task tree should have input nodes for initial ingredient states, motion nodes for actions, and output nodes for resulting states.

{ex1}
{ex2}

please go through the above examples and give proper output
"""
prompt2=f"""
Here are some sample task trees for cooking different dishes:

{ex1}
{ex2}

Given the list of ingredients for ***
And the kitchen items available: {kitchen_itmes}

Please generate a task tree in JSON format for cooking $$$, following the same structure as the example task trees provided.

i just need output in the format of json.i am not expecting any other type of output.
"""
p3_1="I want to cook a dish"
p3_2="using the following available ingredients: "
prompt3=f"""
And the following kitchen items: {kitchen_itmes}

Based on the provided ingredients and kitchen items, generate a task tree in JSON format for preparing a suitable dish. The task tree should include:

- Input nodes representing the initial states of available ingredients
- Motion nodes specifying the actions to be performed using the available kitchen items
- Output nodes showing the resulting states after each action

If any crucial ingredients or kitchen items are missing for a specific dish, do not generate a task tree for that dish. Instead, provide a note suggesting alternatives or substitutions, or stating that the dish cannot be prepared with the given items.

{ex1}

"""
p4=f"""
Your task is to generate comprehensive task trees to simplify the cooking process for various dishes. Each task tree should consist of the following essential components:

Input Nodes:
- These nodes represent the initial states of ingredients and utensils required for each step of the recipe.
- List all necessary components, specifying their labels, states (e.g., sliced, diced), ingredients (if any), and containers.

Motion Node:
- This node specifies the action or operation to be performed using the input elements.
- Clearly define the motion, whether it's chopping, mixing, simmering, or any other action involved in the cooking process.

Output Nodes:
- These nodes describe the resulting states of ingredients and utensils after executing the action specified in the motion node.
- Provide details on the labels, states, ingredients, and containers of the output elements.

Your task trees must adhere to the specified JSON format meticulously, ensuring consistency and clarity. Here is an example of the expected JSON format:

[EXAMPLE_TASK_TREE_JSON]
{ex1}
If a crucial ingredient or kitchen item is not available for a particular dish, the output should state: "Cannot prepare dish name with available ingredients and kitchen items."

Here are the available kitchen items: {kitchen_itmes}

"""