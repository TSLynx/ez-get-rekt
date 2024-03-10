# necessary imports

FOV = 60
sens = 1.00
speed = 2

screen = [1920, 1080]

screen_center = [screen[0] / 2, screen[1] / 2]

# function to move cursor
def move(x, y):
  # replace with your actual logic
  print("")

def get_entities():
  # replace with your actual entityList code
  print("")

def world_to_screen(x,y,z):
  # replace with your actual W2S code
  print("")

while True:
  for entity in entities:
    # get screen coordinates of entity
    x,y,z = entity.get_position()
    # fov check
    if abs(x - screen_center[0]) < FOV and abs(y - screen_center[1]) < FOV:
      delta_x = x - screen_center[0]
      delta_y = x - screen_center[1]
      # adjust values to sensitivity
      delta_x = delta_x * 1.00 / sens
      delta_y = delta_y * 1.00 / sens
      # apply speed
      delta_x = delta_x * speed
      delta_y = delta_y * speed
      # move mouse accordingly
      move(delta_x, delta_y)
