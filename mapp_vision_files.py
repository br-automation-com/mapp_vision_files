""" This app generates mapp Vision configuration files (.visionapplication and .visioncomponent) """

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QCheckBox, QPushButton, QMessageBox, QFormLayout, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QFont

def btn_gen_file_pushed():
    """ Generate files button pressed """
    # Copy VF index-related settings
    if cbx_vf.currentIndex() == 0:
        vf_string = 'vf-datacode'
        mp_in = mp_in_cr
        mp_out = mp_out_cr
    elif cbx_vf.currentIndex() == 1:
        vf_string = 'vf-blob'
        mp_in = mp_in_blob
        mp_out = mp_out_blob
    elif cbx_vf.currentIndex() == 2:
        vf_string = 'vf-matching'
        mp_in = mp_in_match
        mp_out = mp_out_match
    elif cbx_vf.currentIndex() == 3:
        vf_string = 'vf-ocr'
        mp_in = mp_in_ocr
        mp_out = mp_out_ocr
    else:
        vf_string = 'vf-measurement'
        mp_in = mp_in_meas
        mp_out = mp_out_meas

    # Create the Vision Component file
    file_types = 'Vision Application (*.visionapplication);;'
    path = QFileDialog.getSaveFileName(filter = file_types)
    if len(path[0]) > 0:
        f_name = os.path.splitext(os.path.basename(path[0]))[0]
        f_handle = open(path[0], 'w+')

        # Header
        f_handle.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Configuration>\n\t<Element ID=\"' + f_name + '\" Type=\"visionapplication\">\n')
        f_handle.write('\t\t<Group ID=\"ImgProcessingInputs\">\n')
        k = 0
        for j in range(len(mp_in)):
            if mp_in[j] & chk_in[j].isChecked():
                f_handle.write('\t\t\t<Group ID="Input[' + str(k) + ']\">\n')
                f_handle.write('\t\t\t\t<Property ID=\"ChannelID\" Value=\"' + chk_in[j].text() + '\" />\n')
                f_handle.write('\t\t\t</Group>\n')
                k = k + 1
        f_handle.write('\t\t</Group>\n')
        f_handle.write('\t\t<Group ID=\"ImgProcessingVariables\" />\n')
        f_handle.write('\t\t<Group ID=\"VisionFunctionSet\">\n')
        f_handle.write('\t\t\t<Group ID=\"VfInstance[1]\">\n')
        f_handle.write('\t\t\t\t<Property ID=\"VfName\" Value=\"' + txt_vf.text() + '\" />\n')
        f_handle.write('\t\t\t\t<Property ID=\"VfExecutionNr\" Value=\"1\" />\n')
        f_handle.write('\t\t\t\t<Selector ID=\"VfType\" Value=\"' + vf_string + '\">\n')
        f_handle.write('\t\t\t\t\t<Group ID=\"VfConstants\">\n')
        f_handle.write('\t\t\t\t\t\t<Property ID=\"MaxStringSize\" Value=\"254\" />\n')
        f_handle.write('\t\t\t\t\t\t<Property ID=\"NumResultsMax\" Value=\"1\" />\n')
        f_handle.write('\t\t\t\t\t</Group>\n')
        f_handle.write('\t\t\t\t\t<Group ID=\"VfWirings\">\n')

        # Inputs
        f_handle.write('\t\t\t\t\t\t<Group ID=\"Image\">\n')
        f_handle.write('\t\t\t\t\t\t\t<Selector ID=\"SourceType\" Value=\"ImageAcquisition\">\n')
        f_handle.write('\t\t\t\t\t\t\t\t<Property ID=\"IaParameter\" Value=\"Image01\" />\n')
        f_handle.write('\t\t\t\t\t\t\t</Selector>\n')
        f_handle.write('\t\t\t\t\t\t</Group>\n')
        k = 0
        for j in range(len(mp_in)):
            if mp_in[j] & chk_in[j].isChecked():
                f_handle.write('\t\t\t\t\t\t<Group ID=\"' + chk_in[j].text() + '\">\n')
                f_handle.write('\t\t\t\t\t\t\t<Selector ID=\"SourceType\" Value=\"Input\">\n')
                f_handle.write('\t\t\t\t\t\t\t\t<Property ID=\"IoParameter\" Value=\"' + chk_in[j].text() + '\" />\n')
                f_handle.write('\t\t\t\t\t\t\t</Selector>\n')
                f_handle.write('\t\t\t\t\t\t</Group>\n')
                k = k + 1
        f_handle.write('\t\t\t\t\t</Group>\n')
        f_handle.write('\t\t\t\t</Selector>\n')
        f_handle.write('\t\t\t\t<Group ID=\"Position\">\n')
        f_handle.write('\t\t\t\t\t<Property ID=\"X\" Value=\"1\" />\n')
        f_handle.write('\t\t\t\t\t<Property ID=\"Y\" Value=\"0\" />\n')
        f_handle.write('\t\t\t\t</Group>\n')
        f_handle.write('\t\t\t</Group>\n')
        f_handle.write('\t\t</Group>\n')

        # Outputs
        f_handle.write('\t\t<Group ID=\"ImgProcessingOutputs\">\n')
        k = 0
        for j in range(len(mp_out)):
            if mp_out[j] & chk_out[j].isChecked():
                f_handle.write('\t\t\t<Group ID=\"Output[' + str(k) + ']\">\n')
                f_handle.write('\t\t\t\t<Property ID="ChannelID" Value=\"' + chk_out[j].text())
                # SymbolType - the same name for input and output - prevent AS error
                if j == 2:
                    f_handle.write('Out')
                f_handle.write('\" />\n')
                f_handle.write('\t\t\t\t<Group ID=\"VpOutputWire\">\n')
                f_handle.write('\t\t\t\t\t<Property ID=\"SourceVfName\" Value=\"' + txt_vf.text() + '\" />\n')
                f_handle.write('\t\t\t\t\t<Property ID=\"VfOutputParameter\" Value=\"' + chk_out[j].text() + '\" />\n')
                f_handle.write('\t\t\t\t</Group>\n')
                f_handle.write('\t\t\t</Group>\n')
                k = k + 1
        f_handle.write('\t\t</Group>\n')
        f_handle.write('\t</Element>\n')
        f_handle.write('</Configuration>\n')
        f_handle.close()

    # Create the Vision Component file
    if chk_comp.isChecked():
        file_types = 'Vision Component (*.visioncomponent);;'
        path = QFileDialog.getSaveFileName(filter = file_types)
        if len(path[0]) > 0:
            f_name_comp = os.path.splitext(os.path.basename(path[0]))[0]
            f_handle = open(path[0], 'w+')
            f_handle.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n')
            f_handle.write('<Configuration>\n')
            f_handle.write('\t<Element ID=\"' + f_name_comp + '\" Type=\"visioncomponent\">\n')
            f_handle.write('\t\t<Property ID=\"VisionApplicationReference\" Value=\"' + f_name + '\" />\n')
            f_handle.write('\t</Element>\n')
            f_handle.write('</Configuration>\n')
            f_handle.close()

    # Change the Package.pkg file
    if chk_include.isChecked():
        if os.path.exists(os.path.dirname(path[0]) + '/Package.pkg'):
            f_handle = open(os.path.dirname(path[0]) + '/Package.pkg', 'r')
            f_handle_copy = open(os.path.dirname(path[0]) + '/Package.pkg.tmp', 'w+')
            f_line = f_handle.readline()
            while f_line.find('</Objects>') == -1 and f_line.find('<Objects />') == -1:
                f_handle_copy.write(f_line)
                f_line = f_handle.readline()
            if f_line.find('<Objects />') > -1:
                f_handle_copy.write('  <Objects>\n')
            if chk_comp.isChecked():
                f_handle_copy.write('    <Object Type=\"File\">' + f_name_comp + '.visioncomponent</Object>\n')
            f_handle_copy.write('    <Object Type=\"File\">' + f_name + '.visionapplication</Object>\n')
            f_handle_copy.write('  </Objects>\n')
            f_handle_copy.write('</Package>')
            f_handle.close()
            f_handle_copy.close()
            os.remove(os.path.dirname(path[0]) + '/Package.pkg')
            os.rename(os.path.dirname(path[0]) + '/Package.pkg.tmp', os.path.dirname(path[0]) + '/Package.pkg')

    # Show finished window
    box_fin.setVisible(True)
    widget.activateWindow()

