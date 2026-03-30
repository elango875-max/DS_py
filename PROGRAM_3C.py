def areacalculator():
  _input_ = input("Enter the shape you want to calculate area of: ")
  area = 0
  pie = 3.14
  if _input_ == "Square":
     side = int(input("Enter the value of side: "))
     area = area + (side ** 2)
  elif _input_ == "Circle":
     radius = int(input("Enter thevalue of radius: "))
     area = area + (2 * pie * radius)
  elif _input_ == "Rectangle":
     length = int(input("Enter the valueof length: "))
     width = int(input("Enter the value of length: "))
     area = area + (length * width)
  elif _input_ == "Triangle":
     base = int(input("Enter the value of base: "))
     height = int(input("Enter the value of height: "))
     area = area +(0.5 * base * height)
  else:
     print ("Select a valid shape")
     print ("%.2f" % area)
     areacalculator()