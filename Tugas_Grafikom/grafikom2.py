from graphics import *

def main():
    win = GraphWin("Azhari Ramadhan", 1300, 250)
    win.setBackground(color_rgb(236, 240, 241))

    # bentuk huruf G

    Gbentuk1 = Line(Point(200,100), Point(150,50))
    Gbentuk1.setWidth(5)
    Gbentuk1.draw(win)
    Gbentuk2 = Line(Point(150,50), Point(100,50))
    Gbentuk2.setWidth(5)
    Gbentuk2.draw(win)
    Gbentuk3 = Line(Point(100,50), Point(50,100))
    Gbentuk3.setWidth(5)
    Gbentuk3.draw(win)
    Gbentuk4 = Line(Point(50,100), Point(50,150))
    Gbentuk4.setWidth(5)
    Gbentuk4.draw(win)
    Gbentuk5 = Line(Point(50,150), Point(100,200))
    Gbentuk5.setWidth(5)
    Gbentuk5.draw(win)
    Gbentuk6 = Line(Point(100,200), Point(150,200))
    Gbentuk6.setWidth(5)
    Gbentuk6.draw(win)
    Gbentuk7 = Line(Point(150,200), Point(200,150))
    Gbentuk7.setWidth(5)
    Gbentuk7.draw(win)
    Gbentuk8 = Line(Point(200,150), Point(200,125))
    Gbentuk8.setWidth(5)
    Gbentuk8.draw(win)
    Gbentuk9 = Line(Point(200,125), Point(150,125))
    Gbentuk9.setWidth(5)
    Gbentuk9.draw(win)

    # bentuk angka 1

    bt1 = Line(Point(250,50), Point(250,200))
    bt1.setWidth(5)
    bt1.draw(win)

    # bentuk huruf A

    Abentuk1 = Line(Point(375,50), Point(300,200))
    Abentuk1.setWidth(5)
    Abentuk1.draw(win)
    Abentuk2 = Line(Point(375,50), Point(450,200))
    Abentuk2.setWidth(5)
    Abentuk2.draw(win)
    Abentuk3 = Line(Point(340,125), Point(415,125))
    Abentuk3.setWidth(5)
    Abentuk3.draw(win)

    # bentuk angka 0

    bt0 = Rectangle(Point(475,50), Point(575,200))
    bt0.setWidth(5)
    bt0.draw(win)

    # bentuk angka 15

    Angkatan1 = Line(Point(650,50), Point(650,200))
    Angkatan1.setWidth(5)
    Angkatan1.draw(win)
    Angkatan5_1 = Line (Point(800,50), Point(700,50))
    Angkatan5_1.setWidth(5)
    Angkatan5_1.draw(win)
    Angkatan5_2 = Line(Point(700,50), Point(700,125))
    Angkatan5_2.setWidth(5)
    Angkatan5_2.draw(win) 
    # ubah di sini untuk merubah angkatan
    Angkatan5_3 = Line(Point(700,125), Point(800,125))
    Angkatan5_3.setWidth(5)
    Angkatan5_3.draw(win)
    # jika angkatan 16 hapus bagian bawah sampai
    # Angkatan5_5.draw(win)
    Angkatan5_4 = Line(Point(800,125), Point(800,200))
    Angkatan5_4.setWidth(5)
    Angkatan5_4.draw(win)
    Angkatan5_5 = Line(Point(800,200), Point(700,200))
    Angkatan5_5.setWidth(5)
    Angkatan5_5.draw(win)

    # bentuk nomor mahasiswa

    Nomor1 = Rectangle(Point(825,50), Point(925,200))
    Nomor1.setWidth(5)
    Nomor1.draw(win)
    # di bawah ini untuk mengubah 2 digit terakhir
    Nomor2 = Line(Point(1050,50), Point(950,50))
    Nomor2.setWidth(5)
    Nomor2.draw(win)
    Nomor3 = Line(Point(950,50), Point(950,125))
    Nomor3.setWidth(5)
    Nomor3.draw(win)
    Nomor4 = Line(Point(950,125), Point(1050,125))
    Nomor4.setWidth(5)
    Nomor4.draw(win)
    Nomor5 = Line(Point(1050,125), Point(1050,200))
    Nomor5.setWidth(5)
    Nomor5.draw(win)
    Nomor6 = Line(Point(1050,200), Point(950,200))
    Nomor6.setWidth(5)
    Nomor6.draw(win)
    # dibawah ini untuk mengubah 1 digit terakhir
    Nomor7 = Rectangle(Point(1100,50), Point(1200,125))
    Nomor7.setWidth(5)
    Nomor7.draw(win)
    Nomor8 = Line(Point(1200,125), Point(1200,200))
    Nomor8.setWidth(5)
    Nomor8.draw(win)
    Nomor9 = Line(Point(1200,200), Point(1100,200))
    Nomor9.setWidth(5)
    Nomor9.draw(win)


    win.getMouse()
    win.close()
main()