def cbx_curr_idx_changed(idx):
    """ VF combobox selected index changed """
    if idx == 0:
        # Code Reader
        txt_vf.setText('VfCodeReader')
        for j in range(len(chk_in)):
            if mp_in_cr[j]:
                chk_in[j].setVisible(True)
            else:
                chk_in[j].setVisible(False)
        for j in range(len(chk_out)):
            if mp_out_cr[j]:
                chk_out[j].setVisible(True)
            else:
                chk_out[j].setVisible(False)
    elif idx == 1:
        # Blob
        txt_vf.setText('VfBlob')
        for j in range(len(chk_in)):
            if mp_in_blob[j]:
                chk_in[j].setVisible(True)
            else:
                chk_in[j].setVisible(False)
        for j in range(len(chk_out)):
            if mp_out_blob[j]:
                chk_out[j].setVisible(True)
            else:
                chk_out[j].setVisible(False)
    elif idx == 2:
        # Matching
        txt_vf.setText('VfMatching')
        for j in range(len(chk_in)):
            if mp_in_match[j]:
                chk_in[j].setVisible(True)
            else:
                chk_in[j].setVisible(False)
        for j in range(len(chk_out)):
            if mp_out_match[j]:
                chk_out[j].setVisible(True)
            else:
                chk_out[j].setVisible(False)
    elif idx == 3:
        # OCR
        txt_vf.setText('VfOcr')
        for j in range(len(chk_in)):
            if mp_in_ocr[j]:
                chk_in[j].setVisible(True)
            else:
                chk_in[j].setVisible(False)
        for j in range(len(chk_out)):
            if mp_out_ocr[j]:
                chk_out[j].setVisible(True)
            else:
                chk_out[j].setVisible(False)
    else:
        # Measurement
        txt_vf.setText('VfMeasurement')
        for j in range(len(chk_in)):
            if mp_in_meas[j]:
                chk_in[j].setVisible(True)
            else:
                chk_in[j].setVisible(False)
        for j in range(len(chk_out)):
            if mp_out_meas[j]:
                chk_out[j].setVisible(True)
            else:
                chk_out[j].setVisible(False)
    widget.setFixedSize(layout.sizeHint())


