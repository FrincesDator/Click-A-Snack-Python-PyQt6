import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import uic 


class Buyer (QWidget):

    def __init__(self):
        super(Buyer,self).__init__()
        uic.loadUi('OnlineCafe.ui',self)
        
        self.push_order.clicked.connect (self.compute_order)
        self.push_submit.clicked.connect (self.see_rate)
        self.push_repeat.clicked.connect (self.see_order)
     
    def compute_order(self):
        
         total = 0
         items = 0
         
         if self.check_sdonut.checkState() == Qt.CheckState.Checked:
             total += 29
             items += 1
         if self.check_mdonut.checkState() == Qt.CheckState.Checked:
             total += 29
             items += 1
         if self.check_adonut.checkState() == Qt.CheckState.Checked:
             total += 29   
             items += 1
         if self.check_ppie.checkState() == Qt.CheckState.Checked:
             total += 35              
             items += 1
         if self.check_cpie.checkState() == Qt.CheckState.Checked:
             total += 35              
             items += 1
         if self.check_apie.checkState() == Qt.CheckState.Checked:
             total += 35              
             items += 1
         if self.check_scookie.checkState() == Qt.CheckState.Checked:
             total += 29               
             items += 1
         if self.check_dcookie.checkState() == Qt.CheckState.Checked:
             total += 39   
             items += 1
         if self.check_pcookie.checkState() == Qt.CheckState.Checked:
             total += 39                
             items += 1
         if self.check_icetea.checkState() == Qt.CheckState.Checked:
             total += 30      
             items += 1
         if self.check_juice.checkState() == Qt.CheckState.Checked:
             total += 30                
             items += 1            
         if self.check_soda.checkState() == Qt.CheckState.Checked:
             total += 40                
             items += 1           
         if self.check_tea.checkState() == Qt.CheckState.Checked:
             total += 60                
             items += 1          
         if self.check_cocoa.checkState() == Qt.CheckState.Checked:
             total += 50   
             items += 1          
         if self.check_coffee.checkState() == Qt.CheckState.Checked:
             total += 50                
             items += 1
             
         discount = self.combo_discount.currentText()
         
         if discount == "0 %":
             total_discount = total - (total * .0)
         elif discount == "10 %":
             total_discount = total - (total * .10) 
         elif discount == "20 %":
             total_discount = total - (total * .20) 
         elif discount == "30 %":
             total_discount = total - (total * .30) 
         elif discount == "40 %":
             total_discount = total - (total * .40) 
         elif discount == "50 %":
             total_discount = total - (total * .50) 
         elif discount == "60 %":
             total_discount = total - (total * .60) 
         elif discount == "70 %":
             total_discount = total - (total * .70) 
         elif discount == "80 %":
             total_discount = total - (total * .80) 
         elif discount == "90 %":
             total_discount = total - (total * .90) 
         elif discount == "100 %":
             total_discount = total - (total * .100)           
           
         donate = int(self.line_donate.text())
         donation = total_discount + donate
         delivery = donation + 50

         if self.rb_cod.isChecked():
             mop = "Cash On Delivery"
         elif self.rb_online.isChecked():
             mop = "Online Payment"
         
         name = str(self.line_name.text())
         email = self.line_email.text()
         number = self.line_number.text()
         address = self.line_address.text()
         
         self.label_titems.setText(str(items))
         self.label_tamount.setText(str(total))
         self.label_tdamount.setText(str(total_discount))
         self.label_tdadonation.setText(str(donation))
         self.label_delivery.setText(str(delivery))
         self.label_mop.setText(str(mop))
         self.label_name.setText(str(name))    
         self.label_email.setText(email) 
         self.label_number.setText(number)
         self.label_address.setText(address)                   
         self.label_remarks2.setText("Thank you for choosing to shop with us!\nExpect your order/s within 20-30 minutes.\n\nPlease come again!")
         self.label_remarks2.setAlignment(Qt.AlignCenter)
         
    def see_rate(self):
        
        rate_remarks = str(self.line_service.text())
        
        
        if self.rb_5.isChecked() and rate_remarks!= "":
             rate = "You have rated us 5 stars!\nThank you for taking your time \nin improving our shop."
        elif self.rb_4.isChecked() and rate_remarks!= "":
             rate = "You have rated us 4 stars!\nThank you for taking your time \nin improving our shop."
        elif self.rb_3.isChecked() and rate_remarks!= "":
             rate = "You have rated us 3 stars!\nThank you for taking your time \nin improving our shop."
        elif self.rb_2.isChecked() and rate_remarks!= "":
             rate = "You have rated us 2 stars!\nThank you for taking your time \nin improving our shop."   
        elif self.rb_1.isChecked() and rate_remarks!= "":
             rate = "You have rated us 1 star!\nThank you for taking your time \nin improving our shop."    
        else:
             rate = "Please give us a rating and a feedback.\nThankyou!"
         
        self.label_remarks3.setText(rate)
        self.label_remarks3.setAlignment(Qt.AlignCenter)  
        
    def see_order(self):
        
        order = []
         
        if self.check_sdonut.checkState() == Qt.CheckState.Checked:
             order.append("Strawberry Filled Donut")
        if self.check_mdonut.checkState() == Qt.CheckState.Checked:
             order.append("Mango Filled Donut")
        if self.check_adonut.checkState() == Qt.CheckState.Checked:
             order.append("Avocado Filled Donut")
        if self.check_ppie.checkState() == Qt.CheckState.Checked:
             order.append("Peach Pie")
        if self.check_cpie.checkState() == Qt.CheckState.Checked:
             order.append("Cherry Pie")
        if self.check_apie.checkState() == Qt.CheckState.Checked:
             order.append("Apple Pie")
        if self.check_scookie.checkState() == Qt.CheckState.Checked:
             order.append("Simple Chocolate Cookie")
        if self.check_dcookie.checkState() == Qt.CheckState.Checked:
             order.append("Double Chocolate Cookie")
        if self.check_pcookie.checkState() == Qt.CheckState.Checked:
             order.append("Chocolate Cookie with Peanuts")
        if self.check_icetea.checkState() == Qt.CheckState.Checked:
             order.append("Lychee Iced Tea")
        if self.check_juice.checkState() == Qt.CheckState.Checked:  
             order.append("Plum Juice")
        if self.check_soda.checkState() == Qt.CheckState.Checked:   
             order.append("Blueberry Soda")
        if self.check_tea.checkState() == Qt.CheckState.Checked:
             order.append("Milk Tea")
        if self.check_cocoa.checkState() == Qt.CheckState.Checked:
             order.append("Hot / Cold Cocoa with Marshmallows")
        if self.check_coffee.checkState() == Qt.CheckState.Checked:
             order.append("Hot / Cold Coffee with Marshmallows")
             
        listToStr = '\n'.join([str(elem) for elem in order])
        
        QMessageBox.about(self, "Here's your order:", listToStr)
        
app = QApplication(sys.argv)
widget = Buyer()
widget.show()
sys.exit(app.exec())   

