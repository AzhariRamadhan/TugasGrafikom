from graphics import *

def main():
    win = GraphWin("Azhari Ramadhan", 2500, 500)
    win.setBackground(color_rgb(236, 240, 241))

    # bentuk huruf G

    Gbentuk1 = Line(Point(400,200), Point(300,100))
    Gbentuk1.setWidth(10)
    Gbentuk1.draw(win)
    Gbentuk2 = Line(Point(300,100), Point(200,100))
    Gbentuk2.setWidth(10)
    Gbentuk2.draw(win)
    Gbentuk3 = Line(Point(200,100), Point(100,200))
    Gbentuk3.setWidth(10)
    Gbentuk3.draw(win)
    Gbentuk4 = Line(Point(100,200), Point(100,300))
    Gbentuk4.setWidth(10)
    Gbentuk4.draw(win)
    Gbentuk5 = Line(Point(100,300), Point(200,400))
    Gbentuk5.setWidth(10)
    Gbentuk5.draw(win)
    Gbentuk6 = Line(Point(200,400), Point(300,400))
    Gbentuk6.setWidth(10)
    Gbentuk6.draw(win)
    Gbentuk7 = Line(Point(300,400), Point(400,300))
    Gbentuk7.setWidth(10)
    Gbentuk7.draw(win)
    Gbentuk8 = Line(Point(400,300), Point(400,250))
    Gbentuk8.setWidth(10)
    Gbentuk8.draw(win)
    Gbentuk9 = Line(Point(400,250), Point(300,250))
    Gbentuk9.setWidth(10)
    Gbentuk9.draw(win)

    # bentuk angka 1

    bt1 = Line(Point(500,100), Point(500,400))
    bt1.setWidth(10)
    bt1.draw(win)

    # bentuk huruf A

    Abentuk1 = Line(Point(750,100), Point(600,400))
    Abentuk1.setWidth(10)
    Abentuk1.draw(win)
    Abentuk2 = Line(Point(750,100), Point(900,400))
    Abentuk2.setWidth(10)
    Abentuk2.draw(win)
    Abentuk3 = Line(Point(680,250), Point(830,250))
    Abentuk3.setWidth(10)
    Abentuk3.draw(win)

    # bentuk angka 0

    bt0 = Rectangle(Point(950,100), Point(1150,400))
    bt0.setWidth(10)
    bt0.draw(win)

    # bentuk angka 15

    Angkatan1 = Line(Point(1300,100), Point(1300,400))
    Angkatan1.setWidth(10)
    Angkatan1.draw(win)
    Angkatan5_1 = Line (Point(1600,100), Point(1400,100))
    Angkatan5_1.setWidth(10)
    Angkatan5_1.draw(win)
    Angkatan5_2 = Line(Point(1400,100), Point(1400,250))
    Angkatan5_2.setWidth(10)
    Angkatan5_2.draw(win) 
    Angkatan5_3 = Line(Point(1400,250), Point(1600,250))
    Angkatan5_3.setWidth(10)
    Angkatan5_3.draw(win)
    Angkatan5_4 = Line(Point(1600,250), Point(1600,400))
    Angkatan5_4.setWidth(10)
    Angkatan5_4.draw(win)
    Angkatan5_5 = Line(Point(1600,400), Point(1400,400))
    Angkatan5_5.setWidth(10)
    Angkatan5_5.draw(win)

    # bentuk 059

    Nomor1 = Rectangle(Point(1650,100), Point(1850,400))
    Nomor1.setWidth(10)
    Nomor1.draw(win)
    Nomor2 = Line(Point(2100,100), Point(1900,100))
    Nomor2.setWidth(10)
    Nomor2.draw(win)
    Nomor3 = Line(Point(1900,100), Point(1900,250))
    Nomor3.setWidth(10)
    Nomor3.draw(win)
    Nomor4 = Line(Point(1900,250), Point(2100,250))
    Nomor4.setWidth(10)
    Nomor4.draw(win)
    Nomor5 = Line(Point(2100,250), Point(2100,400))
    Nomor5.setWidth(10)
    Nomor5.draw(win)
    Nomor6 = Line(Point(2100,400), Point(1900,400))
    Nomor6.setWidth(10)
    Nomor6.draw(win)
    Nomor7 = Rectangle(Point(2200,100), Point(2400,250))
    Nomor7.setWidth(10)
    Nomor7.draw(win)
    Nomor8 = Line(Point(2400,250), Point(2400,400))
    Nomor8.setWidth(10)
    Nomor8.draw(win)
    Nomor9 = Line(Point(2400,400), Point(2200,400))
    Nomor9.setWidth(10)
    Nomor9.draw(win)


    win.getMouse()
    win.close()
main()