def chk_in_state_changed():
    """ Select all inputs checkbox """
    if chk_in_SelectAll.isChecked():
        for j in range(len(chk_in)):
            chk_in[j].setChecked(True)
    else:
        for j in range(len(chk_in)):
            chk_in[j].setChecked(False)


def chk_out_state_changed():
    """ Select all outputs checkbox """
    if chk_out_SelectAll.isChecked():
        for j in range(len(chk_out)):
            chk_out[j].setChecked(True)
    else:
        for j in range(len(chk_out)):
            chk_out[j].setChecked(False)


if __name__ == "__main__":
    app = QApplication([])

    # Header widgets
    font_bold = QFont()
    font_bold.setBold(True)
    label_header = QLabel('This app generates mappVision configuration files')
    label_header.setFont(font_bold)

    cbx_vf = QComboBox()
    cbx_vf.addItem('Code Reader')
    cbx_vf.addItem('Model-based Blob')
    cbx_vf.addItem('Matching')
    cbx_vf.addItem('OCR')
    cbx_vf.addItem('Measurement')
    cbx_vf.currentIndexChanged.connect(cbx_curr_idx_changed)

    txt_vf = QLineEdit()
    txt_vf.setText('VfCodeReader')

    chk_comp = QCheckBox('Generate .visioncomponent file')
    chk_include = QCheckBox('Include files to AS project')

    # Input widgets
    label_in = QLabel('Inputs')
    label_in.setFont(font_bold)

    chk_in_SelectAll = QCheckBox('Select all')
    chk_in_SelectAll.stateChanged.connect(chk_in_state_changed)

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
    chk_out_SelectAll.stateChanged.connect(chk_out_state_changed)

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
                QCheckBox('FunctionProcessingTime'),
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

    # Footer widgets
    btn_gen_file = QPushButton('Generate file')
    btn_gen_file.clicked.connect(btn_gen_file_pushed)

    box_fin = QMessageBox()
    box_fin.setWindowTitle('Finished')
    box_fin.setText('Successfully finished.')
    box_fin.setVisible(False)

    # Layout settings
    layout = QFormLayout()
    layout.addRow(label_header)
    layout.addRow(QLabel('__________________________________________________________________________________'))
    layout.addRow(QLabel('Select your Vision function: '), cbx_vf)
    layout.addRow(QLabel('Instance name: '), txt_vf)
    layout.addRow(QLabel('          '), chk_comp)
    layout.addRow(QLabel('          '), chk_include)
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
    chk_comp.setChecked(True)
    chk_include.setChecked(True)
    chk_in_SelectAll.setChecked(True)
    for i in range(len(chk_in)):
        if mp_in_cr[i] == 0:
            chk_in[i].setVisible(False)
    for i in range(len(chk_out)):
        if mp_out_cr[i] == 0:
            chk_out[i].setVisible(False)

    # Set widget and run
    widget = QWidget()
    widget.move(500, 200)
    widget.setLayout(layout)
    widget.show()
    widget.setWindowTitle('Mapp Vision Files')
    sys.exit(app.exec_())
