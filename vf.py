import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def on_currentIndexChanged(idx):
    if idx == 0:
        # Code Reader
        txt_vf.setPlaceholderText('VfCodeReader')
        for i in range(len(chk_in)):
            if mp_in_cr[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)
        for i in range(len(chk_out)):
            if mp_out_cr[i]:
                chk_out[i].setVisible(True)
            else:
                chk_out[i].setVisible(False)        
    if idx == 1:
        # Blob
        txt_vf.setPlaceholderText('VfBlob')
        for i in range(len(chk_in)):
            if mp_in_blob[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)
        for i in range(len(chk_out)):
            if mp_out_blob[i]:
                chk_out[i].setVisible(True)
            else:
                chk_out[i].setVisible(False)  
    if idx == 2:
        # Matching
        txt_vf.setPlaceholderText('VfMatching')
        for i in range(len(chk_in)):
            if mp_in_match[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)
        for i in range(len(chk_out)):
            if mp_out_match[i]:
                chk_out[i].setVisible(True)
            else:
                chk_out[i].setVisible(False)  
    if idx == 3:
        # OCR
        txt_vf.setPlaceholderText('VfOcr')
        for i in range(len(chk_in)):
            if mp_in_ocr[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)
        for i in range(len(chk_out)):
            if mp_out_ocr[i]:
                chk_out[i].setVisible(True)
            else:
                chk_out[i].setVisible(False)  
    if idx == 4:
        # Measurement
        txt_vf.setPlaceholderText('VfMeasurement')
        for i in range(len(chk_in)):
            if mp_in_meas[i]:
                chk_in[i].setVisible(True)
            else:
                chk_in[i].setVisible(False)
        for i in range(len(chk_out)):
            if mp_out_meas[i]:
                chk_out[i].setVisible(True)
            else:
                chk_out[i].setVisible(False)  


def chk_in_stateChanged():
    if chk_in_SelectAll.isChecked():
        for i in range(len(chk_in)):
            chk_in[i].setChecked(True)
    else:
        for i in range(len(chk_in)):
            chk_in[i].setChecked(False)


def chk_out_stateChanged():
    if chk_out_SelectAll.isChecked():
        for i in range(len(chk_out)):
            chk_out[i].setChecked(True)
    else:
        for i in range(len(chk_out)):
            chk_out[i].setChecked(False)


if __name__ == "__main__":

    app = QApplication([])

    # Header widgets
    cbx_vf = QComboBox()
    cbx_vf.addItem('Code Reader')
    cbx_vf.addItem('Model-based Blob')
    cbx_vf.addItem('Matching')
    cbx_vf.addItem('OCR')
    cbx_vf.addItem('Measurement')
    cbx_vf.currentIndexChanged.connect(on_currentIndexChanged)

    txt_vf = QLineEdit()
    txt_vf.setPlaceholderText('VfCodeReader')
    
    # Input widgets
    font_bold = QFont()
    font_bold.setBold(True)
    label_in = QLabel('Inputs')
    label_in.setFont(font_bold)

    chk_in_SelectAll = QCheckBox('Select all')
    chk_in_SelectAll.stateChanged.connect(chk_in_stateChanged)

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

    # Output widgets
    label_out = QLabel('Outputs')
    label_out.setFont(font_bold)

    chk_out_SelectAll = QCheckBox('Select all')
    chk_out_SelectAll.stateChanged.connect(chk_out_stateChanged)

    chk_out = [ QCheckBox('NumResults'),
                QCheckBox('DecodedData'),
                QCheckBox('SymbolType'),
                QCheckBox('OCRData'),
                QCheckBox('GradingValue'),
                QCheckBox('Clipped'),
                QCheckBox('Area'),
                QCheckBox('Score'),
                QCheckBox('PositionX'),
                QCheckBox('PositionY'),
                QCheckBox('Orientation'),
                QCheckBox('Result'),
                QCheckBox('FunctionProccessingTime'),
                QCheckBox('EnhancedGradingInformation'),
                QCheckBox('MeanGrayValue'),
                QCheckBox('Length'),
                QCheckBox('Width'),
                QCheckBox('ModelNumber'),
                QCheckBox('Scale'),
                QCheckBox('RotCenterX'),
                QCheckBox('RotCenterY'),
                QCheckBox('Xmin'),
                QCheckBox('Xmax'),
                QCheckBox('Ymin'),
                QCheckBox('Ymax'),
                QCheckBox('Circularity'),
                QCheckBox('Rectangularity'),
                QCheckBox('Anisometry')
            ]

    mp_out_cr = [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    mp_out_blob = [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    mp_out_match = [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    mp_out_ocr = [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mp_out_meas = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    # Layout settings
    layout = QFormLayout() 
    layout.addRow(QLabel('Select your Vision function: '), cbx_vf)
    layout.addRow(QLabel('Instance name: '), txt_vf)
    layout.addRow(QLabel('__________________________________________________________________________________'))

    vbox_in = QVBoxLayout()
    vbox_in.addWidget(label_in)
    vbox_in.addWidget(chk_in_SelectAll)
    vbox_in.addWidget(QLabel('=============================='))
    for i in range(len(chk_in)): 
        vbox_in.addWidget(chk_in[i]) 
    vbox_in.addStretch()

    vbox_out = QVBoxLayout()
    vbox_out.addWidget(label_out)    
    vbox_out.addWidget(chk_out_SelectAll)
    vbox_out.addWidget(QLabel('=============================='))
    for i in range(len(chk_out)):
        vbox_out.addWidget(chk_out[i])
    vbox_out.addStretch()

    hbox = QHBoxLayout()
    hbox.addLayout(vbox_in)
    hbox.addLayout(vbox_out)
    layout.addRow(hbox)
    
    # Set initial visibility
    for i in range(len(chk_in)):
        if mp_in_cr[i] == 0:
            chk_in[i].setVisible(False)
    for i in range(len(chk_out)):
        if mp_out_cr[i] == 0:
            chk_out[i].setVisible(False)

    # Set widget and run
    widget = QWidget()
    widget.setLayout(layout)
    widget.show()
    sys.exit(app.exec_())
