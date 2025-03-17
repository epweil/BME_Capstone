import board
import busio
import time 
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
from test_arm import servo
from camera import camera
import argparse
from alg import cacualte_image
class screen():
      def __init__(self, lcd_columns = 16, lcd_rows = 2, lcd_color = [100, 0, 0], go = True):
            self.lcd_columns = lcd_columns
            self.lcd_rows = lcd_rows
            self.i2c = busio.I2C(board.SCL, board.SDA)
            self.lcd = character_lcd.Character_LCD_RGB_I2C(self.i2c, self.lcd_columns, self.lcd_rows)
            self.lcd.color = lcd_color
            self.modes = { 
                  0:"Run", 
                  1:'Volume', 
                  2:'Area',
                  3:'Exit'}
            self.current_mode = 0
            self.current_volume = 0
            self.current_area = 0
            self.servo = servo()
            self.camera = camera()
            if(go):
                  self.set_message()
                  self.on()
            else:
                  self.run_thing()



      def get_mode(self,mode):
            if(mode < 0):
                  return mode + len(self.modes)
            elif(mode > 3):
                  return mode - len(self.modes)
            return mode
            
            
            
      def set_message(self, top_message = None, bottom_message = None):
            self.lcd.clear()
            current_mode = self.modes[self.current_mode]
            left_mode = self.modes[self.get_mode(self.current_mode -1)]
            right_mode = self.modes[self.get_mode(self.current_mode + 1)]
            
            if(bottom_message is None):
                  bottom_message = f"<- {left_mode}  {right_mode} ->"
                  
                  
            if(top_message is None):
                  
                  if(self.current_mode == 1):
                        top_message =  f"{current_mode}: {self.current_volume}"
                  elif(self.current_mode == 2):
                        top_message =  f"{current_mode}: {self.current_area}"
                  else:
                        top_message =  f"{current_mode}\n"

            message = f"{top_message}\n{bottom_message}"
            self.lcd.message = message
            return message 
      
      
      
      def run_thing(self):
            self.set_message(top_message = "Running")
            time.sleep(1)
            increment = 0.125
            servo_pos = -1
            ind = 0
            folder = None
            results = []
            for progress in range(0, 16):  # Update every 5%
                  str_disp = chr(255) * progress
                  self.set_message(top_message = str_disp, bottom_message = "")
                  self.servo.set_servo_angle(servo_pos)
                  servo_pos += increment
                  image_path , folder = self.camera.take_photo(image_num = ind, folder = folder)
                  calc = cacualte_image(image_path)
                  results.append(cacualte_image)
                  ind += 1
                  time.sleep(0.5)
            self.set_message(top_message = "Run Finished")
            self.current_area = np.asarray(results).mean().round(5)
            time.sleep(0.5)
            self.current_mode = 2
            self.set_message()
            
             
      def clear(self):
            self.lcd.clear()
            
            
      def on(self):
            while True:
                  if(self.lcd.left_button):
                        self.current_mode = self.get_mode(self.current_mode-1)
                        self.set_message()
                  if(self.lcd.right_button):
                        self.current_mode = self.get_mode(self.current_mode+1)
                        self.set_message()
                  if(self.lcd.select_button):
                        if(self.current_mode == 3):
                              self.clear()
                              return
                        if(self.current_mode == 0):
                              self.run_thing()
                  
                        
                  

                  
            
                  
if __name__ == "__main__":
      
      parser = argparse.ArgumentParser(
        description="Train DQN agent with optional modes: normal, asymmetric, believer, e2e, or true."
      )
      parser.add_argument("--test", type=bool, default=False)
      args = parser.parse_args()
      current_screen = screen(go = not args.test)
            




