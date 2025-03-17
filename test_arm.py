
import lgpio
import time

from gpiozero import Servo
from time import sleep

# Initialize the servo on GPIO pin 14
# min_pulse_width and max_pulse_width may need to be adjusted for your servo

class servo():
      def __init__(self, SERVO_PIN = 16):


            self.servo = Servo(SERVO_PIN)
            

      def set_servo_angle(self, angle):
            self.servo.value = angle

      def test(self):
            print("Moving servo...")
            self.set_servo_angle(-1)
            time.sleep(3)

            self.set_servo_angle(0)
            time.sleep(3)

            self.set_servo_angle(1)
            time.sleep(3)

if __name__ == "__main__":
      serv = servo()
      serv.test()