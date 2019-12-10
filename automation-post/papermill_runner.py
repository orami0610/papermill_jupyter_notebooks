import papermill as pm
import pathlib

inputs_path = pathlib.Path('./input_data')
input_pattern = "*.xlsx"

for input_file in inputs_path.glob(input_pattern):
    file_name = input_file.stem
    print(file_name)

    file_month = ''
    pm.execute_notebook(
        './nb_template/template.ipynb',
        f'./output_nbs/{file_name}.ipynb',
        parameters=dict(filename=f'./input_data/{file_name}.xlsx')
    )
