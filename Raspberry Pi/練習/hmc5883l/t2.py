import py_qmc5883l
from time import sleep
sensor = py_qmc5883l.QMC5883L(output_range=py_qmc5883l.RNG_8G)
sleep(1)
magnet = sensor.get_magnet()
x_mag_init = magnet[0]
y_mag_init = magnet[1]
while True:
    bearing = sensor.get_bearing()
    magnet = sensor.get_magnet()
    x_mag = magnet[0] - x_mag_init
    y_mag = magnet[1] - y_mag_init
    print('x_mag:%d y_mag:%d bearing:%d' %(x_mag, y_mag, bearing))
    sleep(0.01)