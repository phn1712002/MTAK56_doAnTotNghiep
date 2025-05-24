import os
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsScene, QGraphicsTextItem
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter, QBrush, QColor, QPen, QFont, QTextCharFormat, QTextCursor
from ui_main import Ui_MainWindow
from src.parameter_vk import Parameter_VK
from src.parameter_p_dn_max import Parameter_P_DN_MAX
from src.flowchart import NodeRectangle

class Ui_Funtion(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Setup graphics scene for flowchart
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setFocusPolicy(Qt.StrongFocus)
        self.graphicsView.setFocus()
        
        # Variables for rectangle
        self.current_rect = None
        self.selected_node = None
        
        # Disable delete button initially
        self.btn_del_node.setEnabled(False)
        
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
        self.btn_insert_node.clicked.connect(self.insert_flowchart_rectangle)
        self.btn_del_node.clicked.connect(self.delete_selected_node)
        self.btn_fit_flowchart.clicked.connect(self.fit_flowchart_to_view)
        self.graphicsView.scene().selectionChanged.connect(self.handle_selection_changed)
        self.btn_zoomout_flowchart.clicked.connect(self.zoom_in_flowchart)
        self.btn_zoomin_flowchart.clicked.connect(self.zoom_out_flowchart)

    def zoom_in_flowchart(self):
        """Zoom in the flowchart view"""
        self.graphicsView.scale(1.2, 1.2)

    def zoom_out_flowchart(self):
        """Zoom out the flowchart view"""
        self.graphicsView.scale(0.8, 0.8)

    def fit_flowchart_to_view(self):
        """Fit all flowchart nodes to visible view with padding"""
        if not self.scene.items():
            return
            
        # Calculate union of all node bounds
        rect = None
        for item in self.scene.items():
            if isinstance(item, NodeRectangle):
                item_rect = item.sceneBoundingRect()
                rect = item_rect if rect is None else rect.united(item_rect)
        
        if rect:
            # Add 10% padding
            padding = rect.width() * 0.1
            rect.adjust(-padding, -padding, padding, padding)
            self.graphicsView.fitInView(rect, Qt.KeepAspectRatio)

    def lambda_process_click_btn_calculation_parameter(self):
        return self.process_click_btn_calculation_parameter()
    
    def insert_flowchart_rectangle(self):
        path_config_flowchart = os.path.join(self.base_dir, 'config/flowchart.json')
        self.current_rect = NodeRectangle(0, 0, path_config_flowchart)
        self.current_rect.setPos(0, 0)
        self.scene.addItem(self.current_rect)

    def showEvent(self, event):
        super().showEvent(event)
        if self.tabWidget_rating.currentIndex() == 2:  # Tab rating strucs
            self.graphicsView.setFocus()

    def handle_selection_changed(self):
        """Enable/disable delete button based on selection"""
        selected = self.scene.selectedItems()
        self.btn_del_node.setEnabled(len(selected) > 0)
        self.selected_node = selected[0] if selected else None

    def delete_selected_node(self):
        """Delete the currently selected node"""
        if self.selected_node:
            self.scene.removeItem(self.selected_node)
            self.selected_node = None
            self.btn_del_node.setEnabled(False)
        
    def process_tabwidget_rating_parameter_currentchanged(self):
        index_tab_current = str(self.tabWidget_rating_parameter.currentIndex())
        tab_current = self.LIST_TAB_CALCULATION_PARAMETER.get(index_tab_current)
        tab_current.set_formula()
        self.process_click_btn_calculation_parameter = tab_current.process_click_btn_calculation
