from picamzero import Camera
import os
import re
class camera():
      def get_highest_numbered_folder(self, directory):
            highest_number = -1  # Default if no valid folders are found
            
            for folder in os.listdir(directory):
                  if os.path.isdir(os.path.join(directory, folder)):  # Ensure it's a directory
                        match = re.match(r'(\d+)', folder)  # Match folders starting with numbers
                        if match:
                              number = int(match.group(1))
                              highest_number = max(highest_number, number)
            
            return highest_number+1 if highest_number != -1 else "0"
      def __init__(self, dir_out = './camera_test/'):
            self.dir_out = dir_out
            self.cam = Camera()
      def take_photo(self, image_num = 0, folder = None):
            if(folder is None):
                  folder = self.get_highest_numbered_folder(self.dir_out)
            if(not os.path.exists(f"{self.dir_out}{folder}")):
                  os.mkdir(f"{self.dir_out}{folder}")
            self.cam.take_photo(f"{self.dir_out}/{folder}/{image_num}.jpg")
            return f"{self.dir_out}/{folder}/{image_num}.jpg", folder


if __name__ =="__main__":
      cam = camera()
      cam.take_photo()