import os
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from src.flowchart import NodeRectangle, Arrow
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
        
        # Variables for rectangle and connection
        self.current_rect = None
        self.selected_node = None
        self.connection_start_node = None
        self.current_arrow = None
        
        # Disable buttons initially
        self.btn_del_node.setEnabled(False)
        self.btn_con_node.setEnabled(False)
        
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
        self.btn_con_node.clicked.connect(self.handle_connection)
        self.btn_fit_flowchart.clicked.connect(self.fit_flowchart_to_view)
        self.graphicsView.scene().selectionChanged.connect(self.handle_selection_changed)
        self.graphicsView.mouseMoveEvent = self.handle_mouse_move
        self.btn_zoomout_flowchart.clicked.connect(self.zoom_in_flowchart)
        self.btn_zoomin_flowchart.clicked.connect(self.zoom_out_flowchart)

    def handle_mouse_move(self, event):
        """Handle mouse move events to detect node hover and update temporary arrow"""
        item = self.scene.itemAt(event.pos(), self.graphicsView.transform())
        
        # Update temporary arrow position during connection
        if self.connection_start_node and self.current_arrow:
            scene_pos = self.graphicsView.mapToScene(event.pos())
            self.current_arrow.update_position(temp_end_pos=scene_pos)
            
        QGraphicsView.mouseMoveEvent(self.graphicsView, event)

    def handle_connection(self):
        """Start node connection process"""
        if self.selected_node and not self.connection_start_node:
            self.connection_start_node = self.selected_node
            self.current_arrow = Arrow(self.connection_start_node)
            self.scene.addItem(self.current_arrow)

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
        """Handle node selection and automatic connection"""
        if not self.scene:
            return
            
        try:
            selected = self.scene.selectedItems()
            has_selection = len(selected) > 0
            self.btn_del_node.setEnabled(has_selection)
            
            # Enable connection button when node is selected (same as delete button)
            self.btn_con_node.setEnabled(has_selection)
            
            if not selected:
                self.selected_node = None
                return
                
            self.selected_node = selected[0]
            
            # Automatic connection logic
            if self.connection_start_node and self.selected_node != self.connection_start_node:
                # Complete connection
                self.current_arrow.set_end_node(self.selected_node)
                self.current_arrow.update_position()
                self.connection_start_node = None
                self.btn_con_node.setEnabled(False)
                
        except RuntimeError:
            # Scene was deleted
            self.btn_del_node.setEnabled(False)
            self.btn_con_node.setEnabled(False)
            self.selected_node = None

    def delete_selected_node(self):
        """Delete the currently selected node and its connected arrows"""
        if self.selected_node:
            # Remove all connected arrows first
            for arrow in list(self.selected_node.connected_arrows):
                self.scene.removeItem(arrow)
                
            # Remove the node
            self.scene.removeItem(self.selected_node)
            self.selected_node = None
            self.btn_del_node.setEnabled(False)
            self.scene.update()
        
    def process_tabwidget_rating_parameter_currentchanged(self):
        index_tab_current = str(self.tabWidget_rating_parameter.currentIndex())
        tab_current = self.LIST_TAB_CALCULATION_PARAMETER.get(index_tab_current)
        tab_current.set_formula()
        self.process_click_btn_calculation_parameter = tab_current.process_click_btn_calculation
