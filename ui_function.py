import os
from ui_main import Ui_MainWindow
from src.parameter_vk import Parameter_VK
from src.parameter_p_dn_max import Parameter_P_DN_MAX


class Ui_Funtion(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        #! Tab
        #? Tab calculation vk
        path_image_formula = os.path.join(self.base_dir, 'images_formula/vk.jpg')
        formulas = [self.image_calculation_p_formula, path_image_formula]
        means = [self.input_mean_vk_ik, self.input_mean_vk_m, self.input_mean_vk_zk, self.input_mean_vk_cty, self.input_mean_vk_d]
        var = [[self.checkbox_var_vk_ik, self.input_var_vk_ik], 
                  [self.checkbox_var_vk_m, self.input_var_vk_m], 
                  [self.checkbox_var_vk_zk, self.input_var_vk_zk],
                  [self.checkbox_var_vk_cty, self.input_var_vk_cty],
                  [self.checkbox_var_vk_d, self.input_var_vk_d]
                  ]
        outputs = [self.input_calc_min, self.input_calc_max, self.calculation_p_result]
        self.tab_calculation_parameter_vk = Parameter_VK(formulas, means, var, outputs)
        
        
        path_image_formula = os.path.join(self.base_dir, 'images_formula/p_dn_max.jpg')
        formulas = [self.image_calculation_p_formula, path_image_formula]
        means = [self.input_mean_p_dn_max_q, self.input_mean_p_dn_max_w, self.input_mean_p_dn_max_mu, self.input_mean_p_dn_max_pT]
        var = [[self.checkbox_var_p_dn_max_q, self.input_var_p_dn_max_q],
               [self.checkbox_var_p_dn_max_w, self.input_var_p_dn_max_w],
               [self.checkbox_var_p_dn_max_mu, self.input_var_p_dn_max_mu],
               [self.checkbox_var_p_dn_max_pT, self.input_var_p_dn_max_pT]
               ]
        self.tab_calculation_parameter_p_dn_max = Parameter_P_DN_MAX(formulas, means, var, outputs)
        
        
        #? All list tab
        self.LIST_TAB_CALCULATION_PARAMETER = {
            '0': self.tab_calculation_parameter_vk,
            '1': self.tab_calculation_parameter_p_dn_max
        }

        #! Start
        INDEX_TAB_START = 0
        self.tabWidget_rating.setCurrentIndex(INDEX_TAB_START)
        self.tabWidget_rating_parameter.setCurrentIndex(INDEX_TAB_START)
        self.LIST_TAB_CALCULATION_PARAMETER[str(INDEX_TAB_START)].set_formula()
        self.process_click_btn_calculation_parameter = self.LIST_TAB_CALCULATION_PARAMETER.get(str(INDEX_TAB_START)).process_click_btn_calculation
        
    def processSignalAndSlot(self):
        self.tab_calculation_parameter_vk.processSignalAndSlot()
        self.tab_calculation_parameter_p_dn_max.processSignalAndSlot()
        self.tabWidget_rating_parameter.currentChanged.connect(self.process_tabwidget_rating_parameter_currentchanged)
        self.btn_calcutation_parameter.clicked.connect(self.lambda_process_click_btn_calculation_parameter)

    def lambda_process_click_btn_calculation_parameter(self):
        return self.process_click_btn_calculation_parameter()
    
    def process_tabwidget_rating_parameter_currentchanged(self):
        index_tab_current = str(self.tabWidget_rating_parameter.currentIndex())
        tab_current = self.LIST_TAB_CALCULATION_PARAMETER.get(index_tab_current)
        tab_current.set_formula()
        self.process_click_btn_calculation_parameter = tab_current.process_click_btn_calculation