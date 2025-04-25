from .calculation import Calculation_Parameter
import numpy as np
from autograd import grad

class Parameter_VK(Calculation_Parameter):
    def __init__(self, formulas_vk, mean_vk, var_vk, outputs_vk):
        super().__init__(formulas_vk, outputs_vk)
        self.IDX_INPUTS_TOLS = {
            "ik": 0, 
            "m": 1,
            "zk": 2,
            "cty": 3,
            "d": 4,
            "check_box": 0,
            "input_var": 1
            }
        self.mean_vk = mean_vk
        self.var_vk = var_vk
    
    def get_idx_inputs_vars(self, key):
        return int(self.IDX_INPUTS_TOLS[key])
    
    def get_check_box(self, key):
        return self.var_vk[self.get_idx_inputs_vars(key)][self.get_idx_inputs_vars('check_box')]
        
    def get_input(self, key):
        return self.mean_vk[self.get_idx_inputs_vars(key)]
    
    def get_value_input_mean(self, key):
        return self.get_input(key).value()
    
    def get_input_var(self, key):
        return self.var_vk[self.get_idx_inputs_vars(key)][self.get_idx_inputs_vars('input_var')]
    
    def get_value_input_var(self, key):
        return self.get_input_var(key).value()
    
    def processSignalAndSlot(self):
        self.get_check_box('ik').stateChanged.connect(lambda: self.process_click_checkbox_var(self.get_check_box('ik'), self.get_input_var('ik')))
        self.get_check_box('zk').stateChanged.connect(lambda: self.process_click_checkbox_var(self.get_check_box('zk'), self.get_input_var('zk')))
        self.get_check_box('m').stateChanged.connect(lambda: self.process_click_checkbox_var(self.get_check_box('m'), self.get_input_var('m')))
        self.get_check_box('d').stateChanged.connect(lambda: self.process_click_checkbox_var(self.get_check_box('d'), self.get_input_var('d')))
        self.get_check_box('cty').stateChanged.connect(lambda: self.process_click_checkbox_var(self.get_check_box('cty'), self.get_input_var('cty')))

    def function_calc(self, ik, m, zk, cty, d):
        return np.pi * ik * zk * np.square(d) / (4 * cty * m)
    
    def process_click_btn_calculation(self):
        min, max = self.get_value_min_max_calc()
        value_ik_mean = self.get_value_input_mean('ik')
        value_zk_mean = self.get_value_input_mean('zk')
        value_m_mean = self.get_value_input_mean('m')
        value_d_mean = self.get_value_input_mean('d')
        value_cty_mean = self.get_value_input_mean('cty')
        
        df_dik = grad(lambda x: self.function_calc(x, value_m_mean, value_zk_mean, value_cty_mean, value_d_mean))
        df_dik = df_dik(value_ik_mean)
        
        df_dm = grad(lambda x: self.function_calc(value_ik_mean, x, value_zk_mean, value_cty_mean, value_d_mean))
        df_dm = df_dm(value_m_mean)
        
        df_dzk = grad(lambda x: self.function_calc(value_ik_mean, value_m_mean, x, value_cty_mean, value_d_mean))
        df_dzk = df_dzk(value_zk_mean)
        
        df_dcty = grad(lambda x: self.function_calc(value_ik_mean, value_m_mean, value_zk_mean, x, value_d_mean))
        df_dcty = df_dcty(value_cty_mean)
        
        df_dd = grad(lambda x: self.function_calc(value_ik_mean, value_m_mean, value_zk_mean, value_cty_mean, x))    
        df_dd = df_dd(value_d_mean)
        
        value_ik_var = self.get_value_input_var('ik')
        value_zk_var = self.get_value_input_var('zk')
        value_m_var = self.get_value_input_var('m')
        value_d_var = self.get_value_input_var('d')
        value_cty_var = self.get_value_input_var('cty')
        
        std_deviation_function = np.sqrt(np.square(df_dik) * value_ik_var + np.square(df_dm) * value_m_var + np.square(df_dzk) * value_zk_var + np.square(df_dcty) * value_cty_var + np.square(df_dd) * value_d_var)
        mean_function = self.function_calc(value_ik_mean, value_m_mean, value_zk_mean, value_cty_mean, value_d_mean)
        result, error = self.quad_function_normal_distribution(mean_function, std_deviation_function, min, max)
        
        result = round(result, self.VALUE_DEFAULT['round'])
        error = round(error, self.VALUE_DEFAULT['round'])
        self.set_value_result(result)
        
    