from printing_functions import print_models, print_completed_models

models = ['iphone case', 'robot pendant', 'dodecahedron']

print_models(models)

completed_models = []
while models:
    current_model = models.pop()
    print(f"Printing {current_model}...")
    completed_models.append(current_model)

print_completed_models(completed_models)
