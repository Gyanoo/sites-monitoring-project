
lineEdit = """
        QLineEdit{
             background-color: white;
             border: 1 solid #ddd;
             border-radius: 5px;
             font: 12pt "Corbel";
             color: #43454f;
             padding:10px;
        }
        """
lineEdit_warning = """
    QLineEdit{
         background-color: white;
         border: 1 solid #c00;
         border-radius: 5px;
         font: 12pt "Corbel";
         color: #43454f;
         padding:10px;
    }

"""
label_lineEdit = """
        QLabel{
            font-size: 23px;
            font: 12pt "Corbel";
            color: #43454f;
        }
        """
label_title = """
QLabel{
    text-align: center;
    font: 23pt "Corbel";
    color: #43454f;
}
"""

btn_radio = """
QRadioButton {
    font: 16pt 'Reem Kufi';
    font-size: 23px;
    font: 13pt 'Corbel';
    color:        #7b826b;
}
QRadioButton::indicator {
    background-color: #a8ad9e;
    width: 13px;
    height: 13px;
    border-radius: 11px;
    border: 5px solid #788f49;
}
QRadioButton::indicator:checked {
    background-color:		#43454f;
    border:                		5px solid #83a836;
    border-radius:         	11px;
}
QRadioButton:checked {
    color:      #83a836;
    border:        none;
}
QRadioButton::indicator:unchecked {
    background-color:    #7b826b;
    border: 5px solid #7b826b;
}
"""
btn_light = """
QPushButton{
    background-color:  #fff;
    border: 1 solid #83a836;
    border-radius: 20px;
    font: 13pt "Corbel";
    padding:6px;
    color: #83a836;
}
QPushButton:hover{
    background-color:  #aaa;
    border: 1 solid #ddd;
    color: #fff;
}
QPushButton:pressed{
    background-color:  #43454f;
    border: 1 solid #ddd;
    color: #fff;
}
"""

btn_dark = """
QPushButton{
    background-color:  #43454f;
    border: 1 solid #ddd;
    border-radius: 20px;
    font: 13pt "Corbel";
    padding:6px;
    color: #fff;
}
QPushButton:hover{
    background-color:  #aaa;
    border: 1 solid #ddd;
    color: #fff;
}
QPushButton:pressed{
    background-color:  #fff;
    border: 1 solid #83a836;
    color: #83a836;
}
"""

label_icon_name = """
QLabel{
    font-size: 20px;
    color: white;
    font: 16pt "Reem Kufi";
}
"""
frame_about = """
QFrame{
    margin: 0px;
    max-height:400px;
    max-width: 600px;
    background-color: #fff;
    border-radius: 20%;
}
"""
label_about_c = """
QLabel{
    margin: 0 40px 40px 40px;
    color: #555;
    font: 15pt "Corbel";
}
"""
label_about_name = """
QLabel{
    font-size: 20px;
    color: #43454f;
    font: 25pt "Reem Kufi";
}
"""
label_about_version = """
QLabel{
    margin: 0 40px 40px 40px;
    padding-top: 30px;
    border-top: 1px solid #aaa;
    border-radius: none;
    color: #555;
    font: 15pt "Corbel";
}
"""
label_allegro_monitored_stat = """
QLabel{
    border: none;
    font-size: 23px;
    font: 10pt "Corbel";
    color: #43454f;
}
"""
label_allegro_monitored_name = """
QLabel{
    font: 75 12pt "Noto Serif Lao";
    border: none;
    font-size: 23px;
    font: 10pt "Corbel";
    font: 75 12pt "Noto Serif Lao";
    color: #43454f;
}
"""


def main():
    pass
