import sys
from PyQt5.QtWidgets import *

def on_currentIndexChanged(idx):
    if idx == 0:
        # Code Reader
        chk_cr.setEnabled(False)
    if idx == 1:
        # Blob
        chk_blob.setEnabled(False)   
    if idx == 2:
        # Matching
        chk_match.setEnabled(False)

def chk_stateChanged():
    if (chk_in_SelectAll.isChecked()):
        chk_in[0].setChecked(True)
        chk_in[1].setChecked(True)
    else:
        chk_in[0].setChecked(False)
        chk_in[1].setChecked(False)

if __name__ == "__main__":
    app = QApplication([])

    cbx_vf = QComboBox()
    cbx_vf.addItem('Code Reader')
    cbx_vf.addItem('Model-based Blob')
    cbx_vf.addItem('Matching')
    cbx_vf.addItem('OCR')
    cbx_vf.addItem('Measurement')

    cbx_vf.currentIndexChanged.connect(on_currentIndexChanged)

    chk_in_SelectAll = QCheckBox('Select all')
    
    chk_in = [QCheckBox('Enable'), QCheckBox('NumSearchMax')]
    chk_in_Timeout = QCheckBox('Timeout')
    chk_in_SymbolType = QCheckBox('SymbolType')
    chk_in_ParameterMode = QCheckBox('ParameterMode')
    chk_in_CodeGrading = QCheckBox('CodeGrading')
    chk_in_ParameterOptimization = QCheckBox('ParameterOptimization')
    chk_in_EnableRobustness = QCheckBox('EnableRobustness')
    chk_in_TestExecute = QCheckBox('TestExecute')
    chk_in_Alignment = QCheckBox('Alignment')
    chk_in_OffsetROIX = QCheckBox('OffsetROIX')
    chk_in_OffsetROIY = QCheckBox('OffsetROIY')
    chk_in_OffsetROIOrientation = QCheckBox('OffsetROIOrientation')
    chk_in_OffsetROIRotCenterX = QCheckBox('OffsetROIRotCenterX')
    chk_in_OffsetROIRotCenterY = QCheckBox('OffsetROIRotCenterY')

    # TBC
    chk_in_SelectAll.stateChanged.connect(chk_stateChanged) 
    
    layout = QGridLayout()
    layout.addWidget(QLabel('Select your Vision function: '), 0, 0)
    layout.addWidget(cbx_vf, 0, 1)

    layout.addWidget(QLabel('_____________________________________________'), 1, 0)
    layout.addWidget(QLabel('Inputs'), 2, 0)
    layout.addWidget(chk_in_SelectAll, 3, 0)
    layout.addWidget(QLabel('_____________________________________________'), 4, 0)
    POS_CHK_IN_1 = 5
    POS_CHK_IN_2 = 0
    layout.addWidget(chk_in[0], POS_CHK_IN_1, POS_CHK_IN_2)
    layout.addWidget(chk_in[1], POS_CHK_IN_1 + 1, POS_CHK_IN_2)
    layout.addWidget(chk_in_Timeout, POS_CHK_IN_1 + 2, POS_CHK_IN_2)
    layout.addWidget(chk_in_SymbolType, POS_CHK_IN_1 + 3, POS_CHK_IN_2)
    layout.addWidget(chk_in_ParameterMode, POS_CHK_IN_1 + 4, POS_CHK_IN_2)
    layout.addWidget(chk_in_CodeGrading, POS_CHK_IN_1 + 5, POS_CHK_IN_2)
    layout.addWidget(chk_in_ParameterOptimization, POS_CHK_IN_1 + 6, POS_CHK_IN_2)
    layout.addWidget(chk_in_EnableRobustness, POS_CHK_IN_1 + 7, POS_CHK_IN_2)
    layout.addWidget(chk_in_TestExecute, POS_CHK_IN_1 + 8, POS_CHK_IN_2)
    layout.addWidget(chk_in_Alignment, POS_CHK_IN_1 + 9, POS_CHK_IN_2)
    layout.addWidget(chk_in_OffsetROIX, POS_CHK_IN_1 + 10, POS_CHK_IN_2)
    layout.addWidget(chk_in_OffsetROIY, POS_CHK_IN_1 + 11, POS_CHK_IN_2)
    layout.addWidget(chk_in_OffsetROIOrientation, POS_CHK_IN_1 + 12, POS_CHK_IN_2)
    layout.addWidget(chk_in_OffsetROIRotCenterX, POS_CHK_IN_1 + 13, POS_CHK_IN_2)
    layout.addWidget(chk_in_OffsetROIRotCenterY, POS_CHK_IN_1 + 14, POS_CHK_IN_2)

    widget = QWidget()
    widget.setLayout(layout)
    widget.show()

    sys.exit(app.exec_())

# QComboBox