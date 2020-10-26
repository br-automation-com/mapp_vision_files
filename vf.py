import sys
from PyQt5.QtWidgets import *

def on_currentIndexChanged(idx):
    if idx == 0:
        # Code Reader
        for i in range(len(chk_in)):
            if mp_in_cr[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)
    if idx == 1:
        # Blob
        for i in range(len(chk_in)):
            if mp_in_blob[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)
    if idx == 2:
        # Matching
        for i in range(len(chk_in)):
            if mp_in_match[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)
    if idx == 3:
        # Matching
        for i in range(len(chk_in)):
            if mp_in_ocr[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)
    if idx == 4:
        # Matching
        for i in range(len(chk_in)):
            if mp_in_meas[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)


def chk_stateChanged():
    if chk_in_SelectAll.isChecked():
        for i in range(len(chk_in)):
            chk_in[i].setChecked(True)
    else:
        for i in range(len(chk_in)):
            chk_in[i].setChecked(False)

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

    chk_in = [  QCheckBox('Enable'),
                QCheckBox('NumSearchMax'),
                QCheckBox('ParameterMode'),
                QCheckBox('Timeout'),
                QCheckBox('Alignment'),
                QCheckBox('RegionFeatures'),
                QCheckBox('EnhancedBlobInformation'),
                QCheckBox('MinScore'),
                QCheckBox('MaxOverlap'),
                QCheckBox('Grading'),
                QCheckBox('ParameterOptimization'),
                QCheckBox('SymbolType'),
                QCheckBox('EnableRobustness'),
                QCheckBox('CodeGrading'),
                QCheckBox('OffsetROIX'),
                QCheckBox('OffsetROIY'),
                QCheckBox('OffsetROIOrientation'),
                QCheckBox('OffsetROIRotCenterX'),
                QCheckBox('OffsetROIRotCenterY')
            ]
    mp_in_cr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    mp_in_blob = [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    mp_in_match = [1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    mp_in_ocr = [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    mp_in_meas = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    # Set initial inputs visibility
    for i in range(len(chk_in)):
        if mp_in_cr[i] == 0:
            chk_in[i].setVisible(False)

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
    for i in range(len(chk_in)):
        layout.addWidget(chk_in[i], POS_CHK_IN_1 + i, POS_CHK_IN_2)

    widget = QWidget()
    widget.setLayout(layout)
    widget.show()

    sys.exit(app.exec_())

# QComboBox