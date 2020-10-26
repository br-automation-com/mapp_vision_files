
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def btn_genFile():
    file_types = 'Vision application (*.visionapplication);;'
    path = QFileDialog.getSaveFileName(filter = file_types)
    f_name = os.path.splitext(os.path.basename(path[0]))[0]

    f_handle = open(path[0], 'w+')
    f_handle.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Configuration>\n\t<Element ID=\"')
    f_handle.write(f_name)
    f_handle.write('\" Type=\"visionapplication\">\n')
    
    f_handle.write('\t\t<Group ID=\"ImgProcessingInputs\">\n')

    if cbx_vf.currentIndex() == 0:
        mp_in = mp_in_cr
        mp_out = mp_out_cr
    elif cbx_vf.currentIndex() == 1:
        mp_in = mp_in_blob
        mp_out = mp_out_blob
    elif cbx_vf.currentIndex() == 2:
        mp_in = mp_in_match
        mp_out = mp_out_match
    elif cbx_vf.currentIndex() == 3:
        mp_in = mp_in_ocr
        mp_out = mp_out_ocr
    else:
        mp_in = mp_in_meas
        mp_out = mp_out_meas

    k = 0
    for j in range(len(mp_in)):
        if mp_in[j] & chk_in[j].isChecked():
            f_handle.write('\t\t\t<Group ID="Input[')
            f_handle.write(str(k))        
            f_handle.write(']\">\n')
            f_handle.write('\t\t\t\t<Property ID=\"ChannelID\" Value=\"')
            f_handle.write(chk_in[j].text())
            f_handle.write('\" />\n')
            f_handle.write('\t\t\t</Group>\n')
            k = k + 1
    f_handle.write('\t\t</Group>\n')
    f_handle.write('\t\t<Group ID=\"ImgProcessingVariables\" />\n')
    f_handle.write('\t\t<Group ID=\"VisionFunctionSet\">\n')
    f_handle.write('\t\t\t<Group ID=\"VfInstance[1]\">\n')
    f_handle.write('\t\t\t\t<Property ID=\"VfName\" Value=\"')
    f_handle.write(f_name)
    f_handle.write('\" />\n')
    f_handle.write('\t\t\t\t<Property ID=\"VfExecutionNr\" Value=\"1\" />')

    #     <Selector ID="VfType" Value="vf-datacode">
    #       <Group ID="VfConstants">
    #         <Property ID="MaxStringSize" Value="254" />
    #         <Property ID="NumResultsMax" Value="1" />
    #       </Group>

    f_handle.close()

def cbx_currentIndexChanged(idx):
    if idx == 0:
        # Code Reader
        txt_vf.setText('VfCodeReader')
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
        txt_vf.setText('VfBlob')
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
        txt_vf.setText('VfMatching')
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
        txt_vf.setText('VfOcr')
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
        txt_vf.setText('VfMeasurement')
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
    cbx_vf.currentIndexChanged.connect(cbx_currentIndexChanged)

    txt_vf = QLineEdit()
    txt_vf.setText('VfCodeReader')

    # txt_dir = QLineEdit()
    # dir_name = os.getcwd()
    # txt_dir.setPlaceholderText(dir_name)
    # btn_dir = QPushButton('...')
    # btn_dir.setFixedWidth(25)
    # btn_dir.clicked.connect(btn_getDir)

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
    
    
    # Header widgets
    btn_gen_file = QPushButton('Generate file')
    btn_gen_file.clicked.connect(btn_genFile)

    # Layout settings
    layout = QFormLayout() 
    layout.addRow(QLabel('Select your Vision function: '), cbx_vf)
    layout.addRow(QLabel('Instance name: '), txt_vf)
    # hbox_header = QHBoxLayout()
    # hbox_header.addWidget(QLabel('Save to: '))
    # hbox_header.addWidget(txt_dir)
    # hbox_header.addWidget(btn_dir)
    # layout.addRow(hbox_header)
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
    
    layout.addRow(QLabel('__________________________________________________________________________________'))
    layout.addRow(btn_gen_file)
    

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
