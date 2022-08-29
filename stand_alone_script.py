import sys
import os

from qgis.core import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QLineEdit, QProgressBar
from PyQt5.QtGui import QIntValidator

import processing
from processing.core.Processing import Processing

class Window(QWidget):

   def __init__(self):
      super().__init__()

      # Define the GUI
      self.GUI()

   def GUI(self):
      # Set-up the window dimensions and title
      self.setGeometry(500,60,560,620)  #  setGeometry(x, y, width, height)
      self.setWindowTitle("GroundWater Buffer Generator")

      # Set-up the "Find Vector File" Label
      self.FindVfile_Label = QLabel(self)
      self.FindVfile_Label.setText("Enter Vector File Path")
      self.FindVfile_Label.move(25,10)

      # Set-up the Line edit for users to enter the original (to be buffered) Vector file
      self.FindVFile_LineEdit = QLineEdit(self)
      self.FindVFile_LineEdit.resize(360, 32)
      self.FindVFile_LineEdit.move(25,30)

      # Set-up the button to select the original Vector file
      self.FindVFile_Button = QPushButton('Find File', self)
      self.FindVFile_Button.move(405,33)
      self.FindVFile_Button.clicked.connect(self.FindVFile_Button_clicked)
      self.FindVFile_Button.show()

      # Set-up the "Find Raster File" Label
      self.FindRfile_Label = QLabel(self)
      self.FindRfile_Label.setText("Enter Raster File Path")
      self.FindRfile_Label.move(25,80)

      # Set-up the Line edit for users to enter the original Raster file
      self.FindRFile_LineEdit = QLineEdit(self)
      self.FindRFile_LineEdit.resize(360, 32)
      self.FindRFile_LineEdit.move(25,100)

      # Set-up the button to select the original Raster file
      self.FindRFile_Button = QPushButton('Find File', self)
      self.FindRFile_Button.move(405,103)
      self.FindRFile_Button.clicked.connect(self.FindRFile_Button_clicked)
      self.FindRFile_Button.show()

      # Set-up the "Buffer Extent (m)" Label
      self.SelectExt_Label = QLabel(self)
      self.SelectExt_Label.setText("Buffer Extent (m)")
      self.SelectExt_Label.move(25,150)

      # Set-up the Line edit for users to enter the buffer extent
      self.SelectExt_LineEdit = QLineEdit('75', self)
      self.SelectExt_LineEdit.setValidator(QIntValidator()) # only integers can be entered
      self.SelectExt_LineEdit.resize(360, 32)
      self.SelectExt_LineEdit.move(25,170)

      # Set-up the "Set Original Raster..." Label
      self.SelectPixExt_Label = QLabel(self)
      self.SelectPixExt_Label.setText("Set Original Raster pixel sixe (x,y) and extent (xmin, xmax, ymin, ymax)")
      self.SelectPixExt_Label.move(25,220)

      # Set-up the Line edit for users to enter the original raster pixel size and extent
      self.SelectPixExt_LineEdit = QLineEdit('-tr 1 1 -txe 0 0 -tye 0 0', self)
      self.SelectPixExt_LineEdit.resize(360, 32)
      self.SelectPixExt_LineEdit.move(25,240)

      # Set-up the "Select Output Folder for the Full Buffer Raster" Label
      self.FindFullFold_Label = QLabel(self)
      self.FindFullFold_Label.setText("Select Output Folder for the Full Buffer Raster")
      self.FindFullFold_Label.move(25,290)

      # Set-up the Line edit for users to enter the output folder for the full buffer raster
      self.FindFullFold_LineEdit = QLineEdit(self)
      self.FindFullFold_LineEdit.resize(360, 32)
      self.FindFullFold_LineEdit.move(25,310)

      # Set-up the button to select the output folder for the full buffer raster
      self.FindFullFold_Button = QPushButton('Find Folder', self)
      self.FindFullFold_Button.move(405, 313)
      self.FindFullFold_Button.clicked.connect(self.FindFolder_FullBuff_Button_clicked)
      self.FindFullFold_Button.show()

      # Set-up the "Select Output Folder for the Only-Buffer Raster" Label
      self.FindOnlyFold_Label = QLabel(self)
      self.FindOnlyFold_Label.setText("Select Output Folder for the Only-Buffer Raster")
      self.FindOnlyFold_Label.move(25,360)

      # Set-up the Line edit for users to enter the output folder for the only buffer raster
      self.FindOnlyFold_LineEdit = QLineEdit(self)
      self.FindOnlyFold_LineEdit.resize(360, 32)
      self.FindOnlyFold_LineEdit.move(25,380)

      # Set-up the button to select the output folder for the only buffer raster
      self.FindOnlyFold_Button = QPushButton('Find Folder', self)
      self.FindOnlyFold_Button.move(405, 383)
      self.FindOnlyFold_Button.clicked.connect(self.FindFolder_OnlyBuff_Button_clicked)
      self.FindOnlyFold_Button.show()

      # Set-up the error-message Label
      self.Error_Message_Label = QLabel(self)
      self.Error_Message_Label.setText("")
      self.Error_Message_Label.move(25,460)

      # Set-up the button to create GroundWater Buffer
      self.Process_Button = QPushButton('Create Buffer', self)
      self.Process_Button.move(200,500)
      self.Process_Button.clicked.connect(self.create_GW_Buffer)
      self.Process_Button.show()

      # Set-up Progress Bar
      self.Pbar = QProgressBar(self)
      self.Pbar.setGeometry(25, 550, 500, 30)  #  setGeometry(x, y, width, height)
      self.Pbar.show()

      Processing.initialize()

      self.show()

   def FindVFile_Button_clicked(self):
      # getOpenFileName(self, label, default path to search for files, types of files to look for)
      fname = QFileDialog.getOpenFileName(self, "Open File", "D:/IBI_Group/Projects/ Custom_Raster_Buffer", 
                                          "Shape File (*.shp);;GeoPackage (*.gpkg)")
      self.FindVFile_LineEdit.setText(str(fname[0]))

   def FindRFile_Button_clicked(self):
      # getOpenFileName(self, label, default path to search for files, types of files to look for)
      fname = QFileDialog.getOpenFileName(self, "Open File", "D:/IBI_Group/Projects/ Custom_Raster_Buffer", "GeoTiff (*.tif)")
      self.FindRFile_LineEdit.setText(str(fname[0]))

   def FindFolder_FullBuff_Button_clicked(self):
      # getExistingDirectory(self, label, default path to search for folder)
      foldname = QFileDialog.getExistingDirectory(self, "Open Directory")
      self.FindFullFold_LineEdit.setText(str(foldname) + "/FullBuff.tif")

   def FindFolder_OnlyBuff_Button_clicked(self):
      # getExistingDirectory(self, label, default path to search for folder)
      foldname = QFileDialog.getExistingDirectory(self, "Open Directory")
      self.FindOnlyFold_LineEdit.setText(str(foldname) + "/OnlyBuff.tif")

   def create_GW_Buffer(self):
      self.Pbar.setValue(0) # reset progress bar
      self.Error_Message_Label.setText("") # reset error message to blank

      # Set function parameters
      VFileName = self.FindVFile_LineEdit.text()
      RFileName = self.FindRFile_LineEdit.text()
      BufferExtent = self.SelectExt_LineEdit.text()
      PixExt = self.SelectPixExt_LineEdit.text()
      FullFold = self.FindFullFold_LineEdit.text()
      OnlyFold = self.FindOnlyFold_LineEdit.text()

      # Error Handling: Check for empty parameters
      if not FullFold or not OnlyFold or not PixExt or not BufferError or not RFileName or not VFileName:
         self.Error_Message_Label.resize(400, 20)
         self.Error_Message_Label.setText("WARNING: One or more of your parameters are empty")
         return
      
      # Error Handling: Check if the selected files exist
      if os.path.isfile(VFileName) is False or os.path.isfile(RFileName) is False:
         self.Error_Message_Label.resize(400, 20)
         self.Error_Message_Label.setText("WARNING: One or more of your selected files do not exist")
         return
      
      ### START THE PROCESSING CODE TO CREATE GW RASTER BUFFER ####################################

      fix_geom = processing.run("native:fixgeometries", {'INPUT':VFileName,
                                                         'OUTPUT': 'memory:'})
      self.Pbar.setValue(10)
      vertex_points = processing.run("native:extractvertices", {'INPUT':fix_geom['OUTPUT'],
                                                                'OUTPUT':'memory:'})
      self.Pbar.setValue(15)
      Sample_points = processing.run("native:rastersampling", { 'INPUT':vertex_points['OUTPUT'],
                                                                'RASTERCOPY':RFileName,
                                                                'COLUMN_PREFIX': 'SAMPLE_VAL',
                                                                'OUTPUT': 'memory:'})
      self.Pbar.setValue(20)
      extract_Sample_points = processing.run("qgis:extractbyexpression", { 'INPUT':Sample_points['OUTPUT'],
                                                                           'EXPRESSION':'SAMPLE_VAL1 is not NULL',
                                                                           'OUTPUT': 'memory:'})
      self.Pbar.setValue(25)
      first_Buff = processing.run("gdal:gridnearestneighbor", {'INPUT':extract_Sample_points['OUTPUT'],
                                                               'RADIUS_1':int(BufferExtent),
                                                               'RADIUS_2':int(BufferExtent),
                                                               'NODATA': -100,
                                                               'Z_FIELD':'SAMPLE_VAL1',
                                                               'EXTRA':PixExt,
                                                               'DATA_TYPE':5, # Float32
                                                               'OUTPUT':FullFold})
      self.Pbar.setValue(60)
      Extent_poly = processing.run("native:extenttolayer", {'INPUT':first_Buff['OUTPUT'],
                                                            'OUTPUT':'memory:'})
      self.Pbar.setValue(65)
      Dif_poly = processing.run("qgis:difference", {'INPUT':Extent_poly['OUTPUT'],
                                                    'OVERLAY':fix_geom['OUTPUT'],
                                                    'OUTPUT': 'memory:'})
      self.Pbar.setValue(70)
      final_Buff = processing.run("gdal:cliprasterbymasklayer", { 'INPUT':first_Buff['OUTPUT'],
                                                                  'MASK':Dif_poly['OUTPUT'],
                                                                  'NODATA':-100,
                                                                  'ALPHA_BAND':False,
                                                                  'CROP_TO_CUTLINE':True,
                                                                  'KEEP_RESOLUTION':True,
                                                                  'SET_RESOLUTION':False,
                                                                  'MULTITHREADING':False,
                                                                  'DATA_TYPE':0,
                                                                  'OUTPUT':OnlyFold})
      ### END OF PROCESSING CODE ##################################################################
      
      self.Pbar.setValue(100)

if __name__ == '__main__':
   	
	# create pyqt5 app
	App = QApplication(sys.argv)

	# create the instance of our Window
	window = Window()

	# start the app
	sys.exit(App.exec())