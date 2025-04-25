from PySide6.QtGui import QPixmap
import numpy as np
from scipy.integrate import quad

class Calculation_Parameter:
    def __init__(self, formulas, outputs):
        self.formulas = formulas
        self.outputs = outputs
        self.IDX_OUTPUTS_FORMULAS = {
            "input_calc_min": 0, 
            "input_calc_max": 1,
            "calculation_result": 2,
            "label_image": 0,
            "path_image": 1
            }
        self.VALUE_DEFAULT = {
            'input': 0,
            'round': 4
        }

    def process_click_btn_calculation(self):
        pass
    
    def processSignalAndSlot(self):
        pass
    
    def function_normal_distribution(self, x, mean , std):
        return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-np.square(x - mean) / (2 * np.square(std)))

    def quad_function_normal_distribution(self, mean, std, min, max):
        return quad(lambda x: self.function_normal_distribution(x, mean, std), min, max)
    
    def get_idx_outputs_formulas(self, key):
        return int(self.IDX_OUTPUTS_FORMULAS[key])
    
    def get_label_path_formula(self):
        label = self.formulas[self.get_idx_outputs_formulas('label_image')]
        path = self.formulas[self.get_idx_outputs_formulas('path_image')]
        return (label, path)
    
    def get_value_min_max_calc(self):
        min = self.outputs[self.get_idx_outputs_formulas('input_calc_min')].value()
        max = self.outputs[self.get_idx_outputs_formulas('input_calc_max')].value()
        return (min, max)
    
    def set_value_result(self, value):
        return self.outputs[self.get_idx_outputs_formulas('calculation_result')].setText(str(value))
    
    def set_formula(self):
        label, path = self.get_label_path_formula()
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        
    def process_click_checkbox_var(self, checkbox, input):
        status_checkbox = checkbox.isChecked()
        input.setEnabled(status_checkbox)
        if not status_checkbox: input.setValue(self.VALUE_DEFAULT['input'])