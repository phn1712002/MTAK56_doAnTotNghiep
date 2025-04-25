from .calculation import Calculation_Parameter
import numpy as np
from autograd import grad

class Parameter_P_DN_MAX(Calculation_Parameter):
    def __init__(self, formulas_vk, inputs_vk, var_vk, outputs_vk):
        super().__init__(formulas_vk, outputs_vk)
        self.IDX_INPUTS_TOLS = {
            "q": 0, 
            "w": 1,
            "mu": 2,
            "pT": 3,
            "check_box": 0,
            "input_var": 1
            }
        self.inputs_vk = inputs_vk
        self.var_vk = var_vk
    
    def get_idx_inputs_vars(self, key):
        return int(self.IDX_INPUTS_TOLS[key])
    
    def get_check_box(self, key):
        return self.var_vk[self.get_idx_inputs_vars(key)][self.get_idx_inputs_vars('check_box')]
        
    def get_input(self, key):
        return self.inputs_vk[self.get_idx_inputs_vars(key)]
    
    def get_value_input_mean(self, key):
        return self.get_input(key).value()
    
    def get_input_var(self, key):
        return self.var_vk[self.get_idx_inputs_vars(key)][self.get_idx_inputs_vars('input_var')]
    
    def get_value_input_var(self, key):
        return self.get_input_var(key).value()
    
    def processSignalAndSlot(self):
        self.get_check_box('q').stateChanged.connect(lambda: self.process_click_checkbox_var(self.get_check_box('q'), self.get_input_var('q')))
        self.get_check_box('w').stateChanged.connect(lambda: self.process_click_checkbox_var(self.get_check_box('w'), self.get_input_var('w')))
        self.get_check_box('mu').stateChanged.connect(lambda: self.process_click_checkbox_var(self.get_check_box('mu'), self.get_input_var('mu')))
        self.get_check_box('pT').stateChanged.connect(lambda: self.process_click_checkbox_var(self.get_check_box('pT'), self.get_input_var('pT')))

    def function_calc(self, q, w, mu, pT):
        numerator = (1 + (1/2) * (w / (mu * q)))
        denominator = (1 + (1/3) * (w / (mu * q)))
        p_dn_max = (numerator / denominator) * pT
        return p_dn_max
    
    def process_click_btn_calculation(self):
    
        min, max = self.get_value_min_max_calc()
        value_q_mean = self.get_value_input_mean('q')
        value_w_mean = self.get_value_input_mean('w')
        value_mu_mean = self.get_value_input_mean('mu')
        value_pT_mean = self.get_value_input_mean('pT')
        
        df_dq = grad(lambda x: self.function_calc(x, value_w_mean, value_mu_mean, value_pT_mean)) 
        df_dq = df_dq(value_q_mean)
        
        df_dw = grad(lambda x: self.function_calc(value_q_mean, x, value_mu_mean, value_pT_mean)) 
        df_dw = df_dw(value_w_mean)
        
        df_dmu = grad(lambda x: self.function_calc(value_q_mean, value_w_mean, x, value_pT_mean)) 
        df_dmu = df_dmu(value_mu_mean)
        
        df_dpT = grad(lambda x: self.function_calc(value_q_mean, value_w_mean, value_mu_mean, x)) 
        df_dpT = df_dpT(value_pT_mean)   
        
        value_q_var = self.get_value_input_var('q')
        value_w_var = self.get_value_input_var('w')
        value_mu_var = self.get_value_input_var('mu')
        value_pT_var = self.get_value_input_var('pT')
        
        std_deviation_function = np.sqrt(np.square(df_dq) * value_q_var + np.square(df_dw) * value_w_var + np.square(df_dmu) * value_mu_var + np.square(df_dpT) * value_pT_var)
        mean_function = self.function_calc(value_q_mean, value_w_mean, value_mu_mean, value_pT_mean)
        result, error = self.quad_function_normal_distribution(mean_function, std_deviation_function, min, max)
        
        result = round(result, self.VALUE_DEFAULT['round'])
        error = round(error, self.VALUE_DEFAULT['round'])
        self.set_value_result(result)
        
    